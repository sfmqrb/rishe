# Verification process log — verify-page-311


## [2026-09-04T14:27:11.841Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 311 (chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-311.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-311.json). Use WebFetch/WebSearch for sources. Write /home/sfmqrb/git/rishe/data/verification/page-311.json and reply with the short summary described in the instructions.


## [2026-09-04T14:27:14.821Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T14:27:14.834Z] TOOL RESULT

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
45	## Sources to use (in roughly this order)
46	
47	- **Wiktionary** (en.wiktionary.org) — has the best coverage of Persian, Middle Persian,
48	  Avestan, Old Persian, Sogdian, Arabic etymologies, with citations (Cheung 2007, Hasandust,
49	  MacKenzie 1971, Bartholomae, Horn, Hübschmann, Nourai himself). Fetch the word's page AND
50	  the `Reconstruction:Proto-Indo-European/…` / `Reconstruction:Proto-Iranian/…` pages.
51	  Use URL-encoded Persian/Arabic script for those pages.
52	- **Etymonline** (etymonline.com/word/<word>) for English/French/Latin/Greek chains.
53	- **American Heritage Dictionary IE roots** (ahdictionary.com/word/indoeurop.html or
54	  ahdictionary.com/word/search.html?q=<root>) — Nourai's "AHD" citations refer to the 1975
55	  appendix; the online appendix is the updated edition of the same list.
56	- **Pokorny** — via indo-european.info, starlingdb.org, or Wiktionary's Pokorny citation;
57	  Nourai's "POK:nnn" is a page number in Pokorny's IEW.
58	- **Klein's Comprehensive Etymological Dictionary** (KLN) and **Horn's Grundriss der
59	  neupersischen Etymologie** (HRN), **Hübschmann's Persische Studien** (HUB),
60	  **MacKenzie's Concise Pahlavi Dictionary** (PHD), **Bartholomae AiW** (BRT) are on archive.org
61	  if needed for a hard case.
62	- **Encyclopaedia Iranica** (iranicaonline.org) for historical/cultural routes.
63	- **Nişanyan Sözlük** (nisanyansozluk.com) for Turkish; **Lisān al-ʿArab** / Wiktionary for Arabic.
64	- Use WebSearch when you don't know the right page; use WebFetch to read a page.
65	
66	Do NOT fabricate sources. If a page did not load or didn't help, don't cite it.
67	If a chain is well known and uncontroversial (e.g. Latin → Old French → English), one good
68	source covering the chain is enough; spend your effort on the Iranian and Semitic links,
69	which are where errors are likelier.
70	
71	## Output — write ONE file per page
72	
73	Write `/home/sfmqrb/git/rishe/data/verification/page-<pdf>.json` (UTF-8, no BOM):
74	
75	```json
76	{
77	  "pdf_page": 126,
78	  "book_page": 96,
79	  "verified_by": "claude-fable-5-1",
80	  "verified_on": "2026-09-04",
81	  "entries": [
82	    {
83	      "entry": 0,
84	      "root": "Dheigh, Dhigha",
85	      "verdict": "confirmed",
86	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
87	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
88	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
89	      "nodes": [
90	        {
91	          "id": 6,
92	          "lang": "Avestan",
93	          "words": "pairi-daeza",
94	          "verdict": "confirmed",
95	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' (PIE *dʰeyǵʰ-, o-grade *dʰoyǵʰ-o- > Iranian *daiza-). Attested in the Vidēvdād (pairi-daēzaiiąn) …",
96	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza", "https://www.etymonline.com/word/paradise"]
97	        },
98	        {
99	          "id": 9,
100	          "lang": "Greek",
101	          "words": "paradeisos",
102	          "verdict": "confirmed",
103	          "derivation": "Borrowed from Old Iranian *paridaiza- (Median/Old Persian form with -d-, cf. Elamite par-te-taš, Akkadian pardēsu) in the 5th c. BCE; first in Xenophon (Anabasis 1.2.7) for the Persian kings' walled hunting parks. Greek -ei- renders Iranian /ai/ ~ /ē/; -os is the Greek nominative ending. The Septuagint (3rd c. BCE) used it for the Garden of Eden, whence the 'heaven' sense.",
104	          "sources": ["https://en.wiktionary.org/wiki/παράδεισος"]
105	        }
106	      ]
107	    }
108	  ]
109	}
110	```
111	
112	Rules:
113	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
114	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
115	- `words` = the transliterations of the node joined by "; " (copy from the chart).
116	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
117	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
118	- Keep `note` on the entry for root-level comments and for anything cross-cutting
119	  (e.g. "Nourai's whole Semitic branch here is rejected by Klein …").
120	- If a node lists several words, cover each word; if they differ in verdict, use the worst
121	  verdict for the node and explain per word in `derivation`.
122	- Where the chart's own NOTE already records a dispute (e.g. "POK:694 derives Latin mattus
123	  from root Mad"), evaluate it: say which side modern scholarship takes.
124	- Valid JSON only. Test it with `python3 -m json.tool` before finishing.
125	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
126	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason).
127	  Do not paste the JSON back into your reply.
128	
```


## [2026-09-04T14:27:15.532Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-311.txt"
}
```


### [2026-09-04T14:27:15.545Z] TOOL RESULT

```
1	=== PDF page 311 (book page 281) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Leudh, Rei : to grow  (refs POK:684; KLN:885; SYN:874; VDQ:39)
4	#1 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raod 1, raoda, raodha : growth, face
5	  #2 (parent #1) [Persian] refs=BQT:944 | rŭy-îdan «روییدن ( رُستن )» : to grow ; rŭy 1 «روی ۱ ( رو )» : face
6	    #3 (parent #2) [Persian] refs=BQT:944; FSF:199 | raz «رَز ۱ ( رَزبان ، رَزبُن )» : garden, vineyard, vine
7	      #4 (parent #3) [Arabic] refs=PLA:138 | rauza : garden | NOTE: AFM:75 derives this from Persian "rîxtan: to pour"; see "Leigh 2".  VDQ:226 derives it from Pahlavi "rôt: river"; see "Ser 1".
8	        #5 (parent #4) [Persian] refs=MON | rowzeh «روضه ( ریاض )» : garden
9	    #6 (parent #2) [Persian] refs=None | rŭnîk «رونیک ( نیکروی )» : beautiful ☞Nei 1
10	      #7 (parent #6) [Arabic] refs=AFM:74 | raonaq : beauty, splendor
11	        #8 (parent #7) [Persian] refs=MON:1694 | rownaq «رونق» : growth, success
12	#9 (parent #0) [Pahlavi] refs=MON:1689 | rôstâk : village
13	  #10 (parent #9) [Persian] refs=IEC:1103; MON:1689 | rŭstâ «روستا ( روستای )» : village
14	#11 (parent #0) [Avestan] refs=KLN:885; SYN:874 | raodha-taxma : grown strong, name of a legendary hero ☞Tenk
15	  #12 (parent #11) [Persian] refs=BQT | Rostam «رُستم» : a legendary hero
16	#13 (parent #0) [Avestan] refs=VDQ:39; MAG:186 | hava-rd : well grown, well built, beautiful ☞Su 1
17	  #14 (parent #13) [Pahlavi] refs=MAG:186; VDQ:39 | hu-rust : well built, beautiful ☞Su 1
18	    #15 (parent #14) [Arabic] refs=VDQ:39; MAG:186 | hŭr : houries of paradise
19	      #16 (parent #15) [Persian] refs=MON:1378 | hŭr 1 «حور» : a heavenly woman | extra: حوری ، حورالعین ، حوروش
20	#17 (parent #0) [Sogdian] refs=SOD:344 | rwd : to grow
21	#18 (parent #0) [Indo-European] refs=KLN:885 | leudho : people ; leudheros : free
22	  #19 (parent #18) [Latin] refs=None | liber : free
23	    #20 (parent #19) [English] refs=None | liberty, deliver, Latvia
24	
```


## [2026-09-04T14:27:15.835Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-311.json"
}
```


### [2026-09-04T14:27:15.847Z] TOOL RESULT

```
1	{
2	  "pdf_page": 311,
3	  "book_page": 281,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Leudh, Rei",
8	        "lang": "Indo-European",
9	        "refs": "POK:684; KLN:885; SYN:874; VDQ:39",
10	        "gloss": "to grow"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "KLN:885; SYN:874",
18	          "words": [
19	            {"translit": "raod 1, raoda, raodha", "gloss": "growth, face", "script": null}
20	          ],
21	          "script_extra": null,
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:944",
30	          "words": [
31	            {"translit": "rŭy-îdan", "gloss": "to grow", "script": "روییدن ( رُستن )"},
32	            {"translit": "rŭy 1", "gloss": "face", "script": "روی ۱ ( رو )"}
33	          ],
34	          "script_extra": null,
35	          "note": null,
36	          "quote": null
37	        },
38	        {
39	          "id": 3,
40	          "parent": 2,
41	          "lang": "Persian",
42	          "refs": "BQT:944; FSF:199",
43	          "words": [
44	            {"translit": "raz", "gloss": "garden, vineyard, vine", "script": "رَز ۱ ( رَزبان ، رَزبُن )"}
45	          ],
46	          "script_extra": null,
47	          "note": null,
48	          "quote": {"text": "چو ببرید رستم تن شاخ گز - بیامد ز دریا بایوان و رَز", "poet": "Ferdowsî"}
49	        },
50	        {
51	          "id": 4,
52	          "parent": 3,
53	          "lang": "Arabic",
54	          "refs": "PLA:138",
55	          "words": [
56	            {"translit": "rauza", "gloss": "garden", "script": null}
57	          ],
58	          "script_extra": null,
59	          "note": "AFM:75 derives this from Persian \"rîxtan: to pour\"; see \"Leigh 2\".  VDQ:226 derives it from Pahlavi \"rôt: river\"; see \"Ser 1\".",
60	          "quote": null
61	        },
62	        {
63	          "id": 5,
64	          "parent": 4,
65	          "lang": "Persian",
66	          "refs": "MON",
67	          "words": [
68	            {"translit": "rowzeh", "gloss": "garden", "script": "روضه ( ریاض )"}
69	          ],
70	          "script_extra": null,
71	          "note": null,
72	          "quote": {"text": "امشب آن نیست که درخواب رود چشم ندیم - خواب در روضهٔ رضوان نکند اهل نعیم", "poet": "Sa`dî"}
73	        },
74	        {
75	          "id": 6,
76	          "parent": 2,
77	          "lang": "Persian",
78	          "refs": null,
79	          "words": [
80	            {"translit": "rŭnîk", "gloss": "beautiful", "script": "رونیک ( نیکروی )", "see": ["Nei 1"]}
81	          ],
82	          "script_extra": null,
83	          "note": null,
84	          "quote": null
85	        },
86	        {
87	          "id": 7,
88	          "parent": 6,
89	          "lang": "Arabic",
90	          "refs": "AFM:74",
91	          "words": [
92	            {"translit": "raonaq", "gloss": "beauty, splendor", "script": null}
93	          ],
94	          "script_extra": null,
95	          "note": null,
96	          "quote": null
97	        },
98	        {
99	          "id": 8,
100	          "parent": 7,
101	          "lang": "Persian",
102	          "refs": "MON:1694",
103	          "words": [
104	            {"translit": "rownaq", "gloss": "growth, success", "script": "رونق"}
105	          ],
106	          "script_extra": null,
107	          "note": null,
108	          "quote": null
109	        },
110	        {
111	          "id": 9,
112	          "parent": 0,
113	          "lang": "Pahlavi",
114	          "refs": "MON:1689",
115	          "words": [
116	            {"translit": "rôstâk", "gloss": "village", "script": null}
117	          ],
118	          "script_extra": null,
119	          "note": null,
120	          "quote": null
121	        },
122	        {
123	          "id": 10,
124	          "parent": 9,
125	          "lang": "Persian",
126	          "refs": "IEC:1103; MON:1689",
127	          "words": [
128	            {"translit": "rŭstâ", "gloss": "village", "script": "روستا ( روستای )"}
129	          ],
130	          "script_extra": null,
131	          "note": null,
132	          "quote": null
133	        },
134	        {
135	          "id": 11,
136	          "parent": 0,
137	          "lang": "Avestan",
138	          "refs": "KLN:885; SYN:874",
139	          "words": [
140	            {"translit": "raodha-taxma", "gloss": "grown strong, name of a legendary hero", "script": null, "see": ["Tenk"]}
141	          ],
142	          "script_extra": null,
143	          "note": null,
144	          "quote": null
145	        },
146	        {
147	          "id": 12,
148	          "parent": 11,
149	          "lang": "Persian",
150	          "refs": "BQT",
151	          "words": [
152	            {"translit": "Rostam", "gloss": "a legendary hero", "script": "رُستم"}
153	          ],
154	          "script_extra": null,
155	          "note": null,
156	          "quote": null
157	        },
158	        {
159	          "id": 13,
160	          "parent": 0,
161	          "lang": "Avestan",
162	          "refs": "VDQ:39; MAG:186",
163	          "words": [
164	            {"translit": "hava-rd", "gloss": "well grown, well built, beautiful", "script": null, "see": ["Su 1"]}
165	          ],
166	          "script_extra": null,
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 14,
172	          "parent": 13,
173	          "lang": "Pahlavi",
174	          "refs": "MAG:186; VDQ:39",
175	          "words": [
176	            {"translit": "hu-rust", "gloss": "well built, beautiful", "script": null, "see": ["Su 1"]}
177	          ],
178	          "script_extra": null,
179	          "note": null,
180	          "quote": null
181	        },
182	        {
183	          "id": 15,
184	          "parent": 14,
185	          "lang": "Arabic",
186	          "refs": "VDQ:39; MAG:186",
187	          "words": [
188	            {"translit": "hŭr", "gloss": "houries of paradise", "script": null}
189	          ],
190	          "script_extra": null,
191	          "note": null,
192	          "quote": null
193	        },
194	        {
195	          "id": 16,
196	          "parent": 15,
197	          "lang": "Persian",
198	          "refs": "MON:1378",
199	          "words": [
200	            {"translit": "hŭr 1", "gloss": "a heavenly woman", "script": "حور"}
201	          ],
202	          "script_extra": "حوری ، حورالعین ، حوروش",
203	          "note": null,
204	          "quote": null
205	        },
206	        {
207	          "id": 17,
208	          "parent": 0,
209	          "lang": "Sogdian",
210	          "refs": "SOD:344",
211	          "words": [
212	            {"translit": "rwd", "gloss": "to grow", "script": null}
213	          ],
214	          "script_extra": null,
215	          "note": null,
216	          "quote": null
217	        },
218	        {
219	          "id": 18,
220	          "parent": 0,
221	          "lang": "Indo-European",
222	          "refs": "KLN:885",
223	          "words": [
224	            {"translit": "leudho", "gloss": "people", "script": null},
225	            {"translit": "leudheros", "gloss": "free", "script": null}
226	          ],
227	          "script_extra": null,
228	          "note": null,
229	          "quote": null
230	        },
231	        {
232	          "id": 19,
233	          "parent": 18,
234	          "lang": "Latin",
235	          "refs": null,
236	          "words": [
237	            {"translit": "liber", "gloss": "free", "script": null}
238	          ],
239	          "script_extra": null,
240	          "note": null,
241	          "quote": null
242	        },
243	        {
244	          "id": 20,
245	          "parent": 19,
246	          "lang": "English",
247	          "refs": null,
248	          "words": [
249	            {"translit": "liberty, deliver, Latvia", "gloss": null, "script": null}
250	          ],
251	          "script_extra": null,
252	          "note": null,
253	          "quote": null
254	        }
255	      ]
256	    }
257	  ]
258	}
259	
```


## [2026-09-04T14:27:30.642Z] TOOL CALL #4: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T14:27:30.650Z] TOOL RESULT

```


```


## [2026-09-04T14:27:35.812Z] TOOL CALL #5: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁lewdʰ-",
 "prompt": "Give the root form, glosses, descendants (especially Iranian: Avestan, Old Persian, Middle Persian, Persian; Latin liber; Germanic), and any notes/references (Pokorny, etc.)."
}
```


## [2026-09-04T14:27:38.192Z] TOOL CALL #6: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian etymology section of رویيدن / روییدن (to grow): Middle Persian, Old Persian/Avestan, Proto-Iranian, PIE forms and cited references. Also list related forms like رستن."
}
```


## [2026-09-04T14:27:39.606Z] TOOL CALL #7: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C",
 "prompt": "Give the Persian etymology section of روی (face): Middle Persian, Avestan, Proto-Iranian, PIE forms and cited references."
}
```


## [2026-09-04T14:27:40.951Z] TOOL CALL #8: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B2",
 "prompt": "Give the Persian etymology section of رز (vine, vineyard): Middle Persian, Old Iranian, Proto-Iranian, PIE forms, cognates, and cited references."
}
```


### [2026-09-04T14:27:41.822Z] TOOL RESULT

```
# Proto-Indo-European Root *h₁lewdʰ-

**Root Form:** *h₁lewdʰ-

**Glosses:**
1. To grow
2. People

**Notable Descendants:**

*Iranian:*
- Avestan: raoδa
- Persian: rostan (to grow)
- Talysh: lolo (people)
- Kurdish variants: rûstin, rwan, rûwayene

*Latin:*
- lībertus, līberta (freedman/freedwoman)

*Germanic:*
- Proto-Germanic *leudaną (see further descendants)

*Slavic:*
- Proto-Slavic *ľudъ (people)

*Sanskrit:*
- róhati (to grow)
- ródha (obstruction/growth)

**Key References:**
Pokorny's "Indogermanisches etymologisches Wörterbuch" (1959) and Rix's "Lexikon der indogermanischen Verben" (2001) document this root across multiple Indo-European language families, demonstrating its semantic range from growth processes to human populations.
```


## [2026-09-04T14:27:42.701Z] TOOL CALL #9: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9",
 "prompt": "Give the Arabic etymology of روضة (garden): Semitic root, cognates, any suggested Persian/Iranian origin, and references. Also list the Persian section if present."
}
```


### [2026-09-04T14:27:42.970Z] TOOL RESULT

```
Based on the provided Wiktionary page content, I cannot fulfill this request. The page shows only that **روییدن** (Ruyidan) is "a verb" with two definitions:

1. "alternative form of رفتن"
2. "alternative form of رستن"

The page contains **no etymology section** detailing Middle Persian, Old Persian, Avestan, Proto-Iranian, or Proto-Indo-European forms. No references or citations are provided on this entry.

To obtain the comprehensive etymological information you're seeking—including historical language forms and scholarly sources—you would need to consult:
- The Persian Wiktionary edition (fa.wiktionary.org)
- Dedicated Persian etymology resources
- Academic historical linguistics publications

The English Wiktionary entry presented here is minimal and lacks the etymological depth your question requires.
```


## [2026-09-04T14:27:44.144Z] TOOL CALL #10: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82",
 "prompt": "Give the Arabic and Persian etymology sections of رونق (splendor): root, any suggested Persian origin, and references."
}
```


### [2026-09-04T14:27:45.367Z] TOOL RESULT

```
# Persian Etymology: روی (Face)

**Middle Persian:** _𐫡𐫇𐫏_ (rwy /⁠rōy⁠/, "face")

**Proto-Iranian:** _*rauda-_ ("appearance"), with semantic shift from "growth, development" to "appearance"

**Proto-Indo-European:** _*h₁lewdʰ-_ ("to grow")

The etymological chain traces this noun through "to grow" → "growth/development" → "appearance/face."

**Cited References:**
- Edelʹman, D. I. (2020), _Etimologičeskij slovarʹ iranskix jazykov_ [Etymological Dictionary of Iranian Languages], Vol. 6, Vostochnaya Literatura, p. 402
- Cheung, Johnny (2007), _Etymological Dictionary of the Iranian Verb_, Brill, p. 193
```


## [2026-09-04T14:27:45.828Z] TOOL CALL #11: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B3%D8%AA%D8%A7",
 "prompt": "Give the Persian etymology section of روستا (village): Middle Persian rōstāg, Old Iranian reconstruction, Arabic رستاق borrowing, and references."
}
```


## [2026-09-04T14:27:47.467Z] TOOL CALL #12: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85",
 "prompt": "Give the Persian etymology section of رستم (Rostam): Middle Persian, Avestan Raoδas-taxma or *Rautas-taxma, meaning, and references."
}
```


### [2026-09-04T14:27:47.717Z] TOOL RESULT

```
# Persian Etymology of رز (Vine, Vineyard)

**Middle Persian Origins:**
The term derives from Middle Persian with the form /raz/, continuing ancient Iranian roots.

**Proto-Iranian and PIE Forms:**
The word traces back to Proto-Iranian ancestry, with cognates appearing across Indo-European languages including Ancient Greek "ῥάξ" (rháx, meaning grape), Latin "racēmus," and English "raisin."

**Etymology Statement:**
"[Middle Persian] (lc), [script needed] (lz /⁠raz⁠/). Cognates include [Ancient Greek] ῥόδον (rhódon)... [Latin] racēmus, and their descendants, including [English] raisin."

**Key Cognates:**
- Ancient Greek: ῥάξ (rháx) - grape
- Latin: racēmus
- English: raisin (modern descendant)

**Descendant:**
Ottoman Turkish borrowed the Persian term as رز (rez), demonstrating the word's historical influence across related language communities.
```


## [2026-09-04T14:27:49.143Z] TOOL CALL #13: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1",
 "prompt": "Give the Arabic etymology of حور (houris): root ح و ر, meaning, any suggested Persian/Pahlavi origin, and references. Also give the Persian section etymology."
}
```


### [2026-09-04T14:27:49.808Z] TOOL RESULT

```
# Etymology of روضة (Garden)

## Semitic Root
The word روضة derives from the Semitic root **ر و ض** (r w ḍ), as documented in the Wiktionary entry.

## Primary Meaning
In Arabic, روضة (rawḍa) fundamentally means "garden" or "meadow," with a secondary modern meaning of "kindergarten." The term appears in classical Islamic texts, including the Qur'an (30:15), where it refers to a garden in Paradise.

## Cognates and Descendants
The word has influenced several languages:
- **Gulf Arabic**: روضة (rōḏ̣a) — "kindergarten"
- **Moroccan Arabic**: روضة (rūḍa) — "graveyard"
- **Bengali**: রওজা (rôuza) — "mausoleum, garden"
- **Persian**: روضه (rowze) — "eulogy of the Battle of Karbala"

## Note on Persian Section
The page does not contain a dedicated Persian section. The Persian derivative is listed only in the Descendants section under the main Arabic entry, indicating that Persian borrowed this term from Arabic rather than the reverse.
```


## [2026-09-04T14:27:50.406Z] TOOL CALL #14: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/liberty",
 "prompt": "Give the full etymology of liberty, including Latin liber and PIE root, and any cross-refs to deliver."
}
```


## [2026-09-04T14:27:51.270Z] TOOL CALL #15: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Latvia",
 "prompt": "Give the full etymology of Latvia / Latvian as stated."
}
```


## [2026-09-04T14:27:53.028Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/liber#Latin",
 "prompt": "Give the Latin etymology of līber (free): Old Latin loebertatem, Proto-Italic, PIE *h₁lewdʰ-, cognates, references (de Vaan)."
}
```


## [2026-09-04T14:27:54.701Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the entry for the root leudh- (to mount up, grow; people, free) and quote its full text including derivatives (liberty, deliver, etc.)."
}
```


### [2026-09-04T14:27:59.642Z] TOOL RESULT

```
# Etymology of رونق (Splendor)

## Arabic Section

**Root:** The word belongs to the Semitic root "ر ن ق" (r n q)

**No Persian origin suggested:** Arabic is the origin language; the word is not borrowed from Persian.

**Pronunciation:** /raw.naq/

**Meanings in Arabic:** The noun (masculine) denotes "beauty, glamour," "splendour," and "radiance, glow, luster"

**References cited:**
- Almaany Arabic dictionary
- Hans Wehr's "A Dictionary of Modern Written Arabic" (1979)

## Persian Section

**Etymology:** Persian borrowed this term directly from Arabic. As stated: "Borrowed from Arabic رَوْنَق (rawnaq)"

**No independent Persian root:** The word originates from the Arabic root, not from Persian linguistic innovation.

**Attestation:** Classical Persian adopted the Arabic loanword, which subsequently spread to related languages including Chagatai, Hindustani (Hindi/Urdu), and Kurdish.

**Persian meanings expand** the original Arabic senses to include "boom, heyday, flourishing" in addition to the aesthetic meanings.
```


### [2026-09-04T14:28:01.247Z] TOOL RESULT

```
# Persian Etymology of روستا

Based on the Wiktionary entry, here's the etymology section:

**Origin:** The word derives from Middle Persian *rōstāg*, which also influenced related terms across multiple languages.

**Related Forms:** The etymology shows connections to:
- Classical Syriac *rustāqā*
- Arabic *rustāq* (رُسْتَاق)
- Old Armenian *ṙotastak*, borrowed from a Parthian cognate

**Key Quote:** "From Middle Persian (lwstʾk' /⁠rōstāg⁠/), whence Classical Syriac _rustāqā_, Arabic _rustāq_."

The entry notes that this etymological reconstruction remains incomplete, with Wiktionary requesting further elaboration on the term's ultimate origins. The documented path shows the word traveled through Middle Persian into multiple language families—Semitic (Arabic, Syriac) and Indo-European (Armenian, Persian)—making it a significant linguistic borrowing across ancient Near Eastern and Mediterranean regions.
```


### [2026-09-04T14:28:02.761Z] TOOL RESULT

```
# Persian Etymology of رستم (Rostam)

Based on the Wiktionary entry, here's the etymology information:

**Middle Persian Origin:**
The word derives from Middle Persian *lwtsthm* (/⁠rōdstahm⁠/), which combines two elements: *lwd* (/⁠rōd⁠/, "river") and *stʾhmb* (/⁠stahm⁠/, "force, power"), literally meaning "strong as a river."

**Earlier Attestation:**
The etymological tree shows progression through Proto-Iranian *hráwtah* and Old Persian *r-u-t* (/⁠rautaʰ⁠/).

**Avestan Connection:**
The page does not mention Avestan forms or "Raoδas-taxma" in the etymology section provided. The documentation traces the lineage back through Proto-Indo-European roots (*ser-* and *srew-*), but no specific Avestan reference appears in this source material.

**Folk Etymology:**
Interestingly, the entry notes that Ferdowsi's *Shāhnāma* provides an alternative folk etymology linking the name to "rastam" (meaning "I escaped"), referencing the hero's birth by Caesarean section.
```


### [2026-09-04T14:28:04.287Z] TOOL RESULT

```
# Etymology of حور (Houris)

## Arabic Etymology

**Root:** ح و ر (ḥ w r)

**Origin:** The Arabic term is likely borrowed from Classical Syriac ܚܘܪܐ (ḥawwərā), based on several factors: "the range of distribution of the white poplar is outside Arabia, but inside the Aramaic language area" and the Syriac root relates to whiteness concepts broadly.

**Meaning:** The root encompasses both "contrasting white" and "returning" or "changing one's position or state."

## Persian Etymology

The Wiktionary entry does not include a dedicated Persian section with etymology details. However, the descendants section indicates that Classical Persian حور (hur) derives from the Arabic حُور (ḥūr), which then influenced subsequent languages including Bengali, Hindi, Urdu, and Punjabi.

The word ultimately traces back through Arabic to Aramaic linguistic sources, representing a cross-cultural linguistic borrowing in the medieval Islamic world.
```


### [2026-09-04T14:28:05.954Z] TOOL RESULT

```
# Etymology of Liberty

**Origin:** Late 14c., from Old French *liberte* "freedom, liberty, free will," derived from Latin *libertatem* (nominative *libertas*), meaning "civil or political freedom, condition of a free man; absence of restraint; permission."

**Latin Root:** The Latin term derives from *liber*, meaning "free" (related to the adjective *liberal*).

**Proto-Indo-European Root:** The etymology traces back to PIE *\*leudh-ero-*, "probably originally meant 'belonging to the people,'" though the precise semantic development remains uncertain. This suffixed form stems from the base *\*leudh-* (2), meaning "people," which also produced Old Church Slavonic *ljudu*, Lithuanian *liaudis*, Old English *leod*, and German *Leute*.

**Semantic Development:** The word initially applied to persons; by the late 15c., it extended to communities describing "state of being free from arbitrary, despotic, or autocratic rule or control."

**Cross-references:** Related terms include *liberal*, *libertarian*, *libertine*, and *licence* (formal authorization from Latin *licentia*).
```


### [2026-09-04T14:28:05.966Z] TOOL RESULT

```
# Etymology of Latvia / Latvian

According to the Online Etymology Dictionary, Latvia's name derives from its inhabitants. The entry states: "named for its inhabitants, Latvian _Latvji_, whose ancient name is of unknown origin."

The name became standardized when "Latvia" emerged as a Baltic nation's designation in 1918, following independence. In English, the inhabitants were traditionally called "Lett" (from German _Lette_), though this term may represent a folk-etymologizing of the native _Latvji_ label.

Historically, parts of the modern state were known as Livonia (derived from Estonian _liiv_ meaning "sand") and Courland (from the Curonians, a Lettish people group whose name origin remains uncertain).

The related adjective is _Latvian_.
```


### [2026-09-04T14:28:08.946Z] TOOL RESULT

```
# Latin Etymology of Līber (Free)

**Etymology Chain:**
The Latin adjective *līber* ("free") derives from Old Latin *loeber*, which came from Proto-Italic *\*louðeros*, ultimately tracing to Proto-Indo-European *\*h₁léwdʰeros* (meaning "free") with roots in *\*h₁lewdʰ-* ("to grow").

**Key Cognates:**
According to the source, related words include Ancient Greek *eleútheros*, Sanskrit *ródhati*, Dutch *lieden*, German *Leute*, and Russian *ljúdi* ("people").

**References:**
The etymology is documented in de Vaan's *Etymological Dictionary of Latin and the other Italic Languages* (2008, Brill), page 338, which traces the Proto-Indo-European origin and provides the detailed linguistic development across ancient language families.
```


### [2026-09-04T14:28:11.169Z] TOOL RESULT

```
I cannot find the entry for **leudh-** in the provided web page content. The excerpt shows entries from **ad-** through **bheudh-**, but does not include entries from the **L** section where **leudh-** would appear alphabetically.

To locate this entry, you would need to navigate to the "L" section using the jump links at the beginning of the document, or search the full Indo-European Roots Appendix directly.
```


## [2026-09-04T14:28:31.600Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86",
 "prompt": "Give the Persian etymology section of رستن (to grow): Middle Persian rustan, Avestan raoδ-, Proto-Iranian, PIE, references (Cheung, Hasandust), and the list of related forms."
}
```


## [2026-09-04T14:28:33.112Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B2",
 "prompt": "Quote verbatim the Persian section's Etymology 1 text for رز (vine), including any Middle Persian form, Proto-Iranian reconstruction, cognate list and reference names (Hasandust, Cheung, Beekes, etc.)."
}
```


## [2026-09-04T14:28:34.602Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=leudh-",
 "prompt": "Quote the full Indo-European root entry for leudh- (both senses: 'to mount up, grow' and 'people'), with all derivatives listed."
}
```


## [2026-09-04T14:28:36.119Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/deliver",
 "prompt": "Give the full etymology of deliver, including Latin liberare/liber and the PIE root."
}
```


## [2026-09-04T14:28:37.606Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/rostam-1",
 "prompt": "What does the article say about the etymology of the name Rostam (Avestan Raoδas-taxma, *Rautas-taxma, 'strong as a river', Middle Persian Rōdstahm, Sogdian Rwstmy, etc.)? Quote the relevant passage."
}
```


## [2026-09-04T14:28:38.354Z] TOOL CALL #23: WebSearch

```json
{
 "query": "Middle Persian rōstāg etymology \"rōd\" river district Persian روستا etymology Hasandust"
}
```


### [2026-09-04T14:28:38.815Z] TOOL RESULT

```
# Persian Etymology 1 for رز (vine)

Based on the Wiktionary content provided, here is the Persian Etymology 1 section:

**Etymology Source:** "Middle Persian [script needed] (lc), [script needed] (lz /⁠raz⁠/)"

**Cognates Listed:** The entry identifies related terms in Ancient Greek _ῥάξ_ (rháx, "grape"), Latin _racēmus_, and their descendants, including English _raisin_.

**Key Note:** The entry explicitly states the Middle Persian forms lack proper script display in the source document, showing only placeholder text rather than actual characters. No individual reference names (such as Hasandust, Cheung, or Beekes) are cited in this particular section of the entry.

The etymology traces the word through Middle Persian to Indo-European roots shared with grape-related terminology across multiple language families.
```


### [2026-09-04T14:28:38.942Z] TOOL RESULT

```
I cannot provide the full Indo-European root entry for leudh- as requested. The web page content provided does not contain the actual dictionary entries themselves—it only describes where such information can be found.

The page mentions that "Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages" and directs users to the [Indo-European Roots](/word/indoeurop.html) appendix, but the specific entry for leudh- with its derivatives is not included in this page's content.

To access that information, you would need to visit the Indo-European Roots appendix directly through the dictionary website.
```


## [2026-09-04T14:28:39.112Z] TOOL CALL #24: WebSearch

```json
{
 "query": "Avestan \"huraoδa\" well-grown beautiful Bartholomae"
}
```


### [2026-09-04T14:28:39.446Z] TOOL RESULT

```
# Etymology of رستن (to grow)

Based on the Wiktionary entry, here is the Persian etymology for the "grow" sense:

## Etymology Source

The word derives from "Proto-Iranian *Hráwdah, from Proto-Indo-Iranian *Hráwdʰas, from Proto-Indo-European *h₁lewdʰ- (to grow)."

## Language Cognates

Related forms appear across Indo-Iranian languages:
- Baluchi: ردگ (ruddag)
- Sanskrit: रोधति (rodhati)

## Pronunciation Notes

The term shows dialectal variation in pronunciation across Persian varieties, ranging from /rus.ˈtan/ in Classical Persian to \[rʊs.t̪ʰán\] in formal Dari.

## Related Terminology

The entry lists رستنی (rostani) as an associated form.

**Note:** The provided text does not include explicit Middle Persian or Avestan etymological stages, nor does it cite Hasandust. The single reference provided is Cheung (2007), which addresses the verb's other meaning (to escape/liberate) rather than this growth sense.
```


## [2026-09-04T14:28:39.859Z] TOOL CALL #25: WebSearch

```json
{
 "query": "Sogdian \"rwδ\" OR \"rwd\" \"to grow\" Cheung *raud Iranian verb"
}
```


### [2026-09-04T14:28:40.563Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:28:40.609Z] TOOL CALL #26: WebSearch

```json
{
 "query": "Pokorny \"leudh-\" 684 \"emporwachsen\" Avestan raoδa- Leute liber"
}
```


## [2026-09-04T14:28:41.358Z] TOOL CALL #27: WebSearch

```json
{
 "query": "Arabic rawnaq رونق etymology Persian origin \"رونق\" معرب"
}
```


## [2026-09-04T14:28:42.874Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/houri",
 "prompt": "Give the full etymology of houri as stated, including the Arabic and Persian forms."
}
```


### [2026-09-04T14:28:42.969Z] TOOL RESULT

```
# Full Etymology of "Deliver"

**Origin:** The word "deliver" traces back to circa 1200 through Old French *delivrer*, meaning "to set free; remove; save, preserve; hand over (goods)."

**Latin Roots:** It derives from Late Latin *deliberare*, composed of the prefix *de* ("away") plus Latin *liberare* ("to free"). The root *liber* means "free, unrestricted, unimpeded."

**Proto-Indo-European Root:** The ultimate source is PIE *\*leudh-ero-*, which "probably originally meant 'belonging to the people,'" though the exact semantic development remains unclear. This suffixed form derives from the base *\*leudh-* (2), meaning "people," which also produced Old English *leod* and German *Leute* ("nation, people").

**Semantic Evolution:** Originally meaning "save, rescue, set free, liberate," the word's sense shifted by circa 1300 to "hand over, give, yield"—a meaning "in opposition to its etymological sense." By circa 1400, it also acquired the meaning "to project, cast, strike, throw."
```


## [2026-09-04T14:28:43.423Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hrawdah",
 "prompt": "Give the reconstruction, meaning, etymology (PIE), and descendants (Avestan, Old Persian, Middle Persian, Persian, Sogdian, etc.)."
}
```


### [2026-09-04T14:28:47.332Z] TOOL RESULT

```
Web search results for query: "Middle Persian rōstāg etymology "rōd" river district Persian روستا etymology Hasandust"

Links: [{"title":"Persian rustaki and Latin rusticus \"rustic\" | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/"},{"title":"Persian: Etymology of Rostam | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/"},{"title":"رود - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF"},{"title":"رستم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85"},{"title":"Surkh-Rōd District - Wikipedia","url":"https://en.wikipedia.org/wiki/Surkh-R%C5%8Dd_District"},{"title":"Surkh Rod District, Nangarhar, Afghanistan","url":"https://www.mindat.org/loc-226914.html"},{"title":"Rodag","url":"https://en.wikipedia.org/wiki/Rodag"},{"title":"Qohrud i. Historical Geography - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/qohrud-i-district/"},{"title":"Roknabad, Shiraz","url":"https://en.wikipedia.org/wiki/Roknabad,_Shiraz"},{"title":"Rosta","url":"https://en.wikipedia.org/wiki/Rosta"}]

Based on the search results, I found relevant information about the etymology of Middle Persian rōstāg:

Middle Persian rōstāg and New Persian rōstā meaning "district" or "river bed" are derived from Middle and New Persian rōd, Old Persian rautah- meaning "river", with Indo-Iranian rautas- and Indo-European *sreu- meaning "to flow".

The search results also show that Parthian rōdestāg suggests this derivation pattern, and the compound *raudas-tāka- (from the Old Iranian word raudah-) > rōstāg is another proposed etymology.

Additionally, the results indicate broader usage patterns: Rod means river or canal, as seen in place names like "Surkh Rod" (red river) and geographic features named after their rivers.

However, I did not find specific information about "Hasandust" in relation to rōstāg etymology in these search results. If you're looking for additional scholarly sources or more specific information about that reference, please let me know and I can conduct another search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:28:49.419Z] TOOL RESULT

```
Web search results for query: "Avestan "huraoδa" well-grown beautiful Bartholomae"

Links: [{"title":"Young Avestan_Skjærvø 3-6 Flashcards | Quizlet","url":"https://quizlet.com/274698526/young-avestan_skjaervo-3-6-flash-cards/"},{"title":"BARTHOLOMAE, CHRISTIAN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/bartholomae-christian-german/"},{"title":"Imbued with the essence of the Gods: the intersection between Zoroastrian theology and the Old Avestan possessive adjectives derived from personal pronouns | Bulletin of SOAS | Cambridge Core","url":"https://www.cambridge.org/core/journals/bulletin-of-the-school-of-oriental-and-african-studies/article/imbued-with-the-essence-of-the-gods-the-intersection-between-zoroastrian-theology-and-the-old-avestan-possessive-adjectives-derived-from-personal-pronouns/A1F3B35738599F9683A4E18737C0305C"},{"title":"Altiranisches Wörterbuch by Bartholomae Christian - AbeBooks","url":"https://www.abebooks.com/book-search/title/altiranisches-w%F6rterbuch/author/bartholomae-christian/"},{"title":"Old Avestan Dictionary. : languagehat.com","url":"https://languagehat.com/old-avestan-dictionary/"},{"title":"Bartholomae's law - Wikipedia","url":"https://en.wikipedia.org/wiki/Bartholomae's_law"},{"title":"Fig. Fig. Fig. Fig. 7 7 7 7: The Avestan alphabet in BARTHOLOMAE... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Fig-Fig-Fig-Fig-7-7-7-7-The-Avestan-alphabet-in-BARTHOLOMAE-1895-1901-161_fig1_366272448"},{"title":"Books on Avestan (Avesta) Language","url":"https://www.avesta.org/abooks.html"},{"title":"AVESTA: YASNA: (English)","url":"https://www.avesta.org/yasna/"}]

The search results provide information about the Avestan word "huraoδa" and Christian Bartholomae's work on Avestan linguistics.

The Avestan word huraoδa means "well-shaped" (adjective). This appears in a flashcard compilation from an Avestan language study resource.

Regarding Bartholomae, he met the challenge of the Old Iranian texts, both the Avesta and the Old Persian inscriptions, breaking new ground in the linguistic investigation of these texts, establishing their phonological development and morphological structure. Bartholomae's publications on Old Iranian ranged from Das altiranische Verbum (1878) to the Altiranisches Wörterbuch (1904) with its supplementary volume (1906). Bartholomae's Altiranisches Wörterbuch has been called "one of the best and most complete dictionaries written of any language".

While the search results confirm Bartholomae's prominent role in Avestan studies and identify "huraoδa" as meaning "well-shaped," the results don't specifically connect the word to the meanings "well-grown" or "beautiful" as part of your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:28:50.474Z] TOOL RESULT

```
Web search results for query: "Sogdian "rwδ" OR "rwd" "to grow" Cheung *raud Iranian verb"

Links: [{"title":"(PDF) Sogdian etymological notes","url":"https://www.researchgate.net/publication/275759045_Sogdian_etymological_notes"},{"title":"Iranian group","url":"https://starlingdb.org/new100/irn.pdf"},{"title":"(PDF) Rev.: Etymological Dictionary of the Iranian Verb","url":"https://www.academia.edu/8075087/Rev_Etymological_Dictionary_of_the_Iranian_Verb"},{"title":"Etymological Dictionary of the Iranian Verb","url":"https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf"},{"title":"Etymological Dictionary Of The Iranian Verb : Johnny Cheung : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/etymological-dictionary-of-the-iranian-verb"},{"title":"Sogdian","url":"http://www.languagesgulper.com/eng/Sogdian.html"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"Sogdian etymological notes in: Acta Orientalia Academiae Scientiarum Hungaricae Volume 64 Issue 2 (2011)","url":"https://www.akjournals.com/view/journals/062/64/2/article-p161.xml"},{"title":"CHAPTER FIVE SOGDIAN Yutaka Yoshida t INTRODUCTION I. t Overview 1.1.1 History","url":"https://theswissbay.ch/pdf/Books/Linguistics/Mega%20linguistics%20pack/Indo-European/Iranian/Sogdian%20(Yoshida).pdf"}]

I've performed the web search for your query. The search results include several academic sources related to Sogdian etymology and Johnny Cheung's "Etymological Dictionary of the Iranian Verb" (2007), which appears to be a comprehensive reference work covering Iranian verbal roots including Sogdian.

The search results primarily reference Cheung's 2007 etymological dictionary and contain academic articles on Sogdian etymology, though the specific entry for the Sogdian term "rwδ" or "rwd" with the meaning "to grow" and its connection to the Iranian root *raud doesn't appear prominently in these particular results.

If you're looking for more specific information about this etymology, you may want to consult:
- The full text of Cheung's Etymological Dictionary of the Iranian Verb published by Brill in 2007
- The academic article "Sogdian etymological notes" which appears in the search results and may contain relevant etymological discussions

Would you like me to search with different terms to find more specific information about this root?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:28:52.195Z] TOOL RESULT

```
Web search results for query: "Pokorny "leudh-" 684 "emporwachsen" Avestan raoδa- Leute liber"

Links: [{"title":"Pokorny's dictionary : Query result","url":"https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181"},{"title":"Reconstruction:Proto-Indo-European/h₁lewdʰ- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European/h%E2%82%81lewd%CA%B0-"},{"title":"Indo-European etymology : Query result","url":"https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=/data/ie/piet&text_number=2351&root=config"},{"title":"liber - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/liber"},{"title":"Indo-European etymology : List with all references","url":"https://starlingdb.org/cgi-bin/etymology.cgi?single=1&basename=/DATA/IE/piet&text_number=678&root=config"},{"title":"EWA – Article – liut","url":"https://ewa.saw-leipzig.de/articles/liut/en"},{"title":"Germanic etymology : List with all references","url":"https://starlingdb.org/cgi-bin/etymology.cgi?single=1&basename=/data/ie/germet&text_number=457&root=config"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Avesta","url":"https://en.wikipedia.org/wiki/Avesta"}]

I found search results related to your query. The results show information about Pokorny's Proto-Indo-European root "leudh-" on page 684, with the German meaning "emporwachsen, hochkommen" (to grow up).

The search results confirm the etymological connections you're looking for. The material includes Avestan raoδaiti "wächst" (grows) and raoδa- m. "Wuchs, Ansehen" (growth, appearance). Additionally, the root connects to Latin līber "free" through the derived form *leudhero-s.

The etymological entry demonstrates the semantic connection between the concepts of growth and freedom in Indo-European languages, with cognates appearing across Avestan, Sanskrit, Greek, Latin, and other language families.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:28:52.840Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:28:53.320Z] TOOL RESULT

```
# Etymology of Houri

According to the Online Etymology Dictionary, the word "houri" has the following etymological path:

The term entered English in 1737 from French *houri* (1650s), which derived from Persian *huri* meaning "nymph in Paradise." The Persian word itself came from Arabic *haura*, which means "to be beautifully dark-eyed, like a gazelle," plus the Persian singular formative element *-i*.

The complete definition describes it as a "nymph of Muslim paradise," with the ultimate sense rooted in the Arabic concept of beautiful, dark-eyed beauty.
```


### [2026-09-04T14:28:54.719Z] TOOL RESULT

```
Web search results for query: "Arabic rawnaq رونق etymology Persian origin "رونق" معرب"

Links: [{"title":"Meaning of the name Rawnaq","url":"https://www.wisdomlib.org/names/rawnaq"},{"title":"रौनक़ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%95%E0%A4%BC"},{"title":"رونق - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82"},{"title":"Meaning of the name Rawan","url":"https://www.wisdomlib.org/names/rawan"},{"title":"Arabic Words of Persian Origin | Arabic Language Blog","url":"https://blogs.transparent.com/arabic/30-arabic-words-of-persian-origin/"},{"title":"Rawandiyya","url":"https://en.wikipedia.org/wiki/Rawandiyya"},{"title":"Rawda","url":"https://en.wikipedia.org/wiki/Rawda"},{"title":"What Does The Name Rawnaq Mean?","url":"https://www.names.org/n/rawnaq/about"},{"title":"ARABIC LANGUAGE ii. Iranian loanwords in Arabic - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/arabic-ii/"}]

Based on the search results, here's what I found regarding the etymology of the Arabic word "rawnaq" (رونق):

## Etymology

The word rawnaq (رونق) was borrowed from Classical Persian رَوْنَق (rawnaq), which was itself borrowed from Arabic رَوْنَق (rawnaq). This suggests a complex etymological relationship between Arabic and Persian forms of the word.

## Meaning

The name rawnaq derives from Persian origins, carrying the beautiful meaning of "splendor," "brilliance," or "flourishing beauty." The name is closely related to the Persian root "rawan" meaning "flowing" or "smooth," combined with suffix elements that intensify its meaning to convey a sense of radiant prosperity and luminous charm.

## Linguistic Context

The word is classified as a "moʿarrab" (معرب/arabicized) word. Loanwords in Arabic, traditionally called moʿarrab (arabicized) or daḵīl (foreign words), include a considerable number of Iranian elements.

The word appears across multiple languages in South Asia and the Middle East, with Hindi/Urdu variant Raunak (रौनक) sharing the same etymological roots and meanings of splendor and festivity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:29:07.780Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181",
 "prompt": "Find the entry for root \"leudh-\" (Pokorny page 684, 'emporwachsen, hochkommen') and quote its full text including Avestan raoδa-, Latin liber, Germanic Leute etc. Also note whether 'leudh-' has a second sense 'Volk'."
}
```


## [2026-09-04T14:29:10.785Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/",
 "prompt": "Summarize the scholarly etymologies of Rostam discussed (Avestan Raoδas-taxma / *Rautas-taxma 'strong as a river', raoδa- 'growth', Middle Persian Rōdstahm, Sogdian, etc.) and the scholars cited (Justi, Mayrhofer, Schmitt, Iranica)."
}
```


### [2026-09-04T14:29:12.734Z] TOOL RESULT

```
The server returned HTTP 418 I'm a Teapot.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:29:13.038Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/",
 "prompt": "Summarize the etymologies of Persian rustā / Middle Persian rōstāg given (from rōd 'river' / Old Persian rautah-, *raudas-tāka-, Parthian rōdestāg), with the scholars cited."
}
```


## [2026-09-04T14:29:14.540Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF",
 "prompt": "Give the Persian etymology of رود (river): Middle Persian rōd, Old Persian rautah-, Proto-Iranian *hrawtah, PIE *srew-. Also list any derived terms like روستا or رستم mentioned."
}
```


### [2026-09-04T14:29:14.819Z] TOOL RESULT

```
The server returned HTTP 418 I'm a Teapot.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:29:16.724Z] TOOL RESULT

```
# Entry for Root "leudh-1"

**Root:** _leudh-_

**English meaning:** to grow up; people; free

**German meaning:** 'emporwachsen, hochkommen'

**Derivatives:** _leudho-_, _leudhi-_ 'Nachwuchs, Volk'; _leudhero-_ 'zum Volk gehörig, frei'

## Key Material Examples (selected):

The entry demonstrates the root across multiple language families. In Avestan, _raoδaiti_ means 'wächst' (grows). Latin _līber_ means 'frei' (free). For Germanic languages, Old High German _liut_ means 'Volk' (people), while Old Saxon _liodan_ and Old English _lēodan_ both mean 'wachsen' (grow). Old Church Slavic _ljudьje_ refers to 'die Leute' (the people).

**Yes, 'leudh-' carries a dual sense:** The entry explicitly notes that the meaning shifted from "growth" to "people/folk" through the semantic development "Nachwuchs = Menge, Volk" (offspring = multitude, people).

**Pages:** 684-685
```


## [2026-09-04T14:29:16.798Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BF%A5%CE%AC%CE%BE",
 "prompt": "Give the Ancient Greek etymology of ῥάξ (grape), including Beekes's view (Pre-Greek?) and any Persian/Iranian cognates mentioned."
}
```


## [2026-09-04T14:29:18.292Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D9%87",
 "prompt": "Give the Persian etymology of روضه: borrowed from Arabic روضة? meanings, references."
}
```


## [2026-09-04T14:29:19.051Z] TOOL CALL #36: WebSearch

```json
{
 "query": "\"رونیک\" نیکروی دهخدا"
}
```


## [2026-09-04T14:29:19.796Z] TOOL CALL #37: WebSearch

```json
{
 "query": "Iranica Rostam name etymology \"Raoδas-taxma\" OR \"Rautas-taxma\" \"strong as a river\""
}
```


### [2026-09-04T14:29:20.471Z] TOOL RESULT

```
# Persian Etymology of رود (River)

## Etymology Chain
According to the Wiktionary entry, the Persian word رود traces back through these stages:

- **Middle Persian**: lwd (rōd, "river")
- **Old Persian**: 𐎼𐎢𐎫 (r-u-t /rautaʰ/, "river, torrent")
- **Proto-Iranian**: *hráwtah
- **Proto-Indo-Iranian**: *sráwtas
- **Proto-Indo-European**: *srew-, possibly from *ser- ("flow")

## Derived Terms
The Wiktionary entry does **not** mention روستا (rustā, village) or رستم (Rostam) as derived terms. 

The documented derived terms in Persian are:
- رودخانه (rudxâne, "riverbed/river channel")
- ورارود (varârud)

The entry notes that رود also has an obsolete sense meaning "musical instrument" or "song" in Persian, though the etymology provided focuses on the hydrological meaning.
```


## [2026-09-04T14:29:20.545Z] TOOL CALL #38: WebSearch

```json
{
 "query": "Wiktionary Reconstruction Proto-Iranian \"*Hrawdah\" OR \"*rawdah\" grow Avestan raoδa Middle Persian rōy"
}
```


### [2026-09-04T14:29:22.065Z] TOOL RESULT

```
# Etymology of ῥάξ (grape)

## Direct Etymology

According to the Wiktionary entry, ῥάξ is "reminiscent of ῥάματα (rhámata, 'bunch of grapes'), as well as of Latin racēmus ('bunch of grapes')." The word also shows similarities to Sanskrit rájanī ('grape; lac'), Persian raz ('vine'), and Albanian rrush ('grape').

## Beekes's Perspective

The entry does not explicitly state Beekes's view regarding Pre-Greek origins. However, it cites Beekes's *Etymological Dictionary of Greek* (2010) in the "Further reading" section, suggesting his analysis is relevant to understanding this term's etymology, though his specific conclusions about Pre-Greek elements are not detailed in this source.

## Persian Cognates

Persian raz ('vine') is explicitly mentioned as a cognate in the etymology section, indicating a shared Indo-European or broader linguistic connection to the word for vine-related vocabulary across multiple language families.
```


## [2026-09-04T14:29:22.076Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=liberty",
 "prompt": "Quote the etymology of 'liberty' and the Indo-European root it links to (leudh-), with the root's gloss."
}
```


### [2026-09-04T14:29:23.498Z] TOOL RESULT

```
# Persian Etymology of روضه

**Origin:** The word روضه is "Borrowed from Arabic _رَوْضَة_ (rawḍa, 'garden')."

**Religious Development:** The religious sense became established through the influential work _روضة الشهدا_ (Garden of the Martyrs), composed by Husayn Kâshefi (1436–1504). This text, which describes the tragedy at Karbala, popularized the term's association with Shia Islamic mourning practices.

**Meanings:**
1. A eulogy of the Battle of Karbala (Shia Islamic context)
2. Garden (archaic or Islamic usage)
3. A shrine or sacred burial place

The word demonstrates how a simple Arabic term for "garden" evolved into a specifically religious concept within Persian culture through a single foundational literary work.
```


## [2026-09-04T14:29:23.547Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/hura%C5%8D%C4%91a",
 "prompt": "Give the Avestan entry huraoδa: meaning, etymology (hu- + raoδa-), attestation, references."
}
```


## [2026-09-04T14:29:25.353Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/%E1%B8%A5awir-",
 "prompt": "Give the reconstruction, meaning ('white'), and descendants including Arabic ḥ-w-r words (ḥawar, ḥūr, aḥwar), Hebrew, Aramaic."
}
```


### [2026-09-04T14:29:26.644Z] TOOL RESULT

```
Web search results for query: ""رونیک" نیکروی دهخدا"

Links: [{"title":"نیک روی نیکروی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%86%DB%8C%DA%A9-%D8%B1%D9%88%DB%8C-%D9%86%DB%8C%DA%A9%D8%B1%D9%88%DB%8C/"},{"title":"رونیک - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9/"},{"title":"رونیکا - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9%D8%A7/"},{"title":"معنی رونیک | واژه یاب","url":"https://vajehyab.com/?q=%D8%B1%D9%88%D9%86%DB%8C%DA%A9"},{"title":"معنی نیک رو | فرهنگ فارسی عمید","url":"https://www.vajehyab.com/amid/%D9%86%DB%8C%DA%A9+%D8%B1%D9%88-2"},{"title":"گنجور » فرخی سیستانی » دیوان اشعار » قصاید » شمارهٔ ۱۳۲ - در مدح سلطان محمود غزنوی گوید","url":"https://ganjoor.net/farrokhi/divanf/ghasidefk/sh132"},{"title":"جست‌وجوی نیک‌رو","url":"https://www.vajehyab.com/?q=%D9%86%DB%8C%DA%A9%E2%80%8C%D8%B1%D9%88"},{"title":"رونیک - YouTube","url":"https://www.youtube.com/playlist?list=PLEdCSbM90V3SXdj6HGGJimwvQDvOAUflw"},{"title":"معنی نیکروی - فرهنگ فارسی به پهلوی","url":"https://lamtakam.com/dictionaries/pahlavi/1185/%D9%86%DB%8C%DA%A9%D8%B1%D9%88%DB%8C"},{"title":"Aftabir","url":"https://www.aftabir.com/companies/company/177136/%D9%86%DB%8C%D9%83%D8%B1%D9%88%DB%8C-%D8%A7%D8%B5%D9%84%DB%8C"}]

I've completed the web search for "رونیک نیکروی دهخدا". The search results show dictionary entries and references to these Persian/Farsi words:

The word "رونیکا" (Runika) in Persian means "زیبارو" (beautiful-faced), "روی زیبا" (beautiful face), and relates to "نیک رو" (good-faced/handsome). 

The term "نیک روی نیکروی" appears in the Dehkhoda Dictionary as an adjective meaning "نیک رندهٔ خوش رو" (good-natured, good-looking).

The search results primarily include dictionary entries from Dehkhoda Dictionary and other Persian dictionaries (Amid, Moein, etc.) that define these related words. The results indicate these are Persian vocabulary terms that relate to appearance, character, or qualities associated with goodness and beauty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:29:28.180Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:29:28.532Z] TOOL RESULT

```
# Etymology of Liberty

According to the dictionary entry, the etymology is traced as follows:

"[Middle English _liberte_, from Old French, from Latin _lībertās_, from _līber_, free; see **leudh-**"

The entry references the Indo-European root **leudh-** in the Appendix of Indo-European roots, though the specific gloss or meaning of that reconstructed root is not provided in the content shown. The dictionary indicates that _līber_ (Latin for "free") derives from this proto-language root, which ultimately gave rise to the English word "liberty."
```


### [2026-09-04T14:29:29.788Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:29:30.005Z] TOOL RESULT

```
Web search results for query: "Iranica Rostam name etymology "Raoδas-taxma" OR "Rautas-taxma" "strong as a river""

Links: [{"title":"Persian: Etymology of Rostam | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/"},{"title":"(PDF) Rustam and his zīn-i palang","url":"https://www.academia.edu/19632304/Rustam_and_his_z%C4%ABn_i_palang"},{"title":"Meaning of the name Rostom","url":"https://www.wisdomlib.org/names/rostom"},{"title":"Meaning, origin and history of the name Rostam - Behind the Name","url":"https://www.behindthename.com/name/rostam"},{"title":"رستم - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85"},{"title":"Rostam - Legitimate Baby Names","url":"https://legitimatebabynames.com/2025/10/16/rostam/"},{"title":"Meaning of the name Rustam","url":"https://www.wisdomlib.org/names/rustam"},{"title":"Rostam (disambiguation)","url":"https://en.wikipedia.org/wiki/Rostam_(disambiguation)"},{"title":"Rostam (name)","url":"https://en.wikipedia.org/wiki/Rostam_(name)"},{"title":"Babr-e Bayan","url":"https://en.wikipedia.org/wiki/Babr-e_Bayan"}]

Based on the search results, I found relevant information about the Rostam name etymology you inquired about.

The name possibly derives from Iranian roots *rautas "river" and *taxma "strong". More specifically, the most popular theory is that it derives from *rautas-taxma "strong like a river".

Additionally, from Middle Persian lwtsthm (/⁠rōdstahm⁠/), from Middle Persian lwd (/⁠rōd⁠/, "river") and stʾhmb (/⁠stahm⁠/, "force, power"), meaning "strong as a river".

Another analysis suggests that it is a compound of raudah- (Av. raoδah-) or rautah- (OP rautah-, NP rōδ) "river" and taxman- "flowing, running" (verb tač- "to run"), with *raudas-taxman- meaning "whose running is (like that of) a river".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:29:31.075Z] TOOL RESULT

```
Web search results for query: "Wiktionary Reconstruction Proto-Iranian "*Hrawdah" OR "*rawdah" grow Avestan raoδa Middle Persian rōy"

Links: [{"title":"Reconstruction:Proto-Indo-European/h₁lewdʰ- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81lewd%CA%B0-"},{"title":"روی - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C"},{"title":"Reconstruction:Proto-Iranian/cwáHdaH - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/cw%C3%A1HdaH"},{"title":"Reconstruction:Proto-Iranian/ráwčah - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/r%C3%A1w%C4%8Dah"},{"title":"Reconstruction:Old Persian/r̥difyah - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Old_Persian/r%CC%A5difyah"},{"title":"Reconstruction:Proto-Iranian/wayd- - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wayd-"},{"title":"Reconstruction:Old Persian/rāivāh - Wiktionary, the free dictionary","url":"https://en.m.wiktionary.org/wiki/Reconstruction:Old_Persian/r%C4%81iv%C4%81h"},{"title":"Reconstruction:Proto-Indo-Iranian/Hrawdʰás - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/Hrawd%CA%B0%C3%A1s"},{"title":"Reconstruction:Proto-Iranian/háčaH - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/h%C3%A1%C4%8DaH"},{"title":"Proto-Indo-Iranian language","url":"https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language"}]

Based on the search results, I found relevant Wiktionary information about Proto-Iranian reconstructions related to the root meaning "to grow":

The Proto-Iranian reconstruction *Hráwdah has cognates including Avestan raoδa, Baluchi ruddag, Pashto loyedal, and Persian rostan.

Additionally, the Middle Persian rōy (meaning "face" or "copper, brass") is inherited from Proto-Iranian *Hraud- meaning "to grow (bigger)", which derives from Proto-Indo-European *h₁lewdʰ- meaning "to grow".

The search results show that these reconstructions appear in Wiktionary's Proto-Iranian and Proto-Indo-Iranian reconstruction pages, demonstrating the etymological connections between various Indo-Iranian languages and their common proto-language ancestor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:29:41.099Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/Hrawdʰás",
 "prompt": "Give the reconstruction, meaning, etymology, and full descendants list (Iranian: Avestan, Old Persian, Middle Persian, Persian, Sogdian, Pashto, Baluchi; Indo-Aryan)."
}
```


## [2026-09-04T14:29:42.583Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/raoδa",
 "prompt": "Give the Avestan entry raoδa: meaning, etymology, references, related terms (raoδah-, huraoδa-, raoδas-taxma-)."
}
```


## [2026-09-04T14:29:44.083Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B1%D9%88%D9%86%DB%8C%DA%A9/",
 "prompt": "What do the Persian dictionaries (Dehkhoda, Moin, Amid) say about رونیک: meaning, whether it is a real attested word, whether it is said to be the origin of Arabic رونق, any citations of poetry."
}
```


### [2026-09-04T14:29:44.890Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:29:46.336Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D9%82",
 "prompt": "Give the Arabic etymology of رستاق (rustāq): borrowed from Middle Persian rōstāg? Any deeper etymology given; references."
}
```


### [2026-09-04T14:29:46.856Z] TOOL RESULT

```
# Proto-Indo-Iranian *Hrawdʰás

**Reconstruction:** *Hrawdʰás (masculine a-stem noun)

**Meaning:** "red metal, copper"

**Etymology:** The term derives from substantivization of an adjective meaning "red, reddish," ultimately from Proto-Indo-European *h₁rowdʰ-ó-s ("red").

**Descendants:**

*Proto-Indo-Aryan:*
- Sanskrit: लो॒ह (lohá, "red metal, copper, iron")

*Proto-Iranian:*
- Sogdian: rwδ (rōδ)
- Baluchi: رود (rōd)
- Parthian: 𐫡𐫇𐫔 (rōδ, "copper")
- Old Persian: *raudah
- Middle Persian: rwy/rôy ("copper, brass")
  - Persian: روی (roy)

The term shows consistent phonetic development across Iranian languages, with the original sense of "red metal" preserved in most attested descendants.
```


## [2026-09-04T14:29:47.130Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/rostam",
 "prompt": "What does the article say about the etymology of the name Rostam? Quote the relevant passage."
}
```


## [2026-09-04T14:29:48.588Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Latvia",
 "prompt": "Give the etymology of Latvia (from Latvian Latvija, latvis, possibly Latgalians / river Latava etc.). Any connection to Latin liber or PIE *leudh-?"
}
```


## [2026-09-04T14:29:49.335Z] TOOL CALL #48: WebSearch

```json
{
 "query": "Wiktionary Sogdian \"rwδ\" grow OR \"rwδ-\" Gharib Sogdian dictionary \"to grow\""
}
```


### [2026-09-04T14:29:49.976Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:29:50.739Z] TOOL RESULT

```
# Etymology of رستاق (rustāq)

According to the Wiktionary entry, the Arabic word رستاق comes from **Middle Persian rōstāg** (written in Book Pahlavi as lwstʾk'), which subsequently influenced Classical Persian روستا (rōstā).

The document does not provide any deeper etymological information beyond this Middle Persian origin. No further linguistic ancestry or references extending the etymology beyond Middle Persian are included in the entry.
```


## [2026-09-04T14:29:50.897Z] TOOL CALL #49: WebSearch

```json
{
 "query": "Arabic rawḍa روضة etymology Persian origin \"rōd\" OR \"rīxtan\" Addai Sher moʿarrab garden Semitic r-w-ḍ"
}
```


### [2026-09-04T14:29:51.021Z] TOOL RESULT

```
I cannot provide the specific information you're requesting based on the webpage content provided. While the page mentions that Abadis Dictionary includes several major Persian lexicons—including Dehkhoda, Moin, and Amid—the actual dictionary entries and their definitions for the word "رونیک" are not displayed in this content excerpt.

The page only shows that these resources are available within the Abadis platform, but doesn't contain the substantive lexicographic details about meaning, attestation, etymology, or poetic citations you're asking about. To access that information, you would need to view the actual dictionary entries themselves on the Abadis website.
```


## [2026-09-04T14:29:52.395Z] TOOL CALL #50: WebSearch

```json
{
 "query": "Arabic ḥūr houri etymology Persian origin claim \"hu-rust\" OR \"hūrust\" OR \"huraoδa\""
}
```


## [2026-09-04T14:29:53.633Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AD_%D9%88_%D8%B1",
 "prompt": "Give the Arabic root ح و ر page: meanings (whiteness, return), derived words including حور ḥūr / حوراء ḥawrāʾ, and Proto-Semitic etymology / cognates."
}
```


### [2026-09-04T14:29:57.062Z] TOOL RESULT

```
# Etymology of Latvia

Based on the Wiktionary content provided, the etymology of Latvia traces back to Latvian origins:

**Source Etymology:**
According to the Norwegian Bokmål section, the Latvian name is "a 19th-century formation from *latvis* ('Latvian, Lett') and the country-name suffix *-ija*." The text notes that "the underlying ethnonym is considerably older, but its deeper origin is uncertain. A connection with a local river name has been proposed."

**What the source actually states:**
The page explicitly acknowledges uncertainty about deeper origins but mentions a proposed connection to a local river. However, the document does not discuss any connections to Latin *liber* or the Proto-Indo-European root *leudh-*. These etymological possibilities are absent from the provided Wiktionary entry.

The entry confirms the word was first recorded in Latvian text in 1862 and became established throughout that century, but the ultimate source of the *latvis* root itself remains unresolved in this reference material.
```


### [2026-09-04T14:30:00.096Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:30:00.911Z] TOOL RESULT

```
Web search results for query: "Wiktionary Sogdian "rwδ" grow OR "rwδ-" Gharib Sogdian dictionary "to grow""

Links: [{"title":"Sogdian Dictionary: Sogdian - Persian - English by B. Gharib: New Hardcover (1995) 1st Edition. | Anis Press","url":"https://www.abebooks.com/first-edition/Sogdian-Dictionary-Persian-English-B-Gharib/30040190515/bd"},{"title":"Sogdian Dictionary: Sogdian - Persian - English - B. Gharib: 9789645558060 - AbeBooks","url":"https://www.abebooks.com/9789645558060/Sogdian-Dictionary-Persian-English-Gharib-9645558069/plp"},{"title":"SOGDIAN LANGUAGE ii. Loanwords in Persian - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sodgian-language-i-loanwords/"},{"title":"Full text of \"Ù Ø±Ù‡Ù†Ú¯ Ø³ØºØ¯ÛŒ sogdian dictionary\"","url":"https://archive.org/stream/SogdianDictionary/GharibSogdianDictionnary_djvu.txt"},{"title":"Sogdian - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Sogdian"},{"title":"Sogdian Dictionary Sogdianpersianenglish B Gharib | PDF","url":"https://www.slideshare.net/slideshow/sogdian-dictionary-sogdianpersianenglish-b-gharib/279974034"},{"title":"Sogdian dictionary : Sogdian, Persian, English / B. Gharib ; [editorial supervisor, A. Mansouri ; editor, S. Fotouhi.] | Book | Badr al-Zamān Qarīb 1929 or 1930- (Mansouri, Ahmad | Mansouri, Ahmad;Fotouhi, Sharzad | The National Library of Israel","url":"https://www.nli.org.il/en/books/NNL_ALEPH990018188540205171/NLI"},{"title":"Sogdian alphabet","url":"https://en.wikipedia.org/wiki/Sogdian_alphabet"},{"title":"Badr al-Zaman Gharib","url":"https://en.wikipedia.org/wiki/Badr_al-Zaman_Gharib"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"}]

I found some references to the Gharib Sogdian Dictionary but the search results don't contain specific information about the entry "rwδ" or its meaning "to grow." Let me search more specifically for this term.

Links: [{"title":"Word Family - Red","url":"https://www.aidanem.com/word-family-red.html"},{"title":"TITUS Texts: Sogdian Corpus (NSW), arranged by texts","url":"https://titus.uni-frankfurt.de/texte/etcs/iran/miran/sogd/sogdnswc/sogdn216.htm"},{"title":"Sogdiana (singer)","url":"https://en.wikipedia.org/wiki/Sogdiana_(singer)"},{"title":"r 997. ( rʼβʼn /Rāvan?/ m.: B N(M?), ZK rʼβʼn xwβw: Tales, J8, p. 483; rty","url":"https://austriaca.at/0xc1aa5572_0x0024e90f"},{"title":"Sogdia","url":"https://en.wikipedia.org/wiki/Sogdia"},{"title":"English index to the Dictionaries of Manichaean and Christian Sogdian - PDF Free Download","url":"https://idoc.tips/english-index-to-the-dictionaries-of-manichaean-and-christian-sogdian-pdf-free.html"},{"title":"Reconstruction:Proto-Indo-Iranian/Hrawdʰás - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/Hrawd%CA%B0%C3%A1s"},{"title":"graphsearch.epfl.ch","url":"https://graphsearch.epfl.ch/concept/93965"},{"title":"depts.washington.edu","url":"https://depts.washington.edu/silkroad/exhibit/sogdians/essay.html"}]

Based on my search results, I found relevant information about the Sogdian term "rwδ":

In Sogdian, "rwδ" refers to copper, according to etymological word family documentation. Additionally, Wiktionary lists Sogdian "rwδ" (pronounced /rōδ/) as a reflexes of Proto-Indo-Iranian *Hrawdʰás.

However, the search results do not contain specific information about "rwδ-" or entries in Gharib's Sogdian Dictionary explicitly defining it as "to grow." The search results do suggest that this term may be etymologically connected to roots meaning growth or strengthening in related Indo-European languages, but I cannot confirm the specific dictionary entry you're looking for from the Gharib Sogdian Dictionary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:30:02.981Z] TOOL RESULT

```
Web search results for query: "Arabic rawḍa روضة etymology Persian origin "rōd" OR "rīxtan" Addai Sher moʿarrab garden Semitic r-w-ḍ"

Links: [{"title":"Meaning of the name Rawda","url":"https://www.wisdomlib.org/names/rawda"},{"title":"Rauza - Wikipedia","url":"https://en.wikipedia.org/wiki/Rauza"},{"title":"Rawda","url":"https://en.wikipedia.org/wiki/Rawda"},{"title":"Rawzat as-safa","url":"https://en.wikipedia.org/wiki/Rawzat_as-safa"},{"title":"ARABIC LANGUAGE ii. Iranian loanwords in Arabic - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/arabic-ii/"},{"title":"Riad (architecture) - Wikipedia","url":"https://en.wikipedia.org/wiki/Riad_(Morocco)"},{"title":"Paradise garden","url":"https://en.wikipedia.org/wiki/Paradise_garden"},{"title":"Rawda Khwani","url":"https://en.wikipedia.org/wiki/Rawda_Khwani"},{"title":"Rawda, Kuwait","url":"https://en.wikipedia.org/wiki/Rawda,_Kuwait"},{"title":"Riad - Name Origin, Meaning & Statistics","url":"https://onomaverse.com/first-names/riad"}]

Based on the search results, here's what I found regarding the etymology of Arabic rawḍa:

## Etymology and Semitic vs. Persian Origins

Etymologically, Arabic rawḍa is derived from the Arabic root r-w-d, which relates to the concepts of pasturage, verdancy, and tranquility. The word translates to "garden," "meadow," or "a place of lush vegetation," often carrying connotations of paradise or a beautiful, blooming landscape.

The search results indicate that rawḍa has a Semitic root in Arabic. However, the results also note the relationship with Persian vocabulary. The word rauza is derived through Persian from the Arabic rawdah (روضة rawḍah) meaning garden, but extended to tomb surrounded by garden. This suggests that while the word originates from Arabic roots, it traveled through Persian and was applied to Persian architectural and cultural contexts.

## Moʿarrab and Iranian Loanwords

Loanwords in Arabic, traditionally called moʿarrab (arabicized) or daḵīl (foreign words), include a considerable number of Iranian elements. This establishes that the category of moʿarrab exists for studying Iranian influences on Arabic vocabulary.

However, the search results I found do not specifically address the theory attributing rawḍa to Persian origins like "rōd" or "rīxtan," nor do they reference the work of Addai Sher on this topic. To find information specifically about those claims and Addai Sher's analysis, a more specialized search focusing on historical etymological scholarship might be needed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:30:04.069Z] TOOL RESULT

```
Web search results for query: "Arabic ḥūr houri etymology Persian origin claim "hu-rust" OR "hūrust" OR "huraoδa""

Links: [{"title":"Understanding Hur and Houris in Islam | PDF | Islamic Texts | Abrahamic Religions","url":"https://www.scribd.com/document/612333241/al-hur"},{"title":"houri - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/houri"},{"title":"Houri - Definition, Meaning & Synonyms | Vocabulary.com","url":"https://www.vocabulary.com/dictionary/houri"},{"title":"HOURI Definition & Meaning - Merriam-Webster","url":"https://www.merriam-webster.com/dictionary/houri"},{"title":"Houri | Encyclopedia.com","url":"https://www.encyclopedia.com/philosophy-and-religion/islam/islam/houri"},{"title":"HOURI Definition & Meaning | Dictionary.com","url":"https://www.dictionary.com/browse/houri"},{"title":"Houri Definition & Meaning | YourDictionary","url":"https://www.yourdictionary.com/houri"},{"title":"Houri (disambiguation)","url":"https://en.wikipedia.org/wiki/Houri_(disambiguation)"},{"title":"Houria","url":"https://en.wikipedia.org/wiki/Houria"},{"title":"Houri","url":"https://en.wikipedia.org/wiki/Houri"}]

Based on the search results, I found information about the etymology of the word "houri," but the specific Persian origin claims you mentioned ("hu-rust," "hūrust," or "huraoδa") do not appear in the search results.

Here's what the search results show about the etymology:

The word houri comes from French, through Persian, and ultimately from Arabic, specifically from ḥūriyya and ḥūriyy, which are derived from ḥūr, traced to Classical Arabic ḥūrun ʕīnun meaning "fair maidens, black-eyed ones". 

In Arabic, the plural (hur) and singular (hawra') are related to the verb root hwr, which is associated with whiteness. The Koranic phrase hur 'ayn is understood to refer to the sclerotic part of the eye, and by implication, the houri is a being with large or dark eyes like a gazelle.

The standard etymological references in these sources trace the word's origin to Arabic and indicate that Persian borrowed from Arabic, rather than the reverse. However, the specific Persian etymological forms you mentioned in your query do not appear in these search results. To find information about those specific claimed Persian origins, you would need specialized academic sources on Persian-Arabic etymology or philological studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:30:13.883Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf",
 "prompt": "Find the entry for the root *raud (to grow) — quote the reconstruction, meaning, and the attested forms listed (Avestan raoδ-, Middle Persian rustan/rōy-, Persian rustan/rōyīdan, Sogdian forms, Khotanese, Pashto, etc.), plus the IE etymology given."
}
```


## [2026-09-04T14:30:15.388Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/Hr%C3%A1wdah",
 "prompt": "Give the reconstruction, meaning, etymology, and full descendants list."
}
```


## [2026-09-04T14:30:16.142Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Rostam_(name)",
 "prompt": "Quote the etymology section of the name Rostam in full."
}
```


### [2026-09-04T14:30:17.174Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:30:17.702Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Houri",
 "prompt": "Quote the etymology section for houri (Arabic root ḥ-w-r, whiteness, ḥawrāʾ, Aramaic connections, any Persian-origin claims)."
}
```


## [2026-09-04T14:30:19.281Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Rustaq",
 "prompt": "Quote what the article says about the etymology of the word rustaq / rōstāg."
}
```


## [2026-09-04T14:30:20.008Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/houri",
 "prompt": "Give the full etymology of houri as stated, including Arabic forms and root and any Persian intermediate."
}
```


### [2026-09-04T14:30:20.903Z] TOOL RESULT

```
I cannot provide the etymology section in full because there is no dedicated etymology section in the Wikipedia article provided. 

The article only mentions that **Rostam** "is a name referring to the Persian mythical hero **Rostam** who was immortalized by the poet Ferdowsi in the _Shahnameh_ (_Book of Kings_)." This brief description is the closest the article comes to explaining the name's origins, but it does not constitute a formal etymology section.
```


### [2026-09-04T14:30:22.145Z] TOOL RESULT

```
I cannot locate the entry for the root *raud (to grow) in the provided PDF content. The document appears to be a title page and introductory material from a scholarly work, but the main etymological entries and their detailed reconstructions are not visible in the text provided.

To find this specific entry with its reconstruction, meaning, attested forms across Avestan, Middle Persian, Persian, Sogdian, Khotanese, Pashto and associated IE etymology, you would need to access the actual dictionary pages containing the etymological entries, which are not included in the current document excerpt.

[Binary content (application/pdf, 5.1MB) also saved to /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/webfetch-1788532219149-q16dru.pdf]
```


## [2026-09-04T14:30:22.490Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D8%B1%D9%88%D9%86%DB%8C%DA%A9",
 "prompt": "What do the dictionaries (Dehkhoda, Moin, Amid) say about رونیک: its meaning, any citation of poetry, and any note that it is the origin of Arabic رونق?"
}
```


### [2026-09-04T14:30:24.144Z] TOOL RESULT

```
# Etymology of Houri

Based on the Wikipedia article's Etymology section:

## Arabic Root and Meaning

The word derives from classical Arabic _ḥūr_, which is the plural of both masculine _ʾaḥwar_ and feminine _ḥawrāʾ_. These terms translate to **"having eyes with an intense contrast of white and black."**

## Proposed Persian Origin

Scholars like Arthur Jeffery suggest an Iranian source, proposing the **Middle Persian _hū̆rust_ meaning 'well grown'** as the etymological root.

## European Adoption

The term "houri" entered European languages during the 17th and 18th centuries, spreading through translations and scholarly works.

The article does not establish definitive Aramaic connections in its Etymology section, though it notes scholarly debate about potential influences from multiple linguistic traditions in forming the modern understanding of the concept.
```


### [2026-09-04T14:30:24.629Z] TOOL RESULT

```
# Etymology of Rustaq

According to the article's Etymology section:

The name derives from Middle Iranian _rōstāg_, meaning **"district"**. The article notes this term also appears in Baluchi, Persian, and Kumzari languages, with New Iranian _rusta_ meaning a **"large village."**

The word is cognate to Indo-European languages, particularly Latin _rustica_, which carries the same meaning and is the source of the English word **"rustic."**
```


### [2026-09-04T14:30:27.949Z] TOOL RESULT

```
# Etymology of "Houri"

According to the Wiktionary entry, houri originates through the following path:

**English → French → Persian → Arabic**

The word entered English from French *houri*, which was borrowed from Persian *حوری* (hurî). The Persian term derives from Arabic *حُورِيّ* (ḥūriyy) and *حُورِيَّة* (ḥūriyya)—described as "adjective and feminine singulative" forms.

These Arabic words stem from the root *حُور* (ḥūr), which comes from Classical Arabic *حُورٌ عِينٌ* (ḥūrun ʕīnun), meaning "fair maidens, black-eyed ones." The entry notes related Arabic adjectives: *أَحْوَر* (ʔaḥwar, masculine) and *حَوْرَاء* (ḥawrāʔ, feminine).

In essence, the term traveled westward from its Arabic origins through Persian intermediaries before being adopted into French and subsequently English.
```


### [2026-09-04T14:30:28.634Z] TOOL RESULT

```
Based on the webpage content provided, I cannot answer your question about what the classical Persian dictionaries (Dehkhoda, Moin, Amid) say regarding رونیک, its meanings, poetic citations, or etymological connections to Arabic رونق.

The page shown is a search results interface from a Persian-English dictionary website. The only substantive definition offered comes from the "واژه‌نامه آزاد" (Open Dictionary), which states: "نیک رو، خوش رو، زیبارو" (literally: nice-faced, pleasant-faced, beautiful-faced).

The results also include related name entries and morphologically similar words, but no excerpts from the major classical dictionaries you mentioned, nor any poetic citations or etymological notes about Arabic origins.

To find this information, you would need to consult those specific dictionary sources directly.
```


## [2026-09-04T14:30:37.277Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cp /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/webfetch-1788532219149-q16dru.pdf cheung.pdf && (which pdftotext && pdftotext -layout cheung.pdf cheung.txt && wc -l cheung.txt && grep -n -i \"raud\" cheung.txt | head -40) || echo \"no pdftotext\"",
 "description": "Extract text from Cheung PDF and grep for *raud"
}
```


### [2026-09-04T14:30:44.734Z] TOOL RESULT

```
/usr/bin/pdftotext
27292 cheung.txt
4087:•IE COGNATES: Lat. fraus ‘deception’, Umb. frosetum ‘fraudatum’
4498:unconnected (cf. NEVP: 91), rather from *Hraud (Cheung 2004: 129).
8990:*(H)raud ‘to tear, break’
9000:                                                  *Hraud                                            193
9002:◊ The evidence for an Ir. root *(H)raud, which would derive from IE *(H)reud-, is
9013:*Hraud ‘to grow (bigger)’
9044:194                                           *(H)raudH
9054:*(H)raudH ‘to moan, (be)wail’
9068:•IE COGNATES: Lat. rudō ‘to cry, roar’, OCz. ruditi ‘to sadden’, Lith. raudà, Latv.
9669:*H1l(e)udh- (> Ir. *Hraud) that has given rise to a new ablaut series: > IIr. *Hurdh/
14348:*raud ‘to hinder, block, ward off’
14391:if there is a possible Ir. cognate, on which see *raud. On the etymology see also
17198:•NWIR: NP tarfand(ah), tarvand(ah) ‘lie, falsehood, deceit, fraud’, Zaz. tiritiš/tiren-
19527:’rws- does not derive from *raud.  Ghilain: 49, 81 | DMMPP: 53
19778:contamin. with *xraud)
19979:448                                           *xraud
19997:*xraud ‘to become/make angry ?, afraid ?, confused ?’
20006:*pari/a-xrauda( a)-.  Samadi: 158 f.
20254:from *us-rauda-ka-) || (+ *- ?) M. axšōw-/axšēvd-, Yi. axšōw- ‘to chew, gnaw’ || (+
26216:spu-el, 354       br?kšti, 22                kikénti, 443          raudà, 194
26832:    (of), fear       *rah, *ram, *xraud               to bestow            *ba, *baxš, *nau (s.v.)
26833:to become agitated *iauz (s.v.), *span(d)/sfan(d),     to bewail            *(H)raudH, *zarH3
26836:                     *xraud, *zarH1 (s.v.)              to bite              *dans, *gaz, *xšau (s.v.)
26843:to become            *gaiz (s.v.), *raub, *uaxš       to block             *Hram (s.v.), *marH2, *raud,
26845:                     (s.v.), *xraud, *xšai (s.v.),      to bloom             *(H)spar(H) , *spaič
26856:to become pleasant *huad                                                    *bra,*(H)raud, *Hraup,
26870:to bring up       *Hraud (s.v.), *san (s.v.)                             *sai (s.v.), *saru, *skar
26879:to burst          *Hrais (s.v.), *(H)raud (s.v.),                        (s.v.), *xšau
26971:to drive            *hauH1, *Haz, *skar, *uaz           afraid (of)       *rah, *ram, *xraud
27021:to go forth         *rai1, *ura, *zgad                to hinder            *marH2, *raud
27032:to grow             *Hraud, *(H)uard, *uarHz,          to impel             *čaud, *sar2, *tau1, *zai1
27076:to lick           *raiz1                         to moan              *(H)raudH, *karp, *mār,
27099:to make angry     *xraud                         to occur, happen   *čiau (s.v.), *gan, *garš1
27239:to stick             *čap, *kard                                               *harč, *Hrais, *(H)raud,
27252:to throw            *čiaH2, *dais2, *duanH,           to wail            *(H)raudH, *nau(H)
27262:                    (s.v.), *had (s.v.), *sač2 (s.v.)   to ward off        *Huar2, *raud
```


## [2026-09-04T14:30:49.186Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && sed -n 9010,9050p cheung.txt; echo ----; sed -n 9660,9675p cheung.txt; echo ----; grep -n -i \"rōstāg\\|rustāg\\|rōstā\\|huraoδa\\|hurust\\|Rōdstahm\\|raoδas\" cheung.txt | head",
 "description": "Read Cheung *Hraud 'to grow' entry"
}
```


### [2026-09-04T14:30:49.295Z] TOOL RESULT

```
•REFERENCES: Edel’man 1971: 240; EVS: 75b, 57a, 59a f.


*Hraud ‘to grow (bigger)’
•AVESTAN: YAv. rao- (ru-) ‘to grow’ || (+ *fra-) ‘to grow to(wards)’ || (+ *ni-) ‘to
suffer from dystrophy, wear out, von Kräften kommen (vel sim.)’ || (+ *i-) ‘to
outgrow’  Liste: 59
Pres. them. {1}: IND. 2sg. med. YAv. raoahe (Y 10.4), YAv. vīraoahe (Y 10.12), 3pl. YAv. raoti
(V 5.19), impf. 3sg. YAv. araoa (Y 9.11), INJ. 3sg. YAv. raoa (Yt 19.40, F 587); Pres. a- {2}: SUBJ.
3sg. YAv. +nī.uruuiii (V 16.7); Perf.: ? YAv. urruduš(a) (Y 10.3); Inf.: pres. ?? YAv. raose (Y 10.4);
Caus.: IND. (med. ?) 3sg. YAv. frraoaiieiti/e (V 18.46); Partic.: perf. pass. YAv. urusta- (V 19.18),
YAv. frurusta- (Yt 18.6), YAv. niuruzda- (N 17). ◊ On the interpretation of YAv. +nī.uruuiii and
niuruzda- see *raid. The past participle ºuruzda- is the regular outcome of IIr. *Hrudh-ta- > *Hrudzdha-
(Bartholomae’s Law) > Ir. *Hruzda-, Skt. rha-. The form *Hrusta- is the result of a frequent analogical
development in Ir.
•MIDDLE PERSIAN: MMP rwy-, BMP lwd- /rōy-/ ‘to grow’  DMMPP: 303a
Pres.: IND. 3sg. BMP rwdyt /rōyēd/, 3pl. MMP rwyynd, SUBJ. 3pl. MMP rwy’nd, rwyy’nd; Partic.: perf.
pass. MMP rwst, BMP lwst /rust/; Caus.: pres. IND. 2sg. MMP rwynyy
•PARTHIAN: rwd- ‘to grow’ || (+ *abi-) ’brwd ‘plants’  Ghilain: 65 | DMMPP:
299a, 14b
Pres.: IND. 3pl. rwdynd; Partic.: perf. pass. rwst, rws
•KHOTANESE: OKh. *rrd- (rrvī-) ‘to grow’ || (+ *fra-) hr(u)v- (hrs-) ‘to grow’ || (+
*ham-) habrui- (habrri-), LKh. habrDñ- (caus.) ‘to heal’  SGS: 116, 144
•SOGDIAN: BSogd. rw-, MSogd. rws (pret. stem) ‘to grow’ || (+ *pati-) SSogd.
ptrw-, CSogd. ptryst-, MSogd. ptrw- ‘to grow up’
Pres.: IND. 3sg. BSogd. rwtt, BSogd. rwt, SUBJ. 3sg. BSogd. rw’t, 3pl. MSogd. rw’nd (Sogdica:
46); Inf.: BSogd. rw’y || (+ *pati-) Impf.: IND. 3sg. MSogd. pyrw (BBB: 35); Pret.: intr. IND. 3sg.
SSogd. ptrwsty; Partic.: perf. pass. SSogd. ptryst (lit. ’grown’) PN; Inf.: pret. CSogd. ptrysty ||
•NWIR: NP rustan/rōy-, Zaz. ruwyiš/ruwen- ‘to bud, blossom’, Gz. rōn-/ruft ‘to
grow’, Bal. rust, rudit/rud-, rōēnθ/rōēn- (caus.) ‘to bring up, educate’ || (+ *ham-)
? Bal. amrust/amrud- ‘to arch, stretch the body’
•NEIR: Yghn. rut-/rústa ‘to grow’ || (+ *i-) Pash. wrost m., wrastá ‘rotten, decayed
(of wood, matting)’ (Cheung 2004: 129)
•MISC: Par. rust ‘high, elevated’
194                                           *(H)raudH

•SANSKRIT: rodh ‘to grow’ (RV+)  EWAia II: 467
•PIE *H1leudh- ‘to grow, rise’  LIV: 248 f. | Pok.: 306 f., 684 f.
•IE COGNATES: Gr.  (m.) ‘free man, non-slave’, OIrish luss ‘plant’, Goth.
liudan, OE lēodan ‘to grow’
•REFERENCES: IIFL I: 285a; Andreev – Peščereva: 316b; DKS: 367a; WIM II/1: 82; Werba 1997: 229 f.;
----
336a
Pres.: IND. 3pl. MMP w’rynd; Partic.: perf. pass. BMP w’lynyt /wlēnīd/; Inf.: BMP w’lytn /wlīdan/
•NWIR: NP blīdan/bl- ‘to grow, prosper’
•NEIR: Pash. w+ ‘successful, winning’, wa+na ‘winning, gaining, success’ || (+ *-)
Oss. I. awærdyn/awærst, D. awærdun/aurst ‘to spare, save (money)’
•MISC: Udm. (LW) vord- ‘to grow; spare’ (< pre-Oss. ?)
•SANSKRIT: vardh ‘to let grow, promote, increase [act.]; to grow, become big [med.]’
(RV+)  EWAia II: 520
◊ This IIr. root is according to Schindler apud Krisch: 24 f. from (metathesized) IE
*H1l(e)udh- (> Ir. *Hraud) that has given rise to a new ablaut series: > IIr. *Hurdh/
Hardh. No explanation has been provided for the assumed metathesis of *ru > *r.
Perhaps, this root has been contaminated with semantically similar roots, notably
*Hard1. The Manichaean (West) Iranian forms MMP w’r-, BMP w’l- /wl-/ ‘to
grow, prosper’ are to be separated from w’r- ‘to be glad, happy’ (*arHz).
•PIE –  LIV: 228 | Pok.: 1167
•IE COGNATES: –
----
```


## [2026-09-04T14:31:08.413Z] TOOL CALL #61: WebSearch

```json
{
 "query": "Persian raz رز \"vine\" etymology Middle Persian raz Greek rhax racemus Wanderwort Hasandust OR Horn OR Hübschmann"
}
```


## [2026-09-04T14:31:09.167Z] TOOL CALL #62: WebSearch

```json
{
 "query": "\"rōstāg\" etymology \"raudah\" OR \"raoδah\" OR \"*raudas-tāka\" district Middle Persian"
}
```


## [2026-09-04T14:31:10.666Z] TOOL CALL #63: WebSearch

```json
{
 "query": "Avestan \"huraoδa-\" OR \"huraoδa\" \"wohlgewachsen\" OR \"well-grown\" OR \"well-shaped\" Yasht Bartholomae 1494"
}
```


## [2026-09-04T14:31:10.889Z] TOOL CALL #64: WebSearch

```json
{
 "query": "Jeffery \"Foreign Vocabulary of the Qur'an\" hur houris \"hurust\" OR \"well grown\" Pahlavi Tisdall"
}
```


### [2026-09-04T14:31:16.377Z] TOOL RESULT

```
Web search results for query: "Persian raz رز "vine" etymology Middle Persian raz Greek rhax racemus Wanderwort Hasandust OR Horn OR Hübschmann"

Links: [{"title":"رز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D8%B2"},{"title":"racemus - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/racemus"},{"title":"raisin - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/raisin"},{"title":"\"رز\" meaning in All languages combined","url":"https://kaikki.org/dictionary/All%20languages%20combined/meaning/%D8%B1/%D8%B1%D8%B2/%D8%B1%D8%B2.html"},{"title":"ῥάξ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E1%BF%A5%CE%AC%CE%BE"},{"title":"راز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B1%D8%A7%D8%B2"},{"title":"Raceme - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/raceme"},{"title":"Raisin - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/raisin"},{"title":"racemus | Definition of racemus at Definify","url":"http://www.definify.com/word/racemus"},{"title":"Middle Persian","url":"https://en.wikipedia.org/wiki/Middle_Persian"}]

Based on the search results, here's what I found regarding the etymology of Persian raz (رز, "vine"):

## Etymology Summary

Persian raz is cognate with Ancient Greek ῥάξ (rháx, "grape") and Latin racēmus. These words—including Persian رز (raz, "vine")—were presumably borrowed from the same source.

The origin is unknown and probably from an ancient, extinct Mediterranean substrate language. This appears to be the same ancient lost Mediterranean language that gave Greek rhax (genitive rhagos) "grape, berry".

## Related Words

The search results show a connection across multiple languages: The word is reminiscent of Latin racēmus ("bunch of grapes"), Sanskrit रजनी (rajanī, "grape, lac"), Persian رز (raz, "vine") and Albanian rrush ("grape").

Note: While your search query mentioned specific scholars (Hasandust, Horn, Hübschmann), the web search results don't contain citations to these particular etymologists' work on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:31:17.376Z] TOOL RESULT

```
Web search results for query: ""rōstāg" etymology "raudah" OR "raoδah" OR "*raudas-tāka" district Middle Persian"

Links: [{"title":"Persian rustaki and Latin rusticus \"rustic\" | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/"},{"title":"Persian: Etymology of Rostam | WordReference Forums","url":"https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/"},{"title":"Rostaq","url":"https://en.wikipedia.org/wiki/Rostaq"},{"title":"Rostam Rah","url":"https://en.wikipedia.org/wiki/Rostam_Rah"},{"title":"Rustaq - Wikipedia","url":"https://en.wikipedia.org/wiki/Rustak"},{"title":"Rostaq, Afghanistan","url":"https://en.wikipedia.org/wiki/Rostaq,_Afghanistan"},{"title":"Takht-e Rostam","url":"https://en.wikipedia.org/wiki/Takht-e_Rostam"},{"title":"Rostam (name)","url":"https://en.wikipedia.org/wiki/Rostam_(name)"},{"title":"Rostam (disambiguation)","url":"https://en.wikipedia.org/wiki/Rostam_(disambiguation)"},{"title":"Rostaq Rural District","url":"https://en.wikipedia.org/wiki/Rostaq_Rural_District"}]

Based on the search results, I found relevant information about the etymology of rōstāg:

In Old Iranian there are two similar words for "river": rautah- (Old Persian rautah- > New Persian rōd) and raudah- (Avestan raoδah-). The latter seems to be the source of the compound *raudas-tāka- > rōstāg.

The element -tāg in rōstāg means "river-bed, district" and belongs to the Iranian root tač- (tak-) "to flow, to run", with parallels in Bactrian (ταγο "river-valley") and Pashto (tōe "river, mountain torrent").

The term rōstāg, from Middle Iranian, means "district", making it a compound etymology derived from the words for "river."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:31:20.221Z] TOOL RESULT

```
Web search results for query: "Avestan "huraoδa-" OR "huraoδa" "wohlgewachsen" OR "well-grown" OR "well-shaped" Yasht Bartholomae 1494"

Links: [{"title":"BARTHOLOMAE, CHRISTIAN - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/bartholomae-christian-german/"},{"title":"Avesta | Encyclopedia MDPI","url":"https://encyclopedia.pub/entry/35018"},{"title":"AVESTA: YASNA: (English)","url":"https://www.avesta.org/yasna/"},{"title":"Books on Avestan (Avesta) Language","url":"https://www.avesta.org/abooks.html"},{"title":"Hordad Yasht","url":"https://en.wikipedia.org/wiki/Hordad_Yasht"},{"title":"Ardwahisht Yasht","url":"https://en.wikipedia.org/wiki/Ardwahisht_Yasht"},{"title":"Hom Yasht","url":"https://en.wikipedia.org/wiki/Hom_Yasht"},{"title":"Xwarshed Yasht","url":"https://en.wikipedia.org/wiki/Xwarshed_Yasht"},{"title":"ARD YAŠT - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/ard-yast-middle-persian-name-of-the-avestan-hymn-yast-17-dedicated-to-asi-q/"}]

The search results provide information about Bartholomae's scholarly work on Avestan texts and various Yashts, but do not contain specific information about the term "huraoδa" or its translation as "wohlgewachsen" (well-grown) or "well-shaped," nor do they reference page 1494 of any of Bartholomae's works.

The results confirm that Christian Bartholomae published the Altiranisches Wörterbuch (1904) with a supplementary volume (1906), which is a major lexicographical resource for Old Iranian languages including Avestan. However, the specific entry or passage you're seeking is not visible in these search results.

To find the specific reference you're looking for, you would need to access Bartholomae's Altiranisches Wörterbuch directly, or consult specialized academic databases focused on Avestan linguistics and Zoroastrian studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:31:26.652Z] TOOL RESULT

```
Web search results for query: "Jeffery "Foreign Vocabulary of the Qur'an" hur houris "hurust" OR "well grown" Pahlavi Tisdall"

Links: [{"title":"Amazon.com: The Foreign Vocabulary of the Qur'an (Texts and Studies on the Quran, 3): 9789004153523: Jeffery, Arthur, Bowering, Gerhard, McAuliffe, Jane Dammen: Books","url":"https://www.amazon.com/Foreign-Vocabulary-Quran-Texts-Studies/dp/9004153527"},{"title":"(PDF) THE FOREIGN VOCABULARY OF THE QUR\"$N","url":"https://www.academia.edu/24498113/THE_FOREIGN_VOCABULARY_OF_THE_QUR_N"},{"title":"The Foreign Vocabulary of the Qur'an - Arthur Jeffery - Google Books","url":"https://books.google.com/books/about/The_Foreign_Vocabulary_of_the_Qur_an.html?id=YTg4bdQSeLQC"},{"title":"The Foreign Vocabulary of the Qur'an (Arthur JEFFERY) – Quran and Early Islam","url":"https://www.quran-earlyislam.com/The-Foreign-Vocabulary-of-the-Qur"},{"title":"The Foreign Vocabulary of the Qur'an","url":"https://www.answering-islam.org/Books/Jeffery/Vocabulary/index.htm"},{"title":"FOREIGN VOCABULARY OF THE QUR'AN","url":"https://www.answering-islam.org/Books/Jeffery/Vocabulary/pref.htm"},{"title":"Arthur Jeffery: The foreign vocabulary of the Qur'an-BRILL (2007) - Flipbook by Miftahul Akhirat | FlipHTML5","url":"https://fliphtml5.com/maqrd/cfnd/Arthur_Jeffery:_The_foreign_vocabulary_of_the_Qur&"},{"title":"Arthur Jeffery","url":"https://en.wikipedia.org/wiki/Arthur_Jeffery"},{"title":"THE FOREIGN VOCABULARY OF THE QUR\"$N","url":"http://islam-and-muslims.com/Foreign-Vocabulary-of-Quran.pdf"}]

I found results confirming Arthur Jeffery's work on "The Foreign Vocabulary of the Qur'an" and references to Tisdall and Pahlavi sources. Now let me search more specifically for the terms you mentioned - "hur," "houris," "hurust," and "well grown."

Links: [{"title":"Understanding Hur and Houris in Islam | PDF | Islamic Texts | Abrahamic Religions","url":"https://www.scribd.com/document/612333241/al-hur"},{"title":"Houri | Encyclopedia.com","url":"https://www.encyclopedia.com/philosophy-and-religion/islam/islam/houri"},{"title":"Houri - New World Encyclopedia","url":"https://www.newworldencyclopedia.org/entry/Houri"},{"title":"houri - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/houri"},{"title":"Houris in Islam | Definition, Descriptions & References | Study.com","url":"https://study.com/academy/lesson/houri-overview-descriptions-reference-islam.html"},{"title":"“HOURIS (HOOR)” IN PARADISE - Islam and the Quran","url":"https://www.islamandquran.org/research/houris-in-paradise.html"},{"title":"Houri - Definition, Meaning & Synonyms | Vocabulary.com","url":"https://www.vocabulary.com/dictionary/houri"},{"title":"Hur","url":"https://en.wikipedia.org/wiki/Hur"},{"title":"Houri","url":"https://en.wikipedia.org/wiki/Houri"}]

Perfect! I found exactly what you were looking for. Here are the results of my web search:

## Search Results

I found comprehensive information about Arthur Jeffery's "Foreign Vocabulary of the Qur'an" and the etymology of "houri."

**About Jeffery's Work:**
Arthur Jeffery's "The Foreign Vocabulary of the Qur'an" traces the origins of 318 foreign (non-Arabic) words found in the Qur'an. This important study offers scholars access to a foundational text arranged in Arabic alphabetical order, with Jeffery's compendium of philological scholarship remaining an indispensable tool for any serious study of Qur'anic semantics.

**Regarding the Etymology of "Houri":**
Arthur Jeffery and other scholars suggest an Iranian origin for the term, proposing the origins of the word to be the Middle Persian hū̆rust 'well grown'.

**Tisdall's Work:**
The bibliography of Jeffery's work includes W. St. C. Tisdall's "The Original Sources of the Qurān" from London, 1911. Additionally, E. W. West's "Glossary and Index of Pahlavi Texts" from Bombay, 1874 is cited in Jeffery's bibliographical references.

This confirms the scholarly connection between Jeffery's etymological work, Tisdall's research on Qur'anic sources, and Pahlavi (Middle Persian) language studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:31:33.646Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.answering-islam.org/Books/Jeffery/Vocabulary/index.htm",
 "prompt": "List the links/pages for the letter ح (h with dot) entries, and specifically find any link or text for the entry ḥūr / حور (houris). Give URLs."
}
```


## [2026-09-04T14:31:34.705Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Rostaq",
 "prompt": "Quote in full what the article says about the etymology of rōstāg / rostaq (rautah-, raudah-, *raudas-tāka-, -tāg, tač-), including any scholars cited."
}
```


### [2026-09-04T14:31:39.895Z] TOOL RESULT

```
# Response

The webpage provided does not contain any information about the etymology of "rōstāg," "rostaq," or related terms (rautah-, raudah-, *raudas-tāka-, -tāg, tač-). 

This is a disambiguation page that simply lists various geographical locations sharing the name "Rostaq" across Afghanistan, Iran, and Oman. It includes only the Persian rendering (رستاق) without etymological discussion or scholarly citations regarding the term's linguistic origins.
```


### [2026-09-04T14:31:40.036Z] TOOL RESULT

```
Based on the web page content provided, I can identify entries beginning with ح (h with dot):

**Listed entries:**
- Habl
- Hizb
- Hasada
- Hisn
- Hitta
- Hikma
- Hanan
- Hanif
- Hawariyun
- Hub
- Hur
- Harut wa Marut
- Harun
- Haman
- Hawiya

**Regarding ḥūr (houris):**
The entry "Hur" appears in the list under Part 9. However, the page content shows only a table of contents with linked entry names, not the actual articles themselves. The specific URL for the "Hur" entry would follow the pattern of other entries linking to the part pages (Part 1-25), but the exact dedicated URL for this individual entry is not displayed in this index content.

To access the full entry on "Hur," you would navigate to [Part 9](part9.htm) of the work, where it is listed among the entries for that section.
```


## [2026-09-04T14:31:43.774Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.answering-islam.org/Books/Jeffery/Vocabulary/part9.htm",
 "prompt": "Quote in full the entry for Hur (حور, houris): what Arabic philologists said, the Pahlavi/Persian derivation (hurust 'well grown'?), and Jeffery's own conclusion."
}
```


## [2026-09-04T14:31:44.692Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Rustak",
 "prompt": "Quote in full what the article says about the etymology of rōstāg / rustaq (rautah-, raudah-, *raudas-tāka-, -tāg, tač-), including any scholars cited."
}
```


### [2026-09-04T14:31:47.650Z] TOOL RESULT

```
I appreciate your request, but I cannot provide the full entry for Hur from this source material. The web page content you've provided shows only image filenames (128.jpg through 137.jpg) and navigation links—the actual text of the scholarly entries is not included in the transcribed content.

To access the specific information about what Arabic philologists said regarding Hur, the proposed Pahlavi/Persian derivation, and Jeffery's conclusions, you would need to view the actual images or consult the original book directly.

If you can provide the text content from those pages, I'd be happy to help extract and format the relevant information according to your specifications.
```


### [2026-09-04T14:31:50.953Z] TOOL RESULT

```
# Etymology of Rustaq

According to the article's Etymology section, the name derives from Middle Iranian **_rōstāg_**, meaning "district." The article states:

> "The name of this town is a derived from the Middle Iranian _rōstāg_, meaning 'district'"

It also notes the term appears in related languages including Baluchi, Persian, and Kumzari. Additionally, the New Iranian cognate is **_rusta_**, signifying a 'large village.'

The article identifies D. N. Mackenzie's *Concise Pahlavi Dictionary* and John Everett-Heath's *The Concise Oxford Dictionary of World Place Names* as sources. It further notes Indo-European parallels, mentioning Latin *'rustica'* shares the same meaning, which influenced the English word "rustic."
```


## [2026-09-04T14:33:06.941Z] TOOL CALL #69: WebSearch

```json
{
 "query": "\"huraoδa\" Avestan"
}
```


## [2026-09-04T14:33:08.110Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://quizlet.com/274698526/young-avestan_skjaervo-3-6-flash-cards/",
 "prompt": "Quote the flashcard(s) containing huraoδa (meaning) and any others with raoδa-, hu-."
}
```


### [2026-09-04T14:33:11.108Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:33:12.545Z] TOOL RESULT

```
Web search results for query: ""huraoδa" Avestan"

Links: [{"title":"Young Avestan_Skjærvø 3-6 Flashcards | Quizlet","url":"https://quizlet.com/274698526/young-avestan_skjaervo-3-6-flash-cards/"},{"title":"TITUS Texts: Avestan Corpus: Monna's Text","url":"http://titus.uni-frankfurt.de/texte/etcs/iran/airan/avesta/yasna/yasnmn/yasnm058.htm"},{"title":"TITUS Texts: Avestan Corpus: Insler's Text (O)","url":"https://titus.uni-frankfurt.de/texte/etcs/iran/airan/avesta/yasna/yasnino/yasni011.htm"},{"title":"Avesta/Vidēvdād - Wikisource","url":"https://wikisource.org/wiki/Avesta/Vid%C4%93vd%C4%81d"},{"title":"Ashi","url":"https://en.wikipedia.org/wiki/Ashi"},{"title":"SRAOŠA - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/sraosa/"},{"title":"Avestan","url":"https://en.wikipedia.org/wiki/Avestan"},{"title":"Avestan alphabet and language","url":"https://www.omniglot.com/writing/avestan.htm"}]

Based on the web search results, I can provide you with information about "huraoδa" in Avestan:

Huraoδa is an Avestan adjective meaning "well-shaped." 

The word appears in various Avestan texts, including the Yasna and Vidēvdād portions of the Avesta. In particular, it is used to describe the outward appearance of Sraoša (a significant figure in Zoroastrianism) as "handsome."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:33:18.136Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/sraosa/",
 "prompt": "Quote the passage mentioning the epithet huraoδa- ('well-shaped', 'handsome') of Sraoša and any other Avestan epithets listed there."
}
```


## [2026-09-04T14:33:18.802Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://wikisource.org/wiki/Avesta/Vid%C4%93vd%C4%81d",
 "prompt": "Find any occurrence of the word huraoδa / huraoδō / huraoδahe in the text and quote the sentence with its chapter and verse number."
}
```


### [2026-09-04T14:33:19.800Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:33:24.758Z] TOOL RESULT

```
I found one occurrence of a form of "huraoδa" in the text:

**Vd. 3.24.e**: "iδa. carāiti. huraoδa."

This appears in the context of describing paths or ways related to religious practice in the Avestan text.
```


## [2026-09-04T14:35:29.738Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-311.json <<'EOF'\n{\n  \"pdf_page\": 311,\n  \"book_page\": 281,\n  \"verified_by\": \"claude-fable-5-1\",\n  \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Leudh, Rei\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *h₁lewdʰ- 'to grow, rise; (hence) offspring, people' (Pokorny 684-685 leudh-; LIV 248 *h₁leudʰ-; AHD leudh-)\",\n      \"note\": \"Pokorny 684-685 leudh- 'emporwachsen, hochkommen' with the derivatives leudho-/leudhi- 'Nachwuchs, Volk' and leudhero- 'zum Volk gehörig, frei' (Av. raoδaiti 'grows', raoδa- 'Wuchs, Ansehen', Lat. līber, OHG liut, OCS ljudьje) is exactly Nourai's root; Cheung 2007:193 gives the Iranian reflex *Hraud 'to grow (bigger)' and LIV *h₁leudʰ-. The Iranian r- is the regular Proto-Iranian merger of PIE *l with *r, not a separate root: the label 'Rei' has no counterpart in Pokorny/AHD and is unexplained (possibly Nourai's cross-reference label). Two branches of the chart are not from this root at all: the Arabic loans rawḍa (#4) and ḥūr (#15) are native Semitic, Arabic rawnaq (#7) is native Arabic, and rōstāg/Rostam (#9, #11) are today derived from the 'river' word (*srew-), not from 'grow'. The chart's own NOTE on #4 (AFM derives rawḍa from rīxtan, VDQ from rōt) records alternative Persian etymologies that modern lexicography rejects as well.\",\n      \"sources\": [\n        \"https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h₁lewdʰ-\",\n        \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\",\n        \"https://www.ahdictionary.com/word/search.html?q=liberty\"\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"raod 1, raoda, raodha\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan verb raoδ- (raoδaiti 'grows', Vd 5.19; raoδahe Y 10.4; past participle urusta-/rusta- 'grown') and the nouns raoδa- m. 'growth, stature, appearance' (Pokorny: 'Wuchs, Ansehen') and raoδah- n. 'growth' are the direct Iranian reflexes of PIE *h₁lewdʰ-: PIE *l > Proto-Iranian *r, *ew > ao, *dʰ > δ. The sense 'face' is a secondary development of 'appearance, outward form' (Wiktionary روی: Proto-Iranian *rauda- 'appearance' < 'growth'). Nourai's cited KLN/SYN are consistent with Pokorny 684, which is the standard treatment.\",\n          \"sources\": [\n            \"https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181\",\n            \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C\"\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"rŭy-îdan; rŭy 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av./Old Iranian raoδ- → Middle Persian present stem rōy- (Manichaean rwy-, Pahlavi lwd- /rōy-/, 3sg rōyēd) with past participle rust (rwst/lwst), Parthian rwd-/rwst → New Persian rustan/rōy- and the regularized infinitive rōyīdan 'to grow' (Cheung 2007:193; Wiktionary: Proto-Iranian *Hráwdah). Old Iranian intervocalic -d- > MP -y- (raoδa- > rōy) explains the y of rōy-/rūyīdan, while the participle keeps -st- (rust-, rustan). The noun rūy 'face' is MP rōy 'face' < Proto-Iranian *rauda- 'growth, appearance' (Edelman ESIJ 6:402; Cheung 193), the same word: 'growth, stature' → 'appearance' → 'face'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%86\",\n            \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\"\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"raz\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Persian raz 'vine, vineyard' (with the compounds razbān 'vine-keeper', razbun 'vine-stock') is a real word continuing Middle Persian raz (Pahlavi lc /raz/), but no modern source derives it from the root 'to grow': there is no Old Iranian *raza- 'growth', and rūy-/rust- could not yield a form with -z-. Wiktionary and the Greek/Latin etymological literature group Persian raz with Ancient Greek ῥάξ (gen. ῥαγός) 'grape', Latin racēmus 'bunch of grapes', Albanian rrush 'grape' as a Mediterranean/Near-Eastern culture Wanderwort of unknown (substrate) origin; the connection with 'grow' in Borhān-e Qāṭeʿ (BQT) and FSF is folk etymology.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%E1%BF%A5%CE%AC%CE%BE\",\n            \"https://www.etymonline.com/word/raisin\"\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Arabic\",\n          \"words\": \"rauza\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic rawḍa (رَوْضَة) 'garden, meadow' (Qurʾān 30:15 fī rawḍatin), pl. riyāḍ, is a native formation from the Semitic root r-w-ḍ (rāḍa 'to train, tame', rawḍa 'meadow where water collects'); it has the emphatic ḍ, which never arises in Arabic renderings of Persian z (Persian raz would give *rawz/rāz, not rawḍ-). Wiktionary and Wehr treat it as Arabic with no Persian source; Persian rowze is listed only as a descendant. Nourai's PLA:138 derivation from raz, and the alternatives his NOTE records (AFM/Addai Sher from rīxtan 'to pour'; VDQ/Jeffery from Pahlavi rōt 'river'), are all unsupported by modern lexicography; the whole sub-branch #3 → #4 → #5 does not belong to *leudh-.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9\",\n            \"https://en.wikipedia.org/wiki/Rauza\"\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"rowzeh\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge as drawn is correct: Persian rowze «روضه» 'garden; shrine garden' is borrowed from Arabic rawḍa (Arabic ḍ rendered as Persian z, tāʾ marbūṭa as -e/-eh; Saʿdī's رَوْضَهٔ رِضْوان 'garden of Paradise' shows the classical sense), and riyāḍ «ریاض» is the Arabic broken plural. The later Shiʿi sense 'Karbalā elegy' comes from Kāshefī's Rowżat al-shohadāʾ (15th c.). Only the ancestry above #4 is wrong: the word is Semitic, not Indo-European.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B6%D8%A9\"\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"rŭnîk\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"rū-nīk «رونیک», glossed 'beautiful' and equated by the chart with nīk-rūy «نیکروی» 'fair-faced', is a transparent compound of rūy 'face' (#2, < MP rōy < Proto-Iranian *rauda- 'appearance') + nīk 'good' (Nourai's cross-reference Nei 1). Nourai gives no reference for it; I found it only in modern online Persian dictionaries (vajehyab: 'نیک رو، خوش رو، زیبارو') and as the modern given name Rūnīkā, while nīk-rūy itself is in Dehkhoda. The word is morphologically sound and its first element does belong to this root, but I could not verify a classical attestation of rūnīk, and the claim that it is the source of Arabic rawnaq (#7) is rejected below.\",\n          \"sources\": [\n            \"https://vajehyab.com/?q=%D8%B1%D9%88%D9%86%DB%8C%DA%A9\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%DB%8C\"\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Arabic\",\n          \"words\": \"raonaq\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic rawnaq (رَوْنَق) 'beauty, splendour, lustre, radiance' is treated by Wiktionary (citing Wehr and al-Maʿānī) as a native Arabic noun of the root r-n-q (cf. rāniq 'clear, limpid (water)', ranaqa/tarawnaqa 'to be clear, glisten'), of the fawʿal pattern; Persian rownaq is listed as borrowed from it. The Persian source rū-nīk proposed by Nourai (after AFM:74 = Addai Sher, al-Alfāẓ al-fārisiyya al-muʿarraba, 1908, many of whose derivations are no longer accepted) would require the unexplained loss of -y- and an irregular k > q; no modern dictionary follows it.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82\",\n            \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A5%8C%E0%A4%A8%E0%A4%95%E0%A5%BC\"\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"rownaq\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge is correct: Classical Persian rownaq «رونق» 'splendour; flourishing, boom, heyday' is a straightforward loan of Arabic rawnaq (Wiktionary: 'Borrowed from Arabic رَوْنَق'), the Arabic diphthong aw being kept as Persian ow; the meaning 'growth, success' is a Persian semantic extension, and the word spread on from Persian to Urdu/Hindi raunaq, Chagatai and Kurdish. The ancestry drawn above #7 (Persian rūnīk) is not accepted: the word is Arabic in origin.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D9%86%D9%82\"\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"rôstâk\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Middle Persian rōstāg (Pahlavi lwstʾk') 'district, province, rural district' (MacKenzie, Concise Pahlavi Dictionary) is a real word and the source of Arabic rustāq, Syriac rustāqā and Old Armenian ṙotastak (from a Parthian *rōdastāg). Its etymology, however, is a compound *raudas-tāka-/*rautas-tāka- 'river-course, river-district' of Old Iranian rautah-/raudah- 'river' (OP rautah-, MP rōd, NP rūd < Proto-Iranian *hrautah- < PIE *srew- 'to flow') + -tāka- 'course, run' (root tak-/tač- 'to run, flow'; cf. Bactrian tago 'river valley'): rōd + tāg > rōstāg with regular devoicing of the cluster. The Parthian form rōdastāg with -d- shows the 'river' word plainly. Nothing connects it to 'grow' (*leudh-); Wiktionary leaves the deeper etymology open but gives no 'grow' derivation.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B3%D8%AA%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D9%82\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\",\n            \"https://en.wikipedia.org/wiki/Rustak\",\n            \"https://forum.wordreference.com/threads/persian-rustaki-and-latin-rusticus-rustic.3399756/\"\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"rŭstâ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge is correct: MP rōstāg 'district' → Classical Persian rōstā(y) «روستا / روستای» 'countryside, village' with regular loss of the final -g of the MP -āg suffix (as in dānāg > dānā); the Arabic loan rustāq (with -q) and the by-form rostāq preserve the older shape. The semantic narrowing 'rural district' → 'village' is a Persian development. As noted at #9, the root is 'river' (*srew-), not 'grow'.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B3%D8%AA%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D8%A7%D9%82\"\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Avestan\",\n          \"words\": \"raodha-taxma\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"No such word occurs in the Avesta; Rostam is absent from the Avestan texts, and *Raoδas-taxma- is a scholarly reconstruction (Justi, Iranisches Namenbuch) behind Middle Persian Rōdstahm (lwtsthm), Sogdian Rwstmy and New Persian Rostam. The language label should therefore be 'Old Iranian (reconstructed)'. The standard modern analysis (Wiktionary, Iranica, Mayrhofer/Schmitt) reads the compound as *Rautas-/Raudas-taxma- 'strong as a river' or 'whose running is like a river's', i.e. first element Av. raoδah-/OP rautah- 'river' (< *srew- 'flow', the same word as in rōstāg #9) + taxma- 'strong, brave' (Nourai's cross-reference Tenk); the older reading 'grown strong' with raoδah- 'growth' is a minority interpretation not followed by current reference works.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85\",\n            \"https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/\",\n            \"https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%AF\"\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"Rostam\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The name does continue the reconstructed compound behind #11: Old Iranian *Raudas-/Rautas-taxma- → Middle Persian Rōdstahm (lwtsthm; Pahlavi stahm 'force, power' < taxma-) → New Persian Rostam «رستم» (Rustam), with -dst- > -st- and shortening of ō before the cluster; Sogdian Rwstmy shows the same contraction already in Middle Iranian. So the edge is right, but the first element is 'river', not 'growth' (see #11); Ferdowsī's rastam 'I escaped' (Shāhnāma, Rostam's caesarean birth) is a poetic folk etymology.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%D8%AA%D9%85\",\n            \"https://forum.wordreference.com/threads/persian-etymology-of-rostam.3387039/\"\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Avestan\",\n          \"words\": \"hava-rd\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"'hava-rd' is not a possible Avestan form; the book almost certainly printed hu-raodha (Av. huraoδa-), and the scan lost/garbled letters. Av. huraoδa- 'well-grown, well-shaped, handsome' is a real Young Avestan adjective (Vidēvdād 3.24 'iδa carāiti huraoδa'; epithet of Sraoša in Yasna 57), built from hu- 'good, well' (PIE *h₁su-; Nourai's cross-reference Su 1) + raoδa- 'growth, stature' (#1). Its meaning and root membership are exactly as glossed; only the transliteration is corrupt.\",\n          \"sources\": [\n            \"https://wikisource.org/wiki/Avesta/Vid%C4%93vd%C4%81d\",\n            \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\",\n            \"https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181\"\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"hu-rust\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian hurust 'well-grown, well-built, fine' = hu- 'well' + rust, the past participle of rōy-/rustan 'to grow' (Cheung 2007:193: BMP lwst /rust/, MMP rwst; the Iranian participle *Hrusta- is the analogical replacement of expected *Hruzda- < *Hrudʰ-ta-). It is thus the Middle Persian counterpart of Av. huraoδa- (#13), formed on the participle rather than on the noun raoδa-, but from the same root and with the same meaning. Jeffery cites this word as MP hū̆rust 'well grown'.\",\n          \"sources\": [\n            \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\",\n            \"https://en.wikipedia.org/wiki/Houri\"\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Arabic\",\n          \"words\": \"hŭr\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Arabic ḥūr (حُور), the plural of aḥwar (m.) / ḥawrāʾ (f.) 'having eyes with a strong contrast of white and black', in the Qurʾānic phrase ḥūrun ʿīnun (44:54, 52:20, 56:22) 'fair, large-eyed maidens', is a regular Arabic plural of the root ḥ-w-r 'to be white; whiteness of the eye' (Wiktionary, Wehr; cognate with Syriac ḥewwār 'white', Hebrew ḥiwwēr 'pale'). Standard lexica derive it inside Semitic. The Iranian etymology Nourai follows (VDQ:39 = the Persian translation of Jeffery, The Foreign Vocabulary of the Qurʾān, who after Tisdall suggested Pahlavi hurust 'well grown') is a minority hypothesis that would require an unexplained h > ḥ, loss of -st and reinterpretation as a plural; Wiktionary and Etymonline (houri: 'from Arabic haura, to be beautifully dark-eyed') do not accept it.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1\",\n            \"https://en.wiktionary.org/wiki/houri\",\n            \"https://www.etymonline.com/word/houri\",\n            \"https://en.wikipedia.org/wiki/Houri\"\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"hŭr 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge is correct: Classical Persian ḥūr «حور» 'houri, heavenly maiden' and the derivatives ḥūrī «حوری» (with the Persian relational/singulative -ī), ḥūr al-ʿayn «حورالعین» (the Qurʾānic phrase taken over as a unit) and ḥūr-vash «حوروش» 'houri-like' are borrowed from Arabic ḥūr; Persian ḥūrī is in turn the source of French/English houri (1650s/1737). Only the ancestry above #15 is wrong: the word is Semitic, not from hurust.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/houri\",\n            \"https://www.etymonline.com/word/houri\",\n            \"https://en.wiktionary.org/wiki/%D8%AD%D9%88%D8%B1\"\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"Sogdian\",\n          \"words\": \"rwd\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian rwδ- (rwtt, rwt 'grows'; inf. rwδʾy), Manichaean Sogdian preterite stem rws-, and the compound pati-: ptrwδ-/ptryst- 'to grow up', are listed by Cheung 2007:193 under Proto-Iranian *Hraud 'to grow (bigger)' beside Av. raoδ-, MP rōy-/rust, Parthian rwd-, Khotanese rrud-. Sogdian δ is the regular lenition of Old Iranian *d; Nourai's 'rwd' is the same word in a δ-less transliteration. (Homographic Sogdian rwδ 'copper' < *Hrawdʰas 'red' is a different word.)\",\n          \"sources\": [\n            \"https://archive.org/details/etymological-dictionary-of-the-iranian-verb\",\n            \"https://www.parsianjoman.org/wp-content/uploads/2016/04/Etymological-Dictionary-of-the-Iranian-Verb.pdf\"\n          ]\n        },\n        {\n          \"id\": 18,\n          \"lang\": \"Indo-European\",\n          \"words\": \"leudho; leudheros\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pokorny 684-685 lists exactly these derivatives: leudho-/leudhi- 'Nachwuchs, Volk' (OHG liut, OE lēod, German Leute, OCS ljudьje, Lith. liaudis 'people') and leudhero- 'zum Volk gehörig, frei' (Greek ἐλεύθερος, Latin līber); modern notation *h₁léwdʰ-o-, *h₁léwdʰ-ero-. The semantic path is 'growth' → 'offspring' → 'the people (born into the community)' → 'belonging to the people, free-born (as opposed to slave)'.\",\n          \"sources\": [\n            \"https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=%5Cdata%5Cie%5Cpokorny&first=1181\",\n            \"https://en.wiktionary.org/wiki/liber#Latin\",\n            \"https://www.etymonline.com/word/liberty\"\n          ]\n        },\n        {\n          \"id\": 19,\n          \"lang\": \"Latin\",\n          \"words\": \"liber\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"PIE *h₁léwdʰ-ero-s → Proto-Italic *louðeros → Old Latin loebesum/loebertatem (Festus; oe < *ou, intervocalic *dʰ > Italic *ð > Latin b) → Classical Latin līber 'free' (with the regular monophthongization oe > ī); de Vaan 2008:338. The same stem gives lībertās 'freedom', līberāre 'to free' and Līber (the god).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/liber#Latin\"\n          ]\n        },\n        {\n          \"id\": 20,\n          \"lang\": \"English\",\n          \"words\": \"liberty, deliver, Latvia\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"liberty: Latin lībertās (acc. lībertātem) → Old French liberte → Middle English liberte (late 14th c.) — confirmed. deliver: Latin līberāre 'to free' → Late Latin dēlīberāre 'to set free' → Old French delivrer → Middle English deliveren (c. 1200), later 'hand over' — confirmed (Etymonline, AHD leudh-). Latvia, however, has no connection to *leudh-: it is a 19th-century Latvian formation Latv-ija from the ethnonym latvis 'Lett', whose origin is unknown (Etymonline: 'of unknown origin'; Wiktionary: possibly from a river name Latava); neither Etymonline nor Wiktionary nor AHD links it to Latin līber or PIE *leudh-. Node verdict is 'disputed' because of Latvia only.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/liberty\",\n            \"https://www.etymonline.com/word/deliver\",\n            \"https://www.etymonline.com/word/Latvia\",\n            \"https://en.wiktionary.org/wiki/Latvia\"\n          ]\n        }\n      ]\n    }\n  ]\n}\nEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-311.json > /dev/null && echo VALID && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-311.json'))\nfrom collections import Counter\nc=Counter(n['verdict'] for e in d['entries'] for n in e['nodes']); print(c, len(d['entries'][0]['nodes']))\"",
 "description": "Write verification JSON for page 311 and validate"
}
```


### [2026-09-04T14:35:31.814Z] TOOL RESULT

```
VALID
Counter({'confirmed': 10, 'disputed': 7, 'plausible': 2, 'transcription_suspect': 1}) 20
```


## [2026-09-04T14:35:45.856Z] AGENT

Wrote `/home/sfmqrb/git/rishe/data/verification/page-311.json` (valid JSON, 1 entry, 20 nodes).

**Page 311 (book 281), root Leudh "to grow"** — root: confirmed (PIE *h₁lewdʰ-, Pokorny 684-5; the extra label "Rei" is unexplained). Nodes: 10 confirmed, 2 plausible, 7 disputed, 1 transcription_suspect.

- **disputed** — Persian *raz* «رز» 'vine': no link to 'grow'; a Mediterranean Wanderwort with Greek ῥάξ, Latin racēmus (Wiktionary).
- **disputed** — Arabic *rawḍa* 'garden': native Semitic root r-w-ḍ (Qurʾān 30:15); emphatic ḍ rules out Persian *raz*; the NOTE's rīxtan/rōt alternatives are also rejected.
- **disputed** — Arabic *rawnaq* 'splendour': native Arabic root r-n-q (Wiktionary/Wehr); Persian رونق is borrowed *from* Arabic, not the source (AFM/Addai Sher claim).
- **disputed** — Pahlavi *rōstāg* 'district': compound of rōd/raudah- 'river' (*srew-) + -tāg 'course'; not from 'grow'.
- **disputed** — Avestan "raodha-taxma": not attested in the Avesta; reconstructed *Rautas/Raudas-taxma- 'strong as a river' (MP Rōdstahm), first element 'river'.
- **disputed** — Arabic *ḥūr* 'houris': native root ḥ-w-r 'white(-eyed)'; the Pahlavi *hurust* source is a Tisdall/Jeffery minority hypothesis (Nourai's VDQ = Persian translation of Jeffery), not accepted by Wiktionary/Etymonline.
- **disputed** — English node "liberty, deliver, Latvia": liberty and deliver confirmed, but Latvia is of unknown origin (Etymonline/Wiktionary), unrelated to *leudh-.
- **transcription_suspect** — Avestan "hava-rd": impossible form; the book must have printed hu-raodha (Av. huraoδa- 'well-grown, well-shaped', Vd 3.24, Y 57), which does belong to this root.

Plausible: رونیک *rūnīk* (transparent rūy+nīk, but no classical attestation found) and *Rostam* (edge from the compound is right; only the 'growth' reading of the first element is outdated). Sogdian rwδ- 'to grow' confirmed via Cheung 2007:193.
