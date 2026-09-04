# Verification process log — verify-page-51


## [2026-09-04T19:37:36.346Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 51 only. Chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-51.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-51.json. The local reference library is at /home/sfmqrb/git/rishe/data/verification/sources/refs/ (every file in the source matrix exists there; scanned pages via tools/ref_page.py). Use WebFetch/WebSearch for modern sources (archive each cited URL with tools/fetch_source.py), check Nourai's citations in the local reference texts (quote what you find), and consult every relevant book per the source matrix. Write /home/sfmqrb/git/rishe/data/verification/page-51.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 51` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-04T19:37:38.043Z] AGENT

I'll start by reading the instructions.


## [2026-09-04T19:37:40.163Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T19:37:40.176Z] TOOL RESULT

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


## [2026-09-04T19:37:40.465Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-51.txt"
}
```


### [2026-09-04T19:37:40.483Z] TOOL RESULT

```
1	=== PDF page 51 (book page 21) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Ambhi, Mbhi, Obhi, Ebhi : around. Ambhô : both.  (refs POK:34)
4	#1 (parent #0) [Avestan] refs=POK:34 | aiwi, aibi, abi, aiwiš, ubě, uwa : over, above, both
5	  #2 (parent #1) [Avestan] refs=None | aiwi-ruč : to light up ☞Leuk ; aiwi-reg : to straighten up ☞Reg ; aiwi-sâra : around the head ☞Ker 1 ; aiwi-sara : on the head ☞Ker 1
6	    #3 (parent #2) [Persian] refs=HRN:22,23 | afrŭxtan «افروختن» : to light up ; afrâštan «افراشتن» : to raise ; afsâr «افسار» : bridle ; afsar «افسر» : crown, officer | extra: افراز
7	  #4 (parent #1) [Avestan] refs=HUB:16 | aiwi-saoka : burn over ☞Keuk 1 ; aiwi-kand : to throw away ☞Gwhen 1 ; aiwi-zâvayeiti : adds up ☞Geu 2
8	    #5 (parent #4) [Persian] refs=DRM:131; HRN:23 | afsŭs «افسوس» : regret ; afkandan «افکندن» : to throw ; afzŭdan «افزودن» : to add | extra: فزون
9	  #6 (parent #1) [Avestan] refs=None | aiwi-fšân : to spread around ; aiwi-axš : oversee ☞Okw
10	    #7 (parent #6) [Persian] refs=HRN:24; BQT:2143; MON:317 | afšândan «افشاندن» : to spread, sprinkle ; afšûn «افشون» : rake | extra: افشان
11	  #8 (parent #1) [Avestan] refs=None | aiwiš-kar : chase (animals) away ☞Kwer ; aiwiš-tap : in heat, in a hurry ☞Tep
12	    #9 (parent #8) [Persian] refs=BQT:1275; HRN:172,174 | šekâr «شکار» : hunt ; šetâftan «شتافتن» : to hurry | extra: شتاب
13	  #10 (parent #1) [Avestan] refs=AHM:220 | abi-dasta, a-dasta, a-dsta : over hands, sleeve ☞Ghesto
14	    #11 (parent #10) [Persian] refs=AHM:220 | âstîn «آستین» : sleeve
15	#12 (parent #0) [Old Persian] refs=POK:34 | abiš, abiy, abi : over, above
16	#13 (parent #0) [Greek] refs=POK:34; AHD:44 | amphi : around, on both sides
17	  #14 (parent #13) [English] refs=None | amphitheater ; amphibious
18	#15 (parent #0) [Germanic] refs=POK:34; AHD | 
19	  #16 (parent #15) [English] refs=None | both ; be-
20	#17 (parent #0) [Latin] refs=AHD; KLN:512 | ambi-îre : to go around, ambient ☞Ei ; ambactus : one who goes around, messenger, servant
21	  #18 (parent #17) [English] refs=None | ambient ; ambassador ; embassy
22	#19 (parent #0) [Indo-European] refs=IEC:19 | Ambhô-bhor, Ambhor : a two-handled tool ☞Bher 1
23	  #20 (parent #19) [Persian] refs=IEC:19; MON:361 | anbor «انبر» : pliers | extra: انبره ، انبردست
24	
```


## [2026-09-04T19:37:41.725Z] AGENT

I'll read the supporting files.


## [2026-09-04T19:37:44.216Z] TOOL CALL #3: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-04T19:37:44.259Z] TOOL RESULT

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


## [2026-09-04T19:37:46.689Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','HUB','HRN','BQT','MON','AHD','KLN','IEC','DRM','AHM','WLD','SYN','BRT','KNT','PHD','NYB','CHEUNG','SKT','FSD','WEB','HUB']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False))\n    else: print(k,'MISSING')\n\""
}
```


### [2026-09-04T19:37:48.219Z] TOOL RESULT

```
<persisted-output>
Output too large (35KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b1wydf5mc.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-04T19:37:53.293Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['HUB','HRN','BQT','MON','AHD','KLN','IEC','DRM','AHM']:\n    e=d.get(k)\n    if not e: print(k,'MISSING'); continue\n    print('==',k, e.get('title'))\n    print('  kind:',e.get('kind'),' local:',e.get('local_file'))\n    print('  offset:',str(e.get('page_offset'))[:400])\n    print('  hint:',str(e.get('lookup_hint'))[:400])\n    print('  files:',e.get('local_files'))\n\""
}
```


## [2026-09-04T19:37:54.141Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-51.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\""
}
```


### [2026-09-04T19:37:54.993Z] TOOL RESULT

```
== HUB H. Hübschmann, Persische Studien, Strassburg 1895
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
  offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
  files: None
== HRN P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
  offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
  files: None
== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
  kind: archive_djvu+local_scan_ocr  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
  offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numera
  hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metada
  files: None
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
  kind: website+archive_djvu  local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
  offset: None
  hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/ab
  files: None
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
  kind: archive_djvu+website+archive_restricted  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
  offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
  hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.
  files: None
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
  offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
  files: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
== IEC S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
  offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
  files: None
== DRM J. Darmesteter, Études iraniennes, 2 vols., Paris 1883
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt
  offset: Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say which tome - try both. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Tome I is the historical grammar of Persian (numbered §§); Tome II contains the 'Études sur la langue...' incl. etymological notes on Persian words. grep the Persian word in transliteration.
  files: None
== AHM I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  kind: archive_djvu  local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt
  offset: leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
  hint: Commentary is by stanza/note number; the Glossary (end of book) lists Avestan words. grep the Avestan word in transliteration.
  files: None
```


### [2026-09-04T19:37:56.696Z] TOOL RESULT

```
{
 "pdf_page": 51,
 "book_page": 21,
 "entries": [
  {
   "root": {
    "name": "Ambhi, Mbhi, Obhi, Ebhi",
    "lang": "Indo-European",
    "refs": "POK:34",
    "gloss": "around. Ambhô : both."
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:34",
     "words": [
      {
       "translit": "aiwi, aibi, abi, aiwiš, ubě, uwa",
       "gloss": "over, above, both",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Avestan",
     "refs": null,
     "words": [
      {
       "translit": "aiwi-ruč",
       "gloss": "to light up",
       "script": null,
       "see": [
        "Leuk"
       ]
      },
      {
       "translit": "aiwi-reg",
       "gloss": "to straighten up",
       "script": null,
       "see": [
        "Reg"
       ]
      },
      {
       "translit": "aiwi-sâra",
       "gloss": "around the head",
       "script": null,
       "see": [
        "Ker 1"
       ]
      },
      {
       "translit": "aiwi-sara",
       "gloss": "on the head",
       "script": null,
       "see": [
        "Ker 1"
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
     "refs": "HRN:22,23",
     "words": [
      {
       "translit": "afrŭxtan",
       "gloss": "to light up",
       "script": "افروختن"
      },
      {
       "translit": "afrâštan",
       "gloss": "to raise",
       "script": "افراشتن"
      },
      {
       "translit": "afsâr",
       "gloss": "bridle",
       "script": "افسار"
      },
      {
       "translit": "afsar",
       "gloss": "crown, officer",
       "script": "افسر"
      }
     ],
     "script_extra": "افراز",
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 1,
     "lang": "Avestan",
     "refs": "HUB:16",
     "words": [
      {
       "translit": "aiwi-saoka",
       "gloss": "burn over",
       "script": null,
       "see": [
        "Keuk 1"
       ]
      },
      {
       "translit": "aiwi-kand",
       "gloss": "to throw away",
       "script": null,
       "see": [
        "Gwhen 1"
       ]
      },
      {
       "translit": "aiwi-zâvayeiti",
       "gloss": "adds up",
       "script": null,
       "see": [
        "Geu 2"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "DRM:131; HRN:23",
     "words": [
      {
       "translit": "afsŭs",
       "gloss": "regret",
       "script": "افسوس"
      },
      {
       "translit": "afkandan",
       "gloss": "to throw",
       "script": "افکندن"
      },
      {
       "translit": "afzŭdan",
       "gloss": "to add",
       "script": "افزودن"
      }
     ],
     "script_extra": "فزون",
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 1,
     "lang": "Avestan",
     "refs": null,
     "words": [
      {
       "translit": "aiwi-fšân",
       "gloss": "to spread around",
       "script": null
      },
      {
       "translit": "aiwi-axš",
       "gloss": "oversee",
       "script": null,
       "see": [
        "Okw"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Persian",
     "refs": "HRN:24; BQT:2143; MON:317",
     "words": [
      {
       "translit": "afšândan",
       "gloss": "to spread, sprinkle",
       "script": "افشاندن"
      },
      {
       "translit": "afšûn",
       "gloss": "rake",
       "script": "افشون"
      }
     ],
     "script_extra": "افشان",
     "note": null,
     "quote": {
      "text": "بگیرم ادب را ببندم دو لب را - که تا راز گوید لب دُر فشانش",
      "poet": "Molavî"
     }
    },
    {
     "id": 8,
     "parent": 1,
     "lang": "Avestan",
     "refs": null,
     "words": [
      {
       "translit": "aiwiš-kar",
       "gloss": "chase (animals) away",
       "script": null,
       "see": [
        "Kwer"
       ]
      },
      {
       "translit": "aiwiš-tap",
       "gloss": "in heat, in a hurry",
       "script": null,
       "see": [
        "Tep"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 8,
     "lang": "Persian",
     "refs": "BQT:1275; HRN:172,174",
     "words": [
      {
       "translit": "šekâr",
       "gloss": "hunt",
       "script": "شکار"
      },
      {
       "translit": "šetâftan",
       "gloss": "to hurry",
       "script": "شتافتن"
      }
     ],
     "script_extra": "شتاب",
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 1,
     "lang": "Avestan",
     "refs": "AHM:220",
     "words": [
      {
       "translit": "abi-dasta, a-dasta, a-dsta",
       "gloss": "over hands, sleeve",
       "script": null,
       "see": [
        "Ghesto"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 10,
     "lang": "Persian",
     "refs": "AHM:220",
     "words": [
      {
       "translit": "âstîn",
       "gloss": "sleeve",
       "script": "آستین"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 0,
     "lang": "Old Persian",
     "refs": "POK:34",
     "words": [
      {
       "translit": "abiš, abiy, abi",
       "gloss": "over, above",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 0,
     "lang": "Greek",
     "refs": "POK:34; AHD:44",
     "words": [
      {
       "translit": "amphi",
       "gloss": "around, on both sides",
       "script": null
      }
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
      {
       "translit": "amphitheater",
       "gloss": null,
       "script": null
      },
      {
       "translit": "amphibious",
```


## [2026-09-04T19:38:01.322Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==43' POK_01.txt | head -80"
}
```


## [2026-09-04T19:38:02.120Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: m̥bhi\\|lemma: ambhi\\|lemma: m̥bhi\\|ambhi\" POK_full.txt | head -20"
}
```


### [2026-09-04T19:38:03.087Z] TOOL RESULT

```
  Schulze  Lat.  Eig.  541;  mit  ^t-Erwei-   ; terung  (nach  pos-t,  per-t,  Bück  Elementarbuch  65)  osk.  ampt  ,circum^  (wie  9 umbr.  ambr-  zunächst   auf   Grund   des   aus   amf-  vor   Kons,  vereinfachten am-);  alb.  mbi,  mbs  ,bei,  auf,  an^   (G.  ^leyer  Alb.  Wb.  265).
^mbhi:  ai.  abhi-tah,  av.  aiwito  ,zu  beiden  Seiten,  rings^  (über  av.  aibis, apers.  abis  strittiger  Bed.  s.  Pedersen  KZ.  40, 127,  Bartholomae  IF.  19,  Bei- heft S.  106;  die  Endung  -s  in  geschichtlichem  Zusammenhang  mit  der  von gr.  &{.iq)ig?)]  ai.  abhi  kann  in  der  Bed.  ,um*,  apers.  abii/,  av.  aibl,  aiicl in  der  Bed.  ,über,  in  betreff  von^  aus  *mbJii  stammen  oder  idg.  *obhi oder  *ebhi  fortsetzen;  gall.  a mb i-  ,um^  (z.  B.  'A^ßi-ÖQavoi  ,die  am  Fl.  Dra- vos  Wohnenden^),  cjmr.  am-  (durch  i-Umlaut  em-,  ym-),  corn.  bret.  am-, em-,  air.  imb-,  imm-  ,um^;  ahd.  as.  umbi,  aisl.  umb,  ags.  ymb,  ymbe  ,um' (im  Gor.  von  bi  aufgesogen).
bhi'.  got.  bi  in  der  Bed.  ,um^,  mit  Auslautdehnung  in  betonter  Stellung as.  ags.  be-,  bl-,  ahd.  bi-,  bl-,  nhd.  bei  (über  zweifelhafte  Ableitungen  s. Falk-Torp  37  und  1437  unter  bil  II  ,Zwischenraum,  Zeitraum',  73  und 1437  unter  billede  ,BM').
ambhö(u)  ,beide':
Gr.  äuipo)  ,beide'  (Ableitung  a^Kpörsgog)]  lat.  ambö,  -ae,  -ö  .beide';
35
i\  7thhäii  , beide';  av.  uiva-  ds.;  11t.  ahii,  aksl.  oha  ds.;  ^ot.  bai  m.,  ha  n., Gen    *baddje  (hajöps,  s.  zur  Bildung    Brug-mann  .Grdr.  IP  2,  77;    anders
   j,^j  Auso'ang   zu  lat.  nosträtes  —  Fick  III'*  255)^    as.  hü  thie,    ags.  6^^
ha  eno'l.  ^o^^^;  ''^^^d.  ieit/e^  hede,  Viwovdi.  bäder,  Gen.  beggja  ^beide^  (;  g'ot. *baddje  <  baiie)-   toch.  A  6i7?ipz,  ämpe,  B   ant-api.
Von  diesen  wurde  ai.  ubhäu,  av.  «it;a  bislier  als  Zusammeiisetzurg  mit einem  u-  ^zwei^  (lat.  uiginü)  betracbtet;  Sommer  IF.  30,  404  leugnet  ein solcbes  u-  und  betrachtet  die  ar.  Formen  als  durch  den  Labial  bewirkte Verdumpfung-  eines  *  abhält  =  "^mbhöu  unter  Berufung  auf  ai.  Kuber  a-h aus  *Kaberah  (vgl.  Patronymikon  Käberaka-Ij;  Wackernagel  KZ.  41,  314ff.). Lit.  cibü^  aksl.  oba  beruhen  wobl  auf  Umbildung  von  "^amb-o .  zu  einer Zeit,  als  die  Präp.  ^ambhi  ,um'^  zugunsten  von  'f'obJii  (ab.  ob^^  s.  lat.  ob) aufgegeben   wurde.
Das  Verhältnis  *ambhö{ii),  *ambJii :  got.  usw.  bai^  bi  läßt  es  kaum  zweifel- haft sein,  daß  am-  (vielleicht  aus  4.  an-)  ein  erstes  Kompositionsglied
```


### [2026-09-04T19:38:03.134Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:38:11.432Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==42' POK_01.txt | tail -30"
}
```


## [2026-09-04T19:38:12.799Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ambh\\|^m̥bhi\\|ambhi\" AHD_watkins1985.txt | head -20; echo ---; grep -n \"amphi\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T19:38:12.972Z] TOOL RESULT

```
 Grube'^ Xdrta&og  ;,Sauerampfer^  als  ßoTdvrj  'AevcuTtArf  in  der  Bedeutungsfärbung (^ausleeren,  eingefallen^)  doch  erheblich  ab.  Ganz  fragwürdig  auch  alb. (Jokl  SBAk.  Wien  168^  I  48)  laps  ^bin  müde,  überdrüssig^
Ob  hierher  hett.  al-pa-an-da-  (alpant-)  ^krank,  schwach'^?
WP.  I  92,  Couvreur  H  106 f.,  WH.  I  786,  Hirt  Idg.  Gv.  11,  158.
älu-,  älo-  ^bittere  Pflanze?^
Ai.  ähl-Ij,  älukdm-  ^hulbus,  radix  globosa  esculenta^;  lat.  äliim^  älium Jvnoblauch^,  osk.  *allö  aus  *aUä  wohl  als  Grundlage  von  gr.  dXXäq  ,Wurst^; lat.  älum  oder  alus  ^Symphytum  officinale  L.,  Beinwell,  Wallwurz^  eine  um ihrer  Wurzel  willen  geschätzte  Pflanze  (vielleicht  gall.  Wort?  s.  Thesaurus).
WP.  I  90  f.,  WH.  I  30,  33.  Wohl  zum  Folgenden.
alu-  (-d-,  -t')  ,bitter,  Bier,  Alaun^
Gr.  dXvd(p)ip,ov'  Ttiv.QÖv  Ttagä  2(b(pQ0vi  Hes,,  aXuöf-ialveiv'  [TtiycQaivsLv?] lies.  (s.  aber  zur  Bed.  Herwerden  Lex.  Graec.  suppl.  45);  lat.  alüta ,Alaunleder^  und  alämen  ,Alaun^  sind  einfach  Erweiterungen  von  *alii-. Die  Wurzel  erscheint  in  Nordeuropa  mit  der  Bedeutung  ,Bier,  Met' (zu  der  Bedeutungsdifferenz  vergleiche  ksl.  kvas^  , Alaun,  Bier^);  an.  gl n.  ,Bier,   Trinkgelage^,   gldi-   n.    .Trinkgelage'    (*alupra-),    ags.   ealu(d)  n.
3
34
f
,Bier',  as.  in    alo-fat,  mlid.   in   al-schaf  /rrinkg-efäß';  daraus  entlehnt  api alu    n.    ;,Met^,    lit.    alvs    (m.    geworden    wie    medfis  =  preuß.    meddo   n.;1 J.  Schmidt  Pluralbild.   180),  ksl.  oh   (m.  geworden  wie  medi,)  ß'ier'.   Aus' dem  Germ,  ist  auch  iinn.  olnt  ,Bier^  entlehnt. WP.  I  91,  WH.  I  34.
amhhi,   mbhi  ,um-herum,   zu    beiden    Seiten^,  auch   amhhö{u)   Du.  ,beide und  ähnliche  auf  -hhl,  -hho-  ausgehende  Formen. Arm.  amlolj   ^vollständig,   unversehrt^   (zu    oij  .gesund^),   gr.  ^iicpi  ,um' (cc(.i(pl-g  ,zu  beiden  Seiten',  mit  demselben  Adverbial-s  wie  z.  B.  ^'i//,  )uy,oi- cpig,  s.  Brugmann    Grdr.  IP  2,  737);   lat.  amh-   (vor  Vokal,  z.  B.  amhigö), am-,  an-  (vor  Kons.,  z.  B.  amputö,  amiciö  aus  *aw[6i]yacio)    untrennbares Präfix  ,herum,  um,  ringsum*^,  alat.  auch  Präp.  am  ,circum^  m.  Akk.  (ambi- im  Sinne  von  ,beide^,  den  auch   anceps  zeigt,   ist   dagegen   späte  Bildung zu  amhö),  umbr.  amh-  (amholtu),  a-  (ci-ferum  ,circumferre^),  an-  {an-ferener ,circumferendi^),   osk.    amvianniid   ,circuitu,    Umweg^,    amnüd   ,circuitu, causä^  (kaum  *-amh-heno-  :  venia,   sondern  720-Ableitung,   s.  v.  Planta  II  32, 623);    mit    -e7'-Erweiterung    nach   j9?'ae^e?--eö,    intereö   (s.  v.  Planta  II  455, WH.  I  36),  umbr.  ampretu,  ambretnto  ,ambito,  ambiunto^,  vielleicht  auch  i! osk.  amfret   ,ambiunt^   (eher  nach    Schulze   KZ.  45,  182=  Kl.  Sehr.  468  ^ in  *am-ferent  ,circumferurit,  TtSQiayovOi'  zu  zerlegen;    keine   lat.  Spur  der gleichen  -er-Erweiterung  in  amfräctiis  , umgebogen^,  das  vielmehr  aus  am- fräctus)-  über  den  ON  Amiiernum  s.
```


### [2026-09-04T19:38:13.026Z] TOOL RESULT

```
<persisted-output>
Output too large (50.9KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b6edk9v3t.txt

Preview (first 2KB):
261:ag-. To drive. 1. Latin agere, to do, act, drive, conduct, lead: ACT, AGENDUM, AGENT, AGILE, AGITATE; (ALLEGE), AMBAGE, AMBIGUOUS, (ASSAY), (CACHE), COAGULUM, COGENT, ESSAY, EXACT, (EXAMINE), (EXIGENT), FUMI- GATE, INTRANSIGENT, LEVIGATE, LITIGATE, NAVIGATE, OBJURGATE, PRODIGAL, RETROACTIVE, SQUAT, TRANS- act. 2. Greek agein, to drive, lead: -AGOGUE, AGONY; ANAGOGE, (ANTAGONIZE), CHORAGUS, DEMAGOGUE, EPACT, GLUCAGON, HYPNAGOGIC, MYSTAGOGUE, PEDA- GOGUE, PROTAGONIST, STRATAGEM, SYNAGOGUE. 3. Suf- fixed form *ag-to- in Celtic *amb(i)-ag-to-, “one sent around” (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSA- DOR, EMBASSAGE, (EMBASSY). 4. Suffixed form *ag-men- in Latin agmen, a train, a moving forward, a marching column, group: AGMINATE. 5. Suffixed form *ag-ti-, “weighing” (Greek agein, “to lead,” has a sense “to weigh”), whence adjective *ag-ty-o-, “weighty,” in Greek axios, worth, worthy, of like value, weighing as much: AXIOM; AXIOLOGY, CHRONAXY. 6. Possibly suffixed form *ag-ro-, driving, pursuing, grabbing, in Greek agra, a seizing: PELLAGRA, PODAGRA. Derivative agro-. [Pok. ag- 4]
...
</persisted-output>
```


## [2026-09-04T19:38:16.926Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ambhi\\.\" AHD_watkins1985.txt | head; echo \"---entry---\"; grep -n \"^ambhi\" AHD_watkins1985.txt | head"
}
```


### [2026-09-04T19:38:16.986Z] TOOL RESULT

```
280:al-1, Beyond. 1. Variant *ol-, “beyond,” in: a. suffixed forms “*ol-se-, *ol-so- in Old Latin ollus in Latin ille (feminine illa); “yonder,” that: ALARM, ALERT, ALLIGA- TOR; b. suffixed forms “*ol-s, *ol-tero- in Latin uls, *ulter, ultra; beyond: OUTRE, ULTERIOR, ULTIMATE, ULTRA-, UTTERANCE®, 2, Suffixed form *al-tero-, “other of two,” in: a. Latin alter, other, other of two: ALTER, ALTER- CATE, ALTERNATE, ALTRUISM; SUBALTERN; b. Latin adulier, “one who approaches another (unlawfully), an adulterer” (ad-, to; see ad-), hence adulterdre, to commit adultery with, pollute: ADULTERATE, ADULTERINE, ADULTERY. 3. Extended form *alyo-, “other of more than two,” in: a. Germanic *aljaz (with adverbial suffix) in Old English elles, else, otherwise: ELSE; b. Latin alius, other of more than two: ALIAS, ALIEN; ALIBI, ALIQUOT, HIDALGO; Cc. Greek allos, other: AGIO, ALLO-; ALLEGORY, ALLELOMORPH, MORPHALLAXIS, PARALLAX, PARALLEL, TROPHALLAXIS. [Pok. 1. al- 24.] al-2, To wander. 1. Latin ambuldre, to go about, walk (ambi-, around; see ambhi): ALLEY!, AMBULATE; FU- NAMBULIST, PREAMBLE. 2. Latin exsul, exul, wanderer, exile (ex-, out; see eghs): EXILE. [Pok. 3. al- 27.] al-3, To grow, nourish. I. Suffixed (participial) form *al-to-, “grown,” in: 1. Germanic *alda- in: a. Old Eng- lish eald, ald, old: ALDERMAN, OLD; b. Old English (comparative) ieldra, eldra, older, elder: ELDER}; c. Old English (superlative) ieldesta, eldesta, eldest: ELDEST; d. Germanic compound *wer-ald-, “life or age of man” (see wi-ro-). 2. Latin altus, high, deep: ALT, ALTIMETER, ALTO, HAUGHTY, HAWSER; ALTITUDE, ALTOCUMULUS, ALTOSTRATUS, ENHANCE, EXALT, HAUTBOY. II. Latin alere, to nourish: ADOLESCENT, (ADULT), ALIBLE, ALI- MENT, ALIMONY, ALTRICIAL, ALUMNUS; COALESCE. III. Suffixed (causative) form “ol-eye- in Latin abolére, to retard the growth of, abolish (ab-, from; see apo-): ABOLISH. IV. Compound form “pro-al- (pro-, forth; see per’) in Latin prélés, offspring: PROLAN, PROLETARIAN, PROLIFEROUS, PROLIFIC. V. Extended form *aldh- in Greek althein, althainein, to get well: ALTHEA. [Pok. 2. al- 26.] al-4, To grind, mill. Suffixed form ‘*al-euro- in Greek aleuron, meal, flour: ALEURONE. [Pok. 5. al- 28.] [al-5. All. Germanic root. Suffixed form *al-na- in Ger- manic *allaz in Old English all, eall, eal-, al-, all: ALL; ALSO.] albho-. White. 1. Possibly Germanic ‘*albiz, *albaz, if meaning “white ghostlike apparitions,” in: a. Old Eng- lish e/f, elf: ELF; b. Old Norse alfr, elf: OAF; c. Old High German Alberich, “elf-ruler,” akin to the source of Old French Auberon: OBERON. 2. Latin albus, white (> Old Spanish alba, dawn): ABELE, ALB, ALBEDO, ALBESCENT, ALBINO, ALBITE, ALBUM, ALBUMEN, ALBURNUM, AU- BADE, AUBURN; DAUB. 3. Greek alphos, dull-white lep- rosy: ALPHOSIS. [Pok. albho- 30.] alek-. To ward off, protect. Earlier form *olek-. 1. Suf- fixed zero-grade form “alk-d- in Greek alké, strength: ANALCIME. 2. Extended form *aleks- in Greek alexein, to protect: ALEXIPHARMIC. [Pok. aleg- 32.] algwh-. To earn, be worth. Sanskrit arhati, he is worthy: ARHAT. [Pok. algvh- 32.] alu-. In words related to sorcery, magic, possession, and intoxication. Suffixed form *alu-t- in Germanic *aluth- in Old English (e)alu, ale: ALE. [Pok. alu- 33.] ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
---entry---
```


## [2026-09-04T19:38:20.520Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',errors='ignore').read()\ni=t.find('ambhi. Also mbhi.')\nprint(t[i:i+1600])\nEOF"
}
```


### [2026-09-04T19:38:22.034Z] TOOL RESULT

```
ambhi. Also mbhi. Around. Probably derived from ant-. 1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) in: a. Old English bi, bi, be, by: By}; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-; C. Middle Dutch bie, by: BILANDER; d. Old High German bi (> German bei), by, at: Brvouac. 2. Germanic *umbi in: a. Old English ymbe, around: EMBER DAY;
ang"hi-
b. Old Norse um/(b), about, around: OMBUDSMAN; c. Old High German umbi, around: UMLAUT. 3. Latin ambi-, around, about: AMBI-. 4. Greek amphi, around, about: AMPHI-. 5. Celtic *ambi (see ag-). [Pok. ambhi 34.] ambhé. Both. 1. Reduced form *bAd in Germanic *b6-, *bé in Old Norse bdthir, both: BOTH. 2. Latin ambé, both: AMBSACE. 3. Greek amphé, both: AMPHOTERIC. [In Pok. ambhi 34.] amer-. Day. Suffixed form “Gmer-d in Greek hémera, day: EPHEMERAL, HEMERALOPIA. [Pok. dmer- 35.] ames-. Blackbird. 1. Suffixed variant form *ams-ol- in Old English dsle, blackbird: ouzEL. 2. Suffixed variant forms *mes-old, *mes-olo- in Latin merula, merulus, merle, blackbird: MERLE, MERLON. [Pok. ames- 35.] [amma. Various nursery words. Latin root. 1. Medieval Latin amma, mother: AMAH. 2. Reduced form *am- in: a. Latin amare, to love: AMATEUR, AMATIVE, AMATORY, AMORETTO, AMOUR; ENAMOR, INAMORATA, PARAMOUR; b. Latin amita, aunt: AUNT; c. Latin amicus, friend: AMICABLE, AMIGO, AMITY; ENEMY, INIMICAL.] an’. On. Extended form *ana. 1. Germanic *ana, ané in: a. Old English an, on, a, on: ON; b. Old Norse 4, in, on: ALOFT; ¢. Old High German ana (> Middle High Ger- man ane), on: ANLAGE; d. Middle Dutch aan, on: ON- SLAUGHT.
```


## [2026-09-04T19:38:31.359Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',errors='ignore').read()\ni=t.find('ambhi. Also mbhi.')\nleaf=t[:i].count('\\f')\nprint('leaf',leaf,'printed?',leaf-29)\nEOF"
}
```


### [2026-09-04T19:38:32.813Z] TOOL RESULT

```
leaf 31 printed? 2
```


## [2026-09-04T19:38:46.400Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 22 23 24; do echo \"===== HRN printed p.$p (leaf $((p+21))) =====\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-04T19:38:47.888Z] TOOL RESULT

```
===== HRN printed p.22 (leaf 43) =====
- 22
niesen, an. hnjosa, mittelengl. fnesen niesen', ver-
schieden von mittelengl. snesan, engl, to snee:se
(Kluge, Etymolog. Wörterbuch).
kurd. heenlsum *ich niese' (Justi, No. 66, wo auch
die Etymologie).
Die neupersische Grundform müsste *senöse sein.
91. ef-, ew-, Praefix, ß-, fu-,
ap. abiij 'herzu'; aw. aihi, aiwi *herzu, oben' etc.;
phlv. a/-, päz. awa-; ai. abhi 'herzu, oben' etc.
92. uftäden ^fallen', Praes. uft-em, fitaden, uftädegt
(Sa dl, Bostän 4, 1 Graf).
aüa-\- [/^pat'\ phlv. öftätan, öftet (vd. 6, (73) Gl.,
16, (20) Gl.), öftad (vd. 19, 94), oft falle (Göät-I Fr.),
vergl. öfttnltan, äwäZ'öft(i)smh (vd. 16 (64) Gl.),
öft(i)sn (Ys. 43, 4, aw. avapasti-) ^).
Im Neupersischen findet sich bei Dichtern noch
öf laden (die Aussprache mit ö ist allerdings nicht
bezeugt), z. B. Vis und Rämin, S. 61, Vers 5 v. u..
Sahn. I, 88, Vers 494, Sa di, Gul. (Sprenger), 38 Zeile 9.
93. efräiten 'erheben', efrästen, Praes. efräz-em, ewrästen,
ewraz (AM.), ini^N^DN (jüd.-pers.).
phlv. afrästan {afrä/tan zu lesen?) erheben.
Zu [/reg- + ahhi richten, aufrichten'; ai. irajydti
er richtet'; gr. oQfyw^ oQsyvv/Lu Vecke'; lat. rego richte';
got. uf-rakjan 'in die Höhe recken'.
wa;^. püt\rüzam, sar. pat\räzam 'sich recken, gerade
stehen'.
So viel ich sehe, ist die nahe liegende Etymologie
vor KZ. 32, 579 No. 4 noch nicht ausgesprochen
worden.
(Wohl die ersten zwei Misrä^'s eines Rubä*l)
cHn sepled ez m^y-l mü*ambär-t ^öse
göyed k*ekimn nemänd^ jäi/'i senöse
Minöcihrl.
*) Bevorzugter ist im Pehlevl öpa^tan.
===== HRN printed p.23 (leaf 44) =====
OQ
94. efrö^/ten anzünden, erleuchten', Praes. efröz-em^
ewrö/fen [heme-werözT AM. 239 Zeile 1 v. u.), jn5n5N,
furö/ten, furözis^ furöy etc.
aw. aiwi + [^ruc- 'anzünden*; phlv. afröxtan,
a/röcmn, afröcimtan ; skr. abhi + [/'ruc- 'leuchten'.
kurd. vergl. ci]rüstin 'leuchten', dici\rüsi (3. Sg.).
95. ef%är 'Werkzeug', ewzar 'Organ' (AM.).
phlv. afzär 'Werkzeug, "ITZN (Talmud).
Zu ai. 1 V^hur-, Nöldeke, ZDMG. 32, 408.
96. efzuden 'zunehmen, vermehren*, Praes. efzdy-ew,
eirzäden (AM. ; hah-wezäi, 235 Zeile 2), fuzüden, efzün^
fuzün^ efzayis etc.
aw. "^aiwi + \/ snv-, sävaijät 'er wird nützen';
phlv. afzütan^ ofzün^ afzüntk^ afzäyltan, afzäyimtan,
afzäy(i)sn,
97. efsär 'Zügel, Zaum', ßsar.
aw. ^aiwisdra-; phlv. afsdr (Bund.),
syr. talmüd. LW. 1DCN.
98. efsän 'Wetzstein', eusän,^) fesän, vergl. sün,
phlv. afsän (Säy. Näääy. 10, 28); skr. gäna-^) 'Wetz-
stein* + abhi; vergl. B.rm. yesan (H. No. 211).
wa;f. sar. pasän ^Wetzstein'.
99. efser 'Krone'.
aw. ^aiwisara-; phlv. afsar 'Krone' (6ö§t-T Fr.)^).
100. efsurden 'frieren', gefrieren, fusurden^ ßsurden
(Sahn. I, 78 Vers 211).
phlv. afsartan, afsar(i)smh (vd. 19, 12), vergl. arm.
surf, 'Kälte'.
Siehe np. serd (No. 731).
101. efsös 'Spott, Scherz', fisös,
phlv. afsös 'Spott, Scherz'.
Darmesteter's Erklärung, Et. ir. II, 131 aus aw.
*aiwisaoca' ist unhaltbar, da aw. d im Np. nicht zu s
werden kann.
*) ewsün (Vullers).
*) Zu dem n vergl. Joh. Schmidt, KZ. 32, 385.
*J West*, S. 175: awüar; ZPGl. 24, 10; awavBar.
===== HRN printed p.24 (leaf 45) =====
— 24 —
102. ef San den ausschütten', ^'sawrfew.
aw. aiwi + ßünayeinü *sie weiden aus , yt. 14, 56
(Geldner, 3 Yasht, 88) (?); phlv. aßäntan,
103. ef gen den 'wegwerfen', ßgenden^ ewgenden (AM.),
jn::5x (Is. 14, 12).
Kaum etwas anderes als aw. aiwi + [^kan-, wenn-
schon die Bedeutung nicht passt; phlv. afgantan
(Bund.) 'wegwerfen'.
Ein ganz anderes Verbum scheint efgenden, ewgenden
einfüllen, auffüllen zu sein, vergl. AM. 82 Zeile 1 *in
die Harnröhre einführen, einfüllen , 145 Zeile 3 v. u.
'in die Nase einführen, einfüllen* u. ö. (mit und ohne
bäz, letzteres z. B. 50 Zeile 4)^). Post häz ewgened
bei demselben Autor ^bewirkt Abschuppung der Haut'
(140 Zeile 2) gehört natürlich zu efgenden wegwerfen'.
Die Bedeutung auffüllen findet sich dagegen noch in
htm efgenden 'das Fundament auffüllen, den Grund
legen* (Sahn. I, 8 Vers 42 u. o.), synonym mit pei
efgenden (Sahn. I, 48 Vers 262). Ebenso wird die
bei AM. häufige Bedeutung verursachen, z. B. 173
Zeile 8 fBlasenstein), 164 Zeile 10 ('Jucken), 243
Zeile 4 v. u. ('Krankheit') hierher gehören.
Efgenden 'einfüllen, auffüllen' wird zu np. ägenden
(No. 41) zu stellen sein.
104. ek 'Schimpf, Schande, Unglück', ak'^),
aw. aka- *böse. Böses; skr. aka- 'Schmerz, Sünde'
(spät).
*) Als medicinischen t. t. vergl. Abdul Aohundow, Commentar
zum sog. Liber fundamentorum phaemaoologiae des Abu Mansur
Muwaffak-Ben- Ali-el-Hirowi , Dorpater medicinische Doctordissertation
1892, S. 18.
') FR und FJ haben die folgenden Belege (die zweite Stelle ist
in der Strassburger Handschrift des FJ sehr liederlich geschrieben):
äke n^reslde her tu ez men
sed bär^ tnerä zi tu resed äk
m
Sözeni, Metr. Hezej.
an flgende becäh^ behr-i ^em,
oän b^hä'kerd^ kern behezde direm
Senäl, Metr. Xeflf.
```


## [2026-09-04T19:39:08.237Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB p.16 (leaf 26) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==27' HUB.txt; echo; echo \"=== HUB p.15 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==26' HUB.txt | tail -25"
}
```


### [2026-09-04T19:39:10.110Z] TOOL RESULT

```
=== HUB p.16 (leaf 26) ===
— It) —
— ap. *ava-pa8tanait/ (vgl. zd. avapasti- 'das Herab-
fallen) als Neubildung. Ich nehnie daher— wie Mann-
Andreas ZDM6. 47, 702 — an, dass OftGdan zum
Praesens oftad nach dem Muster von ^tadan = praes.
estad gebildet ist. Schwierigkeit macht nur die Bildung
des Praesens, denn Dftad setzt ein ap. ^ava-ftatiy = skr.
*ava'ptati (nach der 6. indischen Klasse von der Wrzl.
pat gebildet^) voraus, das sonst nieht vorliegt. Nach
dem Intinitiv hat sich wie gewohnlich das Particip
gerichtet, daher uftada *lapsns, vastatus, humilis, sub-
missus etc. fur das ursprungliche ptc. ^pasta^ (skr.
patita-), das ich in np. past parvus, depressus, planus,
devastatus, humilis' wiederfinde.-)
93. Np. afraxad ist nach Horn's richtiger Etymologie
(Wrzl. reg^ in ogiyto u. s. w.) — zd. aiwi + razay^iti
(vgl. zd. rdzayfAti 'ordnet', osset. araztn rich ten), also
afraktan der ursprungliche, afraxtan der (nach Analogie
von afrozam : afroxtan u. s. w.) neu gebildete Infinitiv.
Ebenso jetzt Fr. Miiller, WZKM. 8, 186.
95. Np. afzar Werkzeug* (bal. LW. auzar) ~ phi. afzar
geht nach ZDMG. 32, 408 auf ein ap. ^ahizara-, nicht
*abidara- zurtick. Daher bleibt arm. ddar 'arredo, for-
nimento, rimedio* etc. (das Fr. Miiller wieder heran-
zieht) besser weg. Mit ap. ^abizara- deckt sich laut-
lich skr. abhihara-^ das aber 'Herbeibringung, Raub* etc.
bedeutet.
96. Aus aiwi -\- savay^iti ware im Neup. ^afsdyad ge-
worden: das vorliegende afzayad Vermehrt' muss auf
*aiwizavayfiti zuriickgehen % das sich vielleicht zu skr../t^
^) Vgl. skr. avapatati *fallt herab* nach der 1. Klasse.
*) Vgl. afgh. LW. ufiSUiq 'humble, meek' neben afgh. LW. past
*low, abject, lower, below'.
') Bei solchen Reconstructionen mUssten eigentlich imm'er die
altpersischen Grundformen angesetzt werden. Da aber die (vorhandenen)
Zendformen hftufig fiir die (fehlenden) altpersischen eintreten mCLssen,
erlaube ich mir hier mehrfach, das Neupersisohe direkt an das Zend
anzuknupfen, wie auch andere Gelehrte thun.
i

=== HUB p.15 ===
schrieben sein ^) und so dem np. uifndn genau ent-
sprechen, mit dem es auf ap. ^usnctna- = zd. *usnana'
(vgl. zd. uS'Snd Vaschen* und wegen sn fiir sn : ap.
vasna = zd. vasna u. ahnl.) zuriickgehen k5nnte. Ap.
^abisnana^ ware zu np. *afsnan = arm. *ausnan^ osnan^)
geworden.
90. Die germanischen W5rter fiir 'Niesen' fiihrt Kluge auf
die Wurzein vorgermanisch qnus^) und ksmis zuriick."*)
Bildet man aus letzterem ein vorgerm. Substantiv
*ksnoMso- und ubertrS-gt dies ins Iranische, so erhalt
man iran. "^x^nauSa- = phi. *snOsak = np. iSnoSa.
Leider ist die Wurzel ksnus sehr hypothetisch.
92. Np. iiftddan ^fallen* aus oftatan (Gl. and Iiid. 45) von
Wrzl. pat scheint zunachst eine Bildung wie gr. nrwaig^)
von Wrzl. pet {Trl-nT-to), erweist sich aber durch phi. opastan
*) Vgl. aitsakf dSak fur osak — np. wla, arab. pers. tiSSoq 'gummi
ammoniacum'.
*) Vgl. np. afsarn = arm. auSarak, dSdrak,
') qmts — germ, hmts und fnus, vgl. N o r e e n , Abriss der
urgerm. Lautlehre p. 148.
*) Fiir ksnus setzt N o r e e n , Arkiv for Nordisk Filologie 1886,
III. p. 19 : skntts an (nach K 1 u g e ^ s Mittheilung). Beide Wurzein
sind durch Addition der yerschiedenen Formen entstanden.
*) Vgl. TTTijnoficei^ ^nrrjv Yon pta au8 ptoi (Bartholomae,
Stud. II, 183) neben niro/uai.
```


## [2026-09-04T19:39:19.221Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 172 173 174; do echo \"===== HRN p.$p =====\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-04T19:39:20.823Z] TOOL RESULT

```
===== HRN p.172 =====
— 172 -
phlv. östaftan ') (vd. 7 (27) GL, 18 (98), Meii.) eilen,
arm. LW. staij, davon Denomin. stapim 'eilen.
aw. *aiwis + l^tap-, täpaj/eiti *iri Wärme, Hitze
bringen', dann tropisch-).
Zu aiwis vergl. oben np. hes- (No. 221).
778. sHden gehen; sein, werden', Praes. sev-em.
ap. \/^siya€', aslt/avam, asiyuva 'gehen, marschiren';
aw. {/sav-, suvaite'^) gehen'; ai. [/^cyav-, Ci/dvate 'fort-
gehen ; arm. cit 'Aufbruch', ciiem 'aufbrechen' (H.
No. 242).
kurd. eleu 'gehen', dicm; sify, soal 'werden, gehen';
oss. d. t. cäün 'gehen, schreiten, spazieren, fahren'
(319) ; bei. suta, siit, n. suöa, iud^a (322) ; wa;^. cduam,
si/n. oi\zafcam, sar. va]zevsam.
779. siirrän, serrün 'unablässig lliessend', slrän Kegen' (y),
sun-iden^), vergl. sär {äbsär), särulen, ,
ai. l^ksar-, ksdrati 'fliessen, strömen' (Geiger,
Etym. d. Bai. unter No. 66; bei. ö[ur 'Giessbach'
kann aber nicht verglichen werden, s. Htibsch-
mann, ZDMG. 44, 556).
780. Herrn 'Schaam'.
aw. fsarema- 'Schaam'; phlv. sarm *Schaam', sarm-
[gas 'Genitalien' (vd. 16 (5) Gl.).
oss. t. äfsdrm, d. äfsänni 'Schande' (121) ; LW. aty.
bei. (253) sarm 'Schaam', kurd. serm,
781. sest, sest 'sechzig*.
aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
kurd. FD. LW. sest; afy. speta,
782. susten Vaschen', Praes. söy-em^),
phlv. sustan, söyBnd^ söy(i)sn; kurd. LW. sustin
'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
*) Pfiz. qastäftun^ qastäwidan (Men.) ist Unsinn.
*) An ursprüngliches ^sila^ten (vergl. jjuft aus jf*x^) darf man
wegen Praes. siiäb-em natürlich nicht denken.
^) Bartholomae, Ar. Forsch. III, 33 liest staitc.
*) Zum Teil unbelegt.
^j Reimt auf higöyetl, Vis und Rämln S. 70 Vers 6.
===== HRN p.173 =====
— 173 —
södafj , n. sööay, sözay Vaschen, reinigen, baden-
(373).
Passt lautlich, aber nicht der Bedeutung nach zu
a\v. \/^xsaod' *fliessen', während das Umgekehrte für
ai. I ^förfA-, nimUiafi reinigen gilt. Hübschmann,
ZDM6. 44, 560 beanstandet daher die Zusammen-
stellung (doch vergl. Bartholomae, Studien II, 42
und No. 785, 795).
Das Verhältniss des Praes. sürem {*sörem (?); vergl.
auch Kä§.-Dial., jüd.-pers. Is. l, 1(5) zu söi/em ist
nicht klar^).
ses 'sechs'.
aw. /S2?flf^ *sechs': phlv. saä^ sasnm; Sii. sds; arm.
vec (H. No. 26(>).
kurd. LVV. ses; afy. spag; oss. d. t. äx^^äz (45);
wa;f. säl, säd, siyii. /aus etc.
784. snM 'Lunge'.
g. svs,
aw. SKsi' *Lunge* (ZP61.); phlv. sus; ai. vergl.
\/^gvas-, gvasiti ^schnaufen rvasand- *blasend, zischend,
schnaufend*, skr. cvkä?- 'Wind' 2).
afy. sayai; wa;^. LW. sifs, sar. sül.
785. seyäl 'Schakal'.
skr. g^gäld' (die Schreibung srgald- ist wohl falsch)
*) Eine Form äöä/, wie Vamb^ry ZDMG. 45, 414 druckt, giebt
es nicht und hat es nie gegeben. Allerdings wohl bisher auch noch
nicht eine derartige Behandlung eines persischen Textes wie sie die
Gedichte persischer Frauen hier erfahren. Der Autor bezeichnet sich
in seiner *Rei8e in Mittelasien' und in seinen 'Wanderungen und Er-
lebnissen in Persien' durchweg als einen genauen Kenner des Porsischen;
in dem letzterwähnten Buche, 8. 346 der deutschen Ausgabe, spricht or
von seiner 'eleganten persischen Sprache*. Der Leser des Aufsatzes in
der ZDMG. wird hiervon wenig spüren, wenn er nicht gar schon von
vornherein durch die wahrhaft imponirende Nichtbeachtung der ein-
fachsten Regeln persischer Metrik fdie natürlich nicht auf Rechnung
der Dichterinnen kommt) von der Lektüre abgeschreckt wird.
*) Verweis von Prof. Nöldeke. Die Bedeutung des Wortes ist
nbor nicht sicher, vergl. PW. s. v.
===== HRN p.174 =====
174
'Schakal'; plilv. sayäL LW. türk. caqal; ngr. rtjayuh;
deutsch Schakal etcJ).
Die neupersische Form muss statt *seyal stehen;
denn np. s vertritt nicht etwa ai. q\ Als bereits
arisch wird der Schakal auch in der neuesten (4.)
Auflage von Fick's Indog. Wörtbch. , S. 212, an-
genommen 2). über das heutige Vorkommen des
Schakals im Orient heisst es bei Brehm, Säuge-
tiere I-, 545: 'Der Schakal verbreitet sich' von Indien
mit Ceylon aus über den Westen und Nordwesten
des Erdteils, die Euphratländer, Persien, Palästina
und Kleinasien etc.*
In np. seyäl, sunüden (No. 795) und sä/ (No. 766)
entspricht s sicher sanskritischem ^•; andere Fälle
wie äs (No. 29) oder susten (No. 782) können zweifel-
haft sein, während die Zusammenstellung von np.
siften reiben, kratzen'^) mit aw. aiu)i]siföis, yt. 14, 35
(Geldner, 3 Yasht 77) geradezu falsch ist.
786. sikär *Jagd', vergl. hisgerd (No. 224), sikerden, sekere,
iskere 'Jagdhabicht'.
phlv. äkar Magd' (vd. 5 (134) Gl.), sakra Magdhabicht'
(Bund.).
oss. LW. sk'ärun 'treiben, jagen (v. Stackeiberg,
ZDMG. 43, 672)4).
aw. "^aiwis (doch vergl. No. 221) + [/^kar- (de
Lagarde, Beitr. z. altb. Lex. 42, Pers. Stud. 75);
aber dann gewiss nicht zu [/kar- 'tun, machen*, wie
de Lagarde will, sondern zu [/kar- in np. nigär^
niijerlden. Die ursprüngliche Bedeutung findet sich
^) Vergl. auch Miklosich, Denkschr. WAW. 34, 271; 37, 20.
^) Nach anderen wäre hebr. '^Ultfi? 'Fuchs', Schakal' damit identisch
(s. Rödiger-Öesenius, Wörterbuch, S. 1457).
') Die Grundbedeutung von np. sißen ist nicht klar. Mit AbuM
Ma*änl- Versen lässt sich nichts erweisen.
^) Schon Tomaschek, Centralasiat. Studien, II, 891 (wo auch
manches Falsche) hat das ossetische Wort zu dem neupersisohen
gestellt.
```


## [2026-09-04T19:39:38.184Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('CHEUNG.txt',errors='ignore').read()\nfor pat in ['afsār','afsar','šikār','sikār','škar','šitāb','šitāftan','afšāndan','afzūdan','afzāy','afkandan','afgandan','afrōxtan','afrāštan','āstīn']:\n    idx=[m.start() for m in re.finditer(re.escape(pat),t)]\n    print(pat, len(idx))\nEOF"
}
```


### [2026-09-04T19:39:39.853Z] TOOL RESULT

```
afsār 0
afsar 11
šikār 0
sikār 0
škar 0
šitāb 0
šitāftan 0
afšāndan 0
afzūdan 0
afzāy 0
afkandan 0
afgandan 2
afrōxtan 0
afrāštan 0
āstīn 0
```


## [2026-09-04T19:39:43.656Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c CHEUNG.txt && grep -n -i \"afgandan\" CHEUNG.txt | head -5; echo ---; grep -n -i \"ikar\\b\\|sikar\\|skar\" CHEUNG.txt | head -10; echo ---; grep -n -i \"afsan\\|afšan\\|fšan\" CHEUNG.txt | head -10"
}
```


### [2026-09-04T19:39:43.731Z] TOOL RESULT

```
1769485 CHEUNG.txt
15488:afgandan ‘to throw, cast away’ || (+ *upa- ?) Gil. (Rsht.) bägänæœstæ ‘struck against’ 
40688:afgandan, 231 
---
342:^ Т have further used on a large scale the dialect descriptions of Oskar Mann (“Kurdisch-persische For- 
726:Baskard) 
13339:*NWIR: NP laskar ‘army’ (dissim. loss of -x-, from *Hraxsa-kara-) 
15805:(+ *us-) BMP ’wsk’l- /uskar-/ (caus.) ‘to think, consider, discuss’ || (+ *pati-) BMP 
15806:ptk’1/pahikar-/ (caus.) ‘to request, claim, consult, MMP phykr, BMP ptkl /pahikar/ 
15807:‘picture, image’, MMP phyk’r, BMP рік? /pahikar/ ‘battle, struggle’ || (+ *ni-) 
15816:qyryhynd, SUBJ. 3sg. MMP qyryh'd || (+ *us-) Caus.: pres. IND. 3pl. BMP ’wsk’lynd /uskarénd/, 
15822:sk’lynynd /skarénénd/; Partic.: perf. pass. caus. BMP ’wsk’lt /uskard/ || (+ *pati-) Caus.: pres. IND. 3pl. 
22567:*skar 345 
22594:*skar ‘to pursue, drive, look for (the cattle)’ 
---
15400:tremble’, matching Skt. kamp. The Avestan form *kafsan (Yt 10.113), cited in Liste: 
24251:*MIDDLE PERSIAN: (+ *apa-) BMP ’ps’n- (PZKWN-) /afsan-/ ‘to spread, scatter, 
24254:Pres.: IND. 3sg. BMP /afsanéd/ 
24278:strike, swing’, Maz. Sanne ‘he shakes’ || (+ *apa-) NP afsandan/afsan-, Gil. (Rsht.) 
24674:Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
34943:"p3^n- /afsan-/, 371
```


## [2026-09-04T19:39:46.767Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22590,22640p' CHEUNG.txt; echo \"=== afsan ===\"; sed -n '24240,24300p' CHEUNG.txt"
}
```


### [2026-09-04T19:39:46.825Z] TOOL RESULT

```
PeSéereva: 326b; Klingenschmitt 1968: 158 Ё; EVS: 100b; WIM I: 69; WIM 11/1: 80; Steblin-Kamenskij 
1999: 331; Lecoq 2002: 654b 


*skar ‘to pursue, drive, look for (the cattle)’ 

*AVESTAN: ? Y Av. skar- ‘to pursue (?)'. 0 The meaning of the Av. compound YAv. 
skärailat.radahe (Yt 13.108), which seems to be a personal name, is unclear. Szeme- 
rényi 1970: 513 translates it as “he who speeds his chariot’. Alternatively, it can also 
be translated as ‘qui fait rouler son char’ (Kellens 1984: 144), which would have no 
further (DIr. correspondences. = Liste: 63 

Partic.: pres. caus. Y Av. skaraiiat- ‘pursuing ?’ (Yt 13.108) 

*MIDDLE PERSIAN: ВМР SkIk /Skarag/ ‘(bird of) prey’ || (+ *ui-) ВМР wskl /wiskar/ 
“hunting-ground, wilderness’ 

*PARTHIAN: ‘Skr- ‘to hunt, chase’ = Ghilain: 58 | DMMPP: 92a 

Pres.: IND. 3sg. * ‘Skryd, 3pl. ‘Skrynd; Partic.: perf. pass. “га 

*SOGDIAN: SSogd. (")skr-, BSogd. ’sk’r-, BSogd. sk’r-, CSogd. Sqr-, MSogd. škr- ‘to 
lead, take; pursue, persecute’ || (+ *apa- or *upa- or *pati-) BSogd. "pskr- ‘to chase’, 
(pass.) MSogd. pskyr- ‘to be chased’, CSogd. psk’r (m.) ‘persecution’ (C2 68V.13) || 
(+ *fra-) BSogd. ’Bskr-, CSogd. fSqr-, MSogd. fSkr- ‘to expel, drive out’ || (+ *ham-) 
BSogd. ’nskr- ‘to collect, gather’ 

Widely attested: Pres.: IND. 1sg. dur. BSogd. "Skr^m ’skwn, 2sg. BSogd. ’skr’y, 3sg. SSogd. ’Sk’rt, etc. || 
(+ *apa- or *upa- or *pati-) Pres.: IND. 3р1. BSogd. ’pskr’nt, ОРТ. 3sg. CSogd. pSqry; Partic.: perf. pass. 
CSogd. psqrtyt (pl.) ‘persecuted’; Pass.: pres. IND. 35р. MSogd. “pskyrtyy || (+ *fra-) Pres.: IND. 3sg. 
BSogd. ’Bskrt, Impf.: IND. 3р1. CSogd. fSqrnt || (+ *ham-) Pret.: intr. IND. 3sg. BSogd. ’nsk’rt, Partic.: 
perf. pass. BSogd. ’nskrtk, BSogd. ’nskrt’y, BSogd. ’nskrt, Inf.: BSogd. рг... ’nskr’y, Pass.: pperf. intr. 
IND. 3sg. BSogd. ’nskrt’y wm’t ‘had been collected’ 

*BACTRIAN: ор(о)кор-, ғркор- ‘to pursue, chase (off)! = S-W, Bact.: 184b 


346 *skard 


*NWIR: NP 3ikar ‘hunt’ (LW ?, < Sogd. ?) || (+ *ui-) NP bisgar(d) ‘hunter, fowler; 
place for hunting; chase; game’ 

*NEIR: Oss. I. sk’zryr/sk’zrd, D. (&)sk’zrun/(&)sk’ard ‘to chase (animals)’, (caus.) 
І. skaryn/skerst, D. skarun/skarst ‘to explore, look around, seek; to grope one’s 
way’, Sh. (Baj.) Xikar-/Xiküd, Rosh. Xikar-/Xiküg, Sariq. Xiker-/Xikawg, Yzgh. 
Xokor-/Xokord ‘to seek, search for’ (< LW ?, cf. EVS: 102a), Ishk. skarr-/skul ‘to 
seek’, Wa. Skar-/Skard- ‘to mate [of animals]’, Wa. Skur(g)-/Skurd ‘to seek’, Yi. 
Skör-/skär-, M. skör-/skar- ‘to send (a thing)’, ? Pash. skärol ‘to incite (against) || (+ 
*upa-) ? Sh. bixsar-/bixcud ‘to ladle, scoop up (grain, fluid)’ || (+ *pati-) (?) Sariq. 
paxéor-/paxcig, paxcug ‘to fill with water, grain (into receptacles from a store)’ 
=== afsan ===
Pres.: CSogd. ëmm, OPT. 3р1. CSogd. Symynt 

9 The existence of this root in PIr. is uncertain: it is not even clear whether the forms 
above are cognate with each other at all. 

*REFERENCES: Gershevitch, Mithra: 233; Nyberg II: 77a; Sims-Williams 1985: 180 ad 111V; Gharib: 
373,379 


*San ‘to shake (down ?)’ 

*MIDDLE PERSIAN: (+ *apa-) BMP ’ps’n- (PZKWN-) /afsan-/ ‘to spread, scatter, 
sow’ 

Pres.: IND. 3sg. BMP /afsanéd/ 

*PARTHIAN: (+ *aua-) wy8’n- ‘to shake off, down’ = DMMPP: 359b 

Pres.: IND. 2sg. wys’nyh, 3р1. ws^nynd, *wys’nynd, IMPV. 2р1. ws’nyd; Partic.: perf. pass. П wys’n’d 
*KHOTANESE: OKh. safi- ‘to shake down’ = SGS: 127 

*SOGDIAN: BSogd. sn-, CSogd. Sn- ‘to shake, tremble, shiver’ || (+ *pati-) BSogd. 


pts’nkh ‘cross, scaffold (?) || (+ *fra-) CSogd. fsn- ‘to tremble, cower’ 


372 *taé 1 


Pres.: IMPV. 2sg. CSogd. "ën": Impf.: IND. 3sg. BSogd. sn’ || (+ *fra-) Pres.: IMPV. 25р. CSogd. fin’; 
Fut.: IND. 3sg. CSogd. fSntyq’ 


*CHORESMIAN: Sny- ‘to tremble’ = Samadi: 198 

*NWIR: Zaz. Sanayis/Sanen- ‘to shake, scatter’, Bal. Sant/sän- ‘to throw, throw up, 
shake off’, Awrom. sanay/san- ‘to scatter, sow’, Gur. (Kand.) šän-á/-šān- ‘to throw, 
strike, swing’, Maz. Sanne ‘he shakes’ || (+ *apa-) NP afsandan/afsan-, Gil. (Rsht.) 
fisan- ‘to disperse’ || (+ *aua-) Vafsi ho-wsin-/wasenä ‘to shake down’ || (+ *ati- ?) 
Tt. (Owr.) do-sän- ‘to shake down’ || (+ *fra-) Kurd. (Kurm.) rasandin “о spread’ 
*NEIR: Pash. San- ‘to ransack, search, stir’, Sanaw- (caus.) ‘to shake, jolt, stir’ || (+ 
*apa-) Sh. biyen/biyent, (Baj.) biwen-/biwent ‘to shake (fruit, nuts) down from a 
tree’ || (+ *aua-) Ishk. wulin- ‘to shake down’, M. wuson- ‘to churn’ || (+ *fra-) Y1. 
firsön-/firsoy ‘to shake trees’ (Zarubin) 

*MISC: Rom. (LW) usan- ‘to shake down’ 

*SANSKRIT: ? Pkt. chanana ‘sifting’, Khow. chonik ‘to shake down’, Hi. channä ‘to 
be strained’ 

9 An IE etymology for *san is lacking. The root may be related to Sean (which is a 
"substrate" borrowing). 


*PIE — > LIV: — | Pok.: 

*REFERENCES: EVP: 75; KPF II: 181; Christensen, Contributions I: 57; Bailey 1935: 777; IIFL II: 209a; 
MacKenzie 1966: 109; EVS: 19a; DKS: 408b f.; Asatrian — Livshits: 83; Paul 1998: 313b; NEVP: 79; 
Shahbakhsh: s.v. sant
```


## [2026-09-04T19:39:59.315Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"šitāb\\|Sitāb\\|sitāftan\\|Sitaftan\\|itāftan\\|itāb\" CHEUNG.txt | head -20; echo \"=== tap ===\"; sed -n '24650,24700p' CHEUNG.txt"
}
```


### [2026-09-04T19:39:59.372Z] TOOL RESULT

```
41569:Sitaftan/Sitab-, 363 
=== tap ===

*REFERENCES: Horn1893: 88 f.; Fraenkel II: 1077; EVS: 82a; DKS: 282a; Abaev, Slovar’ III: 285; Werba 
1997: 189 f.; Steblin-Kamenskij 1999: 354; Shahbakhsh: s.v. tané-; Korn 2005: 168 f., 365 


*tand ‘to languish, faint’ 

*PARTHIAN: tnd ‘faint, languishing’. 0 The Parthian form cannot be analysed as the 
past participle of *tamH, which would rather be *taHta- > *täta-. > DMMPP: 324b 
*SANSKRIT: fand ‘to become tired, paralysed’ = EWAia I: 623 

© The evidence for the corresponding Ir. root *tand of Skt. tand is confined to 
Parthian. 

«PIE *ten-d- ‘to tire’ = LIV: 627 f. | Pok.: (1066) 

*IE COGNATES: Lith. (dial.) tandus ‘lazy, sloppy’, Lat. tendo ‘I stretch’ 


*tap ‘to warm up, heat’ 

*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
be(come) hot’ — Liste: 24 

Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
YAv. täpaiieiti (Yt 6.1, Yt 7.4, Yt 17.20, etc.), ? YAv. "a.tapaiieiti (V 9.41); Partic.: perf. pass. YAv. 
ham.tapta- (V 4.46) 

*MIDDLE PERSIAN: MMP t’b- ‘to shine’ ?, BMP t’p- /tab-/ ‘to heat, burn (up); shine’. 
© No certain attestations in MMP, DMMPP: ibid. > DMMPP: 321a 

Pres.: IND. 3sg. BMP t’pyt /tabéd /, SUBJ. 35р. ? MMP t’b’d {rather Pth. 7}, OPT. 3sg. ? MMP ®t’byy, 
ІМРУ. 2sg. BMP t^p /tab/; Inf.: BMP t’ptn /taftan/; Partic.: perf. pass. BMP грі /tafi/; Pass.: pres. IND. 
35р. BMP t’pyhyt /tabihed/ 


*tap 379 


*PARTHIAN: t’b- ‘to shine, burn’ || (+ *abi-) *bd’b ‘sunshine’ || (+ *pati-) pt’b- ‘to 
burn into’ || (+ *ui-) wyt’b- ‘to shine’ (young formation) = Ghilain: 72 | DMMPP: 
321a f., 9, 360a 

Pres.: IND. 259. t’byh, 35р. t’byd, t'byd, 3р1. t'bynd, SUBJ. 3sg. t’b’h; Partic: perf. pass. П t^b'd, t’b’d || 
(+ *pati-) Pres.: IND. 3sg. pt'byd, IMPV. 2pl. pt’byd || (+ *ui-) Pres.: IND. 3sg. wyt'byd, SUBJ. 2sg. 
wyt’b’h; Partic.: perf. pass. II wyt’b’d 

*KHOTANESE: ttav- (ttau(s)-) ‘to be(come) hot’ || (+ *a) LKh. ауу- ‘to heat’ || (+ 
*nis-) nastau-/nistau-, (inch.) OKh. nastos- ‘to be consumed’ || (+ *pati-) 
pattav-/pattau- ‘to burn up; illuminate’ || (+ *ui-) LKh. byav- ‘to be hot’ || (+ *ham-) 
OKh. handau- ‘to become hot’, LKh. hamdev- (caus.) ‘to ripen’ = SGS: 38, 9, 67,
```


## [2026-09-04T19:40:03.818Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sitaftan\" CHEUNG.txt; awk 'NR>=41560 && NR<=41575' CHEUNG.txt; echo \"=== find root page 363 ===\"; grep -n \"^\\*[a-zA-Z]* 363\\|363$\" CHEUNG.txt | head"
}
```


### [2026-09-04T19:40:05.496Z] TOOL RESULT

```
41569:Sitaftan/Sitab-, 363 
Sikar, 346 

Sina, 348 

Sinaxtan/Sinas-, 467 

Sinudan, Sunudan, 
Sanidan/Sanav-, 456 

Sitaftan/Sitab-, 363 

Sudan/Sav-, 41 

Sumurdan/Sumar-, 138 

Sunösah, isnösah, 458 
=== find root page 363 ===
23684:*star 363
```


## [2026-09-04T19:40:07.465Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23630,23700p' CHEUNG.txt"
}
```


### [2026-09-04T19:40:07.506Z] TOOL RESULT

```
*NWIR: NP sitehidan (denomin.) ‘to quarrel, brawl’, NP sitezidan ‘to fight’, NP sitéz 
‘battle, combat, conflict’ 

*NEIR: Oss. І. stigyn/stygd, D. (@)st’egun/(z)st’igd ‘to skin; to clean the skin [of 
fruits and vegetables]; to plunder, loot’, ? Yzgh. s(a)tizd/s(a)tiz- ‘to take offence’ (< 
NP ?), ? Sariq. s(1)kit, Wa. štik “game; entertainment; joke’ (LW ?) 

*SANSKRIT: — © EWAia II: 761 

© The root is probably to be separated from Skt. stegh- ‘to march, mount’ (MS). The 
Oss. forms may be closer to the original meaning. 

*PIE *steig- ‘to sting, stab’ LIV: 592 | Pok.: 1016 f. 


*IE COGNATES: Gr. стібо, ёстүрол “I sting, mark’, NHG stechen ‘to sting, stab’ 
*REFERENCES: IIFL П: 543; Edel’man 1971: 240; EVS: 73b; Abaev, Slovar’ Ш: 151 f; 
Steblin-Kamenskij 1999: 347 


*stamb(H) ‘to withstand, be stiff, stern, unmoving’ 
*AVESTAN: YAv. a$a.stombana- ‘having the support/firmness of asa’ (Yt 19.5), ? 
YAv. stanbiia ‘strife, [BMP transl.] stéz’ (F 519) 


*OLD PERSIAN: sta”b- * to revolt, rebel’ = Kent: 210 
Pres. them. aua-: INJ. 2sg. sta bava <s-t-b-v> (DNa 60) 


*MIDDLE PERSIAN: BMP stpl /stabr/, MMP ‘stbr ‘strong, firm’, MMP *‘stmbg, 
‘stmbg’n (pl.), BMP sthmbk /stambag/ ‘oppressive; obstinate’, MMP ‘stft, BMP stpt 
/staft/ ‘hard; firm, strong, cruel; savage, fierce’. 0 Although influenced by *stambH, 
the Persian forms BMP sthm /stahm/, NP sitam ‘tyranny, oppression’, NP sitamidan 
(denomin.) ‘to oppress; to be headstrong’ have a different origin, cf. DKS: 415a, 
NEVP: 76, s.v. stam). They may go back to *stak ‘to resist, oppose’, Av. staxra- 
‘firm’, etc. = DMMPP: 90 

*PARTHIAN: "'stftyft ‘harshness, tyranny’ || (+ *ui-) “wystmbg, *‘wystmbg’n (pl.) 
‘rebellious’, *wystmbgyft ‘rebelliousness’ > Ghilain: 72 | DMMPP: 90, 358b 
*KHOTANESE: staura- ‘severe, cruel’ 

*SOGDIAN: BSogd. ’st’np ‘coarse, rough’ (Dhy. 169, BSTBL: 62), MSogd. stmb 
‘stern’ (Sogdica: 18), MSogd. stBty ‘cruel’ (GMS: par. 157) 

*CHORESMIAN: ’stnb ‘grand, majestic’ (< *‘bold, audacious’) 

*BACTRIAN: otaußo ‘injury, ill-treatment, oppression’ (Y23 f.) = S-W, Bact.: 224b 
*NWIR: NP sitanbah ‘strong, robust, powerful, bold; contumacious, litigious, 
unwilling to listen’ 

*NEIR: Oss. I. stavd, D. (&)stavd ‘thick, coarse’, Yzgh. stüvd ‘thick (fat), dense 
(clouds); many, much’, stavdag ‘grounds, dregs (in soup)’, ? Pash. stam ‘exertion, 


*star 363 


travail, parturition’ (< Pers. s(i)tam, NEVP, 1.с.), ? astoway ‘single, lonely, without 
relations’ (*a-staba-ka- ‘without support’, Morgenstierne 1942: 262). 

*MISC: Arm. (LW) stambak ‘refractory, rebellious’ 

*SANSKRIT: stambh' ‘to support, prop up’; stabhamäna- ‘stiff, conceited’, vistabdha- 
‘stiff (Br.+). 0 On stabhamäna- see Goto 1987: 331. = EWAia П: 754 

Q The root *stamb(H) shows a wide range of meanings, which may suggests 
convergence of two or even more similar IE/Ilr. roots. 

«PIE *stemb’(H)- ‘to be firm, unmoving’, vel sim. = LIV: 595 f., 588 f. | Pok.: 
1012f.
```


## [2026-09-04T19:40:12.599Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*staf\\|\\*staf \\|staftan\\|stab-\\|hurry\" CHEUNG.txt | head -30"
}
```


### [2026-09-04T19:40:12.647Z] TOOL RESULT

```
1912:*SANSKRIT: bhar ‘to move rapidly to and fro, hurry, quiver’ (RV+) > EWAia II: 250 
5309:*SANSKRIT: dhav ‘to walk, to hurry, to flow’ (RV+) = EWAia I: 789 
6441:*PARTHIAN: (+ *ni-) nydf’r- ‘to hasten, hurry’ = Ghilain: 74 | DMMPP: 252b 
8350:Also the East Iranian forms, Chor. yd ‘term’ and Sogd. ’ny’w ‘hurry’, cited by 
19834:‘flying’, Lat. peto ‘I hurry, go somewhere (?)’, OWelsh hedant * volant? 
19886:© This root is connected to Gr. oneÖ8@ ‘I hurry’, Lith. spüdinti ‘to hasten’, etc. by 
23709:*MIDDLE PERSIAN: (+ *abi-) MMP ’wyst’b-, BMP ’wst’p- /awistab-/ ‘to (op)press; 
23719:*NWIR: NP sitaftan/sitab- ‘to hurry’ 
24397:*SANSKRIT: tak ‘to rush, hurry’ (RV+) = EWAia I: 610 
24399:*PIE *tek”- ‘to hurry, rush, walk, flow" > LIV: 620 f. | Pok.: 1059 f. 
25218:*NEIR: Oss. I. tynzyn, D. tunzun/tunst ‘to hasten, hurry, press on’. © The stem of the 
25220:hasten, hurry’, cited by Abaev, Slovar’ III: 338 f., is incorrect: the impf. stem t’ncy- 
25931:*Ouar/tur ‘to hurry, hasten’ 
25936:*MIDDLE PERSIAN: (+ *ni-) BMP nswb'l- /nihar-/ ? ‘to hurry? 
25938:*PARTHIAN: (+ *ni-) nydf’r- ‘to hurry’ = Ghilain: 74 | DMMPP: 252b 
25953:*SANSKRIT: tvar ‘to hurry, hasten’ (KS, Br.+) > EWAia I: 684 f. 
26709:*NEIR: Oss. I. wajyn/wad, D. wajun/wad ‘to hurry, walk, jump’, I. wajyg, D. wajug 
27806:(from)’ || (+ *fra-) ‘ride, drive to, fly’ || (+ *ham-) ‘to be ended up, hurry to join ?’ 
29405:hurry’, Goth. af-skiuban, OE scufan, Engl. to shift. 
34989:’wst’p- /awistab-/, 363 
56829:to hurry
```


## [2026-09-04T19:40:15.488Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23700,23740p' CHEUNG.txt"
}
```


### [2026-09-04T19:40:15.536Z] TOOL RESULT

```
*IE COGNATES: Lith. sterübti, stémbti ‘to oppose’, Gr. &oteugng ‘unshakable’, Toch. 
A stäm-, B stäm- ‘to stand’, A sänm- (caus.) ‘to attach, bind? 

*REFERENCES: EVP: 70; DKS: 434b; K.T. Schmidt 1992: 106 ff.; Werba 1997: 383; NEVP: 11 


*stap ‘to hasten, (op)press’ 

*MIDDLE PERSIAN: (+ *abi-) MMP ’wyst’b-, BMP ’wst’p- /awistab-/ ‘to (op)press; 
hasten [tr.]’, MMP ’wyst’bysn ‘oppression’ || (+ *ni-) MMP “nyst’pt (ppp.) ‘fallen 
headlong, away’ {hapax} > DMMPP: 76b, 254b 

Pres.: IND. 3sg. MMP ’wyst’byd: Partic.: perf. pass. MMP ’wst’ft, ’wyst’pt, "wystptg; Pass.: pres. IND. 
3sg. MMP ’wst’byhyd 

*PARTHIAN: (+ *abi-) ’wyst’bysn ‘oppression’ || (+ *ni-) “nst’ft (ppp.) ‘fallen 
headlong, away’ {hapax} = Ghilain: 72 | DMMPP: 76b, 254b 

*NWIR: NP sitaftan/sitab- ‘to hurry’ 

*MISC: Arm. (LW) stapem ‘I oppress’, štap ‘haste, trouble’ 

© The root may be a "variant" of *stambH (?). The Armenian borrowings Stapem and 
Stap rather favour original *-p-. No doubt, *stap is influenced by *stambH. 

«PIE *step- ‘to press, step’ = LIV: — | Pok.: 1013 

*IE COGNATES: OCS stopiti ‘to tread’, OCS stopa ‘foot-step’, OFr. steppa, stapa, OE 


steppan, Du. stappen, Engl. to step 
«REFERENCES: EVS: 76b; Abaev, Slovar’ III: 145 


*star ‘to sweep, throw down; to sin” 

*AVESTAN: Star- (stri-, stär-) ‘to throw (to earth)’ || (+ *aua-) ‘to throw down’ || (+ 
*4-) ‘to commit a sin, sin’ || (+ *us-) *?’. © The assumed semantic shift to ‘to commit 
a sin’ needs an explanation. Perhaps, it has developed from ‘to fall, zu Grunde 
gericht sein’ < pass. ‘to be thrown down’ (A.L.) ? = Liste: 64
```


## [2026-09-04T19:40:24.453Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15470,15500p' CHEUNG.txt; echo \"=== afgandan ctx ===\"; sed -n '15470,15495p' CHEUNG.txt >/dev/null; awk 'NR>=15455 && NR<=15500' CHEUNG.txt | head -5; echo; grep -n \"^\\*kan\" CHEUNG.txt | head"
}
```


### [2026-09-04T19:40:26.038Z] TOOL RESULT

```
(+ *para-ä-) Pres.: OPT. 2sg. BSogd. pr'kny; Inf.: pret. MSogd. "pr'gndy, MSogd. pr'qndyy, MSogd. 
pr’kndyyh || (+ *ui-) Inf.: ? MSogd. апуу ykynyy (BBB: 33}; Pass.: IND. pres. 3sg. MSogd. wyyndyy 
*CHORESMIAN: (+ *ati-) m/ckn- ‘to pick up’ || (^ *us-) m/sk(y)n- ‘to take out (sword, 
ink)’, ‘to take (revenge)’ || (+ *pati-) pckn- ‘to fulfil/perform (prayer), settle a debt; 
to take in (medicine)’ || (+ *para-ä-) pr’kn- ‘to sow, scatter, apply (medicine) on’ || 
(+ *ni-) nkn- ‘to bury’ || (+ *ui-) wkny- ‘to wear out, become old; be ruined’, 
(tr./caus.) wk’ny- ‘to wear out; ruin, tear down’. Ф Samadi (l.c.) assigns m/sk(y)n- to 
the root *kan- ‘to dig’, which is semantically troublesome. || According to 
MacKenzie 1990: 119, Chor. pckn- in the sense of ‘to (ful)fill, settle (a debt)’ has a 
different root, *Кат- ‘to fill’ ? > Samadi: 51, 181, 140, 149, 129, 215 

*BACTRIAN: (+ *para-à-) Tapayavo ‘sowing’ (J11, L12, V21, V21’) = S-W, Bact.: 
216 

*NWIR: NP kandan/kan-, Meim. bem-Kast (also supplet. bem-vat < *Hyaj)/ a-Ken- 
‘to take out, uproot, pluck’, Gz. békánaend ‘they jump up’, Gil. (Rsht.) daer-gadae/ 
dar-gan- ‘to throw’, (LW) kändcen/kän- ‘to take out, uproot, pluck’ || (+ *apa-) NP 
afgandan ‘to throw, cast away’ || (+ *upa- ?) Gil. (Rsht.) bägänæœstæ ‘struck against’ 
|| (+ *para-à- NP paragandan/paragan-, parakandan/parakan- ‘to disperse; sow; 
diffuse’, (ppp.) NP paragandah ‘dispersed, scattered, disbanded; dissipated’ || (+ 
*pati-) (?) NP paykandan/paykan- ‘to join; to collect; to draw out’ || (+ *pari-) NP 
pargandah ‘dispersed, scattered’ || (+ *ni-) Kurd. (Kurm.) nikandin ‘to bury’ 

*NEIR: (+ *aua-) Oss. D. (w)ogan ‘secret hiding place’ || (+ *fra-) Oss. D. regenun/ 
regzd ‘to shake, spread (salt, pepper for seasoning)’ || (+ *ni-) Oss. I. nyganyn/ 
nygad, D. nigzenun/niged ‘to bury’, Pash. njat-/njan- ‘to implant, imbed, thrust’, ? 
Khf. nijan ‘willow-rope, fastened in groves made in the shaft of a spade’, ? Yi. 
loyán-/loyád-, M. loyon-/loyend ‘to throw away, pour out’, (intr.) Yi. loyn-/loyód-, 
M. nayon-/loyöd- ‘to lie down, fall asleep’ (why -у- ?) || (+ *nis-) ? Oss. I. nykkaend 
‘cellar, underground accommodation’. © The past stem Pash. njat- "is inexplicable", 
=== afgandan ctx ===
surround; to apply’, ? LKh. parkam- (parküfi-) ‘to sprinkle, scatter’ || (+ *ui-) OKh. 
buvan- ‘to be harmed, ruined’, (caus.) OKh. buvañ- ‘to destroy’. © According to 
Emmerick (SGS: 75), the spelling variants of *paljsan-, pijsan- can hardly be 
reconciled with derivation *pari-kan’- ‘to fill’. A different meaning and, 
consequently, different etymology is given by Bailey (DKS: 218b): ‘to spread, 

15356:*kanl 229 
15413:*kan! ‘to throw, place, put; to destroy’ 
15521:*kan? ‘to fill’ 
15552:*kanH! ‘to dig’ 
15588:*kanH2 233 
15629:*kanH? ‘to love, take pleasure in’ 
16277:*kan’). Perhaps, the Chor. form derives from the present stem *ham-krnta- of 
28473:*kanH! would be a present formation (IE *kenH'-) of *xaH, as assumed in LIV: 344 
33508:*kan-, 232 
56314:*kan! (s.v.), *marc, *Hrais
```


## [2026-09-04T19:40:35.415Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwi\\.ruc\\|aiwiruc\\|aiwi\\.raz\\|aiwi\\.saok\\|aiwi\\.fsan\\|aiwi\\.zav\\|aiwis\\.kar\\|aiwis\\.tap\\|aiwi\\.sara\" BRT.txt | head -30; echo \"=== generic aiwi ===\"; grep -c \"aiwi\" BRT.txt"
}
```


### [2026-09-04T19:40:35.475Z] TOOL RESULT

```
=== generic aiwi ===
377
```


## [2026-09-04T19:40:37.699Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwi\" BRT.txt | head -60"
}
```


### [2026-09-04T19:40:37.754Z] TOOL RESULT

```
2405:+  bedeutet,  dasi  das  damit  beteichnete  Wort  oder  das  in  Rede  stehende  Wort  der  damit beieichneien  Stelle  oder  bei  +. . .+  die  ganie  Reihe  von  Wörtern  daiwitchen  in  den  Aus- gaben anders  als  bei  mir  erscheinen.  Doch  ist  '*'  nicht  überall  gesetzt.  In  den  Fällen, auf  die  S  g6^.  57  und  KL.  3.  385  m.  angespielt  wird,  habe  ich  geändert,  ohne  zu  markiren. Sonst  mag  '*'  ab  und  lu  veTseheatlich  fehlen,  kaum  aber  an  einer  Stelle,  bei  der  die Abweichung  von  Belang  ist.
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2464:yat  baväma  aiwi.vanyn  dänavö  . .  ahmi gal'ie  piianähu  Yt.5.73;  —  ahmäi  J/ri- n?nti .  ./ravalayö  buyiil  ahmi  nmäne  giusia va^wa  ..  ". .  dem  . . ;  in  dessen  Hause  . ." V't.  jj-sif.;  Y..;j.6  (s.  2  2  aa);  —  auch bei  Beziehung  auf  das  Subjekt  des  Satzes: (ya^a)nar>m ..  asavamm*jas?nSfm  ahmya nmjne  .  .  paiti  taröpi^wim  dai'i^yät  "als ob  er  einen  Gläubigen,  der  in  sein  (zu ihm  ins)  Haus  kommt  .  ."  V.y.aa;  — naSca  ,  .  *hö  nl  ahmat  haca  gätaot  isaetci fraiütöip  nöit  apaiiitöit(%A.)'B.23.  b)  sub- stantivisch: adä  (sd.)  ta^a  guti  p>r9- sat  as>m  .  .  ahmäi  asä  (als  Subj.)  ,  ■  paitl.- mravat  Y.ag.ii.;  30.t,  46.8,  13;  —  uz- valoayat  zara^ustrS  annm  mainyUm  .  . paiti  ahmäi  adavata  .  .  aarS  mainyus  .  .
2469:—  lia  yaoilayö  .  .  ärmalayö  vatiuhxm iibls  ahm  . .  yazamaidl  ". .  sammt  denen die  gute  A.  .  ."  \.^8.2;  —  ttm  yaz>nia kainina  . .  äa>al  aibyasHt  (DPf.)  tat  avat •lyaftim  YL/j.41;  —  Hwqm  iaininö  .  . "iwam  earilitis  . .  jaioyante  . .  tum  tä aiibyö^  nisirinaväki  Yt.  5. 87 ;  —  mit  Nu- merus Wechsel**:  yeii  arskat  anästUtS  vä anaiwijravanS  (sd.)  v3  dalnqm  aitäeit aäbyS   *s^aaAaiti   3stavanalil>yS  V.J.  40;
2476:—  inVerbindung  mit  x^'aFpat^j'a-.  Aaxaji5 Im  einem  Satz,  der  einem  vorhergehenden ..  kudaena  naiuaUt  mPiö.ao]anhd  (sd.)  Relativsatz  inhaltlich  koordinirt  ist '*': /ru- aesqm  sfaSfaHya  hizvöXt.ig.^^.  2)  auf.  zaiiUlmca  .  .  ytri/id  pourBsca  b»r3jayan ein  Relativum  als  dessen  Korrelat;  a)  ad- 1  nagciica  aiAka  yasäiti  zyänsi  (sd)  Y.  65. jektivisch  (vgl  i  aa) ;  yi  ätnm  . .  ava.-  11;  —  dämSH  urvalsl  .  .  yahmi  sp>ntä baraiti  . .  cvat  ahmäi  natre  mTsd»m  anhat  ^wil  mainyS  urvaisi  jasö  (sd.)  mazdä V.cV.81.  a)  Das  adjekt  Pron.  vertritt  |  :e/flir,7  oAmJ  W:4ä  »H7«aw,4fl  "bei  welchem laL  eius,  eorum  (s.  i  a  a):  yö  mam  .  ,  Ende  du  mit  .  .,  o  M.,  mit  XL,  bei  dem zinät  nöil  ahmi  nmäne  *z3naile  a^rava..'  du  mit  VM.  kommen  wirst"  Y.  4J.6{.;  — aal  ahmi  nmäne  .  .  "wer  .  .,  in  dessen  s.  noch  ahmya  3.  3)  Das  Neutr.  oder Hause  .  .,  sondern  in  seinem  Haus  , ."  Fem.  Sing,  bezieht  sich  substantivisch  auf Y. //.5f.;  —  mit  Numeruswechsel  "> :  _>'ö..  den  Inhalt  eines  Satzes,  bes.  Vordersatzes haom»nvandaita..frä..abyötanubyökaom5  (s.  Z  4);  a)  GSn. 'dess'  sva.  'dafür':  yatba- visäite  (sd)  baliazäi  "quilibet . .  laudat, . .  ■  väni  aiwi.sasto  .  .  eis  atiihe  asti  baSsazö eorum  corporibus  . ."  Y.  jo.  8.  b)  sub-  (sd.)  Yt7.^34;  —  AS  mim  ava>a  vjrj- stantivisch:  yi  maibyä  yaol  ahmäi  asSlt\nüiti  ya^a  ..  Sl  ait?he  asti  uzvar?z)m (sd.)   vahista  .  .    cöiüm  Y.  46.18;  19;  — j  (sd)  V-iS-^^f.;  37,  57,  68';  —  d:7tü  hi
2665:Yt.iV  55;  *;.i9;  —  anjaiii  .  .  'va  aiö.-  J.7(?).  [V.  /J.28;  lies  a^t■<7  i^■,  —  N. s/Sitrf  öium'^  vä  alaonö  xShao%r^m  satsm ,  lo'^:  lies  aiwi^sme.  —  S.  noch  aSvö-^
2798:auf  ein  relativisch  angeschlossenes  Nomen vorausweisend:  >o/<iW:4a/  sp3  urupis  fuai -so  spl  yS  urupis  .  ,  V.5.33;  —  ufa  vä nasus  raz'iwst  .  .  'sa  Jruxi  yä  ttasus  V. J.14;  5.27,  28,  7.1—4,  *.i6,  41',  9.40, 48;  —  ä^ravaium  yaoida^o  ,  .  'so  nä yö  yaoid.1>ryS  V.<).  37— 39;  40,  42,  If). 21,  Vd.iV.  10.  b)  substantivisch;  aStacTva daxmaisva . .  "sö  zl  asH  äaivanam  rapakö V.  7.55f.;  —  daxme  .  .  yat  °/a  pqsnu ra^'>a'.J/(sd-)  V.  7,49f.;  —  aisa  y5..aiwi.- >r}lti^ätus  (sd.)  *aivayaHi  -io  barfsmö.- sbrfiti  ratufris  N.  /Oj;  —  slaotaca  (sd.) yasnäica  . ,  yat  °sa  ahurake  mazda  "Pre is- lieder  .  .:  das  des  AAM."  Vr.if.ö;  6;  — jtal  ..  kmntiit  ava  hö  mirysüe  anJmltÖ si  'SÖ  , .  "wenn  er  . .  operiit  (und)  der foperirte)  stirbt,  dann  ist  er  disqualifizirt.." ^'■7-37;  —  iD  Kongraenz  mit  dem  Prae- diltkt;  cit  ai-at  vacö  äs  ,  J  baya  °h  3s ahunahe  vairyehe  "Was  war  das  für  ein Sprach  .  .?  Das  war  das  Stück  A/iV." 'W  i<).  I  —3,  o)  öfters  zugleich  auf  ein
3081:—  °ya  aiwiitilra  W.i.io;    —    'yanqmca  __  'stisca  V.  7.  57,
3170:Uta  %rayam  vahiltanqm  amiiyS  (sd.) bw^ata  . .  "^raj/am  'tatiqm  aiwi'hyö  buyata V.J.V  17;  —  'y,i  maiyä  Uä  (APn.)  daniö vaxhnii  dagi5jsuitif(%A..)  Y._32.  4; —  aya *mainiv3  varatä  (sd.)  yi  dngvH  'tä Timyö  . .  Y.  30. 5 ;  —  yi  ..  yazli  apä  . . 'bm    mantüm    (sd.)    Y.j;^.  4.  a)    mit
3374:'sd.)  sacinte  "ija  aiwi.game  V.  5. b)  'drum,  so  —  denn',  vor  Imp., Inj.,  Konj.,  Opt  und  Inf.:  tsmca..  laibyo dat  sarim  °%a  Asm  foraSua  %wa  xra^toä ^-  53-3'  —  "^'i  ^^'  västs  (sd.)  xsmat anyö  'äa  möi  sqs/a  (sd.)  veAs  vastrya  Y. 2ij.i;  3l.iS,34-7i —  °^«  «f  ii  humayd.- tara  anAm  Vr,  72.4;  4;  ~  "'ia  tu  n9 gayasca..Rya  y,4'-S'> — "^^  »■'  sasdyai (sd.)  usia  V.57. 16.  4)  anschliessend 'und';  a)  ein  Nomen:  i^a  i  Aaiiyaisd.) nare  "'^ä  jsnayö  Y.  5_J,6  3\  b)   einen
3399:—  'rum  (GS.)  hö  rätanam  . .  isänAaaa (sd.)  Yl  ig.  53;  53';  F.  7^';  — paiH.ä3n?m ainim  baraiti  ..  diwiat  haca  'va  sauAaite V, /<y,  i;  2—4;  —  hial  n3  'va  a^aururum /ia:a  *gai>äöU  *parayat  "wie  weit  soll  ein , Priester  auf  Priesterdienst  aus  dem  Haus gehen?"  N.4; — nsit  ml  apqm  -va  aiwi/ti/. ■  vpnioye  (so.)  dai^Aava  carät  Y.p.z4;  — yS  *mainyde  davi^einti  haomimla  'va- ÄfMi"^  Y.  JO.  15; — 'runqmca  paitl.ajqinm (sd.)..^;/  *iyeyqm  düräi  as^.TsS(sd.)  dah- yunqm  V.42.6;  N.4;  —  °va  dürai/rakat5 (sd.)  Yl/ö.  17; — atl:mi  ma'irjm  mä  fra- äaisayöis  anyat  pure  vä  .  .  'va/iäi*^  vä Yti4.46;  —  °va  kqm^.na/5  Vyt^;  — 'vatum  yaoiäa'^^S  dahmayat  pars  ßfritsit ..daiiiMupailim..V.g.zT,  7.41-  A)  ins- bes.  als  Bezeichnung  für  den  eisten,  den Priesterstand  (s.  unter  ^piltra-):  "va  ra- >aistä  vastrys ßuyqt  hainsY.ig.iT,ii.S, Ytij.89,V.5.28,y*45'; — 'varum  asläya ra^alstärvm  . .  västrXm  /iüyant?m  Vr.j.  2;
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
3491:l-t  Z'  "t"  'Wasser';  s,  unter  ö>. '  i-  (j  g'.  P-)  spa  i)  Adv.  'weg,  getrennt von—'  (nur  Komp.) 'J.  2)  Praev.  (mit karit-,  gauä-,  gatn-,  bar-,  yam-,  itai'- usw.).  A)  bei  Ellipse  des  Verbums: aiwica  apanm  (sd.)  patica  apanm  (sd.) I  'paca  paourvatibya  nSit  dim  ava'i^a  iri- ^an  (sd.)  V.  r5.48 "';  —  daiuan  'pa  asaTan (sd.)  Yt7p.84(?).  tZu  apa  F.2d  und Vyt.44  s.  No.  i.J KompA.;  Ableit  —  S.  auch  apäaadpajcraifa-.
3493:•  j.  apaosB-m.  Name  eines  Z>ii^'a*\  beson- ders des  Gegners  des  Tisiry a  {sd.):  a  dim (näml.  tistrim)  paiti.yas  nizdvaraiti  dalvd yö  °sö  aspake  k)hrpa  sämake  Yt.  tV.  21; 22';  —  ä  dim  bavaiti  aiwi.vanya  tistryö . .  daFnm  yim  °S>m  Yt  <.V.  28;  —  tauna- yeiti  dalum  "sjm  Yt  /Ä  2;  6.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3695:Zum  V.  'Aar:  —  Pu. ;  ie  kiiid  afar  nikitilät i  diiimal.  —  1)  So  Pt4;  NA.  aiwi',  s.  Frol. XXIX  No.  2.  wogegen  lu  bemerken,  dass  aifii in  Pü.  auch  sonst  durch  afar  (bb  m  dm) wiedergegeben  wiid,  iB.  gleich  Y.  //.  8.
3775:•  g-  C  j-)  aibi,  j.  aiwi  (aivi)''*,  p.  abiy 1)  Praen.  II  a)  mit  Akk.  bei  Veiben  der Bewegung;  a)  'ad,  zu  -  hin,  zu,  gegen  - hin':  Aauv  ksrJ' parärasJ'  'biy  vistaspam Bh.  j.  1;  D.  5.3;  —  nadPlabaira"  ..  'biy b-litrum  a/iyavt^  Bh.2.1;  J.14,  5.4;  — iJra*  . ,  hacUmi^  hamtii''iy(^  abavJ'  'biy avatn..astyavt^{sA.)  Bh.y.s;  13,  /.ii,i6% 5.  s;  —  'biy  bubirum  yd^ä  naiy  upilyatn (sd.)  Bh.  j.  19;  —  *adakiy  aham  asnaiy (sd.)  aham  "biy  *uva/am  Bh.  2.4;  —  _fra- vartil  agarbayata  utä  anayatä  "biy  mäm Bh.  2. 13;  J4,  /,  17,  5. 1,  4;  —  pasävc^ adam  käram  . .  fräisayant  'biy  viHäspam Bh.j.  i;  —  yuviyam  (sd)  ii^tanaiy  kacä . .  °biy  drayJ'  /)-«*  . .  D,  i'].y,  3,  Bh.j. 4.  ß)  'adversus,  contra,  gegen' :  pasäva'' kUra^  .,  'biy  avam  ..  aHyazia"  Bh.  1. 18;  — Aauv  karam  fraisaya'^  kari^uvatim . .  'biy avam  Bh.^.9 ;  3, 9, 1 1.||  b) mitLok. 'über, inBetreff  von  -';  /:>rasayai{%^)  'bl  ^Tu.lÄa
3785:•  j.  aibi.gaya-'\  aibi.gäya-'*  Adj.:  -?-, ständiges  Beiwort  des  Aiivisrüi^rima: aiwisrü'äirimsm  'gäim  Y. 2.9;  G.4-Si  — aiwisrO^rimäi  'gayiit  Y.  r.6';  G,  4. 1;  —
3786:aiwi sr Uprima  °gaya  Y. /.so.
3800:•  j.  aiwi-ynixta- Adj.  (fem.  VJ-) 'angenagt, angefressen' :7«i'  nasus  °ta  sünö  v3  k?niß.- s^arö  vayS  vä  k^m/s^i^arö  {%A.)  V.  7. 30; —  'la  V.5.34PÜZ'.
3804:•  j.  aiwi.xiöi^e  Inf.  'zu  bewohnen': to/n  vanm  kirTnava  , .  narqm  aiwixs'  , . gavqm  gävayamm  ". .  zur  Wohnung  für die  Menschen  . .  als  Stall  für  die  'l'iere" V.2.25.
3805:Zum  V,  iay-,  —  VgL  aiwijaelan-;  wegen  xs s.  unter  iay-  No.  3-  —  Pü. ;  mattän  apar  mäniin rii.
3809:•  j.  ''aiwi.didissinna-  Adj.,  PPM. :  s.  kais-.  j
3817:•  j.  aiwi.ta£ina-  i)  Adj.  'heranlaufend, anspringend'  zur  Begattung,  vom  Kamel- hengst:  ustrake  vmairyaos  ,  .  °naAi  Yt 14.11.  i)  n.  'Herzulauf,  Anlauf  (nur Komp.).
3819:•  j.  aiwitay-  f.  'Hinzugehen,  Begehen,  Be- steigen': ya^qmca  par3  masySka  'la^a^a spasitaiiaca  gairinqm  nämqm  dülarv  "und die  (anderen)  Berge,  welchen  früher  die Menschen  Namen  gegeben  haben,  vom Begehen  und  Betrachten  her  (sie  nehmend)" YL/ii,6'>.
3821:•  j.  aiwitara-  Adj.  (fem.  "rJ-)  'aussen (um  das  Land)  herum  gelegen,  fremd"': °räbyö  kaca  daakuiyO  YtJ7. 14.
3823:•  j.  aiwi'tö  Praen,  mit  Akk.  1)  'rings  her
3828:•  j.  aiwi.datiyav-  Adj.  (auch  mask.)  'der (rings)  um  das  Land  ist":  mi^r;>m  °yum (ASm.)  ..  aniari.dahyam  YtiO.144.
3831:aiwi.8atay-
3832:■•  j.  aiwi-aata-  Adj.,  PPfP.:  S.  'rfj-. KompA.,  E.
3833:•  j.  aiwi-8atay-  f.  'Wort:  'laiiism  (AP.) gravasca  {%A.)  maHrahe  Y.g.26.
3835:•  j.  aiwi'9ätö.tarstay-  Adj,  (auch  mask.) 'dem  Schrecken  beigelegt,  beigesellt  ist, schaudererregend  (durch  HässUchkeit)' : aspahe  'isis  (GSm.)  YtS.zi.
3840:•  j,  aiwi.draoxSa-  Adj.  'zu  belügen,  zu betrügen':  mtirim  . .  ys  nsit  kahmäi  'oS nöil  nmänaie  nmandfatje  .  ,  Vt.  10. 1 7.
3842:•  j.  aiwi.druxta-  Adj.,  PPfP.:  s.  draog-, —  aiwi.druxt>m  als  Absol.  sbes.
3844:•  j.  aiwi.druxUm  Absol.  ">  'unter  Belügen, Betrügen  von  — '  (Gen.):  rasnaosÜd  paiti.- sat»h>m  mi'iraAeca  aiwtjiruxtim  "indem er  dem  R.  widerspricht  und  den  M.  be- trügt" V.^S4-
3846:•  j.  aiwi.druxtäe  Inf.  'zu  belügen,  be- trügen' :  nBit  imat  j'Ispim  äuwarU^m  nöil vispsm  üiiiii-df  (n'äml.  varstim)  mi^rö vasnaili  ". .  nicht  alles,  was  zum  Trug (getan  ist)  . ."  Yt.  jo.  io5(?).
3855:•  j.  aiwi-S-äy-:  '^r-  Adj.  'obliegend,  sich befassend  mit  — '  (Gen,) :  ma  %rayqm  va- Äis/anam  '^yff  (NP.)  buyata  . .  "irayam acistanqm  '^yö  buyata  "nicht  befasst  euch mit  den  drei  besten  Dingen,  (vielmehr) befasst  euch  mit  . ."  V. /rf,  17''.
3857:(HBH.ZC.30S  wird  der Sjrniax  nicht  eerechL)*   j.  aiwi.vanttm    Absol.,    mit    asii    (er
3861:•  j.  aiwijiaptim  Absol.,  mit  asti  ('er  be- feuchtet*, sva.)  'er  besudelt  mit  Blut*:  yesi atshal  .  .  aiwi.n°  va  . .  aiwi.vaniim  (sd.) va  V'7,  la.
3863:•  j.  aiwinasE^s'tama-  Adj.  'der  am  meisten erlangt"':  hanhanultfmtm  asaAe  rdiwqm °m»m  Y.'I.$.
3867:•  j.aiwri.vaeSayanta-  Adj.  'der  zugewiesen werden  soll,  wird,  dedicandus':  haoma  . . asiiya  aiwi.vaioayamna  asaya  'la  ". .  qui dedicantur  .  .  dedicabuntur"  Y\.f).$.
3872:bespuckt',  sva.)  'er  besudelt  mit  Speichel' '' : yexi  atthai  upaä^m  v3  aiivi.naptlm  va aiwi.iritlm  va  aiwi.v  vä  "wenn  er  (der Leichnam)  sie  (die  Kleider)  mit  Sunen oder  Blut  oder  Kot  oder  Speichel  besudelt hat"  V.  7.12.
3882:•  j.  aiwi.varSta-  Adj.  (fem,  "/(-)  'be- regnet, worauf  es  geregnet  hat':  vlsp3m\ a  ahmät  nasunam  -a  'ianqm  daxmanqmca ' 'tanqm  hixranqmla  'tanqm  vayanqmüi frariuhantanqm  "bis  dass  es  auf  die  Leich- name geregnet  und  .  .  und  auf  die  Lei- chenausscheidungen geregnet  hat  und  bis die  Vögel  (Alles)  aufgefressen  haben"  V.  ]
3885:■  j.  aiwi.vöi^dayant-  Adj.,  PPA.:  s.  1 vöiidaya:  \
3889:kackt',  sva.)  'er  "besudelt  mit  Kot':  yezi anhat  ..  aiwi.ir'  v3  ami.vatitim  {sd.)  vä
3892:•  j.  aiwi.sravana-  Adj.,  PPM.:  s.  srav-. KompE.
3893:•  j.  aiwi-si^Ora-    n.   Name   der   ersten
3899:•  j.  'aiwi-srüSrima-  m,  Gottheit  der vierten  der  fünf  (priesterlichen)  Tages- abteilungen'*, beigenannt  aib:.gaya-  (sd.): 'm^m  aibi.gaim  asavan^m  aSake  ratüm  Y. 2.6;  G..^.5;    —    'mäi  aibi^ayilt  Y. /.  6;
3904:Ableit.  —  Ableit.  aus  aiwisrü%ra-.  —  Pü.s transskr. ;  Sü.  kt\.\  pürvärdhar��trasamdkyah,
3905:•  j.  "^aiwisrüSrima- ''  Adj.  (fem.  -mä-') 'den  Aiwisrü^rima  betreffend,  ihm  ge- bührend': kahmäi  ißaca)  *°>rimanqm'> ga>anqm  ratu/ris  frajasatti  N.5;.
3907:•  j.  albiz-  Adj,  (auch  fem.)  'etwas  (Gen.) verlangend,  heischend':  /araiii ..'bis(HSf.) /<7/  vaahius  arS3n5  "die  Frau  . .  Gates darum  heischend  vom  Mann"  V.^.24;  — 2/  ..  'bis  (NSf,)  tat  vatthJus  ^aiwiyoüni "die  Erde  . .  Gutes  darum  heischend  beim Bewohner"  y.j.34^.
3909:•  j.  aiwi.zilzuyana-  Adj.,  PPM.:  %.zav:
3910:•  j.  aiwi-zuä-  m.  (auch  mit  sj>an-  m.) Name   einer  Arl   des  Hundegeschlechts:
3914:Ableit.   BUS  aiij/;  s,  JSCHMIDT  Plur.  359. j.  aiwis-ili  N.  4;  lies  aiTaiiüili,
3920:•  j.  aiwi.saetan- :  'sJi^n-'^  m,  'Bewohner'; ti  . .  aibis  {sA.)  tal  vaakSus  *''hni  (LS.)'> V.J.  24.
3922:•  j,  aiwi-sayana-  n,  'Bewohaen':  yaha . .  *aiwUayama  darr/a  -na  . .  b>nymyS.- siabm  (sd.)  H\.to.^^.
3925:•  j.  aiwi-gasta  laf.  'aufzusitzen,  zu  be- steigen (vom  Reiter)':  mä  buyä  aarvatqm yäxta  (sd.)  . .  aiwis°  Y.  /;.  z.
3927:j.  aiwiJSi%Ha\.3.tt>:  \\ü%'%m:  s.  'iailan-.
3928:•  ').  aiwi-äitäe  Inf.:  s.  unter  sitst.
3932:•  j.  aiwi'Stay-  f.  1)  'Studium',  uzw.  spez. der  heiligen  Texte  der  jBozi/ischeQ  Reli- gion: nSit  mi  apqm  ä^rava  °til  (AP,)') ''virmye  (sd.)  daitihava  carlt  (sd.)  Y.  *j. 24.  2)  'Lesen,  Vorlesen',  spez.  liturgi- sches, Lesen  der  Liturgie;  cvat  *°lim''> parayap  "irixsapanm  ka>rähm{sd.)'a.4-
```


## [2026-09-04T19:40:45.004Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwi\\.raoc\\|aiwi\\.ruc\\|aiwi\\.raok\\|aiwi\\.sar\\|aiwis\\|aiwi\\.saok\\|aiwi\\.fs\\|aiwi\\.zav\\|aiwi\\.kan\\|aiwi\\.raz\" BRT.txt | sed -n '1,40p' | cut -c1-300"
}
```


### [2026-09-04T19:40:45.060Z] TOOL RESULT

```
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf) 
3785:•  j.  aibi.gaya-'\  aibi.gäya-'*  Adj.:  -?-, ständiges  Beiwort  des  Aiivisrüi^rima: aiwisrü'äirimsm  'gäim  Y. 2.9;  G.4-Si  — aiwisrO^rimäi  'gayiit  Y.  r.6';  G,  4. 1;  —
3904:Ableit.  —  Ableit.  aus  aiwisrü%ra-.  —  Pü.s transskr. ;  Sü.  kt\.\  pürvärdhar��trasamdkyah,
3905:•  j.  "^aiwisrüSrima- ''  Adj.  (fem.  -mä-') 'den  Aiwisrü^rima  betreffend,  ihm  ge- bührend': kahmäi  ißaca)  *°>rimanqm'> ga>anqm  ratu/ris  frajasatti  N.5;.
3914:Ableit.   BUS  aiij/;  s,  JSCHMIDT  Plur.  359. j.  aiwis-ili  N.  4;  lies  aiTaiiüili,
3925:•  j.  aiwi-gasta  laf.  'aufzusitzen,  zu  be- steigen (vom  Reiter)':  mä  buyä  aarvatqm yäxta  (sd.)  . .  aiwis°  Y.  /;.  z.
4347:•  j.  an-aivi'ätay-  f.:  s.  unter  anaiwislay.
4451:•  j,  an-ä'stüta-  Adj.  'der  sich  nicht  ange- lobt, eingeschworen  hat  auf—'  (Akk.):  aal anhat    °ts    vä    anaiwisravans   (sd.)
4820:—  zu' :  xshms  asamqm  unänö  pärayeinii . .  avi  garS  nmänam  V.  75.32;  —  x3  patti apqm  paräiti  .  .  a^ra  . .  V.  jj.  51;  — xraosyS-taraca  (sd.)  .  .  hv5  urva  paräiti par3.asnäi  amihe  yaia  . .  V,  13. 8;  —  ya- tärö  paurvs  us>hiUaiti  paräiti  vahil
6704:dyum.pe  väcim  *aiwyäs^^^    anaiwisti  (sd.)
6860:'rS  maaiä y7  mazistJ yjzatanqm yJ  vaAi^^  yt,i^.  ^T  \t%v.;  —  cattt  alte  mi^ra  tava  yit yazatanqm  Yt.J7.16; —  °r>m  tnazäqm  ..'.°ra  ma3äaV.4-3;  —  ahm  äuyoarfm 'rahe hudanfam  mazishm  yjzalim  yim  sjvisi?iH  \  mazdii  3^ai>karpm  ain>sanqm  spmtanam /rädat^ali:}m
7036:aahat  ästais  . .  ä°  yezi  aahaj  anäsiütS  . . V.^.40;  5.28-35",  7.13,  IS,  75',  ■^'■37, 99,  106;  —  yeüca  hz  anya  aya  fyao%na fravarita  .  .  ä'  yezi  //  .  .  rigij  fravarila Y.3.21;  Vd.2  aSt  ß)  yezi  .  .  aiwi.- srunvaili  .  .  yezi  J-  nsit  aiwi.surun
7262:atihat  äsfütS  . .  ä°  yezt  atihat  anastals  . . V.J.40;  5.28-35",  7.13,  15,  75',  ,V.37, 99,  106;  — yeiica  ht  anya  aya  syao%iia fravarsta  .  .  ä°  yeii  sl  .  .  nsit  fravarSta V.J. 21;  Vd.2  2 St  ß)  yezi  .  .  aiwt.- srunvaiti  .  .  yezi  ä°  nOii  aiwi.surun
11802:PQ.:  fehlt;  Npü.:  an  samisiän  silambaiar  dar an  iahr  i  Hä,  —  ')  VgL  anairyäca  Jaiiilius.- aiwistära  V.  1.   17.
12845:1)  "halten,  festhalten,  zurückhalten':  yS vS  x^ayqs  adqs  drJtä  (Opt.)>>  ayantsm urvatsii  (sd.)  .  .  Y.  4^.  5 ;  —  ys  mqm (näml.  Aaomsm)  aiwishubm  därayehi  ya%a tsyüm  Y. //.  3;  —  vupe  haoma  . .  yaiäi qsaAu  dtritänks  Y.  10.  17;  —  ya%a v»krk5  vaysi 
12855:Undeutlich:  ti  (näml.  fravasayj)  ysiö- yanti  .  .  have  asaJti  Söi^raica  ya^a  as3 mat^ammia  aiwisitJe  dahära  Yt  J_J.67'5'.
13235:—  tairlm  gäma  (sd.)  frabarat  .  .  urva anayragiva  raocöAva  mdarjät  H.  2. 1 5 ;  1 5^, 33;  vgl.  f;  —  yavat  .  .  kangmrvayqn altavat  . .  Au/ie  (sd.)  zpme  nidaiiyan  V. ''■  29;  31;  —  Ja/W  (sd.)  . .  WM?  nihaite (NDf.)^'>  V.7.45;  49;  —  taohri  ..  ta Al
15660:■)  Mitdem  V/ortttennerdaiwischen;  soX./.2 u.  ö.  —  1)  D.  6.  a  steht  statt  dessen  viipaia-
16617:auf  länger  als  — '  (Abi.);  ^cvat  *aiwiitJm parayal  .  .  ka^irakjm  (sd.)  *xsvas  xiafhS -  ■  y^  'y^  aitahmät  paräiti  ftöil  pascalia 1  anaiwisIXm  äsltyanti  ".  .  wenn  er  noch i  auf  länger  als  diese  Frist  weggehen  soll, . ."
16648:•  j.  baj-ö.däta-  Adj.  'gottgeschaffen':  y.it hx  stäram  'tanam  aiwi.raocayänte  "damit ihn  die  gottgeschaffenen  Sterne  bescheinen" V.  ig.  33.
16758:—  iu%ra  vacS  aoi.büta  (sd.,  näml.  bavan) .  .  iu%ra  tä  fryS  (näml,  api.bata)  bavan Y.65. 9;9'.  a)  negirt;  mS  buyS  aurvatqm yBxta  (sd.)  .  .  aiwisasta  .  .  nihaxta  Y. 77. 2,  b)  mit  dat.:  yezt  ^  , ,  bavaitt saaA>m^i  *anu.sastrai  ianfamat  *anu.- mainyäi  "w
17144:•  '].  b«r9}inya.äaeta-  m.  'willkommene Wohnstätte,  willkommenes  Heim':  ya%a %Wä  *aiwisayama  darrfa  aiwi/ayana husifom  °t>m  "auf  dass  wir  durch  dich bewohnen  mit  langem  Wohnen  eine wohnliche  willkommene  Wohnstätte"  YL /o.  77.
20557:•  j.  misik-  Adj,  (auch  fem.)  —  ?  — '':  asim rSsaintlm  dar^yS.vän^marum  'sacim  Avd.- aiwisilam   'säam    äfrasanhaitim  Y.52.  i.
21036:•  j.  'yaozdä-f,'Reinigung,Purilizirung,Ent- seuchung':  a^sa  aß  'dy.t  (IS.)'*  bavaiti  vasd aiwis.:fari>!a  pasubya  vlraeibya  ". .  wird mit  seiner  Purifikation  beliebig  geniessbar fiir  .."  V.  ^.32;  —  'dya  (IS,)"  ta^inti iips  irayankat  haca  "mit  Reinigung  (sva. ge
21133:52^.  3)  'bis  dass',  mit  (fiit.)  Konj.;  c)  im jAw.:  atät  ahifidty  apymjm..a»/iaf  niväi- ii/{sd.)  \'io.  16.'  III)  örtlich  'wo"";  c) im jAw.:  staomi  amü  y  rasiahe  . .  carämm (sd.)  Y.  10. 4;  —  m3  ..  ahmt  nmäne  ../nm vaocala  mqm  yim  ahunm  mazdqm  y  mi n
21137:aisqm  . .  ahmnS.vihö  bavaiti  y  granis  . . mi^näiti  mihrS  Yt.  10. 39;  —  y  ('insofern als')  asai  xsa'ir?m  cinasti  (Sp.  430  u.) '  aca'  ..^räyö  lialsa  Y.20.3;  —  ava%a saofyqs  y  v}sp?m  ahßm  .  .  sävayat  Yt '3-^39',  "9,  142;  —  ala  a/ar/  zasta paiii  ap
21837:•  j.  yuxta  Inf.  'anzuschirren,  anzuspajinen' : yu"  Id^wan.aspahe  "um  das  Viergespann anzuschirren"  F.4f;  —  mä  buyi  aurvalqm yW  .  .  aiwisasla  ,  .  nihaxta  "du  aollst keinen  Renner  mehr  aufzäumen  -.  besteigen .  .  ziigein"  Y.  11.  z ''.
23333:—  hagmim  .  .  nipatänm  (sd.)  'hu  baire Yt/4.  57; — paoiryai  'hu  mamnaiiai  'hu vaokttse  'hu  vavtnzust  Yt,  13.  88;  —  avat "vohvarl'te  nqma  ahmt  yat  'ha  f^rvtylmi Yt  75.44;  —  natnaisiarS  (sd.)  ya'hanä 'hunqm  mahT  Y.jj.  2;  —  aibii  {ii.)  tat °nhSus  *a
23651:•  j.  *varaiSye  "  Inf.  'augere,  zum  Gedeihen zu  bringen,  auszubreiten':  nöit  ml  apqm a^rava  aiwistis  V  äairikava  carät  (sd) ".  .  studia  (sacra)  ut  augeat  .."  Y.p. 24.
24824:mit  az-i  und  aiwi  'aufflammen  lassen, entzünden  an  — '  (Gen.):  aii  äim  (näml. zanqm)  aiwi.raocayäti  li^rö  V.5.  2.
28438:mit  aiwi  'zu  bewohnen':  ya^a  asS malkaiamca  aiwisitSe  daöära  (Sp.  691  m.) Yty.67.
28640:zu  Ic.  hi,  /f  bezieht  sich  auf  das  Subjekt des  gleichen  Satzes  (Reflcxivum);  nur Sing.;  ha  (n'äml.  andvt)  ^/(fem.)  maiäim nyStata  Vt.5.  ia7;  —  yat  hl  (mask.) *manS  *ahe patti  barät  V.^S-j^fi;  — yesi sl  »aoHrä  baraiti  (Sp.  935  m.}  avi  ii maiharum  YtiO
29503:niit  aiwi  'auskeltern,  durch  Kellern zubereiten',  den  Haoma:  yS  mqm  *aiwis.- hut>m  (näml.  haomun)  därayehi  (sd.) jaia  täyüm  pflSMrim  Y.  i/.  3;  —  s. noch  Ini
30539:'ydha  ^w3  (näml.  mikrim)  *aiwisayama  . . 'ttm  b?rffmya.saS3m  (sd.)  Yt.iO.77. ■AV-  f.,  lum  V.  iay-.  —  ai.  'kfU-  Adj.
```


## [2026-09-04T19:40:53.187Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHM p.220 (leaf 234) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==235' AHM.txt; echo \"=== search astin ===\"; grep -n \"astin\\|āstīn\\|dasta\" AHM.txt | head -20"
}
```


### [2026-09-04T19:40:54.818Z] TOOL RESULT

```
=== AHM p.220 (leaf 234) ===
 appear to have Deen torn out of their original context, the description dowrunam halrakd aiaongm mazdayasnanam would seem to be applicable to Nairy3.sanha in the circumstances contemplated in this fragment, We may perhags amplify the two passages as follows:
Vend. 19.34, (wherever and whenever) Truth-owning men assemble, Nairy5.sapha is with (them);
Yt 10,66, .. .and¢ Nairy3.saaha,) who is together with Truth-owning Mazdayasnians (, whereverand whenever there are) many (of them).
Nairyd.sanha is, of course, sufficiently accredited with Mithra to be acceptable as a memder of his cscort in the present stanza, cf. above, note 52%.
216
COMMENTARY [67.1-53.2
67'. That arazahi- is the eastern (and consequently savahi- the western) Aifwar was made clear by Henning, Sogdica, 28 sq.
67%, The word in question is either ¢ixra, a hapax legamenon rendered by Bth. on etymological grounds as ‘energy’, or, with twa MSS., éaxra, ar, with one MS., ca9rahe. Gdn.’s &fra, which he himself aban- doned in the Addenda to his edition, is an emendation. La., following Wi., translated ‘mit passendem Rad’, Da. ‘avec fa roue qui roule réguli¢rement’. But cixra as lectia diffetlior deserves preference, and there is no point for the present in departing from Bth.’s guess at the meaning.
Wo. took the followinz varaIrayna as the abstract noun, Da. as the name of the god. Either interpretation is possible, since on the one hand we have z@éna hacimnd ‘equipped with a weapon’ in st. 141, on the other hand hacimnd. .rasnu ‘accompanied by Ra$nu’ in Yt 13.3 (see above, p. 37). Considering that Voro@rayna the god comes into his own very shortly (st. 70) I have opted for his presence Seing anticipated at this juncture only through the quality he represents, This view is recom- mended by the comparison of hacimnd xarananha in the present st., with x*arana (thematic) hacimnd in st. 141, which, coming five lines after saena hacimnd, apparently means ‘equipzed with fortune’, nat ‘accom- panied by Fortune’. We are thus relieved of the necessity of speculating whether ¢ixra-, too, instead of a quality, should be taken as the name of the divinity representing this quality.
681. hangrownaiti ‘guides’; thus with Spi., Gda., Bth., Htl. The most accurate rendering is Wi.’s ‘mitergreift’. Da. has ‘souléve’, Hzf., 434, ‘with whom drives in his chariot’.
63°, Here we find Mithra’s two sisters (cf. above, p. 195), ASi and the Religion, in action. A%i appears implicitly as his charioteer in sts. 76 and 143.¢ Elsewhere (Yé 8.33) she and Bounty (Parandi, cf. note $6*) are associated with Mithra, Ahura Mazdah, and the Incremental Immortals (cf. note 5x1), in assisting the arrow which was shot by the legendary archer Hrox8a.f We shall see below, >. 228, that in Y 60.7 ASi and Mithra together are singled aut as bestowers of fortune, riches, and noble progeny, to the house of the faithful. The association of A&Si and Mithra in the minds of early Zoroastrian priests is alsa indicated by what is apparently a gloss added to Yt 17.2: uta. hé.. .ava.baraiti.. uta.hé... jasaiti avanhe yi asim yaxdite zaodrasyé [hi midram yazaite za0Iraryo]
7 A&i drives her own chariot in Yt 17.17. Her charioteering propensities make it likely that her epithet x*anat. caxra-, which she shares with Drvas34, means not ‘deren Rader sausen’, as Bth. has it, Sut ‘imgeller of wheels’ (base "hav-). [On éanat.éaxra- cf. Bailey, TPS, 1955, 135 s9.]
t On the other hand Y¢ 8.7 names as supporters of the arrow Ahura Mazdah, Mithra, the Waters, and the Plants; the last twa alsa accompany Mithra in st. 193 of our Hymn.
217
68.2-68.8]. COMMENTARY
‘she (ASi) Srings...ta htm, and comes to the help of him...who worships A&i with libations [he will worshi Mithra with libations]’.+ Tt i
=== search astin ===
520:Younger Avestan Zoroastrianism to two, monotheistic (viz. ZarathuStrian) and pantheistic Mazdahism, enables us ta redefine the term daéva. It always seemed a contradiction in terms that Zoroastrian hymns to Mithra, Anahita, etc., expressed strong dis- like of daévas, when one might well suspect that these divinities themselves were counted as daévas by ZarathuStra. The obvious answer is that they were not. But, in that case, which gods are daévas? Presumably those who were rejected as evil by pantheistic _ Mazdahians from the time when they were still *Vourunians. That it should be a prerogative of worshippers of the ahura *Vouruna and the gods with whom he was associated to detest the gods of the daéva class is only natural, seeing that the Vedic Varuna is the chief dsura. ZarathuStra, who by means of the “ridge of Truth’ had recognized Ahura Mazdah in *Vouruna (see above, p. 43), could hardly hel sharing with *Vouruna-worshippers the detesta- tion of the anti-*Vourunian da&vas. These were therefore equally disliked ‘yy Zarathu&trians and the non-Zarathuatrian pantheists whom the ZarathuStrians absorbed in about 430 3.c., following, according to our theory, the Achaemenian religious pattern of the time. Hence, in all likelihood, that pattern alsa excluded the daévas from worshi); Xerxes’ prohibition of their cult seems to have had a lasting effect. However, on the fringe of the two all-pervading Mazdih cults, the monotheistic and the pantheistic, the prapitiatory worship of da&vas continued to exist, as Zaehner, Zurvan, 14 s97., has aptly pointed out; we shall revert to this subject below, py. 63 sq.
1039:tim ta? frastindayehi®
1103:TEXT anahitat »ard barasman® anahitayat pard zao9rayat anahitatibyd pard vayzibya*; yim zaotaram stayata ahurd mazda a8ava asu.yasnom! berazi. gaJram; yazata zaota asu.yasno borazi. 24413" barazata vata §zaata ahurai mazdai® zaota amesangm spontangm; ho vax8 us ava raotd agnaot ava pairi imam zgm jasat vijasat vis>4i8 avi karSvqn yaiS hata; y6 paoiryo havana haomg! uzdasta stohrpatsapha mainyutasta? haraidy6 paiti barazaya; boarajayat® ahurd mazda barajayant amo8d sponta yepha kohrpd huraoSay4 yahmai hvare aurvat.aspem durat® nomd baoSayeiti; nom6 midrai vouru. gasyaoitac hazanré. gao8at baévara.CaSmaine!, yesnyo” ahi vahmyé yesnyé buya vahmyd nmanahu masyakanqm; usta Duyst ahmai naire yaso.9wa basa frayazdite aésm4.zastd barasm3.zastd gaozast3 havand.zastd frasnataéibya zastatibya frasnataéibya havanaéibya frastoratat® paiti barasman* uzdatat paiti haomat sravayamnat paiti ahunat vairyat.
1130:97. from whom the Fiendish Spirit, very deadly, recoils in fear, fram whom malignant Wrath, his body forfeited, recoils in fear, from whom long-handed Procrastination? recoils in fear, fram whom all supernatural evil gods, and the concupiscent owners of Falsehood, recoil in
1288:134. now it is the Fiendish Spirit, very deadly, who recoils in fear, now malignant Wrath, his body forfeited, now long-handed Procrastination; now recoil in fear all supernatural evil gods and the concupiscent owners of Falsehood (, all of them erying):?
1547:§ Viz. the time af the atone out af which Saslan was to de born after a period af ‘pregnancy’ lasting nine months.
1779:It would be legitimate to imagine the instr. sz. *vourn. asta being used adverbially (cf. Reichelt, dw. £b.§455) in the sense of German ‘weithin’, hence lit. ‘wide-reachingly’. Such an assumption may account for OPers. avdasta, to be read avadasta, interpreted as ava9a ‘then’ + asta {instr.), and translated ‘up to then, until then’, lit. ‘then-reachingly, reaching (the period called) then’. The passage ia which the word occurs (Beh. Iv, 70 599.) reads as follows:
1780:(a) tuvam ka hya’ aparvam imam dipiin vainahi tyam adam niyapat¥am imaiva patikara matya vikanahi yava da- (line 72) 9a-sa Ghi avadasta paribara ‘you who hereafter will see this inscrigtion which I had engraved,
1978:There is a different *zus-, from which Morgenstierne derived Sanglechi 2d! (ete.} ‘sleeve’, see IZFL, 11, 424, This can Se recognized in Av. 2usa in the Frahang t oim (‘jewel’ according to Bth.), and in Av. frazuf-, epithet of aSfa- ‘gaat’ in Yet 5.126 (quoted note 124%), which is generally thought to mean ‘precious’, As Skt. pra-hasta means ‘long-handed’, cf, Wn., 11, 1, 234, 89 fra- sus- could mean ‘long-sleeved’; cf. A. Waag, Nirangistan, 134, who souzht in aka- a coat with long sleeves. The Pahl. transl. of frazug-, which also accurs in N, looks like fre sew’stk, that of susa in F like xwstwk. Bearing in mind Yidya avldsta ‘sleeve’ < *uda-dasta- (Morz., TFL, 1, 194), and the Pahl. word which Nyberg reads *gpasast and translates ‘Handschutz' (idfsduch des Pehlevi, 1, >. x1), one might read *’wstn% instead of Pahl. xwsiwk, and, with a slight emendation, *wystk instead of xw’sth. *wyst- and ’wst- could represent un older *abi-sta-, amplified by -ka~ and -na-ka- respectively, "Ihe develagment will be as in *abi-stdla-> MPers. *wyst’d> Neers. gsta3, usta3 ‘teacher’, or *ai-stana- > MPers. *wyst’m, Arm. estan, > Pers.-Ar. ustan ‘province’, see Henning, ZI, IX, 195, 224 sg. As to *abista(na)ka-, this may be a reduction of *a37-d(2)sta- (za)ka-, comparable to that which according to H. W. Bailey (personal com- munication) took glace in Oss. fiston, Diz. festone ‘handle’ < *sati-dastanae, cf. Khot. dastgnya ‘handle’, Asia Major, n.3,, 1, 32 (48.1). Perhaps NPers. aszfn ‘sleeve’ similarly goes Yack to *d-d(a)st-. As to zuf in Ye 5.7 Ufa srira zug sispata urvaiti basu.staoyehi) one would agree with 3th, that it ought to be an epithet of Anahita in the nom. sing., if one did nat thereby have to attribute to the goddess also the strange epithet ‘stouter than the arm’, which is scarcely explained by the assumption that Anghita is here a river. The epithet would, however, suit wide sleeves, and the ending -i may be of the neuter dual. Has then zus replaced an earlier zusi, possibly because an attridute of Anadhita, srira. ans ‘having Seautiful sleeves’, was sought in this line? If so, translate ‘she, the beautiful, shows off her flowing sleeves which are armpler than her arms’, the comparative deriving its point from the earlier description of Anahita’s arms as being ‘stauter than horses’ (asd. staayehis).
2194:97°. The explanation of Baiygsta- as ‘procrastination’ was first pro- posed by Wi. in his commentary to this passage. It was repeated by 3th. in KZ, 29 (1838), p. 547, n. 2, and Benv. in Rev. hist. reliz. 139 (1945), 16.
2210:tor. Wo.: ‘an sie verteilt er, (der) die Herrschaft fibrt, gleichmi3ig (seine)...Pfeile. Und wenn er fahrend dahin kommt, wo die mi9ra- feindlichen Lander (liegen), schmettert der als erster die Keule auf RoB und Mann nieder’. Lo.: ‘auf jene (Mithra-feindlichen Valker) schleudert (comparing Ved. ava-dhy, abht-Sra-bhr) er—(denn) er vermag es—auf einmal seine... Pfeile, dann, wenn er dorthin geht, wo die m. Volker sind; er als erster schleudert...’, Wa.’s translation agrees with Spi.’s and Da.’s; the other translators take avi.di¥ to mean ‘against them’, in support of which interpretation Gdn. refers to st. 37. But on the one hand what precedes avi.dzi are Mithra’s assistants, not his opponents, on the other hand the very use of av1-hara- in st. 37 (where Lo. translates ‘bringt er auf sie’) goes against Lo.’s interpretation of this verd as ‘schleudern’ in the present case. The stanza is therefore best under- stoad as contrasting the fighting weapan used by Mithra with thase he distributes among his assistants.
2370:Opinion thus differs on the meaning of 797d, and the value of the second component of satdyus, etc. On the first point, seeing that up to hazanra@s the partics concerned are always twa, it seems obvious that mio here stands for ‘contract’; those who deny this have the obligation, as yet unfulfilled, of producing strong proof to the contrary. In the case of the ten-thousandfold contract of the Mazdayasnian Religion the can- tracting parties can safely e held to be the Religion on the ane hand, and each of the faithful on the other. As regards the second paint it is unlikely that numeral adjectives of different function should have been used in dassing from ninety ta higher figures. I see no objection to assuming that satdyu-, etc., contain ayu- ‘duration’ (cf. Lo.’s translation, and Duch., Com. 177), Yut would conclude from the present passage that ‘lasting one hundred’ had come to 5e used in the sense of ‘hundredfold’.
3080:*abi-dasta(ua)-, 220 n. *dvya-, 200 0. *apavant-, 201 *cam-, 184 *dug-gva-, 230 *havya-, 200 n. *7i(va)Ora-, 260 *lakata-, 182 n. *ndxar|n-, °aka-, 277 *niba-, 282 *pati-dastana-, 220 n. *pati-mauga-, 203 *pitt-, 231
```


## [2026-09-04T19:41:06.516Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 24 25 26; do echo \"=== leaf $n ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' IEC.txt | head -60; done"
}
```


### [2026-09-04T19:41:08.396Z] TOOL RESULT

```
=== leaf 24 ===
ill, all- “other? beside ail ‘second’;
10
20
25
30
35
40
45
Br. all; Cor. yl (for ail); Go. aljis; OE elle, el-, ele-; MHG al-; OS eli-. Cf. also OHG al- les (Eng. else); ON elja ‘concubine’ Arm. ajl "but: Lith. aliái ‘except’; Pol. Cz. ale, Srb. ali Chur fr. a cpd. a-ali-)
aliote (alioto, aliot) ‘elsewhere’. Cf. alios Gk. állose; Go. aljap
alkos, à, is, ios 'shrine, temple, grove. WP I, 90. Cf. aleks- Gk. álsos (grove, fr. *alkios), cf. also *alx, ds. alkí beside alké 'strength, safeguard, de- fence’; Go. alhs ‘temple’; OHG alah, OE eath, id.; Li. alkas *hallowed grove', alka *barrow, mound. Cf. Latv. elks (idol. Vocalism ob- scure)
alksios, alksnios, see al*sos
alkso “hold, protect’, etc. (variant of aleks-, q.v.) Arm. ayxem ‘lock’, ayx, s. id.; W alch ‘grate, grid’
alkis, aləKis "a horned animal’. WP I, 154 Skt. rśah, rsyah; Lat. alces (a Germanic LW for WH); OHG elho, elaho; ON eer R. OCS losí (i-stem) ‘elk’
alm- (?) ‘rot, impurity’ MHG elm “yellow clay’; LG olm (-o- for -a-) ‘rotten wood’; Lith. alme ‘liquor from dung’
almn-, almos ‘grown, reared, tall; growth, height. Cf. alo Gk. cf. phut-álmos ‘parental, fostering’; Lat. almus; alumnus; LL. almen “food”, alimo, -0- nis (queried *pupil); Olr. almain ‘food’; ON álmr ‘man’; G Alm ‘upland’, Elm ‘wooded ridge?
alnos (?) ʻa hollow object
Lat. alnus, gs. 3, f. ‘boat’; OCS (ambig.)
lono ‘bosom’, cf. also lonicí ‘pot’; Srb. lonac, id.
alo (1), alio ‘rear, breed, grow’. WP I, 86 Gk. cf. trog-aliá ‘crops’, phut-aliá ‘plantation’, beside aldo ‘feed’; Lat. alo, Gre cf. co-aleo, alesco; Olr. alim, Ir. alaim, ailim rear, foster’; W alu ‘bring forth”; Br. ala, id.; cf. Cor. els (stepson', fr. *alitos); Go. alan, aljan; ON ala; OE alan
alo (2) ‘wander, err Cf. aleio Gk. aláomai; Lat. cf. amb-ulo (JP thus, but cf. Lat. p-alor ?)
17 alos — ambhi (ombhi, mbhi) 18
alos “growth, increase”. Cf. alo (1) and almn- W ai "litter, produce’; ON áll (shoot, scion’. -à- for -a- before 1)
alóu-péKs *howling-dog, fox’. WP I, 317. Cf. ulqu-peéKs Skt. lopasáh; Per. rübah; Oss. ruvas, robas; Arm. ayues, gs. ayuisu and ayuesi; Gk. alo- pex; Ir. lois. For the first part cf. Gaul. lou- ernio-; Cor. low-arn ‘fox
al^sios (aliksos, al?snos, alksnios) ‘alder’. WP 1, 151 Mac. álixa ‘white poplar’; Lat. alnus; OHG alansa, alunsa, elirs; G Else with variants (see Kluge 17: Erle, Eller); Gmc. LW in Sp. aliso; ON alri, elti, elrir, ọlr; Sw. al; Du. els; OE alor, ellen; Russ. olíxa; Cz. ol$e; Slovak jelša; Srb. jelša and joha; Pol. olcha, olsza; Slovene jelša, olša; Li. alksnis, gs. io; Latv. alksnis, gs. alkšna. Cf. Basque altz “alder”. (The great variety of forms points to a non-IE origin, and the rhyme of Basque altz < *alks-: artz ‘bear’ < *arks- lends colour to this view. The laryngal posited for the prototype is re- flected in the forms o?st- (“bone”, cf. -k- in Li. kab-akštis ‘skeleton’, cf. Gk. ostéon; r?s- “bear”, cf. Gk. árktos; au?som: Lat. aurum: Li. auksas, cf. Basque urhe ‘gold’, in which glottalism is indicated in Lithuanian and Latvian by -k-. The a-vocalism is, for H. Krahe, an indication of *pre-European' origin in names of major lakes and rivers in Europe and W. Asia)
alter- (1) comp. ‘other’. Cf. alios Lat. alter; MHG alder “or, else’; LG alder; Sw. eller, ellers; Du. elders (a gs. form *else- where")
alter- (2) comp. *more grown'. Cf. alo Oss. àldár “elder, chief; Br. aotru ‘lord’; Cor. altrow ‘step-father’; OHG altiron; OE eldran *eld
=== leaf 25 ===
ers'
altos, ios 'high; height, fortress, sacred grove'. WP I, 86. Cf. alo (1) Skt. attah; Hitt. halcis ‘fortress’; Gk. Altis; Lat. altus; MIr. alt; Gaul. alto-; MW allt ‘grove’; Cor. als; Br. aot, pl. -u and ao&u “shore?
alus, u (?) “an edible root or tuber’. WP I, 56 Skt. aluh; Lat. alum (wrongly identified as
15
20
25
30
35
40
45
‘comfrey’ ?), beside alium (allium)
aluos, ios, io ‘hollow, channel, cavity’. WP I, 26; 92: aulos. Cf. Gk. álox, f.; Cyp. (queried) alwon ((quarry, mune or sim.); Lat. alvus, alveus; ON áll (2. ‘deep channel); Sw. alv ‘podzol’; älv “river”, cf. in-elvor ‘entrails’ (Hell- quist otherwise); (?) Li. alve ont
am- (1) "bold Cf. amn-, amsa. WP I, 52, 68 Å am- (2) ‘bitter. Cf. om-, omros. WP I, 179; II, 235
-àm (an adverbial suffix) Gk. cf. mát-en (Dor. -a-), lágd-én; Lat. cf. clam, coram, palam; OCS jeding; Cz. jednou; Li. sédóm; Latv. vietām, kājām
amà (1) “mother, nurse’. Cf. amba. WP I, 53 Tokh. B amma-kki (voc. sg.); Arm. ema (vo- calism obscure); Alb. åmë, ëmë (à, ë from compensatory lengthening); LL amma, cf. am-ita; Osc. amma; OHG amma; MHG amme *mother, midwife, fostermother;  OFris. amme; ON amma ‘grandma’; Sw. amma *nurse'
amå (2), see amn- “holder”
amāið (ammaio), denom. ‘mother, foster". WP I, 53 Lat. amo, -àre; MHG ammen ‘act as midwife’; Sw. amma 'suckle'
ambà, see amà (1). Skt. ambà
ambol- (?), amb- (?) ‘roundness, rim’ Skt. ámbaram ‘circumference, envelope, sky’; Cor. amal ‘side, rim’; W ymyl; cf. LG ampeln ‘to make for, go for and Skt. ambàmi ‘go’. Cf. perhaps Gk. ámbon ‘rim, boss, EW in Lat. ambo, -onis. (For Lat. umbo, -onis, see ombho. The Skt. form is also ambig., *om- bol- ?)
ambros, amros, see omros
ambh- (ombh-, mbh-), px. ‘round’. WP I, 54. Cf. ambhi Arm. cf. amb-oy£ ‘whole’; Gk. cf. ám-, án- in ámpelos, ántux; lat. amb- in ambire, an-quiro, etc.; W am-. Cf. Alem. sich em- meln ‘twist
ambhi (ombhi, mbhi) *on both sides; around, at. WP I, 54. Cf. abhi Myc. api (for *amphi); Gk. amphí; Illyr. ambi-; Alb. mbi, mbé; Lat. Osc. Umb. am-; Lat.
19 ambhi-quolos (ombhi-, mbhi-) — amtlos, om (amətrom)
(also) amb-; Olr. imb, imm; Ir. im, mí, um; cf. also Olr. imbe ‘fence’; Gaul. ambi-; OBrit. am-, aim-, em-; W am; Br. am; OE ymbe; OHG umbi, umbe; ON umb, um
ambhi-quolos (ombhi-, mbhi-) ‘circulating; servant Myc. api-qolo- (*amphiqwolos); Gk. amphi- polos: OLat. anculus. Cf. Skt. abhicarah (fr. *mbhiquelos), and Cz. (ambig.) úkol ‘task’
ambhmn- (ombhmn-, period". WP I, 41 - Arm. (ambig.) am (i-stem: ‘year’. Cf. samos}; Oss. cf. anz (cyear: Li. amžius "age Lat. cf. soll-emnis “annual, ritual’; OLat. per- emnis ‘annual’; MIr. amm “point of time’; Gael. ám, id.; Sequanian amn, amb, am ‘time’; cf. the cpd. am-ser (“time in W. Br.OBrit.Cor.); ON cf. imbru-dagar ('ember-days', fr. *ambheso); OE ymbryne; ymbren; WG imbs *wine-festival
ambhó (ombho, mbhó) ‘both’. WP I, 55. Cf. abh- Arm. cf. am- in am-ordziK “both testicles’; Gk. ámpho; Lat. ambo; Tokh. cf. A àmpi; antapi, antpi (a cpd. form?). (The vocalism of Skt. ubhá, -au is obscure)
ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhóo and bher-, bhor-) *«two-handled vessel. Skt. ambhrnahb: Per. ambar; Myc. and Gk. amphoreüs, amphiphoreus; LW in Lat. am- phora; OHG ampri; OE amber, embren; Du. emmer; Sw. (fr. LG) ámbar; LW fr. Eng. in Mir ambur, ammor, Ir. umar ‘trough’. LW fr. Gmc. in OCS oborükü ‘peck-measure’; Pol. weborek ‘pail and in OPr. wumbar
=== leaf 26 ===
is; Finn. ämpäri. (Note: G Eimer, OHG einbar derives fr. a type *oin-bhor- *one-handled vessel. G Zuber is from an R-grade, of type *du- bhor-, reduced from *dui-bhor-)
amelom (omelom) (?) *a semi-parasitic plant (mistletoe? ivy?y Lat. cf. (bapax) alimon (for *amilon, a plant injurious to trees); OCz. jmelo (spurge-olive? or sim.); Slovak omelo ‘mistletoe’; R oméla, id.; Pol. jemioła; Li. àmalas. (Note: the origin of Lat. amellus ‘aster’, and of G Mistel ‘mistletoe’ is uncertain)
mbhmn-) “circuit,
20
25
30
35
40
45
20
ameslaà (amsola) ‘blackbird, ouzel' WP I, 53 Lat. merula; LL merla; OHG amsala, amusla (variants in Kl. 17: Amsel); OE osle; cf. W mwyal-chen, mwyal-ch; Br. mual-ch, pl. mulchi
amolos, ios ‘dull, dormant, lifeless’ Arm. amul, gs. amlo ‘barren’; Alb. ámull ‘stagnant’; Olr. ambal, ambil ‘dark’; Blg. òmala ‘sultriness’ (a cpd. for Mladenov) amoros, see omros
àmi ‘I say’. (A notional construct to fit Gk. emt impf. en, but without certain cog- nates. Speculations in Bois. and Hof. mostly untenable). WP I, 114
amn- (àmn-) “container, holder’. Cf. am-. WP I, 52, 68 Skt. cf. ámatram ‘pot; Arm. aman, o-st.; Myc. Gk. ama, amé; (LW in Lat. ama 'scuttle"); cf. also Gk. ámma (Bois. untenable), amís; amnion (LW in Alb. an *caul) (Bois other- wise); Lat. amen “thong? (WH untenable, likewise Vanicek); cf. Lat. ampla “handle of shield’; MIr. án “cup, vessel; cf. W -af in byd-af 'bee-hive" (but a Lat. LW in awen, awyn 'rein); Finn. LW amme “vat, tub’. Cf. amsá
amros, see omros
amså (āmsā, is) “holder, handle, ren" Cf. amn-, am-. WP I, 52, 69, cf. also WP II, 318 Gk. En. -enos, -ene, -enon in various cpds. (sol-eén, lág-énos, ap-éné, sub-ene, tág-enon, but henía ‘thong, bridle, rein’: Myc. anija is preferably, though not certainly, from a type *sāniiə (?), despite the existence of Ir. ési Teins'); Lat. anså 'pot-handle, buckle’; Ir. áis ‘handle’; ON áss ‘main beam, sailyard’; G Anse ‘fork-handle’; Li. asa; Latv. oss, osa; OPr. ansis; Finn. LW ansas 'roof-truss', ansa ‘snare’
amsatos (ám-) “handled”. See amså Lat. ansatus; Li. asotas
amos, amos, see OMOS
amtlos, om (amotrom) ‘holder. See am-, amn-, amsá Skt. cf. ámatram 'pot; Myc. atala (*antla *vessels'); Gk. ántios, antlíon
21 an — ang-
an (sentence-particle) “if, whether?. Cf. a, ne. WP I, 56 Oss. cf. an-iu ‘is it not; Arm. pe id.; Gk. an; Alb. n&; Lat. an, cf. also an is est? an- nei: Olr. in; MIr.OBr. an, cf. also MIr. an... an...'whether...0r.. ^; Go. ME an
ana (ono) “on, upon WP I, 57. Cf. ano Skt. (ambig.) a (postp. Here: SE, but EHS otherwise); Av. ana; Tokh. A cf. ana-pár, B ene-pre ‘facing’; Gk. aná; Osc. ana-, an- (a preverb identified usually with Lat. in-); Go. OFris. ana. (For an apophonic relationship with type eni, cf. Gk. eni, en: aná; epí: apó; perí: pará)
anà (hypocoristic) “mother, grandmother”. WP I, 55 Afgh. ana; Oss. áná; Lat. cf. anus, gs. -us "old woman”, beside Dalmatian anna “nurse? (in an inscr.; OHG ana; Gk. cf annis (with hypocoristic doubling, as Dalm. anna). A laryngalized form exists in Hitt. hannas “grandmother”; Lycian xåna, and a reduplica- tion is implied in Alb. nânë, T nënë ‘mother’
andé, ande, ando, and (ndé, etc.) “there, yonder. WP I, 97, 770. Cf. anos, de, de, and antoi, endho and WP II, 336 (note) Tokh. (ambig.) ente ‘where, whence, when’; Arm. and; anti; Cypriot (alleged) ánda; Lat. inde; Olr. and ‘there’; Ir. ann; Br. ann ‘here’; W yna 'there, then’; Go. unte “as far as’; Li. andai ‘the other day’. The Cz. and Ukr. onde “there is a cpd. of on and kde
andhos (1): ondhos, q. v.
andhos (2) -es-, andhio
```


## [2026-09-04T19:41:23.541Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ambassador\\|^ambient\\|^embassy\\|ambactus\" KLN_1966.txt | head -20"
}
```


### [2026-09-04T19:41:23.589Z] TOOL RESULT

```
2416:ambassador,  n.,  a  diplomat  of  the  highest  rank.
2429:ambient,  adj.,  surrounding.  —  L.  ambiens,  gen. -entis,  ‘going  round’,  pres.  part,  of  ambire,  ‘to go  round,  surround’,  compounded  of  ambi-, ‘about,  around’,  and  ire,  ‘to  go’.  See  ambi-  and itinerate  and  cp.  ambition.  Cp.  also  andante, ambiguity,  n.  —  F.  ambiguiU,  fr.  L.  ambiguitatem.
2561:amt,  n.,  a  territorial  division  in  Denmark  and Norway.  —  Dan.,  fr.  G.  Amt,  ‘office’,  fr.  MHG. amheht,  ammet,  fr.  OHG.  ambaht,  ampaht, which  is  of  Celtic  origin.  Cp.  Gaulish-Lat. ambactus,  ‘servant’,  and  see  embassy, amuck,  amok,  adj.,  possessed  with  a  murderous frenzy;  adv.,  in  a  murderous  frenzy.  —  Malay amoq,  ‘in  a  frenzy’.
12920:embassy,  n.  —  OF.  ambassee ,  fr.  It.  ambasciata, ‘embassy’  (whence  also  F.  ambassade),  fr. OProven?.  ambaissada  (whence  also  Sp.  em- bajada),  fr.  OProven?.  *ambaissa,  ‘service’, which  is  a  Teut.  loan  word.  Cp.  Goth,  andbahti, OE.  ambiht ,  OS.  ambaht,  ON.  embxtti,  OHG. ambaht(i),  MHG.  ambehr,  ‘service,  office',  G. Amt,  ‘office’.  The  Teut.  words  themselves  are  of Celtic  origin,  and  lit.  mean  ‘a  going  or  driving around';  cp.  Gaul,-L.  ambactus,  ‘servant’,  lit. ‘one  going  around’.  See  ambages  and  cp.  am¬ bassador,  amt.
```


## [2026-09-04T19:41:28.169Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',errors='ignore').read()\nlines=t.split('\\n')\nfor key in ['ambassador,  n.,  a  diplomat','embassy,  n.','ambient,  adj.']:\n    i=t.find(key)\n    leaf=t[:i].count('\\f')\n    print(key[:20],'leaf',leaf,'≈pp',(leaf-12)*2,(leaf-12)*2+1)\nEOF\nsed -n '2416,2428p' KLN_1966.txt"
}
```


### [2026-09-04T19:41:29.859Z] TOOL RESULT

```
ambassador,  n.,  a  leaf 43 ≈pp 62 63
embassy,  n. leaf 279 ≈pp 534 535
ambient,  adj. leaf 43 ≈pp 62 63
ambassador,  n.,  a  diplomat  of  the  highest  rank.
F.  ambassadeur,  fr.  It.  ambasciatore,  fr.  ambas- ciata,  ‘embassy’.  See  embassy.
Derivatives',  ambassador-ial,  adj.,  ambassador- ial-ly,  adv.
ambassadress,  n.  —  Formed  fr.  ambassador  with suff.  -ess.
ambatoarinite,n.,  a  carbonate  of  the  cerium  met¬ als  and  strontium  (mineral.)  —  Named  after Ambatoarina  in  Madagascar.  For  the  ending see  subst.  suff.  -ite.
amber,  n.  —  ME.,  fr.  OF.  (=  F.)  ambre,  fr.  Arab. 'anbar,  ‘ambergris’.  Cp.  It.  ambra,  Sp.,  Port. ambar,  alambar,  which  all  derive  fr.  Arab,  an- bar.  Cp.  also  amariUo.  Cp.  also  ambrosia  and the  second  element  in  next  word  and  in  Liquid- ambar,  pomander.
Derivatives:  amber,  adj.  and  tr.  v.,  amber-y, adj.
ambergris,  adj.  —  F.  ambre  gris,  ‘gray  amber  . For  the  first  word  see  amber.  F.  gris  is  borrowed fr.  Frankish  *gris,  which  is  rel.  to  Du,  grijs,  ‘gray’, OS.,  OHG.,  MHG.  gris,  ‘gray’,  G.  Greis,  ‘old man’,  and  prob.  also  to  OE.  grasg,  ‘gray’.  See grizzle,  ‘gray’,  and  cp.  gray  and  words  there  re¬ ferred  to.
amberite,  n.,  an  explosive.  —  Formed  fr.  amber with  subst.  suff.  -ite;  so  called  because  it  re¬ sembles  amber.
ambi-,  before  a  vowel  amb-,  combining  form meaning  ‘both,  on  both  sides’.  —  L.  ambi-, amb-, ‘around,  round  about’,  rel.  to  ambo,  ‘both’,  and cogn.  with  Gk.  apcpt,  ‘round  about’,  OI.  abhi- fah,  Avestic  aiwi-to,  ‘on  both  sides’,  OE.  ymbe, OS.,  OHG.  umbi,  ON.  umb ,  um,  MHG.  umbe, iimbe,  G.  um,  Gaul,  ambi-,  OIr.  imb-,  imm-, imme-,  ‘round  about,  about’,  and  with  Gk.  ap.tpo>, ‘both’,  Toch.  A  ampi,  ampe,  B  ant-api,  OI.  ub- hiu,  Avestic  uwa,  OSlav.  oba,  Lith.  abu,  Lett. abi,  OPruss.  abbai,  Goth,  bai,  OE.  ba,  ‘both’. See  both  and  cp.  amphi-  and  the  first  element  in ambsace,  ancile,  ancillary,  ancipital,  umlaut.  Cp. also  ember  days.
ambidexter,  adj.,  using  both  hands  with  equal facility.  —  ML.  ambidexter,  compounded  of ambi-  and  L.  dexter,  ‘on  the  right  side,  right . See  dexter.
Derivatives:  ambidexter,  n.,  ambidexter-ity,  n., ambidextrous  (q.v.)
ambidextrous,  adj.  —  See  prec.  word  and  -ous. Derivatives:  ambidextrous-ly,  adv.,  ambidex- trous-ness,  n.
```


## [2026-09-04T19:41:37.510Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='ignore').read()\nleaves=t.split('\\f')\nfor i in range(275,284):\n    nums=re.findall(r'\\b(\\d{3})\\b',leaves[i][:200]+leaves[i][-200:])\n    print(i, leaves[i][:60].replace('\\n',' '),'|nums',nums)\nEOF"
}
```


### [2026-09-04T19:41:39.354Z] TOOL RESULT

```
275 h. A  ok  at,  B  okt.  Arm.  ut‘  (for  *optd ),  Gk.  oxto |nums []
276 ��uplifted,  ex¬ alted’  (used  as  pp.  of  efferre,  ‘to   |nums []
277 h’,  and  yapi?, ‘grace,  delight’.  The  first  element  is |nums []
278   El.  Heb.  qandh,  ‘he  created or  acquired’,  from  whic |nums []
279  ])  the  letter  m;  2)  anything  shaped  like an  m;  3)  |nums []
280  A  blend  of  em¬ broil  and  brangle. embrasure,  n.,  win |nums []
281 otion  (see  motion)  to  mouvoir,  ‘to  move’.  F. emouvoir |nums []
282 t. ‘marine  lizards’,  compounded  of  Gk.  btulio;, ‘of  th |nums []
283 en-  and  Gk.  xpivov,  ‘lily’.  See  crinoid, encroach,  in |nums []
```


## [2026-09-04T19:41:46.993Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 266 268 270; do echo \"=== leaf $n (≈p$(( (n-12)*2 ))) ===\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -3; done"
}
```


### [2026-09-04T19:41:48.502Z] TOOL RESULT

```
=== leaf 266 (≈p508) ===
  the  stem  of  L.  dux,  gen.  duds, ‘leader’.  See  duke  and  adj.  suff.  -al.
Derivative :  dueal-ly,  adv.
ducat,  n.,  name  of  several  coins.  —  OF.  (  =  F.), fr.  It.  ducato,  of  s.m.,  from  Aooxa?  (fr.  Aou!;, grecization  of  L.  dux,  ‘leader’),  surname  of  the emperor  Constantine  X  of  the  Byzantine  Em¬ pire  (1059-67),  which  was  impressed  upon  the gold  coins  struck  during  his  reign.  This  name was  confused  later  with  It.  ducato,  ‘duchy,  duke¬ dom’,  fr.  duce,  ‘duke’,  fr.  L.  ducem,  acc.  of  dux, ‘leader’  (see  duke).
=== leaf 268 (≈p512) ===
icatid,  ‘a  doubling’,  fr.  duplicatus,  pp.  of duplicare.  See  duplicate,  v.,  and  -ion.
duplicator,  n.  —  L.,  ‘a  doubler’,  fr.  duplicatus, pp.  of  duplicare.  See  duplicate,  v.,  and  agential suff.  -or.
duplicity,  n.,  double-dealing.  —  F.  duplicite,  fr. Late  L.  duplicitatem,  acc.  of  duplicitas,  ‘double¬ ness’,  fr.  L.  duplex,  gen.  duplicis.  See  duplex  and -ity  and  cp.  triplicity.
=== leaf 270 (≈p516) ===
,  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel.  to  OHG.  amen,  arnon, ‘to  reap’,  OE.  ern,  OHG.  aran,  arn,  G.  Ernte, ‘harvest’,  Goth,  asans,  ‘harvest,  summer’,  ON. bnn  (for  *aznu),  ‘work  in  the  field’,  and  cogn. with  OSlav.  jeseni,  Russ,  osen’,  OPruss.  assanis, ‘autumn’.
Derivatives:  earn-er,  n.,  earning,  n.  (q.v.) earnest,  n.,  seriousness.  —  ME.  ernest,  fr.  OE. eornost,  rel.  to  OS.,  OHG.,  ernust,  ‘struggle’, MHG.  ernest,  ‘struggle;  earnest’,  G.  Ernst, ‘earnest,  seriousness’,  Goth,  arniba,  ‘safely’,  ON. jama,  ‘fight,  combat’,  ern,  ‘able,  fit,  vigorous', orig.  ‘able  to  fight’.  Cp.  Ernest.
Derivatives:  earnest,  adj.,  earnest-ly,  adv.,  ear- nest-ness,  n.
```


## [2026-09-04T19:42:00.551Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1971.txt',errors='ignore').read()\nprint(len(t.split('\\f')),'leaves')\nfor key in ['embassy','ambi-','ambient']:\n    i=t.find('\\n'+key)\n    if i<0: i=t.find(key)\n    print(key,'leaf',t[:i].count('\\f'))\n    print(t[i:i+400].replace('\\n',' ')[:400])\n    print()\nEOF"
}
```


### [2026-09-04T19:42:02.232Z] TOOL RESULT

```
1 leaves
embassy leaf 0
 embassy, n. — OF. ambassee, fr. It. ambasciata,  ‘embassy’ (whence also F. ambassade), fr.  OProven?. ambaissada (whence also Sp. em-     bajada ), fr. ©Proven?. *ambaissa, ‘service’,  which is a Teut. loan' word. Cp. Goth, andbahti,  OE. ambiht , OS. ambaht , ON. embxtti , OHG.  ambaht(i), MHG. ambeht , ‘service, office’, G.  Amt , ‘office’. The Teut. words themselves are of  Celtic origin, and 

ambi- leaf 0
 ambi-, before a vowel amb-, combining form  meaning ‘both, on both sides’. — L. ambi-, amb-,  ‘around, round about’, rel. to ambd, ‘both’, and  cogn. with Gk. ‘round about’, OI. abhi-  t ah , Avestic aiwi-to, ‘on both sides’, OE. ymbe,  OS., OHG. umbi, ON. umb, um, MHG. umbe,  iimbe , G. um, Gaul, ambi-, OIr. imb-, imm  imme -, ‘round about, about’, and with Gk. ^^90,  ‘both*, Toch. A dmpi , ampe

ambient leaf 0
 ambient, adj., surrounding. — L. ambiens, gen.  -ends, ‘going round’, pres. part, of ambire, ‘to  go round, surround’, compounded of ambi-,  ‘about, around’, and ire, ‘to go’. See ambi- and  itinerate and cp. ambition. Cp. also andante,  ambiguity, n. — F. ambiguite, fr. L. ambiguitatem ,      29     AM G,     acc. of ambiguitas, ‘double meaning’, fr. ambi-  gluts. See ambiguous and -ity.  ambigu
```


## [2026-09-04T19:42:07.744Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',errors='ignore').read()\ni=t.find('embassy, n. — OF. ambassee')\nseg=t[i-6000:i+6000]\nfor m in re.finditer(r'\\n\\s*(\\d{2,4})\\s*\\n', seg):\n    print(m.group(1), seg[max(0,m.start()-60):m.start()].replace('\\n',' ')[-60:])\nEOF"
}
```


### [2026-09-04T19:42:09.318Z] TOOL RESULT

```
244  emblica , fr. dmleg, Egyptian pronunciation of      EMBODY
```


## [2026-09-04T19:42:17.154Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='ignore').read()\nleaves=t.split('\\f')\nfor i in range(255,300):\n    m=re.findall(r'(?m)^\\s*(\\d{3})\\s*$',leaves[i])\n    if m: print(i,m, leaves[i][:40].replace('\\n',' '))\nEOF"
}
```


### [2026-09-04T19:42:18.919Z] TOOL RESULT

```
255 ['466', '467'] uish (as  well  as  in  extinguish,  adm
256 ['468', '469'] �  L.  diuturnitas,  fr. diuturnus.  See
257 ['470', '471']  on  a  distaff  ( obsol .); 2)  to  bed
258 ['472'] and  theo-.  Dodecatheon  prop,  denotes
259 ['473', '474', '475'] t.,  pres.  part,  of  doiere ,  fr.  L.
260 ['476']   —  ML.  dominicalis,  ‘pertaining to  
261 ['477']  —  F.  dormi,  pp.  of dormir,  ‘to  sl
263 ['480', '481', '483'] oth.  ( ga)tarhjan ,  ‘to  make  distinc
264 ['484', '485'] e,  ‘dregs,  lees’,  OHG. trestir,  MHG.
265 ['486'] astis  and  in  lithontriptic. drop,  tr
266 ['487']   the  stem  of  L.  dux,  gen.  duds, ‘
267 ['488', '489', '490', '491'] re  referred  to. Derivatives:  dull,  t
270 ['497'] ,  fr.  OE.  earnian, ‘to  deserve,  ear
273 ['501', '502', '503'] he  ending  see  subst.  suff.  -ite. Ed
274 ['504', '505'] ?,  ‘an  absolute  master  or  ruler’.  
276 ['506', '507'] ��uplifted,  ex¬ alted’  (used  as  pp. 
277 ['508'] h’,  and  yapi?, ‘grace,  delight’.  The
278 ['510']   El.  Heb.  qandh,  ‘he  created or  ac
279 ['512', '513']  ])  the  letter  m;  2)  anything  shap
281 ['516', '517'] otion  (see  motion)  to  mouvoir,  ‘to 
282 ['518', '519'] t. ‘marine  lizards’,  compounded  of  G
283 ['520', '521'] en-  and  Gk.  xpivov,  ‘lily’.  See  cr
284 ['522', '523'] s).  According to  the  opinion  of  sev
285 ['524', '525'] nd L.  laqueus,  ‘noose,  snare’.  See  
287 ['528', '529'] nter-.  —  Fr.  F.  entre, ‘between,  am
288 ['531']   and  £v8iisiv,  ‘to  put  on (clothes)
289 ['532', '533']  -ic, resp.  also  -al,  and  cp.  endem
290 ['534', '535'] al,  adj.,  pertaining  to,  or  governe
291 ['536', '537'] ofy  (for  *r6^), ‘voice’,  Sacra  (for 
292 ['538', '539'] .  suff.  -ary  and  cp.  prec.  suff. -
293 ['540'] similated  fr.  *f£pfo<;),  Gk.  aprjv, 
294 ['541'] a).  See  -er,  suff.  denoting  connect
295 ['542', '543'] eol.)  —  Tr.  eiscir,  ‘a  ridge’. Eski
296 ['544', '343'] ,  whence also  Gk.  T^nveiv,  ‘to  cut’
298 ['548', '549']   See  prec. word. Etta,  fern.  PN.  — 
299 ['550', '551'] in  and  cp.  words  there  referred  to
```


## [2026-09-04T19:42:28.866Z] TOOL CALL #38: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30"
}
```


### [2026-09-04T19:42:30.411Z] TOOL RESULT

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


## [2026-09-04T19:42:32.532Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1275 --image 2>&1 | tail -40"
}
```


### [2026-09-04T19:42:40.786Z] TOOL RESULT

```
۴ - پیری‌آغوش باز کرده فراخ توهمی کوش با شكافةٌ غوش ‏ کسایی‌مروزی.« اغت‌فرن 8۲۸

و رك : شکافه زن .۰ 8 - رد : شکافه .
# شگار - بکر اول ( درلهجة مرکزی ) اسم از « شکردن » (ه.م.) » قس : شکره»

آشکره؛پولوی 5102۲ (صید): ِ ۱ ۱
استیوع 88008 ( رالات ان 9
سید کردن ) ۰ «اسشق مهد هو وس وش م. زر
آفغانی 2 ۹۳ ( صید ۹ ۳3 رم 7 :5 ی
کردن ۰ لخچیر ) + کردی ع 2
7و (وحعی ) از - شم نی جح کر

3 ی ۸ 1

08 2۲(رك : بشگرد ۱ ی ۱ ۳ هر
سماس ایو
صیدء لخجیر - هرحیوانی که ی ۰ 1 و 7 ۱

ی ۳ پیت ,له

صیدشود - اهر چیز رایگان : ۱.۹۹۹
وهفت - بغما وغارت . کی 0 ۹ هچ

پدشکار گاه_ بکس ی ی" ۹ هرد
۹ ۳ "ی 2 ۳ 1
اول » انجا که ثکارکنند » اوسون.. 7 اس ۰.۳ وا ی رون

محل صید : ۶ نوشیروان‌عادل
را درشکارگاه صیدی کباب شکار خسرو اول انوشروان (بشقاب .نقره . قرن ٩میلادی)‏
کردند.» « کلتان4۱».

شکاتض - بکس اول (درليسهة هر کزی) از: شکاف ۳ تن ( پونده‌مدری). پهلوی
دید «تاوادیاه ۰*۱۹ کردی 01۷/1۵ذهاه, 191613۲۷12ظ (شکوفه زدن «شکفتن)» کردی‌ع

15 (عکافتن » جدا کردن »سربریدن) «بونانی 52۵801۵ (کندن «شکتن).معنی کندن
درف ارسی «کافتن» و «کاویدن» محفوظ مانده «اسشق ۰۷۸۷ اوستا-02111-502011 (نابود کردن»
قلم‌وقمع ) رشه‌کلمه - آربایی 5226 » هتعدی آن‌شکافایدن < اراباه ۱ امک اسر ۵
«هوبشمان ۸۷ ۷»؛ رخنه کردن , چاك کردن ۰ شق کردن » پاره کردن؛ دربدن - شکستن .
```


## [2026-09-04T19:42:50.805Z] TOOL CALL #40: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2143 --image 2>&1 | tail -40"
}
```


### [2026-09-04T19:42:57.761Z] TOOL RESULT

```
REF: BQT:2143  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 226  OCR-lang: fas

-۱۳- ۱ عادست
نغاخمه ۱ - بر وزن شاسته » بمعنی - وامر پتغایدن هم هت پعتی بنغان ۸ -
نشانیده - و لعیین کرده شده باشد ۴ . و نشانده را نیز گفته‌اند که فاعل۹ شادن باشد؛
نشاخیدن ۴ « بروزن ومعنی نشاسن و باین معنی بجز ان
- وتعیین کردن باشد . ترکیپ در آخر ٍ ۵ ۱
نشاده - بکسر اول بروزن آشاره,چوب کلمات متفر ککگ 2
پوسیده را گویند که مانند آرد شده باشد . ی ۱ و ی
نشاستن ؟ - با سین بی‌ضه , بروزن | ۳ ین ۸
صفرا نشان وشیرة ر 4
ومستی ادن باشد ۳۰ کاستی‌حرارت نشان ل
نشارد * بفتح اول‌بروزن علاك, بلفث | - و بممنی هدف بب.
زند و پازند (۱) بممنی شکر باشد که از آن‌حلوا [ ونشانهٌ تیر وتفنکه شان
وچیزهای دیگر پزند . هم‌آمده است .
نغان ‎٩‏ < بکسر اول بر وزن نهان » نشاندن معروف است۱۱- ویمعنی
بممنی‌علامت باشد۷ - وحصه وتصیب رالیز کویند. | نهادن همست ۱۴
(۱) چك : ژند و پاژند .
۱ - اسم مقعول از ۸« نعاختن » (ه.م.) ۴ - بمعنی ۸« سب کرده و نشائیده وممین
و مقر رگشته » در دساتیر آهده 2 فرهنگه دسانیر ص۲۹۹ ۰ ی شاختن («.م.)
۴ - شاختن (ه.م.) . قس : شاندن ؛ و آن متعدی نشستن (۸.م.) است » در پهلوی
[ ۱ اسشق ۰۱۶۳۲ . و ر4 : دارمتتر . تتیعات ج ۱ ص ۰۲۹۷
اقلثه92 هزواری برای 5021687 ( شکرن ) «,وتکرس۲:۹۱*.
‎٩‏ - پهلوی 81810 «در کلمدّمر کب 8190 - 1702۳۷ (نگهبان هرغان) ».از-081280
از-28[2 - 001 ۰ دراوراق مانوی تورفان ‎8٩137180‏ << 2171858280 ( خواهند دید).یپودی-
فارسی 350018 » و درلهجه‌ها -015[3 ( نگاه کردن ) ؛ ایراتی میانه 2151128 » فارسی‌شان»
ارمنی ع 8198 از 0819۳ و 85028 . از 81888 (علامت ۰ نعان) » قس: اوستایی-(۸8791
- ط258 - 2181 نظارت کردن « بارتولمه ۳۹۰ > « نیب رک صس ۱۶۷ ۶ ۰ کردی 8188080 ۰
0و2 (علات . شانه ) « ژابااص ۶۲۰ > ۰ معرب نشان ۸ دزی ج؟ اس ۹۷۶ > و لیشان "دزی
اضا >« تفی >. ۷ - ۶ (وزبر ) گفت : ای پادشاه ؛ نشان خردمند کافی جز آن نیس ت که
بجنین کارها ( امثال وزارت ) تن در دهد . > «گللتان ص ۳۳ .
۸ - رك : شاندن . ‎٩‏ - اسم فاعل مرخم. ۴ از: ش +اندن (پوند
مصدر متعدی) » هتعدی لشتن (ج.م.) کردی نژشن 3 ۱ تیغه کردن نا دیوا ر کمیدن)
« ژابا س ۶2۱۹ .۰ ۱-کی را بنشتن واداشتن » چیزی را در جاپی مستق رکردن.
۳- دفع کردن . خاموش کردن » آرام کردن ( درد » الم ) : ۸ و دردهای چشم و کوش
بنغاند ( لین * شیر ) > «کتاب الابنیه : لین >.
0 نشاسته - بکسر ( و نیز فتح ) اول » معرب آن « شاستج » و نا« تفی » (رك :
شا ) وانیز اشاسته « دزی ج ۲ اس ۹۹۹ :۲ > ؛ مغ زکندم ( با حبوب دیگر ) مضولکوفته ؛
مادای سهی د که از آرد برنج وکندم وامثال آن کیرند » وچینده است « تقس >.
```


## [2026-09-04T19:43:09.629Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"افشاندن\\|افشان\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-04T19:43:09.673Z] TOOL RESULT

```
1291:بین سلسله‌های جبال زرافشان وحصار تکلم ميشود.
9951:یی صبا برسافی بزم اتابك عرضه دار نا از آن جلم زرافشان جرعه‌ای بخشد بمن
12949:که بمعنی پراکندن و یائیدن و افشاندن -
15116:بممنی افشان‌باشد که ازباشیدن و افدانسن‌است ۴
18653:بر شان باشین نفطه‌دار بروزن افشان.
25398:برمشان باشد ۴ - و بمعی افشاندن و برشان
25654:دیگر زده, بلفت زند ویازند (۵) بمعنی‌افشاندن
25657:افشانم ویسانید و پپانید بعنی بیفشالید .
27282:وافشاندن باشد بعنی متفرق ساخت ویریشان کرد
27283:و افشانید ۰
```


## [2026-09-04T19:43:13.578Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',errors='ignore').read()\nleaves=t.split('\\f')\nfor idx,l in enumerate(leaves):\n    if 'افشان' in l and ('افشاندن' in l or 'افشان -' in l):\n        print('leaf',idx)\n# locate the alphabetical entry افشاندن\nfor idx,l in enumerate(leaves):\n    if re.search(r'افشاندن', l):\n        print('---leaf',idx,'---')\n        print(l[:1500])\n        break\nEOF"
}
```


### [2026-09-04T19:43:15.289Z] TOOL RESULT

```
leaf 361
leaf 622
leaf 627
leaf 663
---leaf 361 ---
فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند
و او را برآوردند و پزبان رومی اینچنین شخصی
را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در
زمان او بوجود آمد . وبقوط سین اول بروزن
فربوی هم بنظر امده است -
اغشته با اول وئانی مفتوح و سکون
شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده
وتر کرده باشد؟ .
لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن
کومفندان ساژند؟ .
اغلیسون » با سن بی قطه بر وزن
افربدون ۰ قوس قرح را خوانند .
افتدستا
اغلیقی ‌ َنح اول,قلف سحتا سدكهه
بلفت بونانی؟ ترکیبی است کهآ نرا بغارسی پخته
جوشانیده‌اند ومیفختج همان است » وبکسر اول
نیز آعده شتگن «
اغول ه بر وزن ملول » از روی خشم
وفهر بگوث؛ چشم نگریستن باشد .
اغیرس < بنتح اولوثانی‌بتحتانی رسیده
و کسر رای قرشت و سکون سین سعفص ؛ جوز
رومی است و آن بار درختی باشد که صمغ آن
کهرباست ؛ و بعضی گویند چوب آن درخت
کهرباست .
اغیسی ‏ بروزن نفیس , نخمی اس ت که
آنرا بشیرازی تخم دلاشوب کونند » و ری
افتاد جنم اول بروزن استاد ۰ بعنی از
بای درآمد - و کنابه از دور شد هم هست که
ماضی دورشدن است .
افتاث گان » کاب از مظلومان
ویر بشان شدکان‌باشد .3۶
افتاده ممعثی عاجز و سقط وخراب
که و ژبرن گردننه باخد..
اقتال ‏ یک راون بروزن اقبال . به‌عنی
برا گنده وباشیده - وشکاقه ودریده باشد .
افتا ليفن « بکراول مصدر افتالاست
که بمعنی پراکندن و یائیدن و افشاندن -
وشکافتن ودربدن باشد .
افتان و خیز ان - کنابه از آحته
ودیر براه رفن باشد .
افقد - بنتم اود و کسر الث مر وژن
محجد ؛ و بمعنی ستاننده و متایش. کنده. باق ت
وبععنی شگفت وعجب ونعجب هم‌هسته .
افتدستا - کلمه ابیت مرکب از افتد
ستایش‌عجب وئیکوترین ستاش‌وبند گی- ویمعنی
2 ۱ متفه
۴ - ب
```


## [2026-09-04T19:43:21.177Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='ignore').read()\nleaves=t.split('\\f')\nfor idx in range(360,380):\n    l=leaves[idx]\n    if 'افشا' in l or 'افش' in l:\n        print('=== leaf',idx,'===')\n        import re\n        for m in re.finditer(r'افش\\S*', l):\n            print('  ',m.group(0))\nEOF"
}
```


### [2026-09-04T19:43:22.768Z] TOOL RESULT

```
=== leaf 361 ===
   افشاندن
=== leaf 365 ===
   افشردن
   افشار
   افشرده
   افشلك
   افشنگه
   افشنه
=== leaf 366 ===
   افشین
```


## [2026-09-04T19:43:25.999Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',errors='ignore').read()\nleaves=t.split('\\f')\nprint(leaves[365][:2500])\nEOF"
}
```


### [2026-09-04T19:43:27.829Z] TOOL RESULT

```
ات
وافرا یمرن الیل خوالند .
اسر ۵لن؟ « بر وزن افشردن » بمعنی
سردشدن ویخ بستن ومنجمد کردیدن باشد - واز
چیزی ‏ وکسی‌دل سرد شدن هم هست -
آقتاب عالمتاب است .
افسرسگزی « بکس مین بی شله
و سکون کاف فارسی و زای نقطه دار بتحتانی
رسیده ۰ نام سازی باشد که نوازند - ونام تصنیفی
وقولی است ازصنیفات بارید .
افسر شدن » کنابه از پادشاء خدن
باشك .
افستتین ۴ -
بکسر الث و سکون
نون و فوقانی بتحتانی
رسیده و بنون‌زده» نوعی
از بوی مادران کوهی
است .کلآن بافحوان
وتلخی آن صبر تزديك
است . دردچشم‌را سود
دارد . افنئی
افوس؟ با واو مجپول بر وزن
محبوی » بمعتی ظلم و ستم - ویراهی باشد -
ودریغ و حسرت را نیز گویند - و بمعنی بازی
وظرات - وسخر ولاغ هم‌هست - وبا واو معروف
تام‌شهر دقیاتوی بوده ۴» وبسنی گویند باین‌معنی
افتون
عربی‌است .
افسون؟ » بر وزن افیون ۰ خوادن
حصول مقاصد خود - و بمعنی حیله و تروبر هم
عست ۰ 3
اقشاد - با شین شلهدار بی‌وزن‌دستار ,
بمعنی افتردن باشد یمثیاب ازچیزی‌بزور دست
گرفتن - و ریزنده - و رشن یی دری را یز
گوند - و بسعنی خلالیدن حم آمده است هه
وامر بدین ممنی لیزهست یعنی بخلان و بغشار
ویریز - وبمعنی‌مد ومعاون وشربك ورفیق نیز
کنته‌اند همچو دزد افشار - و نام طایفه ای حم
هست از تر کان ۷ .
اقشره - بنم ناك وفتح رای قرشت »
هرچیز که آنرا افشرده باشند» و بعربی عصاره
گویشد . ۱
افشلك - بروزن چشمك » شبنم‌را گویند
که شبها برروی سبزه و کل ولاله شیند . . :
افشنگه » بر وزن خرچنگه ۰ سسمعتی
فشك است که شبنم باشد .
افشنه - بنتح اود وثاث ونون و سکون
ثانی » نام دهی است از دههای بضارا . گونند
ولادت شیخ ابوعلی آنجا شده ۹
اقشون » بر وزن اون . چیزی باشد
مانند یئجهٌ دست و دسته نیز دارد که دعقانان
۴ - بیونانی
0 « اشتینگای» بمعنی سوزان ودردتاك « نفی» ؛ )25610 ۸۲۱6۵0۲512 از
دستة آ فتابی‌ها وشببه ببومادران واسانس‌بیار ممطردارد « کل کلاب ۲۹۹ «فرهنگه روستابی۲۰۹*.
۴ - مهلوی21565 « دهارله۱۸۰» و02565» بازند 5 تن بومنگ4 ۱۱۵202599
مشتو از 202 (با[ 21۷۷ پیشوند) + 4۵1068 تلفظجنوب‌غربی ممادل لغت‌شمال‌غربی 2۳95۲۵۱011۳2
مشتق از: 5۲11 (شنبدن) « بارتولمه ۱٩۳۷‏ » « نب رکه ۱۵* » زبا کی21805 « کربرسن ۷۰ ۶ .
۴ - ظ . 05۱05 ۸(درکیاد و کیه). ٩‏ مشتق ازافابیدن (مقاسه شود: فاء فای, فاییدن
وغیرء)؛از ربشة ثا5 .۰ (304 و[ با ,. ا0اقط . 120 .4. ۵0۲ناعت) در ,5216008۳ )
۶ دائرالمعارف اسلام » . ۷ نادرخاه ازاین ابل بود . رك: مقالات کسروی ۱: ٩۸‏ بعد.
```


## [2026-09-04T19:43:51.029Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-04T19:43:53.567Z] TOOL RESULT

```
[
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
]
```


## [2026-09-04T19:43:57.678Z] TOOL CALL #46: Bash

```json
{
 "command": "ls data/extracted/ | head; ls data/ | head -20"
}
```


### [2026-09-04T19:43:57.719Z] TOOL RESULT

```
batch
NEXT_CHUNK
RETRY.txt
test
ANOMALIES.md
extracted
EXTRACTION_SPEC.md
research
translations
verification
```


## [2026-09-04T19:43:59.927Z] TOOL CALL #47: Bash

```json
{
 "command": "ls; ls data/verification | head -30; find . -maxdepth 2 -name \"*.pdf\" | head"
}
```


### [2026-09-04T19:43:59.981Z] TOOL RESULT

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
page-48.json
process
sources
./EtymologicalDictionary-persian-english.pdf
```


## [2026-09-04T19:44:02.717Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 -c \"\ntry:\n    import pdfplumber; print('pdfplumber ok')\nexcept Exception as e: print(e)\n\" 2>&1 | head -3; pdftotext -f 51 -l 51 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60"
}
```


### [2026-09-04T19:44:04.233Z] TOOL RESULT

```
No module named 'pdfplumber'
```


## [2026-09-04T19:44:06.282Z] TOOL CALL #49: Bash

```json
{
 "command": "ls tools/ && which pdftotext mutool qpdf 2>&1"
}
```


### [2026-09-04T19:44:06.332Z] TOOL RESULT

```
Exit code 1
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
/usr/bin/pdftotext
/usr/bin/mutool
qpdf not found
```


## [2026-09-04T19:44:11.024Z] TOOL CALL #50: Bash

```json
{
 "command": "pdftotext -f 51 -l 51 -layout EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p51.txt && cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p51.txt"
}
```


### [2026-09-04T19:44:12.967Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-04T19:44:16.797Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && mutool draw -o p51.png -r 200 /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf 51 2>&1 | tail -2; ls -la p51*.png"
}
```


### [2026-09-04T19:44:18.608Z] TOOL RESULT

```
warning: ICC support is not available
page /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf 51
-rw-rw-r-- 1 sfmqrb sfmqrb 239282 Sep  4 15:44 p51.png
```


## [2026-09-04T19:44:20.794Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p51.png"
}
```


### [2026-09-04T19:44:20.817Z] TOOL RESULT

```

```


## [2026-09-04T19:44:40.193Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c MON_part1.txt MON_part2.txt; grep -c \"افشان\" MON_part1.txt; grep -n \"انبر\" MON_part1.txt | head -5"
}
```


### [2026-09-04T19:44:40.283Z] TOOL RESULT

```
4377831 MON_part1.txt
4331421 MON_part2.txt
8709252 total
43
16098:فر مانبر داری. 
16645:فرمان نجای آوردن فرمانبرداری کردن. 
16646:(امسسص.) فرمانبرداری» فرمان‌پذیری» 
16647:فر مانبری. 
16787:انپرود - انبروت - ارمود] (.) (گیا.) گلابی.
```


## [2026-09-04T19:44:44.424Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"انبر\\b\\|انبر ]\\|\\[انبر\" MON_part1.txt | head -20; echo ===; sed -n '16770,16800p' MON_part1.txt"
}
```


### [2026-09-04T19:44:44.482Z] TOOL RESULT

```
Exit code 1
16098:فر مانبر داری. 
16645:فرمان نجای آوردن فرمانبرداری کردن. 
16646:(امسسص.) فرمانبرداری» فرمان‌پذیری» 
16647:فر مانبری. 
16787:انپرود - انبروت - ارمود] (.) (گیا.) گلابی. 
17104:انبردست: 20001-125 (امر.) (مسکد.) 
25310:انقیاد» فر مانبر داری» اطاعت. رغت تمام؛ 
25604:اخلاصمند. مطیع» فرمانبردار. بندة فرمان: 
27979:اسمان» زامیاد» مهر اسفند» انبران». 
29734:(ص‌فا.) قبول کننده» بدبرنده. فرمانبرداره 
29738:کننده» قابل. فرمانبر دار» سخن شنونده. روان 
29749:فرمانبرداری. قبول تأدیةٌ وجه و مال. (سیا.) 
29769:فرمانبرداری کردن» مطاوعت. پذیرفتن از 
30597:اطاعت کر دن» فر مانبرداری کردن: برستیدن 
32903:پنس: 5 (.) کیره» انبر» انس کوچکد» 
36213:فرمانبردار» مطیع» چاکر. آنکه اصحاب 
41337:تطوع: ۳۷0( [ع ۰] (مص‌ل.) فرمانبر داری 
50734:متصل بود و آن را به شکل انبر و زنگ 
51168:قفل» کلید» چفت و رزه» زنجیر» انبر» میخ و 
54092:مطیع» فرمانبر دار. 
(eval):1: == not found
```


## [2026-09-04T19:44:46.709Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17095,17120p' MON_part1.txt"
}
```


### [2026-09-04T19:44:46.760Z] TOOL RESULT

```
انسر: ۲ [ - انیره] (.) آلت فلزی دو 
شاخه که با آن : تش با چیز دیگر را بر گر ند. 

(مکن.) نوعی از اهرم که نیروی کارگر در 
وسط آن قرار دارد و نقطه ابستادگی و 
تکیه گاه در طرفین. ۰و وم اهبرم): 

آتش چین» از لوازم آتشگاه. 

انبردست: 20001-125 (امر.) (مسکد.) 
نوعی از اهرم که تکیه گاه آن بین نقطة 
کارگر و نقطهٌ ابستادگی قرار دارد. 

اثبره: (0-)2000۲2 (ص. ۰) هر جچیز موی 
ريخته را گویند عموماً و شتر موی ریسخته 
انساط: 2 [ع.] (مص‌ل.) باز شدن» 


گسترده شدن» پهناور گردیدن؛ ممتد شدن. 
گشادگی خاطر. گستاخی» ستاخی. (تص.) 
بسط. (فز.) مقدار افزايش طولی و سطحی و 
حجمی اجسام و مایعات و گازها که در برابر 
حرارت پیدا می‌کنند و اين افزایش بر حسب 
نوع شیّ و جنس آن و میزان حرارتی که به 
آن می‌دهند متفاوت است؛ ج. انبساطات. 
انیست: ۱ ([- انسته] (ص.) چیزی که
```


## [2026-09-04T19:44:53.206Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^افشان\\|افشان:\\|افشاندن:\\|افشون\" MON_part1.txt | head -10; echo ===; grep -n \"افشان\" MON_part1.txt | sed -n '1,20p'"
}
```


### [2026-09-04T19:44:53.265Z] TOOL RESULT

```
Exit code 1
3179:استین افشاندن: (مسص ل.) 
3185:کسی افشاندن: با جنبش دست و آستین 
15093:افشان: 2520 [- فشان] (افا.) در بعضی 
15096:افشاندن: «02-:2627 [- افشانیدن - فشاندن 
15098:افشاند» افشاننده» افشانده) ریختن و باشیدن» 
15110:افشون: 2807 (- انشان] (ا.)افزاری است 
28311:افشاندن. ربختن» باچیدن (عم.) شنجیدن. 
32183:افشاندن آب. آب مترشح: یک پشنگ آب. 
33889:افشان این گٌیاه جدا می‌شوند. برگ‌های 
51790:شو د؛ 0 غله بر افشان» افشون» هسته. 
(eval):1: == not found
```


## [2026-09-04T19:44:55.275Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15090,15118p' MON_part1.txt"
}
```


### [2026-09-04T19:44:55.330Z] TOOL RESULT

```
آید: دردافشار. 
افشار: 208 (.) (مس.) گوشه‌ای است در 
دستگاه شور. 
افشان: 2520 [- فشان] (افا.) در بعضی 
کلمات مرکب به معنی افشاننده آید: 
آتش‌افشان. 
افشاندن: «02-:2627 [- افشانیدن - فشاندن 
- فشانیدن] (مص‌م.) (افشاند؛ افشاند» خو اهد 
افشاند» افشاننده» افشانده) ریختن و باشیدن» 
پرا کنده کردن. 
افشردن: 0-]2180 [- فشردن] (مسصمع.) 
(افشرد» افشرد» خواهد افشرد» سیفشر» 
افشر دنده؛ افشر ده) فشار دادن. آب؛ شیر ۵؛ با 
روغن چیزی را به فشار گرفتن؛ عصاره 
گرفتن؛ افشرده گرفتن. استوار کردن. 
افشره: (6-)2150۲-2 [< افشرج» مسعر.] (ا.) 
آبی که از نشردن مبوه‌ها گیرند» عصارة 
مایعی که به وسیلة فشار از مبوه‌ها استخراج 
افشک: 2626 [- انشک - افنشسنگ] (ا.) 
منم ژاله. 
افشون: 2807 (- انشان] (ا.)افزاری است 
دارای بنجه‌ای چوسن (سه شاخه با چهار 
شاخه) و دسته‌ای بلند که به وسبلةٌ آن غلهً 
کوفته را باد دهند و دانه را از کاه جدا سازند؛ 
انگشته» هسته. 
افشه: (50)0ه اقس. فروشک] (.) گندم 


نیم کوفته» بلغور» برغول.
```


## [2026-09-04T19:45:05.021Z] TOOL CALL #58: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T19:45:05.026Z] TOOL RESULT

```


```


## [2026-09-04T19:45:09.274Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82mbʰi",
 "prompt": "Give the reconstructed PIE form, its meaning, and the list of descendants (Greek, Latin, Germanic, Indo-Iranian/Avestan/Old Persian). Also any note on relation to *h₂ent- and on *h₂mbʰoh₁ 'both'."
}
```


## [2026-09-04T19:45:11.118Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D9%88%D8%AE%D8%AA%D9%86",
 "prompt": "Give the full etymology of Persian افروختن afrūxtan 'to light up': Middle Persian form, Proto-Iranian prefix and root, Avestan cognate, and cited sources."
}
```


### [2026-09-04T19:45:11.163Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T19:45:17.184Z] TOOL RESULT

```
# Etymology of Persian افروختن (afrūxtan)

**Middle Persian Form:**
"ʾplwhtn' (abrōxtan, "to light, kindle, illuminate, polish")" — a compound verb

**Proto-Iranian & Proto-Indo-European Components:**
The word combines two elements:
- *af- from Proto-Iranian *Hápa ("off, away, from") or Proto-Indo-European *upó ("under, below, towards")
- *rōx- from Proto-Indo-European *lewk- ("bright, to shine, to see")

**Avestan Cognate:**
The document does not provide an explicit Avestan cognate form.

**Cited Sources:**
The entry references Hayyim, Sulayman's *New Persian–English dictionary* (1934, Teheran: Librairie-imprimerie Béroukhim) and includes a literary citation from Rumi's *Masnavi* (c. 1260s), translated by Reynold A. Nicholson, demonstrating historical usage of the verb meaning "to shine forth."
```


## [2026-09-04T19:45:24.837Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"abrōz\\|abrōxt\\|ʾplwhtn\\|abrāz\\|afsār\\|abzūd\\|abzāy\\|abgan\\|abrāst\" PHD_mackenzie.txt | head -20; echo \"=== PHD.txt ===\"; grep -n \"abrōz\\|abrāz\\|abzūd\\|abgan\\|afsār\\|abdast\\|āstēn\" PHD.txt | head -20"
}
```


### [2026-09-04T19:45:24.898Z] TOOL RESULT

```
798:abgandan, ab~an- [LJ\!IYTWN-tn' < A y rm'; 'pkn- I M 'bgnd, 'bgn-,
2358:  -- abgandan: throw forward.
7776:terror bim, sahrn; v. fear.               throw abgandan, wextan, wistan ;
7778:test (v.) passiixtan, uzmiidan.              abgandan; -- on pahikaftan.
9326:abgan-t                      -,,~      rozgar                          ~,,,~
9327:abgandanl
11402:kan· I                       ... ,~~   abgan-                          -\~~
=== PHD.txt ===
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
167:abgandan ` 4 a-Cárag
168:gs abgan- [LM YT WN-tn! < AV т; > kn- | M *bgnd, *bgn-, N afgan-dan] throw.
172:a-dàd [471], a-dādestān [?- DYNA, -dtst^n'] illegal, unjust. ih: injustice, illegality. a-dahm P@?hm] uninitiated. -ādan [- m! | P dn, N ~] suffix forming secondary infinitives. a-dàn [??п! | M din ignorant. ~ih: ignorance. «адап [??!] wealthy, solvent; wealth. “Аһ: wealth. a-dard [Pdlt'] painless. áüdaróg [wk], ātaxš 1 ~ : the simplest kind of sacred fire. adehig (’dhyk'] indigenous, domestic. adén [?tyn! | М dun) entry. *adén- ['dyn- | = M] bring, lead. ādišt Ptyst'] fire-stand. : ae. D i ‚ (ed уд ádüg Ptwk! | M "?dwg] capable. adur twr! | Mdwr, N ādar] fire; the god ‘Fire’; cal. gth month; oth day. adurestar [twrystl] ashes. ~én [-yx!] ashen. adur- gah [twrg’s] fire altar. ЖЕСЕ, āfrāh PSPs | М ??р?Л] teaching, doctrine. alva 2 KM N facaz\ ‘ace Luch >a-frasāwand [' Bl? wnd] imperishable. afridan, àfrin- / āfur- Pžlytn', ?Blyn-, *pwl- | M 'p(w)ryd, "po -— P >f+yn-, N āfarīdan, afarin-] praise, bless; create. áfrin ['pryn! | M?pryn, N áfarin] praise, blessing. 9544. "tien ~agan [-k”n!] Afrinagan prayers. аїгӧёар [ēlwšk! | N ~ a] a sweetmeat made of flour, butter, and honey. ‚ *afsálàn Pfs'Px!' | (N ābsālān)] springtime. afsān (?psn! | (M ?р?ле), N afsāna] story, fable. afsardan, afsar- ['psi-tn'] cool down. afsārdan, afsar- Pfs?/-tn'] cool, freeze, extinguish. „išn: cooling. afsáy-, v. afsūdan. afsénistan, afsén- [*5syx-stn!, v. abesihén-idan] destroy. --i$n : destruction. afsin [swn | N afsün] spell, incantation. M psan afsös [psws | N ~] scorn, mockery. ~gar [-g/] mocker. afsūdan, afsāy- ['pswtn!, *ps*d-] enchant, protect by spell. afšāndan, afšān- [5Zz?n-tn! | N ~] spread, scatter, sow. afSardan ['5?Its! | N ~] = afšurdan. af$urdan, afšār- 'Pfwltn!,?pP?l- | N ~] press, compress, crush. āfurīdan, afur- ?fwl-ytn', v. Afridan] create. ~išn: creation. -ag [-À! | M -g, N -a] suffix forming (i) adjectives, from nouns and verbal stems, (ii) nouns, from adjectives and present stems.
347:~išn: help, assistance. ~išnig: helpful. frāz [рге | M prz, N faraz] forth, focwarile ~ abgandan: throw forward. ~ 82: after, apart from. ~ bréhénidan: fashion forth, create. ~ griftan: undertake, perform; appoint, decide. ~ 6: up to.
2195:hand-guard abdast.
4004:throw abgandan, wéxtan, wistan; ~ down ēsān-; ~ forward fraz abgandan; ~ on pahikaftan.
4913:rag атат, sīhom” hazārag* larz- larzīdan ram abgan-! abgandan! ramag ras- rascn- rasenidan rahig rasidan rastarih rastan rastag
```


## [2026-09-04T19:45:33.715Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"abrōz\\|abroz\\|abrāz\\|abraz\\|abzūdan\\|abzudan\\|abzay\\|abzāy\\|abestēn\\|astēn\\|ābsār\\|afsār \\[\" PHD.txt | head -20; echo \"=== search 'sleeve' and 'bridle' ===\"; grep -n \"sleeve\\|bridle\" PHD.txt | head -10"
}
```


### [2026-09-04T19:45:33.773Z] TOOL RESULT

```
170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
710:acclivity abraz.
2167:growth ārēyišn, rēyišn; (increase) abzāyišn, abzón, wālišn, waxšišn.
2410:increase (n.) abzón, abzāyišn, fra- dahišnih, mehēnišn.
=== search 'sleeve' and 'bridle' ===
323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
1089:bridle ēwān, padisar.
```


## [2026-09-04T19:45:48.606Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"afsar\\|afsär\\|astin\\|äsHn\\|äslin\\|sikär\\|sikar\\|afsän\\|afsös\\|afsan\" HUB.txt | head -30"
}
```


### [2026-09-04T19:45:48.656Z] TOOL RESULT

```
439:*) Vgl. np. afsarn = arm. auSarak, dSdrak,
489:99. Np. afsar *Krone' — ap. ^abisarah- *um den Kopf liegt
992:auf sikardan jagen' in bi-sgard zu zerlegen und auf
2705:752. Vgl. san und afsan 'Wetzstein'.
2810:'a hawk, falcon' = np. sikara, sakara 'Jagdhabicht'.
2811:Vgl. arm. sakr u. s. w. ZDMG. 46, 266. Np. sikar
3381:952. Np. Idf Trahlerei' (afgh. LW. Ictfa, lapa f. 'boasting,
5122:(aus *afsardan, vgl. paz. awasard , phi. afsart 'frozen*
5124:skr. *g9rta-), dessen Praes. wahrscheinlich "^afsaram gelautet
5125:hat. Ob afsurdan 'auspressen' : pr. afsaram Muster oder
5257:•Grundriss die W9rter: arm *Arm*, astar 'Maulesel*, afsar
5556:(oben p. 30), vgl. np. sikar *Jagd*, sikardan jagen , phi. v(i)skar
6059:(Vullers: iskira) *Jagdhabicht* = sikara, u. s. w.
6084:Wrzl. skap; sikdr 'Jagd*, sikardan jagen'; sikuftan 'auf-
6126:nehmen = fuzudan H. 96; afsar *Ziiger = fisar H. 97;
6127:afsan 'Wetzstein* = fasan H. 98; afsurdan *frieren' = fu-
6313:(afgh. laf a und Idpa boasting')?
6467:H. 96, paz. aw{a)ziidan, oben p. 16; afsar *Zuger H. 97;
6468:afsCLn^ avsan *Wetzstein' H. 98; afsar Krone H. 99, oben
6470:afsos *Spott' H. 101 (?), paz. aw(a)sd8; afsandan ausstreuen'
6606:ausgepresster Saft, Most' (Hohelied) = np. afsara,
7471:afsan *Wetzstein , afsar 'Krone', pdsux *Antwort\ pasand
7824:'neidet* (oben p. 13) ; jask H. 421 ist unsicher, ebenso sikar
8492:skenda-; sikaftan *spalten H. 787, oben p. 80; sikar *Jagd'
8493:H. 786, oben p. 80; sikar 'Kohle H. 742, oben p. 76u.s.w.;
10240:afsar 17.
10737:sikar 80.
```


## [2026-09-04T19:45:52.069Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '485,500p' HUB.txt; echo \"=== p.30 sikar ===\"; sed -n '985,1000p' HUB.txt; echo \"=== 5550 ===\"; sed -n '5548,5562p' HUB.txt"
}
```


### [2026-09-04T19:45:52.136Z] TOOL RESULT

```
*vor warts drS,ngen, fordern', caus. jdvayati, ptc. juta-
^= np. zud schneir stellen l§.sst.
98. Afgh. p'san 'Wetzstein (Raverty) ist LW. wegen -an
(fiir afgh. -ww).
99. Np. afsar *Krone' — ap. ^abisarah- *um den Kopf liegt
im Sanskrit vor als abhigiras-, aber mit der Bedeutung :
*den Kopf richtend nach-, zum Kopfe gerichtet'. Horn
vergleicht mit Recht phi. aparsar (= auf dem Kopfe'
d. i.) *Diadeni, Krone' fiir zd. pws5- ZPQI. 24 (= arm.
psak 'Diadem, Krone, Kranz').
100. Arm. j^surt" in ^rt *kalt' zu verbessern.
101. Np. afsos (afgh. LW. afsos 'sorrow, regret') wird auch
von Fr. Mtiller, WZKM. 7, 367 nicht befriedigend
erklart.
102 — 106. Nicht einwandfrei, besonders der Bedeutung
wegen.
=== p.30 sikar ===
223. Die angefiihrten Dialektformen zeigen deutlich, dass
biskofa 'Bliite' aus vi-skofak, das Bdh. 64, 19 vor-
liegt, entstanden ist. Vgl. sikofa^ sigOfa *Blute' (afgh.
LW. sikufa, sigufa *a flower, a blossom') = phi. skdfak
Bdh. 64, 21. Ob gr. axvcpog, a^vngioq *Becher* dazu ge-
hort, bleibt fraglich.
224. Np. biSgard und bisgar *Jagd* ist mit Riicksicht
auf sikardan jagen' in bi-sgard zu zerlegen und auf
*mskart (vgl. de Lagarde, Pers. Stud. p. 75) zu-
riickzufiihren.^) Vgl. biskofa ^^ phi. viskofak, bidast r=
phi. vitast, bistar ■= g. vistara und unten Nr. 786.
225. Np. bdSotan ist LW. aus dem Avesta und entstellt.
226. Np. bat *Ente' (im Persischen, Kurdischen, Armeni-
schen, Arabischen und Syrischen) ist nach Herkunft
und Etymologic dunkel. Dem alban. pate *Gans'- wurde
nur ein np. *pad lautlich entsprechen, russisch utka
=== 5550 ===
= hustflx (unbelegt), arm. vstah, phi. v[i)staxv ; bistar 'Lager
= gustar, g. vistara ZDMG. 36, 69, vgl. gustardan, von
vi -\- Wzl. star, vgl. zd. stairis; hiskofa *Blute*, jiid. pers.
^) A us urspr. * varta- hatte np. *bard oder *var(f, aus *vrta',
*ti'ii' np. *gurd werden sollen. Siehe oben p. 91.
«) Siehe § 36.— 158 —
mit gu- anlautend (siehe Horn Nr. 223; oben p. 30), phi.
v(i)skdfak Bdh. Gl. 263; bisgard *Jagd* aus phi. *viskart
(oben p. 30), vgl. np. sikar *Jagd*, sikardan jagen , phi. v(i)skar
Bdh. 61. 263?; binjisk 'Sperling = gunjisk^), phi. v(i)nc(i)sk
Gl. and Ind. 248, sivend. bunjis, binjis Journ. asiat. 1893,
252 ; pizmurdan statt bihmtrdan Verwelken, verfallen Gazo-
phyl. p. 167, jiid. pers. mit gu anlautend {gmmurdan\ also
aus mp. ^'viSnmrdan (oben p. 41); arab. Bistdm aus np. Bis-
tahm neben Gustahm = phi. Vistaxm Tab. 96; Bindoi =
```


## [2026-09-04T19:46:11.720Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82m%CC%A5b%CA%B0i",
 "prompt": "Give the PIE reconstruction, meaning, and descendants list (Greek, Latin, Germanic, Indo-Iranian incl. Avestan and Old Persian). Note any relation to *h₂ent-."
}
```


## [2026-09-04T19:46:14.231Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86",
 "prompt": "Give the etymology of Persian آستین āstīn 'sleeve': Middle Persian form, Proto-Iranian reconstruction, any mention of *abi-dasta- or *ā-dasta- 'hand', and cited sources (Hasandust, Gershevitch etc.)."
}
```


### [2026-09-04T19:46:19.103Z] TOOL RESULT

```
# Proto-Indo-European *h₂m̥bʰí

## Reconstruction and Meaning

The PIE adverb **\*h₂m̥bʰí** carries three primary meanings: "around, on either side of, about"; "in exchange for"; and "facing, to, towards, against."

Etymology remains debated. Jasanoff proposes derivation from earlier *h₂n̥t-bʰi, a variant of the instrumental plural *h₂n̥t-mís of *h₂ént-s ("forehead, front"). However, Dunkel questions this semantic development and instead derives *án-bʰi from *án ("on the other side") plus the adverbial locative suffix *-bʰi.

## Major Descendants

**Greek**: Ancient Greek ἀμφί (amphí)

**Latin**: Italic *amβi, yielding Latin ambi-

**Germanic**: Proto-Germanic *umbi (ancestor of English "um-" and related forms)

**Indo-Iranian**: Proto-Indo-Iranian *Habʰí (producing Sanskrit abhí and Avestan aiwi)

**Other branches**: Proto-Celtic *ambi, Proto-Albanian *ambi, Armenian amb-

## Relation to *h₂ent-

The term relates to "the root *h₂ent-" as indicated by category tags, with *h₂ént-s meaning "forehead, front," suggesting a spatial/directional origin for this preposition.
```


### [2026-09-04T19:46:21.604Z] TOOL RESULT

```
# Etymology of Persian آستین (āstīn)

Based on the Wiktionary entry provided, here's what is documented about this word's etymology:

## Current Knowledge Status

The article states the etymology is "of unknown etymology due to not having any clear cognates." No Middle Persian form or Proto-Iranian reconstruction is provided in this source.

## Proposed Borrowing Theory

The only etymology hypothesis mentioned comes from Herzenberg's research. He "compares Pashto _lastúṇay_ ('sleeve') which is related to Pashto _lás_ ('hand')" and proposes the word was potentially borrowed from Southeastern Iranian languages.

Herzenberg's analysis suggests a sound shift mechanism: a /d-/ > /l-/ shift "in some Eastern Iranian languages," with dialectal Persian terms showing initial /l-/ loss, implying borrowing from Pashto or related languages.

## Attestation

The word is documented from Firdawsī (c. 1010 AD), representing its earliest known Persian attestation.

**Note:** The document contains no references to *abi-dasta-, *ā-dasta-, Hasandust, or Gershevitch—only a citation to Herzenberg (2014).
```


## [2026-09-04T19:46:29.465Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1",
 "prompt": "Give the Persian etymology section for شکار (šekār) 'hunt': Middle Persian form, Proto-Iranian root, whether it is a Sogdian loan, and cited sources."
}
```


## [2026-09-04T19:46:31.408Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D8%B1",
 "prompt": "Give the etymology of Persian افسار afsār 'bridle, halter': Middle Persian form, reconstruction (e.g. *abi-sāra- 'around the head'), and cited sources. Also anything about پالهنگ or Aramaic."
}
```


### [2026-09-04T19:46:36.654Z] TOOL RESULT

```
# Persian Etymology of شکار (šekār)

**Middle Persian Form:**
"Not attested in Middle Persian, though related forms are" شکال (škarag, "bird of prey") and وشکل (wiškar, "hunting ground").

**Proto-Iranian Root:**
The word derives from Proto-Iranian *skar- meaning "to pursue, to look for (cattle)," which "has no secure non-Iranian cognates."

**Sogdian Loan Status:**
The entry indicates this is "Perhaps a loanword from Sogdian" 𐽁𐼸𐼰𐽀 (škʾr, "to pursue, to drive"). Both the Middle Persian and Sogdian forms trace back to the same Proto-Iranian root.

**Cited Source:**
Cheung, Johnny (2007), *Etymological Dictionary of the Iranian Verb*, Leiden Indo-European Etymological Dictionary Series; 2, Brill Publishers, page 345.
```


### [2026-09-04T19:46:38.191Z] TOOL RESULT

```
# Etymology of Persian افسار (afsār)

## Middle Persian Origin

The word derives from Middle Persian **\*afsār**, though the page does not provide an explicit reconstruction showing the morphological components (such as a proposed "around the head" etymology).

## Attestation in Related Languages

The Middle Persian term was borrowed into several languages:

- **Classical Syriac**: "ܐܲܦܣܵܪܵܐ (ʾap̄sārā)"
- **Jewish Literary Aramaic**: "אַפִסָרָא (ʾap̄isārā)"
- **Jewish Babylonian Aramaic**: "אַפְסָרָא (ʾap̄sārā), אַפְסִירָא (ʾap̄sīrā)"

## Cognates

Related forms appear in Mazanderani, Kurdish, and possibly Ancient Greek borrowings (ψάλιον, ψαλόν, ψέλιον—all relating to bridle equipment).

## Citation Note

The page references Jacob Levy's 1867 *Chaldäisches Wörterbuch* and other historical lexicographic sources documenting these Aramaic forms, though specific reconstructed morphology is not explicitly discussed in the available content.
```


## [2026-09-04T19:46:45.864Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%B1",
 "prompt": "Give the etymology of Persian افسر afsar 'crown': Middle Persian form, Old Iranian reconstruction (e.g. *abi-sara- 'on the head'), and any cited sources."
}
```


## [2026-09-04T19:46:47.066Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian افزودن afzūdan 'to add, increase': Middle Persian form, the prefix and root reconstructed (abi- + zav-? apa-?), Avestan cognate, and cited sources."
}
```


### [2026-09-04T19:46:52.103Z] TOOL RESULT

```
# Etymology of Persian افسر (afsar) 'crown'

## Middle Persian Form
The word is inherited from Middle Persian (script form not provided in sources), with the reconstructed form showing /⁠aꞵesar⁠/.

## Old Iranian Reconstruction
Scholars propose a Proto-Iranian source, possibly *upasarah, rather than *abisarah. According to Henning (1977), the form "darf nicht auf *abisarah- (> *ōsär) zurückgeführt werden, vielleicht aber auf *upasarah-" (cannot be traced back to *abisarah, but perhaps to *upasarah).

The etymological analysis suggests the word may contain "a deformed prefix to سر (sar, 'head') and a clipped ending."

## Key Sources Cited
- Henning, W. B. (1977) - *Selected Papers*
- Horn, Paul (1893) - *Grundriss der neupersischen Etymologie*
- Steingass, Francis Joseph (1892) - *A Comprehensive Persian–English dictionary*
- Vullers, Johann August (1855) - *Lexicon Persico-Latinum etymologicum*
```


### [2026-09-04T19:46:53.823Z] TOOL RESULT

```
# Etymology of Persian افزودن (afzūdan)

## Middle Persian Form
According to the Wiktionary entry, the word derives from Middle Persian with the form requiring "Book Pahlavi script" (noted as needed but not provided in the current text).

## Morphological Breakdown
The word structure consists of two components:

**Prefix**: From Proto-Indo-Iranian *Habʰí ("to, against, for")

**Root**: Of uncertain origin, potentially connected to Lithuanian gáuti ("to obtain"), though the etymological source remains unclear.

## Etymology Chain
The documented progression traces through:
- Proto-Iranian *Habigaw- ("to increase")
- Middle Persian /abzūdan/
- Early New Persian اڤزودن (aḇzūdan)
- Modern Persian افزودن (afzūdan)

## Sources Cited
The entry references two etymological authorities:
1. Cheung, Johnny (2007) - *Etymological Dictionary of the Iranian Verb*
2. Pokorny, Julius (1959) - *Indogermanisches etymologisches Wörterbuch*

The exact Avestan cognate is not explicitly mentioned in the provided text, though Proto-Iranian connections are documented.
```


## [2026-09-04T19:47:01.738Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"abisarah\\|upasarah\\|afsar\" HENNING_selected_papers.txt | head -10"
}
```


### [2026-09-04T19:47:01.796Z] TOOL RESULT

```
1121:cooled, frozen”. All forms from the base of Av. sarata- (cf. Horn, Grd. Ir. Phil, i, 2, p. 141 ; NP. afsdndan “to press” is probably a mis- spelling of afsardan)—(14) “Institutions,” etc., see BBB., p. 86.— (15) (16) “ Greeting.” MPers. erkaé lit. “(holding the hands) under the armpits”, of. dast-kai, Mir. Man., i, Av.
```


## [2026-09-04T19:47:04.139Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%A9%D9%86%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian افکندن afkandan/افگندن afgandan 'to throw': Middle Persian form, prefix (apa- or abi-?) and root (*kan), and cited sources."
}
```


### [2026-09-04T19:47:09.399Z] TOOL RESULT

```
# Etymology of Persian افکندن (afkandan)

**Middle Persian Source:**
The word derives from Middle Persian *ʾpkntn'* (abgandan), meaning "to throw."

**Morphological Breakdown:**
This is a compound verb with two elements:

1. **Prefix *af-***: Traced to Proto-Iranian *Hápa* ("off, away, from") or Proto-Indo-European *upó* ("under, below, towards")

2. **Root *kan-***: Derived from Proto-Iranian *kánHati* ("to dig")

**Cited Sources:**
The entry references multiple linguistic layers including Middle Persian etymons, Proto-Iranian reconstructions, and Proto-Indo-European roots, situating the word within comparative Indo-European linguistics.

The modern Persian form reflects this ancient compound structure, where the directional prefix combines with an action root to create the sense of forcefully propelling or casting something away.
```


## [2026-09-04T19:47:14.955Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian افشاندن afšāndan 'to scatter, sprinkle': Middle Persian form, prefix (apa- or abi-?), root (*šan / *fšan), and cited sources."
}
```


## [2026-09-04T19:47:16.587Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%AA%D8%A7%D9%81%D8%AA%D9%86",
 "prompt": "Give the etymology of Persian شتافتن šetāftan 'to hurry': Middle Persian form, Proto-Iranian root (*stap?), any mention of abi- + tap 'heat', and cited sources."
}
```


### [2026-09-04T19:47:21.044Z] TOOL RESULT

```
# Etymology of Persian شتافتن (šetāftan)

Based on the Wiktionary entry provided:

**Middle Persian Origin:**
The word is "Inherited from Middle Persian _awištāftan > ōštāftan_."

**Limitations of Available Information:**
The source document does not provide:
- A Proto-Iranian root reconstruction
- Any mention of "abi- + tap" etymology
- Cited scholarly sources beyond the Middle Persian form

The entry indicates this is a "Persian term derived from Middle Persian" but does not elaborate on deeper etymological connections or cite specific linguistic references that would trace the word back to Proto-Iranian or explain the morphological components you've asked about.
```


### [2026-09-04T19:47:22.114Z] TOOL RESULT

```
# Etymology of Persian افشاندن (afšāndan)

## Middle Persian Form
The word derives from Middle Persian **ʾpšʾn-tn'** (/afšāndan/), as documented in MacKenzie's Pahlavi dictionary.

## Components

**Prefix:** *Hápa* ("away") from Proto-Iranian, which functions as the directional element meaning "away" or "off."

**Root:** The Iranian root ***šan*** ("to shake"), which carries the core meaning of the verb. Alternative attestations show ***fšan*** as a variant.

## Etymology Summary
The word combines the Proto-Iranian prefix meaning "away" with a root denoting "shake," yielding the compound sense "to shake away" or "scatter/disperse."

## Cognates
Related forms appear across Iranian languages, including Old Khotanese *ṣāñ*, Baluchi *šánag*, Northern Luri *şənı*, and Gilaki *fišādən*, all reflecting similar semantic fields of scattering, throwing, or dispersing.
```


## [2026-09-04T19:47:29.972Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%B1",
 "prompt": "Give the Persian etymology of انبر (anbor) 'tongs, pliers': is it linked to Greek amphoreus / PIE *ambhi-bher-, or to Middle Persian, or Arabic? Quote any reconstruction and sources."
}
```


## [2026-09-04T19:47:31.435Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/amphi-",
 "prompt": "Give Etymonline's entry for amphi- (Greek amphi, PIE root *ambhi/*mbhi), and any related entries mentioned (amphitheater, amphibious, ambi-, both, by, be-)."
}
```


### [2026-09-04T19:47:34.454Z] TOOL RESULT

```
# Persian Etymology of انبر (anbor)

Based on the Wiktionary article provided, the Persian word انبر derives from **Middle Iranian**, ultimately tracing to Proto-Indo-European.

The source states:

> "From Middle Iranian, from Proto-Indo-European *h₂eḱ- ('sharp')."

The reconstruction connects the term to a PIE root meaning "sharp" rather than to the Greek *amphoreus* or *ambhi-bher-* formations you mention. The etymology emphasizes a Middle Iranian intermediary stage between the ancient PIE source and modern Persian.

The article provides no discussion of Arabic influence or alternative etymological theories. The focus remains on the Indo-European lineage through the Middle Iranian language family.
```


### [2026-09-04T19:47:37.625Z] TOOL RESULT

```
# Etymology of *Amphi-*

## Core Definition
The prefix *amphi-* (or *amph-* before vowels) originates from Greek and means "on both sides, of both kinds; on all sides, all around." It traces back to the PIE root *\*ambhi-*, meaning "around," which also connects to Latin *ambi-*.

## Key Related Terms

**Amphibian** (1630s): Originally described "having two modes of existence," from Greek *amphibios* ("living a double life"), combining *amphi* + *bios* ("life"). The modern zoological restriction to animals with aquatic and terrestrial life cycles dates to 1835.

**Amphitheater**: Greek *amphitheatron* literally means "double theater," describing a structure "with spectators all around," constructed from two semicircular classical theater designs.

**Amphibious**: Related adjective form describing capacity for both aquatic and land existence.

**Ambi-**: Latin cognate prefix sharing the same "both/around" semantic field.

The prefix remains productive in English, appearing in scientific and technical terminology denoting bilateral or surrounding characteristics.
```


## [2026-09-04T19:47:44.300Z] TOOL CALL #77: Bash

```json
{
 "command": "curl -s \"https://en.wiktionary.org/w/index.php?title=%D8%A7%D9%86%D8%A8%D8%B1&action=raw\" | head -80"
}
```


### [2026-09-04T19:47:46.101Z] TOOL RESULT

```
{{also|انتر}}
==Khalaj==

===Noun===
{{head|klj|noun|head=اَنبُر|tr=ambur|definite accusative|اَنبُروُ|plural|اَنبُرلار}}

# {{spelling of|klj|Arabic|ambur|t=[[tongs]]}}

====Declension====
{{klj-arabic-infl-noun-c|u}}

==Persian==

===Alternative forms===
* {{alt|fa|انبور|tr={{fa-xlit|اَنْبُور}}}}

===Etymology===
From {{uder|fa|ira-mid|-}}, from {{uder|fa|ine-pro|*h₂eḱ-||sharp}}.

===Pronunciation===
{{fa-IPA|anbur}}

===Noun===
{{fa-noun|cls=اَنْبُر}}

# [[tongs]]

====Descendants====
* {{desc|az|ambır|bor=1}}
* {{desc|chg|bor=1}}
** {{desc|ug|ئامبۇر}}
** {{desc|uz|ombur|ombir}}
* {{desc|klj|ambur|bor=1}}
* {{desc|tk|ammyr|bor=1}}
```


## [2026-09-04T19:47:56.781Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"انبر\" ARY_pages.txt | head -10; echo \"=== latin index ===\"; grep -n -i \"ANBOR\\|ANBUR\\|AMBHI\\|ANBAR\" ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-04T19:47:56.835Z] TOOL RESULT

```
=== latin index ===
```


## [2026-09-04T19:47:56.930Z] TOOL CALL #79: WebSearch

```json
{
 "query": "Persian انبر anbor \"tongs\" etymology Hasandust *ham-bar Middle Persian"
}
```


### [2026-09-04T19:47:59.110Z] TOOL RESULT

```
Web search results for query: "Persian انبر anbor "tongs" etymology Hasandust *ham-bar Middle Persian"

Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T19:48:06.080Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in HRN.txt HUB.txt; do echo \"== $f\"; grep -n -i \"ambur\\|anbur\\|ambor\\|anbor\\|ambar '\\|anbär\" $f | head -6; done; echo \"== SYN amphora/tongs ==\"; grep -n -i \"tongs\" SYN.txt | head -5; echo \"== WLD ambhi ==\"; grep -n \"ambh\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10"
}
```


### [2026-09-04T19:48:07.744Z] TOOL RESULT

```
== HRN.txt
== HUB.txt
9119:das im Arm. bilabial war: ambar 'Speicher, amharem ich
== SYN amphora/tongs ==
5997:1, IB *dont-, *dnt-, prob. a pple. form of *ed- ‘eat’. But some think this is only a secondary association and con nect with the root of Grk. daxvw ‘bite’, OE tang ‘tongs’, etc. Walde-P. 1.120. ErmoutM. 260f. Walde-H. 1.340 f. Feist 483.
6867:OHG zanga ‘tongs’, etc. Walde-
14144:2. Lat. forfex, esp. pl. forficés (> Olt. forfice, It. forbict, Rum. foarfeci, pl.), history complicated and disputed. Prob. fr. forceps, ‘pair of tongs, forceps’ (cpd. of formus ‘warm’ and root of capere ‘take’) with phonetic changes (through an intermediate forpex by dissim.) and shift of application from ‘tongs’ to ‘shears’ owing to the similarity of shape. Walde-H. 1.526f. (with full refs.). REW 3485.
== WLD ambhi ==
3620:ambhi, pibhi 
3636:ambhi, mbhi „beiderseits wovon, um— herum" (syntaktiscbes s. Brugmann 
3637:Grdr. II 2 2, 795 f.), ambho(u) Du. „beide“, und abnliche auf -bhi, -bho- 
3702:*ambhi „um“ zugunsten von *obhi (ab. oha, s. lat. ob) aufgegeben wurde 
3706:Mindestens das Yerhaltnis *amblio(u), *ambhi : got. usw. bai, bi laBt es 
8066:vor, s. *ambhi); die Spuren eines gr. *£(pi- sind triigerisch, s. Gunther IP. 
8071:mit Dat. (Loc.), auch mit Instr., Praefix ,be-“; s. auch unter *ambh>, das 
8547:emb(h)- : ai. ambhas- n. „Wasser“; ambit n. „AVasser“, gr. opfigog ,,Regen“ 
11444:241 Verb, von abrs mit ai. ambhas- „Gewalt“, cech. obr „Riese‘' (dies mit 
30085:Ai. crambhate, Ptc. crabdha- (mit vi- und andern Praep. 1 . vertrauen,
```


## [2026-09-04T19:48:10.965Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3630,3712p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt"
}
```


### [2026-09-04T19:48:11.024Z] TOOL RESULT

```
*maisa- „klein, winzig" bezogen wegen norw. mdartl. meis „diinne, schwach- 
liche Person", meiseleg „diinn und scbwachlich", tvflam. mijzen „zerkrumeln“, 
mejzel „BiBchen, Kriimchen". Am zuverlassigsten ist der Y ergleich des lat. 
mit dem brit. Worte ( merula nicht besser nach Lehmann KZ. 41, 392 zu 
[MQfia'iQCO „schimmere“). 

ambhi, mbhi „beiderseits wovon, um— herum" (syntaktiscbes s. Brugmann 
Grdr. II 2 2, 795 f.), ambho(u) Du. „beide“, und abnliche auf -bhi, -bho- 
ausgebende Formen. 

Gr. dpcpi „um“ (a/ucpi-s „zu beiden Seiten", mit demselben Adverbial -s, 
wie z. B. uyj, /axQUf ig, s. Brugmann Grdr. II 2 2, 737); lat. amb- (vor Yokal, 
z. B. ambigo ), am-, an- (vor Kons., z. B. ampul o, amicio aus *am[bi] jacio) 
untrennbares Praefix „herum, um, ringsum", altlat. auch Praep. am „cir- 
cum" m. Acc. 

iambi- im Sinne von „beide“, den auch anceps zeigt, ist dagegen Zs.- 
Form *ambo- von ambo), umbr. amb- ( amboltu ), an- ( an-ferener „circum- 
ferendi", an-clersafust „circumdederit“, anseriatu „observato“, s. zu letzterem 
Jacobsobn KZ. 40, 112 f.), osk. amvianud „circuitu, Umweg" amnud 
„circuitu, causa" (kaum *amb-beno- : venio , sondern «o-Ableitung, s. v. Planta 
II 32, 623; nicht zu arnnis oder nach Fay Cl. Bev. 13, 399, Cl. Quart. 4, 80 
als *agmnos zu agmen) : mit -er- Erweiterung nach praeter-eo , intereo (siehe 
Y. Planta II 455, Yf. LEWb. 2 31) umbr. amprehtu. ambretido „ambito, 
ambiunto", vielleicht auch osk. am fret „ambiunt“ (wenn nicht eher nach 
Schulze KZ. 45, 182 in *am-ferent „circumferunt, 7iegiayovai“ zu zerlegen; 
die vermuteten lat. Spuren der gleicben -er-Erweiterung, amfradus , (im- 
brices sind dagegen anders zu beurteilen) ; mit ti- Erweiterung (nach pos-t , 
per-t, Buck Elementarbucb 65) osk. ampt „circum“ (wie umbr. ambr- zu- 
nachst auf Grund des aus amf- vor Kons. vereinfacbten am-)’, alb. mbi , 
mbs „bei, auf, an" (G. Meyer Alb. Wb. 265); unsicher ist arm. amb- = 
apcpl in amb-oij „vollstandig, ganz" neben ot ) , ar-ol) „gesund, ganz" (Hiibsch- 
mann Arm. Gr. I 416, Brugmann Grdr. II 2 2, 795). 

*mbhi : gall, ambi- „um“ (z. B. ’ApfU-dgavoi), cymr. am- (durch i-Umlaut 
em-, pm-), corn. bret. am-, cm-, air. imb-, imm-, immc- „um“; abd. as. umbi, 
aisl. amb, ags. ymb, ymbe „um“ (im Got. von hi aufgesogen); ai. abhi-tah , 
av. aiwito „zu beiden Seiten, rings" (iiber av. aibis , ap. abis strittiger Bed. 
s. Pedersen IvZ. 40, 127, Bartholomae IF. 19, Beiheft S. 106; die Endung 
. .s in geschichtlichem Zusammenbang mit der von gr. dpq ?(£?); ai. abhi 
kann in der Bed. „um“, ap. abiy , av. aibl, aiivi in der Bed. „iiber, in 
betreff von" aus *mbhi stammen, muB es aber nicht, und setzt im iibrigen 
sicher das idg. *obhi oder *ebhi fort. 



an- 


55 


*bhi : got. bi in der Bed. „um“, mit Auslautdehnung in betonter Stellung 
as. ahd. ags. bT, nhd. bei (fiber zweifelhafte Ableitungen s. Falk-Torp 37 
und 1437 unter lil II „Zwischenraum, Zeitraum“, 73 und 1437 unter billede 
„Bild“). 

; ,Beide :< : 

Gr. a/upco „beide“ (Ableitung aurpormog) ; lat. ambo , -ae, -o „beide“; 
ai. ubhilu „beide“, av. uwa- ds. ; lit. abii, aksl. oba ds. ; got. bai m., ba n., 
gen. baddjc ( bajops , s. zur Bildung Brugmann Grdr. II 1 2 * 2, 77 ; anders — 
im Ausgang zu lat. nostrates — Pick III 4 255), as. be thie, ags, ba (pu), 
engl. both, ahd. beide, bede , anord. bader gen. beggja ,,beide“ (mit schwer 
zu erklarendem a). , 

Yon diesen wurde ai. ubhau, av. uwa bisher als Zs. mit einem u- „zwei“ 
(lat. ulgintt) betrachtet; Sommer IF. 30, 404 leugnet ein solcbes u- und 
betraebtet die ar. Formen als durcb den Labial bewirkte Verdumpfung 
eines *abhau~*mbhdu unter Berufung auf ai. Kubcra-h aus *Kabcrah (vgl. 
Patronymikon Raberaka-h; Wackernagel KZ. 41, 3l4ff.). Lit. abu, aksl. 
oba beruhn wohl auf Umbildung von *amb-o zu einer Zeit, als die Praep. 
*ambhi „um“ zugunsten von *obhi (ab. oha, s. lat. ob) aufgegeben wurde 
(kaum nach Solmsen RhMus. 61, 502 A. 1 ursprfinglich zu si. obz mit 
einem Verhaltnis wie zwischen got. bai „beide“ : bi „um, bei, an“). 

Mindestens das Yerhaltnis *amblio(u), *ambhi : got. usw. bai, bi laBt es 
kaum zweifelhaft sein, daB am- (vielleicht aus an-) ein erstes Zsglied sei ; 
Pedersens (Pron. dem. 42) Ansatz eines *mbhi, *mbhou als Grundlage samt- 
licher genannton Formen widerspricht unseren sonstigen Anscliauungen 
fiber idg. Lautverhaltnisse. Andere Lit. fiber den Anlaut unserer Sippe 
bei Brugmann Distr. 22 A. 1, Grdr. 2 II 2, 795, Yf. LEWb. 2 33 (auch gegen 
die Meinung, da8 am- noch in selbstandiger Yerwendung in lat. am-icio ,
```


## [2026-09-04T19:48:18.268Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"abiy\" KNT.txt | head -10; echo \"=== TLM ===\"; grep -n \"abiy\\|abiš\" TLM.txt | head -6"
}
```


### [2026-09-04T19:48:18.326Z] TOOL RESULT

```
389:aiayabiya ‘king’, with 6j from ig.
423:xsdyabiya : dahytiném : Vistaspahyà : Dérayavahaus : z5ayattyahyà : puça : Haxámanisya : puça : Haxdémanisiya : hya : imam : lacaram : akunaus
513:manisiya.» ` abyapara А?$а 4, for *abiyaparam. apan*yükama A’Sa 3, and presumably [n*yá]kama
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
641:$2. Tue InEoGRAMS are five in number, stand- ing respectively for s8dyabiya ‘king’, dahydus ‘province’, bümi$ ‘earth’, Auramazdá ‘Ahura- mazda’, and baga ‘god’; they are transcribed by Хо, DH, BU, AM, BG. In DSk 4 there is what seems to be a ligature for AM-ha,
944:*mbhi, ОР abiy, Skt. abhi, oHG umbi (but see "^ — Lex. s.v. abiy).
1033:Lt. frater. рАг. *abhi,! OP abiy, Skt. abhi. pIE *u-bhó and -bhdu ‘both’, OP фа, Skt.
1035:t Conflux of pIE *mbhi and pIE *obhi, see Lex. s.v. abiy.
1686:The sequence -tya- seems in some instances to contract to -i-; all the examples are in augmented forms of compound verbs, in some of which the uncontracted forms also appear, in which the analogy of the separate uncompounded form is the cause of the failure to contract: abi-javayam, also abiy-ajávayam. ni-Sidayam, also niy-asddayam. ni-Màya, also niy-aStdya and niy-aStayam. ni-yasaya for *niy-ayasaya; perhaps [а|йуа[туа|
1797:VI. With suffix -йа-, becoming Med. -6;a- in zXiyabiya-, and OP -Ea- in anustya-.
=== TLM ===
223:yahya  br-40)[a]ta  pasava  kara  haruva  hami(9riya  abava  haca Kanbujiya  abiy  avarn  41)[a]siyava  uta  Parsa  uta  Mada  uta  aniya dahyava  xsa0ram  hauv  42)  agar  bay  ata  Garmapadahya  mahya  IX raucabis  Sakata  aha"  avaftl  xsa-43)0ram  agarbavata  pasava Kanbujiya  uvamarsiyus  amariyata
246:16.  0atiy  78)  Darayavaus  xsayafliva  va0a  adam  Gaumatam tyam  magum  avajanam  pa-74)sava  I   martiya  A#rina  nama  Upa- dara”mahya1  pu0  a   hauv  udapata[ta  Uvajai]-7o)y  karahya  avafla aflaha  adam  Uvajaiy  xsayatfiya  amiy  pa[sava]  Uva-76)jiya  ham- i0riya  abava"  abiy  avam  [   A   ]<9rinam  asiyava”  hauv  x[saya0iya] 77)abava  Uvajaiy  uta  I   martiya  Babiruviya  Nadi”tabaira  nama Aina[ira]hy-78)a  pu0ra  hauv  udapatata  Babirauv  karam  avafti adurujiya  adam  Nab-79)ukudracara  amiy  hya  Nabunaitahya pu0ra  pasava  kara  hya  Babiruviya  80)haruva  abiy  avam  Nadin- tabairam  asiyava  Babirus  hami(9riya  abava  x-81)sa0ram  tya  Ba- birauv hauv  agarbayata
248:18.  0atiy  Darayavaus  xsayafliya  pasava  adam  Ba-84)  birum  asi- yavam  abiy  avam  Nadintabairam  hya  NabukMracara  aga[ubat]- a   8o)kara  hya  Nadintabairahya  Tigram  adaraya  avada  aistata2  uta 86)abis  n   a   viva  aha  pasava  adam  karam  maskauva  avakanam  am iyam  usa-87)barim3 4  akunavam  aniyahya  asarn*  f ranayam5  Aura- [maz]damaiy  upas[t]am  88)abara  vasna  Auramazdaha  Tigram viyatarayama6  [a]vada  avam  karam  89)tyam  Nadintabairahya adam  ajanam  vasiy  A0r[i]yadiya[h}"a]  mahya  XXYI  rau-90)cabis Sakata  aha“  a[  va0]a  hamaranam  akum[a]
257:8[abiy]avam,  Foy.
275:4.  0atiy  Darayavaujs  xsaya0iya]  adakaiy  adam  asna-12)iy  aham abiy  Uvajam  pasava  liaca[ma  atarsanUva]jiya  avam  Marti-13)yam agarbaya11  hyasam  ma0ista  aha  [utasim  av]ajanan
276:5.  0atiy  D-14)arayavaus  xSaya0iya  I   martiya  Frafvartis  nama Mada]  hauv  udapatat-15)a  Madaiy  karahya  ava0a  a0aha  [adam Xsa0rita  am]iy  D vaxstrah-16)ya  taumaya  pasava  kara  Mada  hya [v'0apatiy  aha]  hacama  hami0riya  a-17)bava  abiy  avam  Fravar- tdm  asiyava  hauv  [xsaya0iya]  abava  Madaiy
```


## [2026-09-04T19:48:24.696Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^abiy\\|abiy, prep\\|abiy prep\\|abiy '\" KNT.txt | head; python3 - <<'EOF'\nt=open('KNT.txt',errors='ignore').read()\ni=t.find('abiy,')\nwhile i>0 and i<len(t):\n    seg=t[i:i+300]\n    if 'prep' in seg or 'Skt' in seg:\n        print(repr(seg)); break\n    i=t.find('abiy,',i+1)\nEOF"
}
```


### [2026-09-04T19:48:26.829Z] TOOL RESULT

```
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
2282:abiy-aparam (written ab*yapara), pati-padam, para-draya (also as two words), pasdva (from *pasd ava), ni-pad y.
2826:nouns. E- ачат, prep. W. асе. ati-, pref, w. verbs. abiy, prep. W. ace. anu», prep. w. instr. and gen. apa-, pref. w. verbs and nouns. abiy, prep. w. acc.; pref. w. verbs and nouns. ava-, pref. w. verbs. ud-, pref. w. verbs and nouns. upd, prep. w. acc.; pref. w. verbs and nouns. upariy, prep. W, асс.; pref. w. verbs. lara, prep. w. acc. ni-, prep. W. loc. in phrasal adv.; pref. w. verbs, nij-, pref. w. verbs. nipadày, prep. W. ace. T patiy, prep. ж. асе.; postp. у. acc, inst, loe; .^
4955:abiy prep. with acc. ‘to’: DB 1.91. Apparently doublet to айу (Ву. Gr. §102), possibly by con- tamination of *a; antevocalic and ati antecon- sonantal, in sandhi ($80; Mt. Gr. $103).
5012:abiy prep. and prefix ‘to, against, in addition to’: GAv. aibi. LAv. aiwi, Skt. abht; conflux of pIE *mbhi, oHG umbi ‘round about’, and pIE *obhi, oCS ой ‘beside, by’.
5019:abiyaparam. adv. ‘later, afterward’, from abiy + aparam (§191.1V). ab*yapara (822, §52.V) A’Sa 4.
'abiy, Skt. abhi, oHG umbi (but see "^ — Lex. s.v. abiy).\n*hmtom ‘100’, in Oata-guš (uncertain etymology,\nsee Lex. s.v.).\n*bhndh-to-, OP basta- ($85), Skt. baddhá-, cf. Eng. bound. negative prefix *n- in a-zSatna-, a-xsala-, etc. *sm-dhe, OP hadà, Skt. sahá ‘with’. I. Before a vowel ог; or у, pIE » a'
```


## [2026-09-04T19:48:33.953Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT both ===\"; grep -n \"^both\\|^ambassador\\|^ambient\\|^amphi\" SKT.txt | head; echo \"=== KLN both ===\"; grep -n \"^both,\\|^amphitheater\\|^amphibious\\|^be-, pref\" KLN_1966.txt | head"
}
```


### [2026-09-04T19:48:34.022Z] TOOL RESULT

```
=== SKT both ===
648:both  sirJes,  around  ;  see  Ambf-.
7038:both  are  from  L.  rtfring^  ^
=== KLN both ===
2547:amphitheater,  amphitheatre,  n.  —  L.  amphi  thea- trum,  fr.  Gk.  dp9iH£dxpov,  lit.  meaning  ‘having
5409:both,  adj.,  pron.  and  conj.  —  ME.  bathe,  bothe, fr.  ON.  bupir,  which  is  rel.  to  OS.  bethia,  OFris. bethe,  Du.  beide,  OHG .beide,  bede  (masc.), beido (fem.),  beidiu  (neut.),  MHG.  beide,  bede  (masc. and  fem.),  beidiu  (neut.),  G.  beide,  Goth,  bajops, ‘both’;  formed  fr.  Teut.  *ba-,  ‘both’,  and  the def.  article  (see  the).  The  first  element  in  both, etc.,  is  rel.  to  OE.  hegen  (masc.),  bd  (fem.  and neut.),  Goth,  bai  (masc.),  ba  (neut.),  ‘both’,  and cogn.  with  the  second  element,  in  01.  u-bhdu (masc.),  u-bhi  (fem.),  Avestic  u-wa  (masc.),  u-be (fem.),  ‘both’,  Toch.  A  am-pi,  am-pe,  B  ant-api, Gk.  ‘both’,  apt-pi,  ‘round  about’,  L.
8280:amphitheater  in  Rome  built  by  Vespasian  and Titus.  —  Neut.  of  the  adj.  colosseus,  used  as  a noun.  See  prec.  word.
```


## [2026-09-04T19:48:45.776Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aiwi\\.ax\\|aiwyäxs\\|aiwyaxs\\|aiwyäx\\|axsaya\\|äxsti\" BRT.txt | head -8; echo \"=== NYB glossary ===\"; grep -n \"abgan\\|abzūd\\|abzay\\|afšān\\|afsōs\\|abrōz\\|abesar\\|abdast\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:48:45.844Z] TOOL RESULT

```
3967:Fa.:  fehlt, j.  armySii  N.  14:  lies  'yäs,  s.  'a*-. j.  aiwyäxiay'  Vf.:  ».  unter  ö;ri-  und  joy-.
4416:•  j.  an-äxätay  f.  'Unfriede':  vainJi  ahmt nmane  .  .  äxstis  "Um  Y,  60,  5 ;  —  iOm axsisis  'tSisÜa  mi>ra  xsayehe  dahyunqm Yt.  10.2  g.
4504:•  j.  anu-matayae-:vr,  "t^e  Inf,  '(und)  im Denken  zu  folgen,  zu  denken  gemäss  -' (Dat",  Gen.):  ya^a  azsm  /nJcayeiie  {sA) .  .  zara%ustr»m  "ISe  dagnayjt  aiiuxtJe  .  . anu.varHSe  Yt.5.18;  —  haxsaya  (sd.)  .  . frat^ma  .  .  aiähl  dasnayj  'iayaeca  , .  Y.
4519:aijuxOe..'t!e  daenayai \t.^.iZ; — haxsaya
6862:■rahe  mazdä  Vr.  14.2;  — yeAh! hltqm  äat yesng  (sd)  paitl  vai)hd  mazdä  'rS  vag'iä Y.  27. 1 5 ;  —  äppm  zazahi  tarn  ys  °rS  mazdä zrayaahal ha'a  z'ouru.kas-lt ha'^ra  Täi?mca dunmqnca  V.5.  15;  isf.'.  60;  —  a'iä  Ml (sd.)  °rB  ma-id\  zard^ustr^m  aoaxsayaUa Y.  /2.  S ;  —  ar>dvlm  . .  yahmya  °rS  mazda ivaiiayal  Yt.  5.85;  —  imat  t!  saahat
7098:•  j.  äxä-''  V.,  niur  mit  ami  'i<f>opäv\ I  Praes.  30  (Iter.)  amyJxsaya-.  Inf. I  aiwyäxstriii.
7106:haxanrim  naram  Syum  nanm   aiwyäxsa~\  .     ,  ,    __v.,    ._.,v   „  ,
7112:kJn"auTh''«i-"'t^."S^'ir^s^zen';!^  •  j-.  g-  G  P-)  'ätar- :  3/^r;..,  Oir-,  ,T//-'> aiwyäxi'  nach  S  ^ö*  3  a  erklären;  das  gilt  m.  'Feuer',  I)  im  jAw.  'Feuer'  im  AIl- auch  für  aa.'yäxU<xr-,  vgl.  Bgm.  BSächsGW.  gemeinen  und  spez.  vom  Herd-  und  vom '°97-  35-  sakralen  Feuer,  oft  persönUch  gedacht  und
=== NYB glossary ===
```


## [2026-09-04T19:48:53.258Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -c NYB_vol2_glossary.txt; grep -n -i \"afšān\\|afsan\\|abgan\\|abzûd\\|abzud\\|abrōz\\|abroz\\|apzût\\|'pzwt\\|afsar\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:48:53.324Z] TOOL RESULT

```
920054 NYB_vol2_glossary.txt
590:api-sar [pysl] crown 6%. — MPrs ’bysr (S); NP afsar. Probably < Olr *upa-sarah- ‘that which is on the head’ (v. sar) > *apa-sara- and then remodelled to "api- sara- with variable accent: *api-sara- > apisar, *ápi-sara- > *apsar > afsar.
6966:afsar: api-sar
```


## [2026-09-04T19:49:01.794Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"api-dast\\|apa-gand\\|api-zūd\\|api-zud\\|apzūd\\|api-rōz\\|api-roz\\|apirōz\\|apzāy\\|apisan\\|afsōs\\|apsōs\\|api-tāp\\|awistāp\\|ōštāp\\|api-kan\" NYB_vol2_glossary.txt | head -20; echo \"=== index lookups ===\"; grep -n \"afzūdan\\|afgandan\\|afšāndan\\|afrōxtan\\|āstīn\\|šitāftan\\|šikār\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:49:01.865Z] TOOL RESULT

```
=== index lookups ===
6963:afgandan, augandan: apa-kandan
```


## [2026-09-04T19:49:04.623Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apa-kandan\\|apa-kan\" NYB_vol2_glossary.txt | head; echo ---; grep -n -A4 \"^apa-kandan\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-04T19:49:04.684Z] TOOL RESULT

```
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
5720:"bgndn: apa-kandan
6963:afgandan, augandan: apa-kandan
---
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
497-apākēh [’p’kyh] 1. company; pat ~ together 5712, — 2. backward movement: pat ~ back 418; v. pat-apākēnītan. — 3. help, assistance 5919-20, 729-26 (opp. ha- mēstārēh). — V. lapāk and ?apäk. Paz. āvāgī. V. also apar-apākēh.
498-apäkenitan [—-ynytn'] to make a p., or a th., one's helper, or companion, or help: hakar vēnākēh apakéné [-yd] (if thou wilt make Clear Vision thy helper
499-==) if thou wilt have recourse to Clear
500-Vision 595, with the gl. ku-t dančikeh bavet ‘that is: (if) knowledge is to be thine’. — Cf also pat-apäkenitan.
```


## [2026-09-04T19:49:11.864Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"api-zūtan\\|api-zut\\|apzūtan\\|api-zav\\|abzūdan\\|zav-\\|api-rōčitan\\|api-rōz\\|apirōč\" NYB_vol2_glossary.txt | head -10; echo ---; grep -n \"afzūdan\\|afzudan\\|afzāyišn\\|afrōxtan\\|afroxtan\" NYB_vol2_glossary.txt | head -10; echo \"=== index near 6963 ===\"; sed -n '6955,6975p' NYB_vol2_glossary.txt"
}
```


### [2026-09-04T19:49:11.946Z] TOOL RESULT

```
874:azbāyišn ['zb'din'] invocation 70H. — Borrowed from Av. (1667 sg.) zav-, pres. zbä-.
5489:zav-: azbayisn
---
=== index near 6963 ===
va + -pi: aivap vara-: ham-var vatsa-: vaccak vāyu-: *vai
vic-: lvéxtan vicära, vicärayati: vicar vijate: ?vöxtan vrsan-: gusn
New Persian
ab: ap
abad, abadan: apatan
abistan: äpustan
abr: avr
ačar, adar: ātur
afgandan, augandan: apa-kandan
afli)rin: àfrin
Afrasiyab: Fräsiyäk
afsar: api-sar
afsös: apa-sos
afsün, austin, afsà, afsa-
|  yidan, afsän, ausän: apa-sutak
afsurdan: apa-särtan
afšurdan, afšardan: apa: šartan
afzun: apa-zon
ägähi: ākāhēh
agar: hakar
ägös, dyoš: ākēš
```


## [2026-09-04T19:49:16.636Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -A6 \"^apa-sōs\\|^apa-sos\\|^apa-zōn\\|^apa-zon\" NYB_vol2_glossary.txt | head -40; echo ===; grep -n \"apa-sos\\|apa-zon\\|apa-zōn\\|apa-sōs\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-04T19:49:16.685Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-04T19:49:19.346Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apa-s[oō]s\\|apa-z[oō]n\\|apasos\\|apazon\" NYB_vol2_glossary.txt | head; echo ===; grep -n \"^apa-\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-04T19:49:19.392Z] TOOL RESULT

```
Exit code 1
565:apazónikéh possession of overflowing spiritual blessings, or gifts, a quality characteristic of Zartuxšt's homestead 502, with the gl. apazon thac ke veš bavet ke mat ke-c rasét? from whom, among those who have come and who are to come, does more (spiritual) in- crease issue [than from Z.’s birthplace]? probably a quotation; — heavenly nature, of Zartuxst 5375. 11019.
2731:nikéritan [nkdlytn'] to look, to watch, to notice; to consider, to reflect: nikér ku nē... take care not to... 45; api-š bé-c nikerit kū ... and she reflected, think- ing (+ dir. speech) 38; apfr rāyēnītan i Zartuxst nikérit he pondered as to how to do away with Z. 501%; — apāc ~ to look up 233-318; — tō an... apar nikéram pat apazonikeh u bavandak-menišneh kū-t pat han xānak nikéram i-t hast as for thee, with (my) heavenly powers and perfect thinking I see through thee, namely, I see thee in that house which is thine [1. e. Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attested by FrP 10. As the spelling -dl- regularly denotes -ér- we have to establish
2802:dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hurmuzd, Ormuz(d).
6436:awazūn: apazon
6967:afsös: apa-sos
6972:afzun: apa-zon
(eval):1: == not found
```


## [2026-09-04T19:49:24.726Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"apa-sōs\\|apa-sös\\|apa-sos \\|apasōs\\|apa-zōn \\|apazon \\[\" NYB_vol2_glossary.txt | head; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',errors='ignore').read()\nimport re\nfor k in ['apazon','apa-sos','apasos','apa-sōs']:\n    for m in re.finditer(re.escape(k), t):\n        s=t[max(0,m.start()-100):m.start()+700]\n        if '<' in s and 'Olr' in s or 'NP' in s:\n            print('###',k); print(s[:800]); print(); break\nEOF"
}
```


### [2026-09-04T19:49:26.960Z] TOOL RESULT

```
536:apa-sös [’psws] derision, mockery, scorn 6616, 7527. — Ps. ?pswsy; Paz. awasos; NP afsós; < OP apa-cauga- < Olr "apa- sraudra- from apa + Av. (1639 sqq.) srav-
### apazon
ondered as to how to do away with Z. 501%; — apāc ~ to look up 233-318; — tō an... apar nikéram pat apazonikeh u bavandak-menišneh kū-t pat han xānak nikéram i-t hast as for thee, with (my) heavenly powers and perfect thinking I see through thee, namely, I see thee in that house which is thine [1. e. Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attested by FrP 10. As the spelling -dl- regularly denotes -ér- we have to establish
140
nipart
the pronunciation nikér- < *ni-karyati (of the same type as the syn. spas-: spasyeiti ‘he espies, finds out’, cf also Skr pasyati), which also accounts for Paz. NP nigar-, niger-, ci men(itan) < *manyati: Paz. manidan, minidan. Hübschmann, PSt. 102, no. 1038, nikir- < *nikriya- (better
```


## [2026-09-04T19:49:32.624Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '560,570p' NYB_vol2_glossary.txt; echo \"=== apa-sos full ===\"; sed -n '536,538p' NYB_vol2_glossary.txt"
}
```


### [2026-09-04T19:49:32.679Z] TOOL RESULT

```
26
apa-zütan
apa-zāyītan pz'dytn'] v. apazütan.
apa-zón [’pzwn'] increase, addition 11217; tan pat-~ kunéh increase thy physical well being 21%, cf s. v. ?pat (11); increase of spiritual blessings 50%. — MPrs ’bzwn (A-H IT); Paz. awazün; NP afzün ‘more, greater’; < *abi-Zavana-, in which api- was substituted for abi-, v.s. v. apa-; from apa-zūtan, q.v. Wikander, Orbis XXXI, 1972, 183—184, prefers the read- ing Ppzn'] = äp-zan ‘a bath(ing vessel)’, NP abzan referring to the corresponding passage of Sn: bi- garmäbah šau ‘go to the warm bath!’
apa-zönik he who has, administers apa- zon, bestower of overflowing, everlasting blessings, epithet of Ohurmazd 399-5. 58$. 59°; of Zartuxšt 1101; sup. ~-tom 57%. — Renders Av. (1618. 1619) spanta-, spē- nista-. Paz. awazuni, Skr. v. guru, brhat (Mx, SGV). Cf Bailey, BSOS VII, 1934, 292—294.
apazónikéh possession of overflowing spiritual blessings, or gifts, a quality characteristic of Zartuxšt's homestead 502, with the gl. apazon thac ke veš bavet ke mat ke-c rasét? from whom, among those who have come and who are to come, does more (spiritual) in- crease issue [than from Z.’s birthplace]? probably a quotation; — heavenly nature, of Zartuxst 5375. 11019.
apa-zütan ["pzwtn'], apa-zāyītan [’pz’dy- tn'], apazäy- ['pz?d-], to increase, to augment, pt. = pret. pass. 3d p. sg. apa- züt 109%, apazäyit ['pz'dt'] 925. — < *abi-jav-, in SW with api- substituted for abi- (v. s. v. apa-) < abi-+ Av. (504) !gav- ‘to procure’; MPrth "bgwdn *bg*w- ‘to increase, to add to’, ?bg^w ‘increase’; Arm lw. augut ‘profit’; — OP caus. abi- jävaya- ‘to add’; MPrs pres. ’bzw- intr., ’bz’y- trans. ‘to increase’; Paz. awazūdan awazüed. Henning, A-H III Gloss. s. v. ’bgwdn; Benveniste, JA 228, 1936, 203- 204; Ghilain 76.
www.parsianjoman.org | ool wok
*apa-Zirisnik
*apa-žīrišnīk ['pcylinyk] "praiseworthy 1063. — Possibly from Av. (512) atbt-*gar- ‘to praise’, (89-90) aibi-jaroti- ‘praise’, aibt-jarotar- *praiser'. Cf āžarm, garämik, gir-; MPrth °bjyrw’ng ‘disciple’ (A-H III).
äp-eihrak [’p'-cyhlk'] containing the seed of the waters 87°; àp- u damik- u urvar- u gospand-cihrak containing the seed of the waters, the earth, the plants and the cattle 8711. — Av. (103 sq.) af$-cidra-; v. cihr and -cihrak.
=== apa-sos full ===
apa-sös [’psws] derision, mockery, scorn 6616, 7527. — Ps. ?pswsy; Paz. awasos; NP afsós; < OP apa-cauga- < Olr "apa- sraudra- from apa + Av. (1639 sqq.) srav-
(HP II, 15); another etymology Bailey, BSOS VII, 1934, 286.
apasös-bar [-~-bl] suffering mockery, scorn 6615,
```


## [2026-09-04T19:49:53.400Z] TOOL CALL #94: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ambassador",
 "prompt": "Give Etymonline's etymology of ambassador and of embassy, including the Latin/Gaulish ambactus, its Celtic *ambi-akto- 'one sent around' analysis, and the PIE root cited."
}
```


## [2026-09-04T19:49:55.214Z] TOOL CALL #95: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D8%A7%D8%B4%D8%AA%D9%86",
 "prompt": "Give the etymology of Persian افراشتن afrāštan 'to raise': Middle Persian form, prefix and root (abi- + raz-?), cited sources."
}
```


### [2026-09-04T19:49:59.560Z] TOOL RESULT

```
# Etymology of Ambassador and Embassy

## Ambassador

According to Etymonline, **ambassador** comes from late 14c., from Old French *embassator/ambassateor*, which derives "via Provençal or Old Spanish from Latin *ambactus* 'a servant, vassal,' from Celtic *amb(i)actos* 'a messenger, servant.'"

The word breaks down to PIE roots: *ambhi-* ("around") + *ag-* ("to drive, draw out or forth, move").

## Embassy

The term **embassy** emerged in the 1570s, from French *embassee* "mission, charge, office of ambassador," tracing back through Old French *ambassee* and Italian *ambasciata* to Old Provençal *ambaisada*. 

Its origin is described as "from Gaulish *\*ambactos* 'dependant, vassal,' literally 'one going around' (from PIE *\*amb(i)-ag-to*, from roots *ambhi-* 'around' + *ag-* 'to drive, draw out or forth, move')."

Both terms ultimately share the same Celtic root concept of a person sent on a mission or moving around on behalf of authority.
```


### [2026-09-04T19:50:01.181Z] TOOL RESULT

```
# Etymology of افراشتن (afrāštan)

## Middle Persian Origin
The word derives from Middle Persian (script not provided in source), transcribed as /abrāštan/, meaning "to lift, raise."

## Morphological Breakdown
The term is a compound verb with two elements:

1. **Prefix *af-**: Derived from Proto-Iranian *Hápa* ("off, away, from") or Proto-Indo-European *upó* ("under, below, towards")

2. **Root *rāš-**: From Proto-Indo-Iranian *Hraštás* ("straightened, right")

## Cited Source
The dictionary references Sulayman Hayyim's *New Persian–English Dictionary* (1934, Teheran: Librairie-imprimerie Béroukhim) for this entry.

**Note**: The source material does not support the "abi- + raz-" analysis you suggested; rather, it indicates *af-* + *rāš-* as the compositional structure.
```


## [2026-09-04T19:50:18.704Z] TOOL CALL #96: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3",
 "prompt": "Give the etymology of Persian افسوس afsūs 'regret, alas; mockery': Middle Persian form and any reconstruction (apa-sraud-? aiwi-saok-?), and cited sources."
}
```


## [2026-09-04T19:50:20.352Z] TOOL CALL #97: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/indoeurop.html#IR005600",
 "prompt": "Find and quote the American Heritage Dictionary Indo-European roots appendix entries for 'ambhi' and 'ambhō' — their glosses and derivatives."
}
```


### [2026-09-04T19:50:25.119Z] TOOL RESULT

```
# Etymology of Persian افسوس (afsūs)

Based on the Wiktionary entry, the Persian word افسوس is "Inherited from Middle Persian" with the form shown as "[script needed] (ʾp̄sws /⁠afsōs⁠/)."

Unfortunately, the source provides **no reconstructed Proto-Indo-European or earlier forms**, nor does it cite scholarly sources for the etymological derivation. The entry acknowledges a gap by noting "[script needed]," indicating the Middle Persian script representation is missing from the documentation.

The word has extensive descendants across multiple languages (Armenian, Bengali, Georgian, Hindi/Urdu, Kashmiri, Ottoman Turkish, Punjabi, Sindhi, Uyghur, and Vaghri), confirming its historical significance, but the original source does not supply the linguistic reconstruction you've requested or reference specific academic citations explaining its deeper etymological origins.
```


### [2026-09-04T19:50:28.562Z] TOOL RESULT

```
# Indo-European Root Entries: ambhi and ambhō

Based on the provided content, I can only locate an entry for **ambhi**. There is no separate entry for "ambhō" in this appendix section.

## ambhi Entry

**Gloss:** "Around. Probably derived from _\*ant-bhi_, 'from both sides'"

**Key Derivatives:** The entry lists numerous English words descending from this root, including:
- "by, be-, beleaguer, bivouac" (from Germanic forms)
- "Ember Day, ombudsman, umlaut" (from Germanic _\*umbi_)
- "ambi-, alley, ambulance, ambulate, andante, funambulist, perambulate, preamble" (from Latin)
- "amphi-" (from Greek _amphi_)

The appendix notes that this root appears in Celtic compounds and shows how the root evolved across different language families with related meanings involving position and surrounding space.
```


## [2026-09-04T19:50:30.404Z] AGENT

Now let me archive the web sources.


## [2026-09-04T19:50:40.366Z] TOOL CALL #98: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82m%CC%A5b%CA%B0i\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D9%88%D8%AE%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%A9%D9%86%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%D8%AA%D8%A7%D9%81%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D8%A7%D8%B4%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3\" \\\n \"https://www.etymonline.com/word/amphi-\" \\\n \"https://www.etymonline.com/word/ambassador\" \\\n \"https://ahdictionary.com/word/indoeurop.html\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 51, root Ambhi/Ambhô: modern check of root and Persian/English nodes\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-04T19:50:45.836Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/371761268e653146.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d13873ad51a4faa2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30cfae5fd997b9f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/12208715571d13ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/578ce31638bcf4c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/07fc0f0526de5a81.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd578855bc4cc3ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/606fdfba158a1d2a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/62baaaaf5a498666.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c11f767c19a71d7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc93e6cd09178bce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b5f815bd0c1c7d9e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae529aabf1bedd3c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a8b21303cb2b0af7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bbf1206f1395eb5f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/24cd7948c66bfb96.txt
```


## [2026-09-04T19:50:48.102Z] TOOL CALL #99: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-04T19:50:48.149Z] TOOL RESULT

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


## [2026-09-04T19:50:55.489Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN both ==\"; grep -n \"13.42\\|‘both’\\|both’. IE\" SYN.txt | head -6; grep -n \"ambho\\|ámpho\\|ambo ‘both\\|ubhau\" SYN.txt | head -6; echo \"== LEW ambi ==\"; grep -n \"^ambi\\|ambi-, amb-\\|ambö\\|ambo,\" LEW_1910.txt | head -6; echo \"== LAT ambi ==\"; grep -n \"^amb\\|ambi-\" LAT.txt | head -8"
}
```


### [2026-09-04T19:50:55.633Z] TOOL RESULT

```
== SYN both ==
23371:13.42 Turrp (Ordinal)
23956:13.41 13.42 THREE THIRD (Ordinal) Tpets tptros
24064:13.42, The ordinals for ‘third’ are derived from the cardinal, most of them
24079:clinable) form. Among such forms, Fr. tiers, Sp. tercio are now specialized to the fractional sense since their replacement as ordinals by troisiéme, tercero (13.42); and Skt. tfttya- neut. is distinguished by the accent from the ordinal trttya-.
31381:5, Lith. abejojimas, abejoné, derivs. of yb, abejott, beside sb. abejas (only in lo- cution be abejo ‘without doubt’) : abu, abeji_ ‘both’, ChSl. oba, Skt. ubhau, Goth. baz, ete. id.
31381:5, Lith. abejojimas, abejoné, derivs. of yb, abejott, beside sb. abejas (only in lo- cution be abejo ‘without doubt’) : abu, abeji_ ‘both’, ChSl. oba, Skt. ubhau, Goth. baz, ete. id.
== LEW ambi ==
10901:ambi, wmpr I 57, IT 210
== LAT ambi ==
1212:ambigue. Le grec a cocpoe, arec a initial; mais le vieux slave ostru a
2035:ambulare?'. Ager est premier terme de compose dans agricola, etc.,
2121:ambiegnus: vieil adjectif du ritnel ( ambegnus, ambignus) cf. Varr.,
2125:Cf. ambo, ambi-.
2323:ambigo: pousser de part d'autre; et "mettre sur les plateaux de la
2327:ambiaxium, sons ambi.
3156:ambactus, -I m.: - apud Snnium (A.605) lingua gallica seruus appel¬
3164:ambages; v. ago.
```


## [2026-09-04T19:50:58.692Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3156,3175p' LAT.txt; echo \"=== ambi- ===\"; grep -n \"^amb-, ambi-\\|amb(i)-\\|^ambo\" LAT.txt | head; sed -n '3180,3215p' LAT.txt"
}
```


### [2026-09-04T19:50:58.769Z] TOOL RESULT

```
ambactus, -I m.: - apud Snnium (A.605) lingua gallica seruus appel¬
latur, ... seruus ambactus, i.e. circumactus dicitur P.F.4,20; dans
Cesar, BG.6,i5,a, il est Egalement appliqu^ aux Gaulois. Mot etranger
- non pas mot d'emprunt.
Sont a rapprocher ambascia qu’on lit dans la lex Burg. et la lex
Sal., cf.M.L.4o8a ambactia et abantonia, synonyme de ancilla, qu'on
lit 6galement lex Sal. cap. VI 5.
Substitut gaulois de i.-e. *ambhi- 1 ^ > olos; v. sous anculus.
ambages; v. ago.
ambi-, amb-, am-, an-: particule attestee seulement comme premier
eliment de compos 4 . Une trace de son emploi comme preposition est encore
dans Charisius, GLK I 231,11, qui cite am fines, am segetes (cf.P.F.
19,16 amsegetes dicuntur quorum ager uiam tangit). Pour le sens, cf.
P.F.4,22, am praepositio loquelaris significat circum, unde supra
seruus ambactus, i.e. circumactus dicitur. Le sens est plutot "de
chaque cote de" que "autour" .(circum et gr. 7 iepl) proprement dit.
Ambi- ne figure plus que dans des mots archaiques conserves par les
grammairiens et les glossateurs, ambiaxium? dans P.F.24*11, ambiaxioque
circumeuntes cateruat in, de ambi- + axium, apparente k agere?; anbie-47
gnus, cf. agnus', et sans doute ap„ Varr., L.L.7,43, ancilia ab ambecisu
=== ambi- ===
3225:ambo, -ae, -0: collectif duel, employe a 1’origine pour designer
3236:ambo (d'aprbs Th£ocr.8,3); Ov. F.6,387 utraque nupserunt, ambae peperisse
70863:amboltu ombr., 47,49.
de oquft>TepoSeE;t,oC; amb ifdrius, -rian ne sont attestes qu'a partir d'Apn-
lee; ambigenus est dans Eugene de Tolede, ambimanus dans les gloses.
Ces formes se rattachent a ambo, et non a ambi-.
Amb- est la forme normale devant voyelle: ambactus, ambages, ambar-
udles, ambegni,ambedo, ambiguus, ambio, ambulo, anburbiales, ambustus;
am-, an- s 1 emploie devant consonne: a ncile(?), ancisus, anculus, ancil¬
la, amfdriam, anquiro; amicio, amplector, amputo. Pour anceps, v. ambo.
Le preverbe lat.amf 1 - de amb-uro, amb-ustus , etc., est evidemment
apparente k gr. ctp,cp t ,: A cote de ambhi, ainsi atteste, le celtique et
le germanique ont *mbhi: v.irl.imb-, imm-, v.h.a .umbi "autour". Le
skr.abhi est ambigu pour la forme et pour le sens (cf. lat. ob ); le
gotique a bi "prfes de"; le sens de "autour" n'est net et constant que
dans les formes comprenant une nasale visible comme gr. oqicpt et v.h.a.
umbi. - Le b de ombr. anb-oltu "ambulato" est issu de f, comme on le
voit par osq. amfret "ambiunt", en face de ombr.amprehtu "ambito", am-
bretuto (plur.); v. an fractus. Une forme am- est dans osq. amnud "cir¬
cuitu".
ambicus: poisaon inconnu (Polem.Silu.). Peut-etre gaulois.
ambio, -is, -iui, -itum, -ire: aller autour, faire le tour de;
specialise dans la langue politique en pariant de candidats qui bri-
guent une magistrature, et font leur cour aux electeurs, cf. Varr., L.L.
5,38, qui populum candidatus circum it, ambit. Cette restriction du
sens a contribue a detacher le verbe de eo, dont il est un compose,
pour le faire passer a la 4 e conjugaison. Cf. Prisc. GLK II 547 , 3 , ambio
ab "eo" compositum solum mutauit paenultimam e iri i; itaque in -io
quidem desinentium regulam seruauit in participio et supino, quippe
producta paenultima: ambitus; in nomine autem differentiae causa in -eo
terminantium regulam seruans corripuit paenultimam: ambitus. Ov., Tac.,
Plin. emploient ambibat, Pline a encore ambibunt; mais dbs Velleius se
repand 1 1 imparf. ambiebam , et Seneque, dans CEd. 505, a un fntur ambiet.
y __ y y y
Mais ambitus, ambitio ont garde l*t de itus, itum.
Ambitus et ambitio se sont differencies dans 1 'usage: ambitus est
surtout employe au sens propre "chemin qui fait le tour de; pourtour"
(cf. Varr., L.L.5,33) ; sens reste dans la langue des arpenteurs et geo¬
metres, e.g. CIL., V 506,8 suppi, locus cum ambitu datus', cf. Pomp.Dig.
```


## [2026-09-04T19:52:14.480Z] AGENT

Now I'll write the verification file.


## [2026-09-04T19:58:43.733Z] TOOL CALL #102: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-51.json <<'JSONEOF'\n{\n  \"pdf_page\": 51,\n  \"book_page\": 21,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Ambhi, Mbhi, Obhi, Ebhi\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₂m̥bʰi 'around, on both sides' (Pokorny 34 ambhi, m̥bhi; also *obhi, *ebhi) and the dual *h₂m̥bʰoh₁ 'both' (Pok. ambhō(u))\",\n      \"note\": \"The root box is exactly Pokorny p.34 and Walde-Pokorny I 54-55: 'ambhi, m̥bhi \\\"beiderseits wovon, um-herum\\\" ... ambhō(u) Du. \\\"beide\\\", und ähnliche auf -bhi, -bho- ausgehende Formen', with the variants *obhi / *ebhi discussed in the same article ('setzt … sicher das idg. *obhi oder *ebhi fort'). Language label 'Indo-European' and both glosses ('around'; 'both') are right. Watkins/AHD has the same pair of entries, 'ambhi. Also mbhi. Around. Probably derived from ant-' and 'ambhō. Both', and Wiktionary reconstructs *h₂m̥bʰí (Jasanoff: from *h₂n̥t-bʰi, instr. pl. of *h₂ént-s 'forehead, front'; Dunkel: *án + *-bʰi) — i.e. modern work adds a pre-history for the root but does not challenge the shape or the meaning.\\n\\nCROSS-CUTTING CAVEAT ON THE PERSIAN BRANCH. Nourai (following Horn 1893) files eight New Persian af-/f- verbs and nouns under Av. aiwi- (*abi-). Since Horn wrote, Persian af- has been shown to continue THREE distinct Old Iranian prefixes that all fall together in Middle Persian: *abi- (> MP ab-/awi-), *apa- 'away' and *upa-. Hübschmann already warned that Horn's nos. 102-106 are 'nicht einwandfrei, besonders der Bedeutung wegen' (HUB p.16-17), and Nyberg's Pahlavi glossary indexes afgandan, afsōs, afsūn, afsurdan under apa-, and afsar under *upa-sarah-. Nourai reproduces Horn's 1893 picture without those corrections, which is why five of the seven Iranian nodes below come out 'disputed'.\\n\\nMIS-CITATION. Node #7 cites BQT:2143 for afšāndan/afšūn. Borhān-e Qāṭeʿ p.2143 (checked with tools/ref_page.py, vol.4 pdf p.226) is the نشان / نشاندن / نشاسته block, nothing to do with افشان; the real entries افشاندن / افشون stand in vol.1 at about p.150 (BQT_v1_pages.txt leaf 365).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82m%CC%A5b%CA%B0i\",\n        \"https://ahdictionary.com/word/indoeurop.html\",\n        \"https://www.etymonline.com/word/amphi-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:34\", \"status\": \"supports\", \"note\": \"POK_01.txt ff-leaf 42 (= printed p.34, the folio '35' falls in the middle of the leaf): 'ambhi, mbhi \\\"um-herum, zu beiden Seiten\\\", auch ambhō(u) Du. \\\"beide\\\" und ähnliche auf -bhī, -bho- ausgehende Formen'; the same article gives '*mbhi: ai. abhi-taḥ, av. aiwito … apers. abiy, av. aibī, aiwi … aus *mbhi stammen oder idg. *obhi oder *ebhi fortsetzen', 'gr. ἀμφί', 'lat. amb-', 'ahd. as. umbi', and under ambhō(u) 'gr. ἄμφω … lat. ambō … ai. ubhāu; av. uwa- ds. … ags. bā, engl. both'. Every element of Nourai's root box is on that page.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwi, aibi, abi, aiwiš, ubě, uwa\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. aiwi (Younger Avestan) / aibī (Gathic) 'to, against, over, in respect of' is the regular Iranian reflex of PIE *h₂m̥bʰi (or of the ablaut variant *obhi, which Pokorny and Kent think has fallen together with it in Indo-Iranian): PIE *m̥bʰi > Proto-Indo-Iranian *Habʰí > Skt. abhí, Av. aibī/aiwi. Before a following sibilant or in sandhi the preverb appears as aiwiš- (Av. aiwiš.hutəm 'pressed out', aiwiš.xᵛarəθa-), which is Nourai's 'aiwiš'. 'abi', however, is Old Persian abiy, not Avestan: Bartholomae's headword reads 'g. aibi, j. aiwi (aivi), p. abiy', so this Avestan box has one Old Persian form smuggled into it (Nourai repeats it correctly as its own node #12). ubě and uwa do not belong to the preposition at all but to the dual pronoun *h₂m̥bʰoh₁ 'both': Av. uwa- (masc.) / ubē (fem.) = Skt. ubhāu/ubhē, and Pokorny/Sommer explain the Indo-Iranian u- as a labial-conditioned darkening of *ambhāu > *abhāu. Grouping them under one heading is Pokorny's own arrangement, so this is a defensible chart, but the gloss 'over, above, both' is really two glosses for two different stems.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%82m%CC%A5b%CA%B0i\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:34\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 42: '*mbhi: ai. abhi-taḥ, av. aiwito \\\"zu beiden Seiten, rings\\\" (über av. aibis, apers. abis strittiger Bed. …); ai. abhi kann in der Bed. \\\"um\\\", apers. abiy, av. aibī, aiwi in der Bed. \\\"über, in betreff von\\\" aus *mbhi stammen'; and further down 'ai. ubhāu \\\"beide\\\", av. uwa- ds.'. Both halves of Nourai's node are on p.34; Pokorny too lists apers. abiy in the same breath, which is where Nourai's 'abi' comes from.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. I pp. 54-55 s.v. ambhi, mbhi\", \"stance\": \"supports\", \"note\": \"'*mbhi: … ai. abhi-taḥ, av. aiwito \\\"zu beiden Seiten, rings\\\" … ai. abhi … ap. abiy, av. aibī, aiwi in der Bed. \\\"über, in betreff von\\\"'; and 'ai. ubhāu \\\"beide\\\", av. uwa- ds.' — the printed source Pokorny 1959 abridged.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. aibi (BRT.txt ff-block containing 'g. (j. p.) aibi, j. aiwi (aivi), p. abiy')\", \"stance\": \"partial\", \"note\": \"Bartholomae's headword is 'g. aibi, j. aiwi (aivi), p. abiy' — i.e. aibi is Gathic, aiwi Younger Avestan and abiy OLD PERSIAN, so 'abi' does not belong in an Avestan box. He also has ~377 aiwi- compounds, incl. aiwiš- forms (aiwis.hut-, aiwis.xᵛarəθa-).\"},\n            {\"src\": \"KLN\", \"where\": \"1966 vol. I p.62 s.v. ambi- and p.512 s.v. both\", \"stance\": \"supports\", \"note\": \"s.v. both: 'cogn. with OI. u-bhāu (masc.), u-bhē (fem.), Avestic u-wa (masc.), u-bē (fem.), \\\"both\\\"' — Klein gives exactly Nourai's pair uwa / ubē with exactly his gloss.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.2 s.vv. ambhi, ambhō\", \"stance\": \"supports\", \"note\": \"'ambhi. Also mbhi. Around' and 'ambhō. Both' are kept as two entries with the same Indo-Iranian material.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwi-ruč; aiwi-reg; aiwi-sâra; aiwi-sara\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four preverb compounds of aiwi-, of which only the first is actually attested. (a) aiwi-ruč = Av. aiwi.raocaya-, causative of raok-/raoč- 'to shine' (PIE *lewk-, Nourai's 'Leuk'), attested Vidēvdād 8.2 'aiiā dim aiwi.raocaiiāt āθrō' and V.19.33 'stārąm aiwi.raocaiiā̊nte', which Bartholomae renders 'mit aiwi: aufflammen lassen, entzünden an —'. (b) aiwi-reg is Horn's and Hübschmann's reconstruction Av. aiwi + razaiieiti 'ordnet, richtet' (root raz-, PIE *h₃reǵ-, Nourai's 'Reg'), not an attested compound; Hübschmann §93 states it explicitly ('zd. aiwi + razayeiti'). (c)/(d) aiwi-sāra- 'around the head' and aiwi-sara- 'on the head' are Horn's starred reconstructions (Horn nos. 97, 99 both print 'aw. *aiwisāra-' / 'aw. *aiwisara-' with an asterisk) built on sarah- 'head'; neither is in the Avesta, and the second is now generally replaced by *upa-sarah- (see node #3). Chart shows them as plain Avestan words with no asterisk, which over-states their status.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the forms are traceable to Horn nos. 93-99 and Hübschmann §93, checked under node #3.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. raok- ('mit aiwi'), and s.v. aiwi.raocayeiti\", \"stance\": \"partial\", \"note\": \"'mit aiwi: aufflammen lassen, entzünden an — (Gen.): aiiā dim (nāml. zaną̇m) aiwi.raocaiiāt āθrō V.8.2'; also 'yaθa hī stārąm baγō.dātanąm aiwi.raocaiiā̊nte V.19.33'. Confirms aiwi-ruč only; no *aiwi.sāra-, *aiwi.sara- or *aiwi.raz- headword exists in AiW.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.16 no. 93\", \"stance\": \"supports\", \"note\": \"'Np. afrāxtan ist nach Horn's richtiger Etymologie (Wrzl. reg, in ὀρέγω u.s.w.) — zd. aiwi + razayeiti (vgl. zd. rāzayeiti \\\"ordnet\\\", osset. arazin \\\"richten\\\")' — supports aiwi-reg, but as a reconstruction.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss pp. 22-23 nos. 93, 94, 97, 99\", \"stance\": \"partial\", \"note\": \"no.97 'efsār … aw. *aiwisāra-' and no.99 'efser \\\"Krone\\\" … aw. *aiwisara-' are printed WITH an asterisk, i.e. unattested.\"},\n            {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar (searched for aiwi-sāra, aiwi-raz)\", \"stance\": \"silent\", \"note\": \"no such compound cited.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"afrŭxtan; afrâštan; afsâr; afsar\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three of the four are sound, the fourth is now rejected. (a) afrūxtan افروختن 'to kindle, light up': Av. aiwi.raocaya- > MP abrōxtan/abrōz- (Book Pahlavi ʾplwhtn', ʾplwc-; Manichaean ʾbrwxt, ʾbrwc-) > NP afrōxtan/afrōz-; the -č- of raoč- gives MP/NP -z- in the present stem and -xt- in the past stem exactly as in sōxtan : sōz-. Confirmed. (b) afrāštan افراشتن 'to raise' (pres. afrāz-, whence the chart's extra افراز): Av. aiwi + raz- 'to make straight' (PIE *h₃reǵ-, cf. Lat. regō, Gk. ὀρέγω, Skt. irajyáti) > MP abrāstan/abrāz- (ʾplstn', ʾplc-; Man. ʾbrʾst), noun abrāz 'acclivity' > NP afrāz; Hübschmann adds that afrāstan is the original infinitive and afrāštan/afrāxtan the analogical remake after afrōz- : afrōxtan. Confirmed. (c) afsār افسار 'bridle, halter': MP *afsār (attested in the Bundahišn), borrowed early into Aramaic — Classical Syriac ʾap̄sārā, Jewish Babylonian Aramaic ʾap̄sārā/ʾap̄sīrā — which shows the word existed in Sasanian Persian; Horn's derivation from *aiwi-sāra- 'that which is round the head' is the classic one and nothing better has replaced it, but it is a starred form. Plausible. (d) afsar افسر 'crown' is DISPUTED: Hübschmann §99 backed *abisarah- (comparing Skt. abhiśiras-), but Henning (Selected Papers, 1977) ruled that afsar 'darf nicht auf *abisarah- (> *ōsar) zurückgeführt werden, vielleicht aber auf *upasarah-', and Nyberg's Pahlavi glossary follows him: 'api-sar [ʾpysl] crown … Probably < OIr *upa-sarah- \\\"that which is on the head\\\" > *apa-sara- and then remodelled to *api-sara- with variable accent: *ápi-sara- > *apsar > afsar'. So the sar 'head' element is right but the prefix is *upa-, and abi- is only a secondary re-formation — i.e. not Nourai's Ambhi at all, or only at one remove. (Nourai's second gloss for afsar, 'officer', is a modern 20th-c. army usage back-formed from afsar 'crown/insignia'; it is not an ancient meaning.)\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D9%88%D8%AE%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B1%D8%A7%D8%B4%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%A7%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:22\", \"status\": \"supports\", \"note\": \"HRN.txt ff-leaf 43 (= printed p.22), no. 93: 'efrāxten \\\"erheben\\\", efrāšten, Praes. efrāz-em … phlv. afrāstan … Zu √reg- + abhi \\\"richten, aufrichten\\\"; ai. irajyáti; gr. ὀρέγω; lat. rego; got. uf-rakjan'. Exactly Nourai's afrāštan arrow.\"},\n            {\"ref\": \"HRN:23\", \"status\": \"supports\", \"note\": \"HRN.txt ff-leaf 44 (= printed p.23): no. 94 'efrōxten \\\"anzünden, erleuchten\\\" … aw. aiwi + √ruc- \\\"anzünden\\\"; phlv. afrōxtan, afrōčīnītan; skr. abhi + √ruc-'; no. 97 'efsār \\\"Zügel, Zaum\\\" … aw. *aiwisāra-; phlv. afsār (Bund.), syr. talmüd. LW.'; no. 99 'efser \\\"Krone\\\". aw. *aiwisara-; phlv. afsar \\\"Krone\\\"'. All three of Nourai's remaining words are on this page with his arrows.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.vv. abrōxtan, abrāstan, abesar\", \"stance\": \"partial\", \"note\": \"'abrōxtan, abrōz- [ʾplwhtn', ʾplwc- | M ʾbrwxt, (ʾ)brwc-, N afrōxtan, afrōz-] light, kindle, illuminate'; 'abrāstan, abrāz- [ʾplstn', ʾplc- | M ʾbrʾst, N (afrāštan), afrāz-] lift, raise'; 'abraz [ʾplc | N afrāz] acclivity'; but 'abesar [ʾpysl | M ʾbysr, N afsar] crown' — the MP form of 'crown' is abesar with abē-, and MacKenzie's MP words for 'bridle' are ēwān and padisār, no afsār.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. api-sar\", \"stance\": \"contradicts\", \"note\": \"'api-sar [ʾpysl] crown … MPrs ʾbysr; NP afsar. Probably < OIr *upa-sarah- \\\"that which is on the head\\\" (v. sar) > *apa-sara- and then remodelled to *api-sara- with variable accent: *api-sara- > apisar, *ápi-sara- > *apsar > afsar.' Nyberg puts the origin in *upa-, not *abi-.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.16 no.93, p.17 no.99\", \"stance\": \"partial\", \"note\": \"no.93 supports afrāštan < aiwi + razayeiti; no.99 'Np. afsar \\\"Krone\\\" — ap. *abisarah- \\\"um den Kopf\\\" liegt im Sanskrit vor als abhiśiras-' — Hübschmann DID back *abisarah- for afsar, which is the view Henning later overturned.\"},\n            {\"src\": \"HENNING\", \"where\": \"Selected Papers (quoted via Wiktionary s.v. افسر)\", \"stance\": \"contradicts\", \"note\": \"afsar 'darf nicht auf *abisarah- (> *ōsār) zurückgeführt werden, vielleicht aber auf *upasarah-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV (searched *raok, *Hraz)\", \"stance\": \"partial\", \"note\": \"Cheung lists the roots but the Persian af- verbs are entered under their roots without committing the prefix to *abi-; his index has no afrōxtan/afrāštan entry disputing Horn.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwi-saoka; aiwi-kand; aiwi-zâvayeiti\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) aiwi-saoka: this is Darmesteter's *aiwi-saoča- (Études iraniennes II 131), a compound of aiwi- with saoč-/saok- 'to burn' (PIE *(s)kewk-, Nourai's 'Keuk 1'), invented to explain afsōs. It is unattested and Horn demolished it on the spot: 'Darmesteter's Erklärung, Et. ir. II, 131 aus aw. *aiwisaoča- ist unhaltbar, da aw. č im Np. nicht zu s werden kann.' Nourai even prints it with -k- rather than Darmesteter's -č-. Disputed. (b) aiwi-kand: Horn no.103 already conceded 'Kaum etwas anderes als aw. aiwi + √kan-, wennschon die Bedeutung nicht passt', and modern Iranists have moved the prefix: Nyberg files MP apa-kandan '< OIr *apa-kan- and *upa-kan-', Cheung puts NP afgandan under '*kan¹ to throw, place, put' with '(+ *apa-)'. Disputed. (c) aiwi-zāvayeiti 'adds up' is the one solid member: it is really the Old Persian causative abiy-ajāvayam / abi-jāvayam (XPg 9, XPh 40) 'I added', from *abi- + gav-/zav- 'to procure, get' (PIE *gʰeu-/*gew-, Nourai's 'Geu 2'); Hübschmann §96 reconstructed *aiwi-zavayeiti in Avestan dress because Av. sav-/zav- and the SW-Iranian z- had to be reconciled. Confirmed as an etymon, but it is Old Persian rather than Avestan, and the box's language label is therefore loose.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%A9%D9%86%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HUB:16\", \"status\": \"supports\", \"note\": \"HUB.txt ff-leaf 26 (= printed p.16), no. 96: 'Aus aiwi + savayeiti wäre im Neup. *afsāyad geworden: das vorliegende afzāyad \\\"vermehrt\\\" muss auf *aiwizavayeiti zurückgehen' — this is precisely Nourai's third form, and Hübschmann's page 16 is the right citation for it. HUB p.16 says nothing about aiwi-saoka or aiwi-kand; on the very next page (p.17) Hübschmann adds 'Nr. 102-106 [= Horn's afšāndan, afgandan …]: Nicht einwandfrei, besonders der Bedeutung wegen.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss p.23 no.101 and p.24 no.103\", \"stance\": \"contradicts\", \"note\": \"p.23: 'Darmesteter's Erklärung, Et. ir. II, 131 aus aw. *aiwisaoča- ist unhaltbar, da aw. č im Np. nicht zu s werden kann.' p.24: 'Kaum etwas anderes als aw. aiwi + √kan-, wennschon die Bedeutung nicht passt.' Horn rejects (a) outright and only tolerates (b).\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.vv. apa-kandan, apa-zūtan, apa-zōn\", \"stance\": \"partial\", \"note\": \"'apa-kandan … < OIr *apa-kan- and *upa-kan-, from kandan … NP afgandan, augandan' (contradicts aiwi-kand); but 'apa-zūtan … < *abi-jav-, in SW with api- substituted for abi- < abi- + Av. ¹gav- \\\"to procure\\\"; … OP caus. abi-jāvaya- \\\"to add\\\"' and 'apa-zōn … < *abi-zavana-, in which api- was substituted for abi-' (supports aiwi-zāvayeiti).\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §521 and Lexicon s.v. abiy\", \"stance\": \"supports\", \"note\": \"'abiyajavayam XPg 9, and abijāvayam XPh 40' — the actual attested form behind Hübschmann's starred Avestan *aiwizavayeiti; Lexicon: 'abiy prep. and prefix \\\"to, against, in addition to\\\"'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.229 ff. s.v. *kan¹\", \"stance\": \"contradicts\", \"note\": \"'*kan¹ \\\"to throw, place, put; to destroy\\\" … *NWIR: NP kandan/kan- … || (+ *apa-) NP afgandan \\\"to throw, cast away\\\"' — prefix *apa-, not *abi-.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW (searched aiwi.saok-, aiwi.kan-)\", \"stance\": \"silent\", \"note\": \"no such compounds are lemmatised; Bartholomae does have aiwi.zūzuyana- s.v. zav-, which is the closest attested aiwi + zav- formation.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"afsŭs; afkandan; afzŭdan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) afsūs افسوس (MP afsōs, Pāzand awasōs), older meaning 'mockery, scorn, jest' (Horn: 'Spott, Scherz'; MacKenzie: 'scorn, mockery'), only later 'alas, regret' — Nourai's gloss 'regret' is the modern sense only. Its etymology is genuinely open: Darmesteter's *aiwi-saoča- 'burning at' (DRM:131) is what Nourai draws, but Horn showed Av. č cannot yield NP s; Hübschmann §101 wrote 'Np. afsōs … wird auch von Fr. Müller nicht befriedigend erklärt'; Nyberg proposes apa-sōs '< OIr *apa-sraud- from apa + Av. srav- \\\"to speak/hear\\\"' (i.e. 'speaking against'). Disputed — modern scholarship does not accept the aiwi- + 'burn' route. (b) afkandan/afgandan افکندن 'to throw (away)': MP abgandan/abgan- (Book Pahlavi with the Aramaic ideogram LMYTWN-tn', Man. ʾbgnd, ʾbgn-) + NP -kandan from the root *kan 'to throw, dig'. The root is undisputed; the PREFIX is: Nyberg '< OIr *apa-kan- and *upa-kan-', Cheung '(+ *apa-)', Wiktionary '*Hápa \\\"off, away\\\" or *upó' — none of them *abi-, and the sense 'throw AWAY' fits apa- 'away' rather than abi- 'towards'. Disputed. (c) afzūdan افزودن 'to add, increase' (pres. afzāy-, noun afzūn فزون, the chart's extra): MP abzūdan/abzāy- (ʾpzwtn', ʾpzʾd-; Man. ʾbzʾy-), abzōn 'increase' > NP afzūn, from *abi-gav-/*abi-zav- 'to add to' — the very formation attested in Old Persian abiy-ajāvayam. Confirmed, and it is the one member of this node that really does descend from Ambhi.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B3%D9%88%D8%B3\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%A9%D9%86%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"DRM:131\", \"status\": \"supports\", \"note\": \"Not directly readable in DRM.txt (Darmesteter, Études iraniennes II p.131), but Horn quotes it verbatim on HRN p.23: 'Darmesteter's Erklärung, Et. ir. II, 131 aus aw. *aiwisaoca-' — so Nourai's page reference is exact, and Darmesteter really is the source of the afsūs ← aiwi-saok- arrow.\"},\n            {\"ref\": \"HRN:23\", \"status\": \"partial\", \"note\": \"HRN.txt leaf 44 (= p.23) has afzūdan (no.96, 'aw. *aiwi + √sav-, sāvayāt \\\"er wird nützen\\\"; phlv. afzūtan, afzūn') — supports the afzūdan arrow — but the same page's no.101 REJECTS the afsūs arrow Nourai draws ('ist unhaltbar'). afkandan is not on p.23 at all; it is Horn no.103 on p.24.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. afsōs, abgandan, abzūdan, abzōn\", \"stance\": \"supports\", \"note\": \"'afsōs [ʾpsws | N ~] scorn, mockery'; 'abgandan, abgan- [LMYTWN-tn' … | M ʾbgnd, ʾbgn-, N afgandan] throw'; 'abzūdan, abzāy- [ʾpzwtn', ʾpzʾd- | M ʾbzʾy-, N afzūdan, afzāy-] increase, grow'; 'abzōn [ʾpzwn' | M, J ʾbzwn, N afzūn] increase, growth'. Confirms all three Middle Persian antecedents (but not the Old Iranian prefixes).\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.vv. apa-sōs, apa-kandan, apa-zūtan\", \"stance\": \"contradicts\", \"note\": \"'apa-sōs [ʾpsws] derision, mockery, scorn … Paz. awasōs; NP afsōs; < OIr *apa-sraud- from apa + Av. srav-' and 'apa-kandan … < OIr *apa-kan- and *upa-kan-' — two of Nourai's three words are taken away from *abi-; only apa-zūtan is conceded to '*abi-jav-'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.16 no.96, p.17 no.101, nos. 102-106\", \"stance\": \"partial\", \"note\": \"no.96 corrects Horn's aiwi+sav- to *aiwi-zavayeiti (supports afzūdan); no.101 'Np. afsōs … wird auch von Fr. Müller, WZKM. 7, 367 nicht befriedigend erklärt'; nos. 102-106 'Nicht einwandfrei, besonders der Bedeutung wegen' (covers afgandan).\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.231 f. s.v. *kan¹ (index 'afgandan, 231')\", \"stance\": \"contradicts\", \"note\": \"afgandan under '*kan¹ … (+ *apa-)'.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 365 (≈ printed p.150), entries افسوس / افسون\", \"stance\": \"partial\", \"note\": \"Borhān-e Qāṭeʿ has 'افسوس … بمعنی ظلم و ستم … و دریغ و حسرت را نیز گویند … و بمعنی بازی و ظرافت - و سخر و لاغ هم هست' ('injustice; also regret and grief; also play and jest; also mockery'), documenting both senses; Moʿin's footnote gives no Old Iranian prefix.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwi-fšân; aiwi-axš\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) aiwi-fšān: Horn no.102 offered 'aw. aiwi + fšūnayeinti \\\"sie weiden aus\\\", Yt 14,56 (?)' with his own question mark, and Hübschmann struck it out with nos.102-106 as 'nicht einwandfrei, besonders der Bedeutung wegen'. Modern Iranian etymology puts NP afšāndan under a root *šan 'to shake (down)' with the prefix *apa-: Cheung, EDIV s.v. *šan, '*MIDDLE PERSIAN: (+ *apa-) BMP ʾpsʾn- /afsan-/ \\\"to spread, scatter, sow\\\" … *NWIR: … (+ *apa-) NP afsandan/afsan-'. Neither the prefix nor the root shape (fšān vs šan) survives. Disputed. (b) aiwi-axš 'oversee' is genuine and well attested: Bartholomae lemmatises the verb 'āxš-, nur mit aiwi \\\"ἐφορᾶν\\\" [to oversee]. Präs. 30 (Iter.) aiwyāxšaya-. Inf. aiwyāxštriš', from aiwi- + axš-/haxš- 'to watch' (Nourai's 'Okw' = PIE *h₃ekʷ- 'to see'). Confirmed. Node verdict follows the weaker member.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is given on this node; the underlying source is Horn no.102 (checked at node #7) and, for aiwi-axš, Bartholomae s.v. āxš-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. āxš- (BRT.txt: 'j. āxš- V., nur mit aiwi \\\"ἐφορᾶν\\\". Präs. 30 (Iter.) aiwyāxšaya-. Inf. aiwyāxštrīš')\", \"stance\": \"supports\", \"note\": \"The compound aiwi + āxš- 'to oversee' is a real Avestan lexeme with exactly Nourai's gloss; e.g. 'hazaŋrəm narąm aiwyāxša-'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.371 f. s.v. *šan 'to shake (down ?)'\", \"stance\": \"contradicts\", \"note\": \"'(+ *apa-) BMP ʾpsʾn- /afsan-/ \\\"to spread, scatter, sow\\\" … (+ *apa-) NP afsandan/afsan-, Gil. (Rsht.) fišan- \\\"to disperse\\\"'. Root *šan, prefix *apa-; 'An IE etymology for *šan is lacking.'\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.17, note on Horn nos. 102-106\", \"stance\": \"contradicts\", \"note\": \"'102-106. Nicht einwandfrei, besonders der Bedeutung wegen.' — Horn's afšāndan ← aiwi + fšān is explicitly among the etymologies Hübschmann will not accept.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. afšāndan\", \"stance\": \"partial\", \"note\": \"'afšāndan, afšān- [ʾpšʾn-tn' | N ~] spread, scatter, sow' — MP form confirmed, prefix not analysed.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"afšândan; afšûn\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"afšāndan افشاندن 'to scatter, sprinkle' < MP afšāndan/afšān- (ʾpšʾn-tn'), pres. stem afšān-, whence the participial noun افشان 'scattering' used in compounds (آتش‌افشان, گل‌افشان; and the chart's Rumi line 'لب دُرفشانش' turns on that). afšūn افشون (also افشان) is the derived instrument noun: Moʿin, Farhang-e Fārsi, 'افشون [= افشان] (اِ.) افزاری است دارای پنجه‌ای چوبین (سه شاخه یا چهار شاخه) و دسته‌ای بلند که به وسیلهٔ آن غلهٔ کوفته را باد دهند و دانه را از کاه جدا سازند' — a long-handled three- or four-pronged wooden winnowing fork, so Nourai's gloss 'rake' is right. The word chain Persian ← Middle Persian is certain; what is disputed is the parent: the modern analysis is Old Iranian *apa-šan- 'to shake off/away' (Cheung; Wiktionary), not *aiwi-fšān-, and Horn's own citation of Yt 14.56 fšūnayeinti carried a question mark that Hübschmann converted into a rejection. Hence 'disputed' for the edge, not for the words.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B4%D8%A7%D9%86%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:24\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 45 (= printed p.24), no.102: 'efšānden \\\"ausschütten\\\", fšānden. aw. aiwi + fšūnayeinti \\\"sie weiden aus\\\", yt. 14, 56 (Geldner, 3 Yasht, 88) (?); phlv. afšāntan.' Horn does draw Nourai's arrow — with his own '(?)'.\"},\n            {\"ref\": \"BQT:2143\", \"status\": \"not_found\", \"note\": \"Fetched with tools/ref_page.py BQT:2143 (vol.4 pdf page 226): that printed page carries نشاختن / نشانده / نشاندن / نشان / نشاسته — 'نشان … بمعنی علامت باشد', 'نشاندن معروف است و بمعنی نهادن هم هست' — nothing about افشان. The Borhān entries Nourai wants are in vol.1 at ≈p.150 (BQT_v1_pages.txt leaf 365): 'افشون - بر وزن افیون، چیزی باشد مانند پنجهٔ دست و دسته نیز دارد که دهقانان [بکار برند]' with Moʿin's footnote 'مشتق از افشاندن'. So the page number is wrong but the content Nourai claims exists elsewhere in the book.\"},\n            {\"ref\": \"MON:317\", \"status\": \"supports\", \"note\": \"Moʿin's page 317 could not be paginated (only the 2-vol Adena abridgement is on disk, unpaginated), but the entry is verbatim: 'افشان [= فشان] (افا.) در بعضی کلمات مرکب به معنی افشاننده آید: آتش‌افشان'; 'افشاندن [= افشانیدن = فشاندن] (مص م.) ریختن و پاشیدن، پراکنده کردن'; 'افشون [= افشان] (اِ.) افزاری است دارای پنجه‌ای چوبین … و دانه را از کاه جدا سازند؛ انگشته، هسته'. Confirms both words and both glosses; alphabetically افشان does fall in the 300s of Moʿin vol.1.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. afšāndan\", \"stance\": \"supports\", \"note\": \"'afšāndan, afšān- [ʾpšʾn-tn' | N ~] spread, scatter, sow'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.371 f. s.v. *šan\", \"stance\": \"contradicts\", \"note\": \"prefix *apa-, root *šan; Khot. ṣāñ- 'to shake down', Pth. wyšʾn- 'to shake off, down' (< *aua-).\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi (2-vol abridgement) s.vv. افشان، افشاندن، افشون\", \"stance\": \"supports\", \"note\": \"quoted in ref_check above.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 365 s.v. افشون\", \"stance\": \"supports\", \"note\": \"'افشون - بر وزن افیون، چیزی باشد مانند پنجهٔ دست و دسته نیز دارد …' — the rake sense, independently of Moʿin's dictionary.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"aiwiš-kar; aiwiš-tap\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both compounds rest on segmenting the š of Persian šikār / šitāftan out of the preverb aiwiš-, and both segmentations have been abandoned. (a) aiwiš-kar: de Lagarde's and Horn's *aiwiš + kar-; but Horn himself refused Nourai's cross-reference to *kʷer- 'to make' — 'aber dann gewiss nicht zu √kar- \\\"tun, machen\\\", wie de Lagarde will, sondern zu √kar- in np. nigār, nigerīdan' — and Hübschmann analysed the doublet bišgard as bi-šgard < *vi-škart, i.e. the š- belongs to the STEM škar-. Cheung's EDIV settles it with a root '*skar \\\"to pursue, drive, look for (the cattle)\\\"' (MP škarag 'bird of prey', wiškar 'hunting-ground', Pth. ʾškr- 'to hunt', Sogd. škr-, Oss. skʼærun 'to chase animals'). Disputed. (b) aiwiš-tap: Horn no.777 derived šitāftan from 'aw. *aiwis + √tap-, tāpayeiti \\\"in Wärme, Hitze bringen\\\", dann tropisch'; but the Middle Persian form is awistāb-/ōštāb- (Man. ʾwystʾb-, BMP ʾwstʾp-), and Cheung files it under an independent root '*stap \\\"to hasten, (op)press\\\"' (PIE *step-, Pok. 1013; Arm. loanwords štapem, štap) with the prefix *abi- — so the preverb is indeed *abi-, but the š-t- is root-initial *st-, not aiwiš + t-. Disputed as segmented.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D8%AA%D8%A7%D9%81%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; the source of both compounds is Horn nos. 777 and 786, checked at node #9.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.345 f. s.v. *skar and p.363 s.v. *stap\", \"stance\": \"contradicts\", \"note\": \"'*skar \\\"to pursue, drive, look for (the cattle)\\\" … *MIDDLE PERSIAN: BMP škarag \\\"(bird of) prey\\\" || (+ *ui-) wiškar \\\"hunting-ground\\\" … *NWIR: NP šikar \\\"hunt\\\" (LW ?, < Sogd. ?)'; and '*stap \\\"to hasten, (op)press\\\" … (+ *abi-) MMP ʾwystʾb-, BMP ʾwstʾp- /awistāb-/ … *NWIR: NP sitāftan/sitāb- \\\"to hurry\\\" … PIE *step- … Pok.: 1013'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.30 no.224 and p.158\", \"stance\": \"contradicts\", \"note\": \"'Np. bišgard und bišgar \\\"Jagd\\\" ist mit Rücksicht auf šikardan \\\"jagen\\\" in bi-šgard zu zerlegen und auf *viškart … zurückzuführen'; p.158 'bišgard \\\"Jagd\\\" aus phl. *viškart …, vgl. np. šikar \\\"Jagd\\\", šikardan \\\"jagen\\\", phl. v(i)škar' — the stem is škar-, the prefix vi-.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW (searched aiwiš.kar-, aiwiš.tap-)\", \"stance\": \"silent\", \"note\": \"neither compound is lemmatised; Bartholomae's aiwiš- forms are aiwiš.hut-, aiwiš.xᵛarəθa- etc.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss p.174 no.786\", \"stance\": \"partial\", \"note\": \"Horn draws the aiwiš + kar- arrow but insists the second element is the kar- of nigār/nigerīdan ('to look'), not Nourai's *kʷer- 'to make'.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"šekâr; šetâftan\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"(a) šekār شکار 'hunt, game' with its verb šikardan, MP škar (Bundahišn glossary), wiškar 'hunting ground', škarag 'bird of prey', Parthian ʾškr- 'to hunt', Sogdian (ʾ)skr-/škr- 'to lead, pursue', Ossetic skʼærun 'to chase (animals)'. Modern Iranists (Cheung 2007: 345, followed by Wiktionary) derive the whole family from a root *skar 'to pursue, drive, look for (cattle)' with no preverb at all, and even suspect New Persian šikār of being a loan from Sogdian škʾr rather than an inherited SW-Iranian word, since MP has only the *wi- compound wiškar. Nourai's aiwiš-kar segmentation is therefore rejected. (b) šetāftan شتافتن 'to hurry' (pres. šitāb-, noun شتاب, the chart's extra) continues MP awistāftan > ōštāftan (Man. ʾwystʾb-, Book Pahlavi ʾwstʾp- 'to press, hasten'), from *abi-stap-; Armenian borrowed it as štapem 'I press', štap 'haste'. So this word does descend from *abi- = Ambhi — but through the root *stap 'to hasten, press' (PIE *step-, Pok. 1013), not through tap 'to be hot': Nourai's gloss 'in heat, in a hurry' is Horn's 1893 rationalisation of a wrong cut. Both words therefore reach the chart's root box, if at all, by a different road than drawn.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DA%A9%D8%A7%D8%B1\",\n            \"https://en.wiktionary.org/wiki/%D8%B4%D8%AA%D8%A7%D9%81%D8%AA%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1275\", \"status\": \"partial\", \"note\": \"Fetched with tools/ref_page.py BQT:1275 (vol.3): the page is the شکار entry — 'شکار - بکسر اول (در لهجهٔ مرکزی) اسم از «شکردن» (ه.م.)؛ قس: شکره، آشکره؛ پهلوی škār (صید) … افغانی … (صید کردن، لخچیر)؛ کردی … (رک: بشگرد) … صید، لخچیر - هر حیوانی که صید شود'. Moʿin's footnote gives the Pahlavi and the Afghan/Kurdish cognates and derives šikār from the verb شکردن — it does NOT give aiwiš + kar-, so the reference has the word but a different (prefix-less) derivation.\"},\n            {\"ref\": \"HRN:172\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 193 (= printed p.172), continuation of no.777 šitāftan: 'phlv. ōštāftan (vd. 7 (27) Gl., 18 (98), Men.) \\\"eilen\\\", arm. LW. štap, davon Denomin. štapim \\\"eilen\\\". aw. *aiwiš + √tap-, tāpayeiti \\\"in Wärme, Hitze bringen\\\", dann tropisch. Zu aiwiš vergl. oben np. hiš- (No. 221).' Exactly Nourai's arrow and gloss.\"},\n            {\"ref\": \"HRN:174\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 195 (= printed p.174), no.786: 'šikār \\\"Jagd\\\" … phlv. škar \\\"Jagd\\\" (vd. 5 (134) Gl.), škara \\\"Jagdhabicht\\\" (Bund.) … aw. *aiwiš (doch vergl. No. 221) + √kar- (de Lagarde …); aber dann gewiss nicht zu √kar- \\\"tun, machen\\\", wie de Lagarde will, sondern zu √kar- in np. nigār, nigerīden.' Horn supports the aiwiš-kar arrow but not Nourai's onward reference to Kwer.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"EDIV p.345 f. s.v. *skar; p.363 s.v. *stap\", \"stance\": \"contradicts\", \"note\": \"quoted at node #8; 'NP šikar \\\"hunt\\\" (LW ?, < Sogd. ?)' and 'NP sitāftan/sitāb- \\\"to hurry\\\"' under *stap.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p.30 no.224, p.158\", \"stance\": \"contradicts\", \"note\": \"bišgard < *vi-škart, stem škar-.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie (searched škar, wiškar, awistāftan)\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no škar/awistāftan headword in the text on disk; the forms come from Cheung's fuller Book-Pahlavi material.\"},\n            {\"src\": \"BQT\", \"where\": \"BQT p.1275 s.v. شکار\", \"stance\": \"partial\", \"note\": \"as quoted in ref_check.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Avestan\",\n          \"words\": \"abi-dasta, a-dasta, a-dsta\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"These are not Avestan words but Gershevitch's reconstructions in the Avestan Hymn to Mithra, p.220 n. (his index entry reads '*abi-dasta(na)-, 220 n.'). Reasoning: Pahlavi has abdast 'hand-guard' (MacKenzie ʾbdst'), and Gershevitch proposes that Pahl. *ʾwstnk / *ʾwystk should be read as *abistānak / *abistak going back to '*abi-sta-, amplified by -ka- and -na-ka-', and that '*abista(na)ka- … may be a reduction of *abi-d(a)sta-(na)ka-', comparing 'Yidgha avidasta \\\"sleeve\\\" < *uda-dasta- (Morgenstierne)' and 'Oss. fiston, Dig. fæstonæ \\\"handle\\\" < *pati-dastanæ, cf. Khot. dastāna \\\"handle\\\"'. The three shapes Nourai prints are Gershevitch's *abi-dasta-, a shortened *ā-dasta- and the still shorter *ā-d(a)st- (the chart's 'a-dsta' is Nourai's rendering of *ā-d(a)st-, not a scan error — the printed page reads 'a-dsta'). Second element dasta- 'hand' (PIE *ǵʰes-to-, Nourai's 'Ghesto'), first element the preverb abi-, so the formation would mean 'that which is over the hands'. Plausible, but reconstructed, and the box's language label 'Avestan' is wrong for a Middle-Iranian-based reconstruction.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHM:220\", \"status\": \"supports\", \"note\": \"AHM.txt, note on p.220 (index: '*abi-dasta(ua)-, 220 n.'): '*wyst- and ʾwst- could represent an older *abi-sta-, amplified by -ka- and -na-ka- respectively … As to *abista(na)ka-, this may be a reduction of *abi-d(a)sta-(na)ka-, comparable to that which according to H. W. Bailey took place in Oss. fiston, Dig. fæstonæ \\\"handle\\\" < *pati-dastanæ, cf. Khot. dastāna \\\"handle\\\" … Perhaps NPers. astīn \\\"sleeve\\\" similarly goes back to *ā-d(a)st-.' Nourai's page and his three forms are exactly Gershevitch's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. abdast\", \"stance\": \"supports\", \"note\": \"'abdast [ʾbdst'] hand-guard' — an actually attested Middle Persian *abi-dasta- compound, the strongest independent support for the formation.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW (searched aibi.dasta-, aiwi.zasta-)\", \"stance\": \"silent\", \"note\": \"no such Avestan compound exists; Avestan uses zasta- for 'hand', so an Avestan *abi-dasta- is impossible in the first place — dasta- is the Old Persian / Middle Persian word.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dasta-\", \"stance\": \"partial\", \"note\": \"OP dasta- 'hand' is the form that makes *abi-dasta- possible in the SW-Iranian branch (Avestan has zasta-).\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"âstîn\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP āstīn آستین 'sleeve', attested from Ferdowsī (c. 1010). Gershevitch's proposal, which Nourai follows, is āstīn < *ā-d(a)st(a)n- < *abi-dasta-na-, i.e. 'the (garment) over the hand', with loss of the intervocalic d in the reduced form and the -īn suffix; the parallel he cites is Ossetic fiston 'handle' < *pati-dastanæ beside Khotanese dastāna 'handle', and the type is supported by Middle Persian abdast 'hand-guard'. The competing modern view is Herzenberg's (2014, cited by Wiktionary): āstīn is a loan from a South-Eastern Iranian language, cf. Pashto lastúṇay 'sleeve' beside lās 'hand', with the *d- > l- shift of some Eastern Iranian languages and loss of the initial l- in Persian; Wiktionary flatly calls the word 'of unknown etymology due to not having any clear cognates'. Both proposals build the word on 'hand', so the semantics of Nourai's arrow are uncontroversial; the specific route through aiwi-/abi- is one scholar's conjecture, not a consensus.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B3%D8%AA%DB%8C%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHM:220\", \"status\": \"supports\", \"note\": \"AHM.txt p.220 n.: 'Perhaps NPers. astīn \\\"sleeve\\\" similarly goes back to *ā-d(a)st-.' Gershevitch's own hedge ('perhaps') should be noted: Nourai draws it as a firm arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss (searched āstīn / astin)\", \"stance\": \"silent\", \"note\": \"Horn has no entry for āstīn — the word is absent from his Grundriss, which is why Nourai has to reach for Gershevitch 1959.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien (searched āstīn)\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie (searched āstēn, 'sleeve')\", \"stance\": \"silent\", \"note\": \"no Middle Persian word for 'sleeve' of this shape is registered; the nearest form is abdast 'hand-guard'.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. آستین (2-vol abridgement)\", \"stance\": \"partial\", \"note\": \"the abridgement lists the idiom 'آستین افشاندن' but gives no etymology.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Old Persian\",\n          \"words\": \"abiš, abiy, abi\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"OP abiy is the regular SW-Iranian reflex of PIE *m̥bʰi / *obhi: PII *Habʰí > OP abiy, used as a preposition with the accusative and as a verbal prefix (Bīsotūn passim: 'hauv … abiy avam ašiyava' 'he marched against him'; XPg 9 abiy-ajāvayam 'I added to'). 'abi' is not a separate word but the pre-consonantal sandhi variant of the same preverb, which Kent documents as a contraction of -iya- to -i-: 'abi-javayam, also abiy-ajāvayam'. 'abiš' is the -s extended adverbial form (Pokorny: 'über av. aibiš, apers. abiš strittiger Bed. s. Pedersen KZ 40, 127, Bartholomae IF 19, Beiheft S.106'), i.e. it is genuinely attested but its meaning has been argued over for a century. Nourai's gloss 'over, above' is only part of the picture: Kent's Lexicon gives 'to, against, in addition to'.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:34\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 42 (= p.34): '*m̥bhi: ai. abhi-taḥ, av. aiwito … (über av. aibiš, apers. abiš strittiger Bed. s. Pedersen KZ. 40, 127, Bartholomae IF. 19, Beiheft S. 106; die Endung -s in geschichtlichem Zusammenhang mit der von gr. ἀμφίς) … apers. abiy, av. aibī, aiwi in der Bed. \\\"über, in betreff von\\\"'. Both abiy and abiš, and Nourai's gloss 'über', are on Pokorny p.34.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. abiy; §521; Grammar table of prepositions\", \"stance\": \"supports\", \"note\": \"'abiy prep. and prefix \\\"to, against, in addition to\\\": GAv. aibi, LAv. aiwi, Skt. abhi; conflux of pIE *m̥bhi, oHG umbi \\\"round about\\\", and pIE *obhi, oCS obĭ \\\"beside, by\\\"'; §521 'abiyajavayam XPg 9, and abijāvayam XPh 40' shows the abi- ~ abiy- doublet Nourai lists.\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon, Bīsotūn text\", \"stance\": \"supports\", \"note\": \"abiy is abundantly attested in the Bīsotūn inscription: 'pasāva kāra hya Bābiruviya haruva abiy avam Naditabairam ašiyava' (DB 1.80).\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. aibi ('g. aibi, j. aiwi (aivi), p. abiy')\", \"stance\": \"supports\", \"note\": \"Bartholomae lists the Old Persian form under the same headword as the Avestan, exactly as Nourai's chart splits it into nodes #1 and #12.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Greek\",\n          \"words\": \"amphi\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gk. ἀμφί 'around, on both sides, about' is the direct reflex of full-grade *h₂m̥bʰi (Mycenaean a-pi already), with the by-form ἀμφίς 'on both sides' carrying the same adverbial -s as OP abiš; the related dual ἄμφω 'both' (< *h₂m̥bʰoh₁) gives ἀμφότερος. As a prefix ἀμφι- is fully productive in Greek and passes into the international vocabulary through Latin.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/amphi-\",\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:34\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 42: 'gr. ἀμφί \\\"um\\\" (ἀμφί-ς \\\"zu beiden Seiten\\\", mit demselben Adverbial-s wie z. B. ἄψ, μυχοῖ-φις) … [and] gr. ἄμφω \\\"beide\\\" (Ableitung ἀμφότερος)'.\"},\n            {\"ref\": \"AHD:44\", \"status\": \"partial\", \"note\": \"Nourai's 'AHD:44' cannot be a page of the Indo-European appendix (pp.1505-1550 in the 1976 New College edition; pp.1-109 in the 1985 Watkins reprint, where ambhi stands on p.2), so it must be the body of the dictionary, where amphi- falls in the mid-40s alphabetically. That printing is not open online. The appendix itself, checked in AHD_watkins1985.txt p.2, says '4. Greek amphi, around, about: AMPHI-' — the arrow is right whichever page is meant.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 54\", \"stance\": \"supports\", \"note\": \"'Gr. ἀμφί \\\"um\\\" (ἀμφί-ς \\\"zu beiden Seiten\\\" …)'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 vol. I p.62 s.v. ambi-\", \"stance\": \"supports\", \"note\": \"'L. ambi-, amb- … cogn. with Gk. ἀμφί, \\\"round about\\\" … and with Gk. ἄμφω, \\\"both\\\"'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.2 s.v. ambhi\", \"stance\": \"supports\", \"note\": \"'4. Greek amphi, around, about: AMPHI-.'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"English\",\n          \"words\": \"amphitheater; amphibious\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"amphitheater: Gk. ἀμφιθέατρον 'theatre with seats all round' (ἀμφι- + θέατρον) > Lat. amphitheātrum > Old French amphitheatre / directly from Latin into 16th-c. English. amphibious: Gk. ἀμφίβιος 'living a double life' (ἀμφι- + βίος 'life'), Englished 1630s as 'having two modes of existence'; the modern zoological restriction to frogs and their kin dates from about 1835. Both are learned borrowings, so the chart's Greek → English arrow skips no intermediate step worth naming beyond Latin.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/amphi-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; the chain is uncontroversial and covered by Klein s.v. amphitheater.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 vol. I p.62 s.v. amphitheater\", \"stance\": \"supports\", \"note\": \"'amphitheater, amphitheatre, n. — L. amphitheatrum, fr. Gk. ἀμφιθέατρον, lit. meaning \\\"having [seats all round]\\\"'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Amphi-\", \"stance\": \"supports\", \"note\": \"cross-reference 'both sides, around; see Ambi-'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.2 s.v. ambhi\", \"stance\": \"supports\", \"note\": \"AMPHI- listed as the English derivative of Greek amphi.\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for Proto-Germanic. Two Germanic continuations are relevant: the reduced *bi (< *bʰi, the tail of *h₂m̥bʰi) giving Goth. bi, OE bī/be, OHG bī, and *umbi (< *m̥bʰi) giving OE ymbe, OHG umbi, ON umb; separately the dual *bō-/*bai (< *h₂m̥bʰoh₁) giving Goth. bai/ba, ON báðir, OE bā/bēgen. That is exactly what Watkins prints: '1. Reduced form *bhi in Germanic *bi … 2. Germanic *umbi …' and, under ambhō, '1. Reduced form *bhō in Germanic *bō-, *bē in Old Norse bāthir, both: BOTH.'\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:34\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 42: 'bhi: got. bi in der Bed. \\\"um\\\", mit Auslautdehnung in betonter Stellung as. ags. be-, bī-, ahd. bi-, bī-, nhd. bei'; and 'ahd. as. umbi, aisl. umb, ags. ymb, ymbe \\\"um\\\" (im Got. von bi aufgesogen)'; under ambhō(u): 'got. bai m., ba n. … as. bē thie, ags. bā, engl. both; ahd. beide, bēde, anord. bāðir'.\"},\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt p.2 s.v. ambhi: '1. Reduced form *bhi in Germanic *bi, *bi- (intensive prefix) … 2. Germanic *umbi …'; s.v. ambhō: '1. Reduced form *bhō in Germanic *bō-, *bē in Old Norse bāthir, both: BOTH.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 55\", \"stance\": \"supports\", \"note\": \"'*bhi: got. bi in der Bed. \\\"um\\\" … as. ahd. ags. bī, nhd. bei'; '\\\"Beide\\\": … got. bai m., ba n. … ags. bā (þū), engl. both, ahd. beide, bēde, anord. bāðer'.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 vol. I p.512 s.v. both\", \"stance\": \"supports\", \"note\": \"'both … fr. ON. bāþir … formed fr. Teut. *ba-, \\\"both\\\", and the def. article … rel. to OE. bēgen (masc.), bā (fem. and neut.), Goth. bai (masc.), ba (neut.)'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Amphi- / Ambi-\", \"stance\": \"silent\", \"note\": \"Skeat's cross-reference network reaches Latin ambi- but he does not set up a Germanic node.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"English\",\n          \"words\": \"both; be-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"both: Middle English bathe/bothe, borrowed in the Viking age from Old Norse báðir (a compound of the inherited dual *bai 'both' with the demonstrative/article, cf. Goth. bajōþs), replacing the native OE bēgen/bā; ON báðir < PGmc *bai + *þai, ultimately PIE *h₂m̥bʰoh₁ (Skt. ubhāu, Av. uwa, Gk. ἄμφω, Lat. ambō). be-: Old English prefix be-, the unstressed form of the preposition bī 'by, about, on all sides', PGmc *bi < the reduced *bʰi of *h₂m̥bʰi; hence the 'all around, thoroughly' force of besiege, bespatter, bewail.\",\n          \"sources\": [\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; Klein p.512 and AHD s.vv. ambhi/ambhō (checked at node #15) cover it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 vol. I p.512 s.v. both\", \"stance\": \"supports\", \"note\": \"quoted at node #15; Klein connects it directly to OI u-bhāu, Avestic u-wa/u-bē and Gk. ἄμφω.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 p.2 s.vv. ambhi 1a-b, ambhō 1\", \"stance\": \"supports\", \"note\": \"'a. Old English bi, bī, be, by: BY; b. Old English bi-, be-, on all sides, be-, also intensive prefix: BE-'; and 'Old Norse bāthir, both: BOTH.'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 55\", \"stance\": \"supports\", \"note\": \"'ags. bā (þū), engl. both'.\"}\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Latin\",\n          \"words\": \"ambi-îre; ambactus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"ambīre 'to go around' = ambi- (the Latin reflex of *h₂m̥bʰi, amb- before a vowel, am-/an- before a consonant) + īre 'to go' (PIE *h₁ey-, Nourai's 'Ei'); its participle ambiēns gives ambient and its noun ambitiō, ambitus 'a going round (canvassing for votes)' gives ambition. That half is straightforwardly Latin and confirmed. ambactus, however, is NOT a Latin formation: every authority makes it a Gaulish word taken into Latin. Festus glosses 'apud Ennium lingua gallica seruus appellatur … seruus ambactus, i.e. circumactus dicitur', Caesar uses it of Gauls (BG 6.15.2), and Ernout-Meillet call it 'Substitut gaulois de i.-e. *ambhi-'; Watkins files it under ag- as 'Celtic *amb(i)-ag-to-, \\\"one sent around\\\" (*ambi, around; see ambhi), in Latin ambactus, servant'. So the box is right about the morphology (*ambhi- + *ag- 'to drive') but wrong to label the word Latin — it is a Celtic compound that Latin (and, through Germanic, Romance) borrowed.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ambassador\",\n            \"https://ahdictionary.com/word/indoeurop.html\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. ag-: '3. Suffixed form *ag-to- in Celtic *amb(i)-ag-to-, \\\"one sent around\\\" (*ambi, around; see ambhi), in Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSADOR, EMBASSAGE, (EMBASSY)'; s.v. ambhi: '3. Latin ambi-, around, about: AMBI-' and '5. Celtic *ambi (see ag-)'. Watkins supports the morphology but assigns ambactus to Celtic, not Latin.\"},\n            {\"ref\": \"KLN:512\", \"status\": \"supports\", \"note\": \"Klein 1966 vol. I p.512 (KLN_1966.txt ff-leaf 279, whose OCR still carries the printed folios '512' and '513') s.v. embassy: 'OF. ambassee, fr. It. ambasciata … fr. OProvenç. *ambaissa, \\\"service\\\", which is a Teut. loan word. Cp. Goth. andbahti, OE. ambiht, OS. ambaht, ON. embætti, OHG. ambaht(i) … The Teut. words themselves are of Celtic origin, and lit. mean \\\"a going or driving around\\\"; cp. Gaul.-L. ambactus, \\\"servant\\\", lit. \\\"one going around\\\". See ambages and cp. ambassador, amt.' Nourai's page number is exact — and Klein, like Watkins, calls the word Gaulish-Latin.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. ambactus, ambi-, ambio\", \"stance\": \"partial\", \"note\": \"'ambactus … apud Ennium lingua gallica seruus appellatur … Substitut gaulois de i.-e. *ambhi-. Mot étranger — non pas mot d'emprunt'; 'ambi-, amb-, am-, an-: particule attestée seulement comme premier élément de composé … am praepositio loquelaris significat circum'; 'ambio … aller autour, faire le tour de … un composé de eo'. Confirms ambi-īre; puts ambactus outside Latin.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lat. etym. Wb. index 'ambi, umbi I 57, II 210'\", \"stance\": \"supports\", \"note\": \"the Latin prefix is filed with Germanic umbi under the same IE heading.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.34\", \"stance\": \"supports\", \"note\": \"'lat. amb- (vor Vokal, z. B. ambigō), am-, an- (vor Kons., z. B. amputō, amiciō aus *am[bi]iacio) untrennbares Präfix \\\"herum, um, ringsum\\\", alat. auch Präp. am \\\"circum\\\" m. Akk.'\"}\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"English\",\n          \"words\": \"ambient; ambassador; embassy\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"ambient: Lat. ambiēns, -entis, present participle of ambīre 'to go round, surround', into English in the 1590s. ambassador / embassy: Gaulish *ambaktos 'one sent around' > Latin ambactus 'vassal, servant'; borrowed into Germanic (Goth. andbahts 'servant', OHG ambaht, whence German Amt 'office'); Germanic *ambaht- 'service' was then re-borrowed into Gallo-Romance as Old Provençal *ambaissa 'service' > ambaissada, Italian ambasciata, whence Old French ambassee > English embassy (1570s) and Italian ambasciatore > Old French ambassadeur > Middle English ambassadour (late 14c.). The chain is thus Celtic → Latin → Germanic → Romance → English, a genuine round trip that the chart's single Latin → English arrow compresses.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ambassador\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; Klein p.62 (ambient) and p.512 (embassy, ambassador) cover it — see node #17.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 vol. I p.62 s.vv. ambient, ambassador; p.512 s.v. embassy; p.63 s.v. amt\", \"stance\": \"supports\", \"note\": \"'ambient, adj., surrounding. — L. ambiens, gen. -entis, \\\"going round\\\", pres. part. of ambire … compounded of ambi- … and ire, \\\"to go\\\"'; 'ambassador … F. ambassadeur, fr. It. ambasciatore, fr. ambasciata, \\\"embassy\\\"'; 'amt … fr. G. Amt, \\\"office\\\" … which is of Celtic origin. Cp. Gaulish-Lat. ambactus, \\\"servant\\\", and see embassy'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ag- 3\", \"stance\": \"supports\", \"note\": \"'Latin ambactus, servant (> Medieval Latin ambactia, office): AMBASSADOR, EMBASSAGE, (EMBASSY)'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat (searched ambassador, ambient)\", \"stance\": \"silent\", \"note\": \"the Concise edition on disk yields only the Amphi-/Ambi- cross-reference.\"}\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"Indo-European\",\n          \"words\": \"Ambhô-bhor, Ambhor\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"This node is taken wholesale from Stuart Mann's Indo-European Comparative Dictionary, whose entry reads 'ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhō and bher-, bhor-) \\\"two-handled vessel\\\"', citing Skt. ambhṛṇaḥ, Gk. ἀμφορεύς / ἀμφιφορεύς, Lat. amphora, OHG ampri, OE amber/embren, Du. emmer, ON/Sw. ámbar. So the reconstruction is real and Nourai's page is right; the reservations are (i) the mainstream analysis of ἀμφορεύς is not *ambhō-bher- 'carried by both (hands)' but simply ἀμφι- + -φορεύς 'carrier around', the shorter ἀμφορεύς being a syncopated ἀμφιφορεύς already in Homer, so *ambhō- 'both' is Mann's own idea; (ii) Mann's dictionary is a lone, unreviewed reconstruction manual with no Pokorny or Walde-Pokorny entry behind this lemma; (iii) Mann glosses the etymon 'two-handled VESSEL', while Nourai converts it to 'a two-handled tool' to make it fit the pliers of node #20.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"IEC:19\", \"status\": \"supports\", \"note\": \"IEC.txt ff-leaf 25 (running head '19 ambhi-quolos (ombhi-, mbhi-) — amtlos, om (amətrom)'): 'ambhor-, ambhr- (for ambh-bhor, -bhr-, cf. ambhō and bher-, bhor-) \\\"two-handled vessel\\\". Skt. ambhṛṇaḥ; Per. ambar; Myc. and Gk. amphoreús, amphiphoreús; LW in Lat. amphora; OHG ampri; OE amber, embren; Du. emmer; Sw. (fr. LG) ámbar …'. Nourai's headword, his gloss and his 'Bher 1' cross-reference are all Mann's.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.34 (ambhi) and s.v. bher-\", \"stance\": \"silent\", \"note\": \"Pokorny has no *ambhi-bher- / *ambhō-bher- compound at all; Greek ἀμφορεύς is not discussed under ambhi.\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 54-55\", \"stance\": \"silent\", \"note\": \"same — no vessel compound under ambhi.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. ambhi, ambhō\", \"stance\": \"silent\", \"note\": \"Watkins lists no *ambhi-bher- derivative; AMPHORA is not among the English derivatives of ambhi.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck, Selected Synonyms (searched for amphora, tongs)\", \"stance\": \"silent\", \"note\": \"Buck's vessel and tool chapters do not set up an IE 'two-handled vessel' etymon.\"}\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"Persian\",\n          \"words\": \"anbor\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"NP anbor / anbur انبر 'tongs, pliers' (with the by-forms انبره anbura and the compound انبردست anbor-dast). Moʿin defines it 'آلت فلزی دو شاخه که با آن آتش یا چیز دیگر را برگیرند' — 'a two-pronged metal implement with which one picks up fire or something else' — so Nourai's gloss and his extras انبره، انبردست are right. The DERIVATION is not. Mann's entry (node #19) does list 'Per. ambar' among the reflexes of *ambhor-, but in a list whose other members are ἀμφορεύς, amphora, OE amber, Du. emmer 'bucket' and Sw. ámbar, Mann's Persian item is plainly the vessel-word انبار anbār 'store, granary' — and Persian anbār is universally derived from Old Iranian *ham-pāra-/*ham-bāra- 'that which is heaped together' (ham- 'together' + bar- 'to carry'), the same prefix that gives انباشتن anbāštan 'to heap up' and انبوه anbūh 'crowd'. That native ham- > NP an-/am- is the obvious source of the an- of انبر too ('that which brings/holds together' — exactly a pair of tongs), and it has nothing to do with *ambhi/*ambhō. Wiktionary, the only modern reference to treat انبر, gives yet a third origin ('From Middle Iranian, from Proto-Indo-European *h₂eḱ- \\\"sharp\\\"', unsourced). No independent authority supports Mann's *ambhō-bher- > Persian pliers, so the edge is disputed even though the word itself is well documented.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"IEC:19\", \"status\": \"partial\", \"note\": \"IEC.txt leaf 25 s.v. ambhor-: the entry does read 'Per. ambar', but under the gloss 'two-handled vessel' and among amphora / OE amber / Du. emmer 'bucket'. Mann's 'ambar' is therefore the vessel-word انبار, not انبر 'pliers'; Nourai has re-pointed it.\"},\n            {\"ref\": \"MON:361\", \"status\": \"supports\", \"note\": \"Moʿin's page number could not be verified (only the unpaginated 2-vol abridgement is on disk), but the entry is there verbatim: 'انبر [= انبره] (اِ.) آلت فلزی دو شاخه که با آن آتش یا چیز دیگر را برگیرند … (مکن.) نوعی از اهرم که نیروی کارگر در وسط آن قرار دارد'; also 'انبردست' and 'انبره'. All three of Nourai's Persian forms and his gloss 'pliers' are Moʿin's; Moʿin supplies no etymology, so he does not support the arrow, only the word. Alphabetically انبر falls in the 360s of Moʿin vol. 1, so the page number is credible.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Grundriss (searched anbor, ambur, anbar)\", \"stance\": \"silent\", \"note\": \"Horn has no entry for انبر.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien (searched ambar, anbur)\", \"stance\": \"silent\", \"note\": \"the only hit is a remark on Armenian ambar 'Speicher' (= انبار 'granary'), i.e. the store-word, not the tongs.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā (Persian and Latin indexes, searched انبر / AMB-)\", \"stance\": \"silent\", \"note\": \"no entry for انبر and no AMBHI headword in the Latin index.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie (searched *ambur, hambār)\", \"stance\": \"silent\", \"note\": \"no Middle Persian ancestor of انبر is registered.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.vv. انبر، انبردست، انبره\", \"stance\": \"partial\", \"note\": \"quoted in ref_check: the word and its senses, but no etymology.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-51.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-04T19:58:46.184Z] TOOL RESULT

```
JSON OK
```


## [2026-09-04T19:58:50.384Z] TOOL CALL #103: Bash

```json
{
 "command": "python3 tools/verify_check.py 51"
}
```


### [2026-09-04T19:58:52.295Z] TOOL RESULT

```
nodes verified: 20/20
node verdicts: {'plausible': 7, 'disputed': 8, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_checked': 6, 'partial': 5, 'not_found': 1}
books consulted: {'supports': 29, 'partial': 16, 'silent': 18, 'contradicts': 13} | by book: {'HUB': 8, 'PHD': 8, 'BRT': 7, 'CHEUNG': 7, 'KLN': 6, 'AHD': 6, 'WLD': 5, 'HRN': 5, 'NYB': 3, 'KNT': 3, 'BQT': 3, 'MON': 3, 'SKT': 3, 'POK': 2, 'AVG': 1, 'HENNING': 1, 'TLM': 1, 'LAT': 1, 'LEW': 1, 'SYN': 1, 'ARY': 1}
```


## [2026-09-04T19:58:55.598Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | grep -i \"51\\|MISSING\" | head -20; echo \"exit=$?\""
}
```


### [2026-09-04T19:58:59.028Z] TOOL RESULT

```
exit=0
```


## [2026-09-04T19:59:18.402Z] AGENT

Done. `data/verification/page-51.json` written and `python3 tools/verify_check.py 51` passes with no PROBLEM lines.

**PDF page 51 (book p.21) — root Ambhi, Mbhi, Obhi, Ebhi / Ambhô "around; both"**

- Root: **confirmed** (Pokorny 34 verbatim; Walde-Pokorny I 54-55; Watkins *ambhi*/*ambhō*).
- Nodes 20/20: **5 confirmed, 7 plausible, 8 disputed**, 0 unverified/transcription_suspect.
- Ref checks: 18 supports, 5 partial, 1 not_found, 6 not_checked (nodes Nourai left unreferenced). 12 books consulted + 16 archived web sources.

Disputed items (all in the Iranian branch, all from Nourai reproducing Horn 1893 without the later corrections — Persian *af-* continues three prefixes, *abi-*, *apa-*, *upa-*, that merged in Middle Persian):

- #3 Persian afsar "crown" — Henning: cannot go back to *abisarah- (would give *ōsar); Nyberg: < *upa-sarah-. (afrūxtan, afrāštan, afsār in the same box are fine.)
- #4 Av. aiwi-saoka — Darmesteter's *aiwi-saoča-, demolished by Horn on the same page Nourai cites ("unhaltbar, da aw. č im Np. nicht zu s werden kann").
- #4/#5 aiwi-kand / afkandan — Nyberg *apa-kan-/*upa-kan-, Cheung "(+ *apa-)"; Horn himself: "die Bedeutung nicht passt".
- #5 afsūs — Horn/Hübschmann call it unexplained; Nyberg: apa- + srav-.
- #6/#7 aiwi-fšān / afšāndan — Cheung: root *šan + *apa-; Hübschmann struck out Horn's nos. 102-106 as "nicht einwandfrei".
- #8/#9 aiwiš-kar / šekār — Cheung *skar "to pursue, drive" (perhaps a Sogdian loan); Hübschmann cuts bi-šgard < *vi-škart, so the š- is root-initial.
- #8/#9 aiwiš-tap / šetāftan — MP awištāftan < *abi-stap- (Cheung, PIE *step-, Pok. 1013): prefix right, but the š-t- is the root, not aiwiš + tap "heat".
- #20 anbor "pliers" — Mann's "Per. ambar" under *ambhor- is the vessel-word انبار (< *ham-bāra-), not انبر; no independent source supports the arrow.

Also recorded: **BQT:2143 is a wrong page** (it is نشان/نشاندن; the افشان/افشون entries are at BQT ≈p.150), and **KLN:512 is exact** (Klein's *embassy*). Nodes #10/#11 (āstīn < Gershevitch's *abi-dasta-) kept as plausible — Wiktionary calls the word etymologically unknown, Herzenberg proposes a Pashto-type SE Iranian loan.
