# Verification process log — verify-pages-101-345


## [2026-09-04T14:27:15.025Z] INPUT

Read the instructions in /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md and follow them exactly for PDF pages 101 and 345 (chart text: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-101.txt and page-345.txt; source JSON in /home/sfmqrb/git/rishe/data/extracted/batch/). Use WebFetch/WebSearch for sources. Write /home/sfmqrb/git/rishe/data/verification/page-101.json and page-345.json and reply with the short summary described in the instructions.


## [2026-09-04T14:27:17.940Z] TOOL CALL #1: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-04T14:27:17.953Z] TOOL RESULT

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


## [2026-09-04T14:27:18.697Z] TOOL CALL #2: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-101.txt"
}
```


### [2026-09-04T14:27:18.709Z] TOOL RESULT

```
1	=== PDF page 101 (book page 71) ===
2	--- entry 0 ---
3	ROOT [Semitic] B.r.k : originally "to kneel" used of the camel. Eventually the root developed the sense of "to bless".  (refs FVQ:75)
4	#1 (parent #0) [Arabic] refs=KLN:164; FVQ:75 | b.r.k : to bless ; barakat : blessing
5	  #2 (parent #1) [Persian] refs=FVA:45 | barekat «برکت» : blessing | extra: تبریک ، تبرّک ، مبارک
6	#3 (parent #0) [Akkadian] refs=KLN:164; AHD:579 | karâbu : to bless (letters are interchanged)
7	#4 (parent #0) [Hebrew] refs=KLN:164, 274 | berâkah : blessing ; kerŭbh : a winged angel (consonants R & B are reversed)
8	  #5 (parent #4) [Arabic] refs=MON:2958 | karŭbiyy : a winged angel
9	    #6 (parent #5) [Persian] refs=MON:2958 | karrŭbî «کرّوبی» : angel | extra: کروبیان، کروبیون
10	  #7 (parent #4) [English] refs=AHD:231 | cherub : a winged angel (of love)
11	  #8 (parent #4) [Greek] refs=AHD:579; KLN:680 | gruphos, grups : an eagle-headed lion
12	    #9 (parent #8) [Latin] refs=AHD:579 | gryphus
13	      #10 (parent #9) [Old French] refs=KLN:680 | grifion
14	        #11 (parent #10) [English] refs=AHD:579 | griffin
15	--- entry 1 ---
16	ROOT [Semitic] B.r.q : to shine  (refs KLN:514)
17	#1 (parent #0) [Arabic] refs=KLN:514 | b.r.q : to shine
18	  #2 (parent #1) [Persian] refs=FVA:45; SOR:35 | barq «برق» : lightning, electricity | extra: برّاق ، بارقه
19	#3 (parent #0) [Akkadian] refs=KLN:514 | baraqtu : lightning
20	#4 (parent #0) [Greek] refs=KLN:514 | smaraldos : a shiny stone, emerald
21	  #5 (parent #4) [Arabic] refs=MON:1746 | 
22	    #6 (parent #5) [Persian] refs=MON:1746; KLN:514 | zomorrod «زمرّد» : emerald
23	  #7 (parent #4) [Latin] refs=KLN:514 | smaragdus
24	    #8 (parent #7) [English] refs=AHD:427 | smaragdite : a green mineral
25	    #9 (parent #7) [Old French] refs=KLN:514 | esmeralde
26	      #10 (parent #9) [English] refs=AHD:427 | emerald
27	#11 (parent #0) [Sanskrit] refs=SKT:163; KLN:514 | marakata : emerald
28	
```


## [2026-09-04T14:27:19.434Z] TOOL CALL #3: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/charts/page-345.txt"
}
```


### [2026-09-04T14:27:19.467Z] TOOL RESULT

```
1	=== PDF page 345 (book page 315) ===
2	--- entry 0 ---
3	ROOT [Pahlavi] Murvârît : small pearl  (refs PLA:247; FVQ:261)
4	#1 (parent #0) [Persian] refs=BQT:1997; FVQ:261; KGW:112 | morvârîd «مروارید» : pearl | NOTE: BQT derives this word from Greek
5	#2 (parent #0) [Aramaic] refs=FVQ:261 | 
6	  #3 (parent #2) [Arabic] refs=FVQ:261; PLA:247 | mardjân : pearl, coral
7	    #4 (parent #3) [Persian] refs=BQT:1981 | marjân «مرجان» : coral
8	#5 (parent #0) [Greek] refs=AHD:1527; KGW:111; FVQ:261 | margarites : pearl
9	  #6 (parent #5) [Latin] refs=None | 
10	    #7 (parent #6) [Old French] refs=None | 
11	      #8 (parent #7) [English] refs=None | margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita
12	--- entry 1 ---
13	ROOT Mus -> redirect to Mu
14	--- entry 2 ---
15	ROOT [Arabic] M.v.t : to die  (refs FVA:384; KLN:946)
16	#1 (parent #0) [Arabic] refs=FVA:387 | maot : death
17	  #2 (parent #1) [Persian] refs=FVA:387; MON:3678,4421 | mawt, mowt «موت ( مَمات )» : death ; mayyet «میّت» : dead person ; mât «مات» : dead, dull, confused ; kîš-mât «کیش مات» : "king is dead", checkmate ☞Ksei 1
18	    #3 (parent #2) [Latin] refs=FSD:1526 | mattus : dull, dead | NOTE: POK:694 derives Latin "mattus" from Indo-European root "Mad: wet".
19	      #4 (parent #3) [French] refs=FSD:1526 | mat : dull
20	        #5 (parent #4) [English] refs=FSD:526 | mat 1 : dull | NOTE: AHD:805 derives English "mat" from root "Mad".
21	      #6 (parent #3) [French] refs=PHN:257; DEV:159 | mat : defeated ; e'chec et mat : checkmate | NOTE: "checkmate" reached Europe through debatable paths
22	        #7 (parent #6) [English] refs=LKT:115; KLN:946 | mate 2 : to overcome ; checkmate
23	#8 (parent #0) [Spanish] refs=KLN:946 | matar : to kill ; matador : (bull) killer
24	  #9 (parent #8) [French] refs=MON:3678 | matador
25	    #10 (parent #9) [Persian] refs=MON:3678 | mâtâdor «ماتادُر»
26	  #11 (parent #8) [English] refs=KLN:946 | matador
27	
```


## [2026-09-04T14:27:22.620Z] TOOL CALL #4: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T14:27:22.627Z] TOOL RESULT

```


```


## [2026-09-04T14:27:24.356Z] TOOL CALL #5: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-101.json; echo ----; cat /home/sfmqrb/git/rishe/data/extracted/batch/page-345.json; echo ----; ls /home/sfmqrb/git/rishe/data/verification/ | head -30",
 "description": "Show source JSON for pages 101 and 345 and list verification dir"
}
```


### [2026-09-04T14:27:24.417Z] TOOL RESULT

```
{
  "pdf_page": 101,
  "book_page": 71,
  "entries": [
    {
      "root": {
        "name": "B.r.k",
        "lang": "Semitic",
        "refs": "FVQ:75",
        "gloss": "originally \"to kneel\" used of the camel. Eventually the root developed the sense of \"to bless\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:164; FVQ:75",
          "words": [
            {
              "translit": "b.r.k",
              "gloss": "to bless",
              "script": null
            },
            {
              "translit": "barakat",
              "gloss": "blessing",
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
          "refs": "FVA:45",
          "words": [
            {
              "translit": "barekat",
              "gloss": "blessing",
              "script": "برکت"
            }
          ],
          "script_extra": "تبریک ، تبرّک ، مبارک",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "KLN:164; AHD:579",
          "words": [
            {
              "translit": "karâbu",
              "gloss": "to bless (letters are interchanged)",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:164, 274",
          "words": [
            {
              "translit": "berâkah",
              "gloss": "blessing",
              "script": null
            },
            {
              "translit": "kerŭbh",
              "gloss": "a winged angel (consonants R & B are reversed)",
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
          "lang": "Arabic",
          "refs": "MON:2958",
          "words": [
            {
              "translit": "karŭbiyy",
              "gloss": "a winged angel",
              "script": null
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
          "refs": "MON:2958",
          "words": [
            {
              "translit": "karrŭbî",
              "gloss": "angel",
              "script": "کرّوبی"
            }
          ],
          "script_extra": "کروبیان، کروبیون",
          "note": null,
          "quote": {
            "text": "به تهدید اگر برکشد تیغ حکم - بمانند کرّوبیان صمّ و بُکم",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:231",
          "words": [
            {
              "translit": "cherub",
              "gloss": "a winged angel (of love)",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "Greek",
          "refs": "AHD:579; KLN:680",
          "words": [
            {
              "translit": "gruphos, grups",
              "gloss": "an eagle-headed lion",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Latin",
          "refs": "AHD:579",
          "words": [
            {
              "translit": "gryphus",
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
          "parent": 9,
          "lang": "Old French",
          "refs": "KLN:680",
          "words": [
            {
              "translit": "grifion",
              "gloss": null,
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
          "refs": "AHD:579",
          "words": [
            {
              "translit": "griffin",
              "gloss": null,
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
        "name": "B.r.q",
        "lang": "Semitic",
        "refs": "KLN:514",
        "gloss": "to shine"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:514",
          "words": [
            {
              "translit": "b.r.q",
              "gloss": "to shine",
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
          "refs": "FVA:45; SOR:35",
          "words": [
            {
              "translit": "barq",
              "gloss": "lightning, electricity",
              "script": "برق"
            }
          ],
          "script_extra": "برّاق ، بارقه",
          "note": null,
          "quote": {
            "text": "چو برق درخشنده از تیره میغ - همی آتش افروخت از هر دو تیغ",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Akkadian",
          "refs": "KLN:514",
          "words": [
            {
              "translit": "baraqtu",
              "gloss": "lightning",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:514",
          "words": [
            {
              "translit": "smaraldos",
              "gloss": "a shiny stone, emerald",
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
          "lang": "Arabic",
          "refs": "MON:1746",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:1746; KLN:514",
          "words": [
            {
              "translit": "zomorrod",
              "gloss": "emerald",
              "script": "زمرّد"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "هرآنکه همچو زمرّد ز آب خود سبز است - نه شأن ابر شناسد نه شوکت دریا",
            "poet": null
          }
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Latin",
          "refs": "KLN:514",
          "words": [
            {
              "translit": "smaragdus",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:427",
          "words": [
            {
              "translit": "smaragdite",
              "gloss": "a green mineral",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Old French",
          "refs": "KLN:514",
          "words": [
            {
              "translit": "esmeralde",
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
          "parent": 9,
          "lang": "English",
          "refs": "AHD:427",
          "words": [
            {
              "translit": "emerald",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "SKT:163; KLN:514",
          "words": [
            {
              "translit": "marakata",
              "gloss": "emerald",
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
}----
{
  "pdf_page": 345,
  "book_page": 315,
  "entries": [
    {
      "root": {
        "name": "Murvârît",
        "lang": "Pahlavi",
        "refs": "PLA:247; FVQ:261",
        "gloss": "small pearl"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1997; FVQ:261; KGW:112",
          "words": [
            {
              "translit": "morvârîd",
              "gloss": "pearl",
              "script": "مروارید"
            }
          ],
          "script_extra": null,
          "note": "BQT derives this word from Greek",
          "quote": {
            "text": "زشوق لعل تو حافظ نوشت شعری چند - بخوان تو نظمش و در گوش کن چو مروارید",
            "poet": "Hâfez"
          }
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Aramaic",
          "refs": "FVQ:261",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "FVQ:261; PLA:247",
          "words": [
            {
              "translit": "mardjân",
              "gloss": "pearl, coral",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1981",
          "words": [
            {
              "translit": "marjân",
              "gloss": "coral",
              "script": "مرجان"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گوهر پاک بباید که شود قابل فیض - ورنه هر سنگ و گِلی لؤلؤ و مرجان نشود",
            "poet": "Hâfez"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1527; KGW:111; FVQ:261",
          "words": [
            {
              "translit": "margarites",
              "gloss": "pearl",
              "script": null
            }
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
          "lang": "Old French",
          "refs": null,
          "words": [],
          "script_extra": null,
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
              "translit": "margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita",
              "gloss": null,
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
        "name": "Mus",
        "redirect": "Mu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "M.v.t",
        "lang": "Arabic",
        "refs": "FVA:384; KLN:946",
        "gloss": "to die"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVA:387",
          "words": [
            {
              "translit": "maot",
              "gloss": "death",
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
          "refs": "FVA:387; MON:3678,4421",
          "words": [
            {
              "translit": "mawt, mowt",
              "gloss": "death",
              "script": "موت ( مَمات )"
            },
            {
              "translit": "mayyet",
              "gloss": "dead person",
              "script": "میّت"
            },
            {
              "translit": "mât",
              "gloss": "dead, dull, confused",
              "script": "مات"
            },
            {
              "translit": "kîš-mât",
              "gloss": "\"king is dead\", checkmate",
              "script": "کیش مات",
              "see": ["Ksei 1"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "من چو ابرم تو زمین موسیٰ نبات - حق شه شطرنج و ما ماتیم مات",
            "poet": "Molavî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Latin",
          "refs": "FSD:1526",
          "words": [
            {
              "translit": "mattus",
              "gloss": "dull, dead",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "POK:694 derives Latin \"mattus\" from Indo-European root \"Mad: wet\".",
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "French",
          "refs": "FSD:1526",
          "words": [
            {
              "translit": "mat",
              "gloss": "dull",
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
          "lang": "English",
          "refs": "FSD:526",
          "words": [
            {
              "translit": "mat 1",
              "gloss": "dull",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "AHD:805 derives English \"mat\" from root \"Mad\".",
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "French",
          "refs": "PHN:257; DEV:159",
          "words": [
            {
              "translit": "mat",
              "gloss": "defeated",
              "script": null
            },
            {
              "translit": "e'chec et mat",
              "gloss": "checkmate",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "\"checkmate\" reached Europe through debatable paths",
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "LKT:115; KLN:946",
          "words": [
            {
              "translit": "mate 2",
              "gloss": "to overcome",
              "script": null
            },
            {
              "translit": "checkmate",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Spanish",
          "refs": "KLN:946",
          "words": [
            {
              "translit": "matar",
              "gloss": "to kill",
              "script": null
            },
            {
              "translit": "matador",
              "gloss": "(bull) killer",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": "MON:3678",
          "words": [
            {
              "translit": "matador",
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
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:3678",
          "words": [
            {
              "translit": "mâtâdor",
              "gloss": null,
              "script": "ماتادُر"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:946",
          "words": [
            {
              "translit": "matador",
              "gloss": null,
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
----
```


## [2026-09-04T14:28:20.772Z] TOOL CALL #6: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/birk-",
 "prompt": "Give the etymology section in full, meaning, and the list of descendants (Arabic, Hebrew, Akkadian, Aramaic etc.) with their meanings. Also note anything on the 'to bless' sense relation to 'knee/kneel'."
}
```


## [2026-09-04T14:28:23.020Z] TOOL CALL #7: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%83%D8%A9",
 "prompt": "For the Arabic entry بركة: etymology, root, meaning, and descendants (Persian, Turkish etc.). Also any mention of the verb بَرَكَ 'to kneel (camel)' and بارك 'to bless'."
}
```


## [2026-09-04T14:28:24.625Z] TOOL CALL #8: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%A9%D8%AA",
 "prompt": "For the Persian entry برکت: etymology, meaning, related words (مبارک, تبریک, تبرک) and any cited references."
}
```


## [2026-09-04T14:28:26.021Z] TOOL CALL #9: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cherub",
 "prompt": "Give the full etymology text for cherub, including anything about Hebrew kerubh, Akkadian karabu/karibu, and any relation to 'bless' or 'griffin'."
}
```


## [2026-09-04T14:28:27.591Z] TOOL CALL #10: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/griffin",
 "prompt": "Give the full etymology text for griffin, including Greek, Latin, Old French forms and any Semitic/Hebrew kerubh suggestion (Klein)."
}
```


### [2026-09-04T14:28:28.691Z] TOOL RESULT

```
# Proto-Semitic *birk- Etymology and Descendants

## Etymology
The term is "often compared to Egyptian _bꜣk_ and to Cushitic forms such as Afar _gulúb_."

## Meaning
The root denotes "knee" and can function as either masculine or feminine gender.

## Notable Reconstruction Detail
In Common Semitic, a metathetic variant emerged, yielding *ruk(u)b-at- ("knee"), which produced forms like Arabic rukba. Both variants left traces across Arabic, Aramaic, and Ge'ez.

## Major Descendant Languages

**East Semitic:**
- Akkadian: birkum

**West Semitic (Arabic branch):**
- Arabic: rukba (via metathesis)
- Maltese: rkoppa, rkobba, rkippa

**West Semitic (Aramaic branch):**
- Jewish Aramaic: birkā
- Classical Syriac: burkā
- Assyrian Neo-Aramaic: birka

**West Semitic (Canaanite):**
- Hebrew: bérekh
- Ugaritic: brk

**Ethiopian Semitic:**
- Ge'ez: bərk
- Amharic: bərk
- Tigrinya: bərki

**Modern South Arabian:**
- Soqotri: bɛrk

**Note:** The page contains no explicit discussion linking "knee/kneel" semantically to "bless," though Hebrew bérekh ("knee") relates to related blessing terminology.
```


## [2026-09-04T14:28:29.088Z] TOOL CALL #11: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%9B%D7%A8%D7%95%D7%91",
 "prompt": "For the Hebrew entry כרוב (cherub): etymology in full (Akkadian karābu, kāribu, etc.), meaning, and descendants (Greek, Latin, Arabic كروبي etc.)."
}
```


### [2026-09-04T14:28:29.649Z] TOOL RESULT

```
# Summary of بركة (Baraka/Birka)

## Etymology and Root
The word derives from the Semitic root **ب ر ك** (b r k), which has 11 related Arabic terms.

## Primary Meanings

**Etymology 1** (baraka): "bliss, blessing, boon" - a spiritual concept of divine favor.

**Etymology 2** (birka): "pond, pool, tank, receptacle" - physical bodies of water.

**Etymology 3** (burka): An obsolete term for "a small white aquatic bird" or "mallard."

## Related Verb Forms
The entry mentions **بَرَكَ** (baraka) relating to "kneeling" - specifically the "mode of kneeling" for camels, with plural **بُرُوك** (burūk).

## Linguistic Descendants
The word spread widely through Persian, Turkish, and Ottoman channels, creating cognates in:
- Azerbaijani, Bengali, Gujarati, Hindustani
- Turkish, Albanian, Armenian, Bulgarian
- Romance languages (French, Spanish, Portuguese)
- Swahili, Hausa, Yoruba

This demonstrates how an Arabic religious/cultural concept traveled across multiple language families through trade and empire.
```


### [2026-09-04T14:28:30.366Z] TOOL RESULT

```
# برکت (Barkat) - Urdu Dictionary Entry

Based on the Wiktionary page, here's what the word means:

## Definition
The term refers to a "blessing" or "good fortune." The entry provides this example: "You receive blessings from doing good deeds."

## Etymology
The word originates from Classical Persian *barakat*, which itself derives from Arabic *baraka*.

## Linguistic Details
- **Part of speech:** Noun (feminine)
- **Pronunciation:** /bəɾ.kət̪/ in Standard Urdu
- **Plural forms:** برکتیں (barkatẽ) and برکتوں (barkatõ)

## Additional Information
Beyond its common noun usage, *barkat* also functions as a female given name in Urdu, derived from Arabic roots.

The entry notes a synonym: **نعمت** (nēmat), and lists antonyms including *baddu'ā* (curse) and *la'anat* (curse/damnation).
```


## [2026-09-04T14:28:31.341Z] TOOL CALL #12: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B3%CF%81%CF%8D%CF%88",
 "prompt": "For Ancient Greek γρύψ: full etymology (Beekes, Semitic/Hebrew kerub suggestions, Pre-Greek), meaning, and descendants (Latin gryps/gryphus, Old French, English griffin)."
}
```


### [2026-09-04T14:28:32.345Z] TOOL RESULT

```
# Etymology of Cherub

The word "cherub" entered English in the late 14th century as an order of angels, originating from Late Latin *cherub*, Greek *kheroub*, and Hebrew *kerubh* (plural *kerubhim*), meaning "winged angel."

According to Klein's theory, the Hebrew term may relate to Akkadian *karubu* ("to bless") and *karibu* ("one who blesses"), which was an epithet for the bull-colossus in ancient Near Eastern mythology.

However, alternative theories exist. As scholar Robert Alter explains, "The root of the terms either means 'hybrid' or, by an inversion of consonants, 'mount,' 'steed,' and they are winged beasts" associated with sky gods in Canaanite mythology and biblical poetry.

The term *griffin* shares a possible Semitic connection—Klein suggests it may derive from the same source as cherub through Hittite mediation, linking the Hebrew *kerubh* and Akkadian *karibu* to the griffin's mythological hybrid nature.

The modern sense of "beautiful child" (cherubs) developed much later, around 1705, distinctly separate from the original theological meaning of these powerful celestial guardians.
```


## [2026-09-04T14:28:33.607Z] TOOL CALL #13: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%B1%D9%88%D8%A8%D9%8A",
 "prompt": "For Arabic كروبي (karūbī): etymology (from Hebrew/Aramaic/Syriac?), meaning, plural forms كروبيون / كروبيين, and descendants (Persian, Turkish)."
}
```


### [2026-09-04T14:28:34.427Z] TOOL RESULT

```
# Full Etymology of Griffin

**Period of Origin:** c. 1200 (as a surname)

**Language Pathway:**
Old French _grifon_ → Late Latin _gryphus_ (misspelling of _grypus_) → Greek _gryps_

**Greek Root:** The Greek term literally meant "curved, hook-nosed," contrasting with _simos_. The word described both the legendary creature and its physical characteristic—the hooked beak.

**Mythological Description:** In Greek tradition, the griffin was "a fabulous bird of Greek mythology" combining "head and wings of an eagle, body and hind quarters of a lion," believed to inhabit Scythia where it guarded gold deposits.

**Semitic Connection:** Scholar Klein proposed a Semitic origin "through the medium of the Hittites," suggesting links to Hebrew _kerubh_ ("a winged angel") and Akkadian _karibu_ (an epithet for the bull-colossus). This theory connects griffin mythology to ancient Near Eastern winged guardian figures.

**Later Semantic Shifts:** By the mid-19th century, "griffin" acquired colloquial meanings in Louisiana (referring to mixed-race individuals) and British India (describing newly arrived Europeans), likely stemming from the concept of a "strange hybrid animal."
```


## [2026-09-04T14:28:35.087Z] TOOL CALL #14: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/kar%C4%81bu",
 "prompt": "For Akkadian karābu: meaning, etymology, root, related words (kāribu, kurību), and any relation to Hebrew כרוב cherub or to the root b-r-k 'bless'."
}
```


### [2026-09-04T14:28:36.035Z] TOOL RESULT

```
# כרוב (Kruv) - Hebrew Word Entry

This Wiktionary entry documents a Hebrew word with two distinct meanings:

## Etymology 1: Cabbage
The word derives from Ancient Greek *κράμβη* (krámbē, meaning "cabbage"). The noun **כְּרוּב** (kruv) is masculine, with plural form כְּרוּבִים. It has a derived term: כְּרוּבִית (kruvít).

## Etymology 2: Cherub/Griffin
This meaning originates from Proto-Semitic roots related to Akkadian terms meaning "to bless" or "one who blesses." The same masculine noun **כְּרוּב** (kruv) serves this definition, also pluralizing to כְּרוּבִים.

## Linguistic Significance
The second sense has influenced numerous languages. The entry notes descendants including Arabic كَرُوبِيّ (karūbiyy), Amharic ኪሩብ (kirub), and Greek χερούβ (kheroúb), which subsequently entered Latin as *cherūb* and spread throughout Romance and Germanic languages, including English "cherub."

The page was last updated January 7, 2025, and is categorized under vegetables, brassicas, and religious terminology.
```


### [2026-09-04T14:28:37.182Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:28:37.340Z] TOOL CALL #15: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Semitic/baraḳ-",
 "prompt": "Give the etymology, meaning ('lightning'), and the descendants list (Akkadian birqu/berqu, Arabic برق, Hebrew ברק, Aramaic, Ge'ez) with their meanings. Note any mention of emerald words (Akkadian barraqtu, Hebrew bareqet)."
}
```


### [2026-09-04T14:28:37.707Z] TOOL RESULT

```
# γρύψ (Ancient Greek Griffin)

**Meaning:** The Ancient Greek noun γρύψ (grū́ps) refers to a griffin, a legendary creature from mythology.

**Etymology:** The word's origin is debated. One theory links it to γρυπός (grūpós, "hook-nosed"), connected to Proto-Indo-European *ger- ("to turn, twist, bend"). However, scholars Beekes and Klein propose an alternative: the term may derive from a Pre-Greek substrate, possibly borrowed through Hittite or other Anatolian languages from Semitic sources like Akkadian karūbu and Hebrew kerúv, making it a doublet of χερούβ (kheroúb).

**Descendants:** The word evolved into:
- Modern Greek: γρύπας (grýpas)
- Latin: grȳps (with further descendants)
- Russian: грифо́н (grifón)

The term appears in ancient texts, including Herodotus's *Histories* and Aeschylus's *Prometheus Bound*.
```


### [2026-09-04T14:28:39.227Z] TOOL RESULT

```
# كروبي (Karūbī) - Dictionary Entry Summary

Based on the Wiktionary page, here's what this Arabic term represents:

## Definition
The word كروبي refers to an **archangel**, typically used in the phrase "الملائكة الكروبيون" (the archangels).

## Etymology
This Arabic noun was "Borrowed from Hebrew" כרוב, demonstrating linguistic exchange between Semitic languages.

## Grammatical Properties
- **Part of speech:** Noun (masculine)
- **Plural forms:** كروبيون (karūbiyyūn) - nominative; كروبيين (karūbiyyīn) - accusative/genitive
- **Feminine:** كروبية (karūbiyya)
- **Classification:** Relative noun (nisba) with triptote declension patterns

## Linguistic Categories
The entry categorizes it as an "Arabic terms borrowed from Hebrew" with detailed declension tables showing singular, dual, and plural variations across all Arabic grammatical cases (nominative, accusative, genitive).
```


## [2026-09-04T14:28:39.665Z] TOOL CALL #16: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%82",
 "prompt": "For Arabic برق and Persian برق entries: etymology, meanings (lightning, electricity), and derivatives (برّاق, بارقة). Note any references cited for Persian."
}
```


## [2026-09-04T14:28:42.651Z] TOOL CALL #17: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%83%CE%BC%CE%AC%CF%81%CE%B1%CE%B3%CE%B4%CE%BF%CF%82",
 "prompt": "For Ancient Greek σμάραγδος: full etymology (Semitic source? Akkadian barraqtu, Hebrew bareqet, Sanskrit marakata, Prakrit maragada, Beekes' view), meaning, variant μάραγδος, and descendants (Latin smaragdus, Arabic زمرد, Persian, Old French esmeralde/esmeraude, English emerald)."
}
```


### [2026-09-04T14:28:43.087Z] TOOL RESULT

```
# Proto-Semitic *baraḳ- (Lightning)

## Etymology
The term derives from Proto-Afroasiatic *bǐrk'-/*bǎrk'- meaning "to flash," with cognates in Egyptian brg/brk ("to give out light") and Proto-Cushitic *bark'-/*birk'- ("spark, flash").

## Meaning
**Lightning** – a masculine noun in Proto-Semitic.

## Major Descendants

**Akkadian:** birqum  
**Arabic:** برق (barq)  
**Hebrew:** ברק (barák)  
**Aramaic:** בַּרְקָא (barqā)  
**Ge'ez:** በርቅ (bärḳ)

The page notes that the Arabic form was "possibly formed as a deverbal noun rather than a true inheritance."

## Note on Related Terms
The Wiktionary entry does not mention emerald-related words like Akkadian barraqtu or Hebrew bareqet. Those terms, while potentially related etymologically through the "flashing/brightness" semantic domain, are not addressed in this reconstruction article.
```


## [2026-09-04T14:28:44.903Z] TOOL CALL #18: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%85%D8%B1%D8%AF",
 "prompt": "For Arabic زمرد and Persian زمرد entries: full etymology (route: Greek smaragdos > Syriac/Aramaic > Middle Persian > Arabic? or Greek > Arabic > Persian?), meanings, and cited references (Hasandust, Nourai, etc.). Also give Middle Persian form if given."
}
```


## [2026-09-04T14:28:46.402Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/emerald",
 "prompt": "Give the full etymology text for emerald: Old French forms, Latin smaragdus, Greek smaragdos, Semitic source (Akkadian barraqtu, Hebrew bareqeth), Sanskrit marakata, and any note on Persian zumurrud."
}
```


### [2026-09-04T14:28:47.195Z] TOOL RESULT

```
# برق (Barq) - Multilingual Dictionary Entry

## Etymology
The word برق originates from **Proto-Semitic *baraḳ-** meaning "lightning." In Arabic, it derives from the root ب ر ق (b r q). Persian borrowed the term directly from Arabic.

## Core Meanings

**Arabic & Related Dialects:**
- Lightning and atmospheric phenomena
- "to produce lightning" or "to shine, glitter, sparkle, flash"
- Telegraph (in modern usage)

**Persian:**
The term expanded semantically to include:
- Electricity
- Lightning
- Electric light (particularly in Dari)
- Brilliance, glint, flash, or sparkle
- Glaze or sheen

**Urdu:**
- Electricity (synonym: بجلی/bijlī)
- Lightning
- Adjective form: quick, active, brisk, alert

## Notable Derivatives
Persian derived terms include برقی (barqi - electric), برق‌کار (barq-kâr - electrician), and تیر برق (tir-e barq - electrical wire).

The Quranic reference (2:19-20) illustrates classical usage: "يَكَادُ ٱلْبَرْقُ يَخْطَفُ أَبْصَارَهُمْ" describing lightning's brilliant flashes.
```


## [2026-09-04T14:28:48.024Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%AE%E0%A4%B0%E0%A4%95%E0%A4%A4",
 "prompt": "For Sanskrit मरकत (marakata): etymology (from Semitic? Greek? Dravidian?), meaning, and descendants/related forms (Prakrit, Pali, Tamil, Greek)."
}
```


### [2026-09-04T14:28:49.742Z] TOOL RESULT

```
# σμάραγδος (Emerald)

**Definition:** The Ancient Greek word σμάραγδος refers to an "emerald," a precious gemstone.

**Etymology:** The term was "borrowed from a Semitic language, related to Hebrew בָּרֶקֶת (baréket, 'emerald, flashing gem')," along with Akkadian and Arabic cognates meaning "shining" or "flashing." The word also connects to Sanskrit मरकत (marakata) and Old Armenian զմրուխտ (zmruxt).

**Linguistic Features:** The noun could function as either feminine or masculine, though it was predominantly feminine during the Classical period before gradually becoming regularized to masculine during the Koine period.

**Historical Usage:** Marcus Aurelius employed this word in his *Meditations* (161-180 CE), writing metaphorically about maintaining one's character: "Whatever any one shall do or say, I cannot but be an emerald and keep my colour."

**Descendants:** The word's influence extended across numerous languages, including Latin (smaragdus), Romance languages like Spanish esmeralda and French émeraude, English emerald, and Persian/Arabic زمرد (zumurrud), which subsequently influenced South Asian, African, and East Asian languages.
```


## [2026-09-04T14:28:50.156Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF",
 "prompt": "For Persian مروارید: full etymology (Middle Persian murwārīd, Old Iranian reconstruction, relation to Greek margarites — which direction?), meaning, cited references, and descendants (Arabic, Turkish, etc.)."
}
```


### [2026-09-04T14:28:51.590Z] TOOL RESULT

```
# Summary of "زمرد" (Emerald) Etymology

## Core Definition
The word زمرد means **emerald** across Arabic, Persian, Pashto, and Urdu.

## Etymology Chain
According to the Wiktionary entry, the word traces back through these stages:

**Ancient Greek** → **Middle Persian** → **Persian/Arabic** → **Modern languages**

Specifically: The Greek term "σμάραγδος" (smáragdos) passed into Middle Persian as ʾwzmbwlt (uzumburd), which became Early New Persian ازمرد (uzmurud), and then evolved into the modern forms زمرد in Persian and Arabic.

## Language-Specific Details

- **Arabic**: Borrowed from Persian زمرد; classified as a masculine noun
- **Persian**: Described as inherited from Middle Persian; considered the source language for other borrowings
- **Pashto**: "Borrowed from Classical Persian"
- **Urdu**: "Borrowed from Classical Persian"

## Notable Feature
The entry notes that Arabic زمرد is "a doublet of زَبَرْجَد" (zabarjad, meaning peridot), suggesting alternate developments from the same root.

The word's descendants span across multiple language families, including Malay, Swahili, Turkish, Russian, and Chinese.
```


### [2026-09-04T14:28:52.409Z] TOOL RESULT

```
# Etymology of Emerald

Based on the Online Etymology Dictionary content provided, here's the etymological progression:

**Old French:** The word entered English around 1300 as "emeraude," derived from Old French "esmeraude" (12th century).

**Latin & Greek:** This came from Medieval Latin "esmaraldus," which traced back to Latin "smaragdus" and Greek "smaragdos," both meaning "green gem."

**Semitic Origin:** The ultimate source was Semitic "baraq," meaning "to shine." The entry notes Hebrew "bareqeth" (emerald) and Arabic "barq" (lightning) as related forms.

**Sanskrit & Persian:** Sanskrit "maragata" and Persian "zumurrud" both derive from the same Semitic root, with Persian forms subsequently influencing Turkish "zümrüd" and Russian "izumrud."

**Notable Caveat:** The source acknowledges that "the identity of which with our emerald is doubtful," noting that medieval references to the stone were often vague and based on classical descriptions rather than precise identification.

The entry also explains the unetymological "e-" prefix arose through Late Latin phonetic shifts affecting words beginning with "sc-" combinations.
```


## [2026-09-04T14:28:53.153Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82",
 "prompt": "For Ancient Greek μαργαρίτης: full etymology (Iranian/Persian source? Middle Persian murwārīd? Old Persian? Beekes' view), meaning, first attestation, and descendants (Latin margarita, Aramaic/Syriac marganita, Arabic مرجان, Old French, English Margaret/margarite)."
}
```


## [2026-09-04T14:28:54.655Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%B1%D8%AC%D8%A7%D9%86",
 "prompt": "For Arabic مرجان and Persian مرجان: full etymology (Aramaic/Syriac marganita > Arabic? from Greek margarites? Middle Persian?), meanings (pearl, coral), and cited references."
}
```


### [2026-09-04T14:28:54.846Z] TOOL RESULT

```
# मरकत (Marakata) - Etymology and Meaning

**Meaning:** The term मरकत means "emerald" in both Hindi and Sanskrit.

**Etymology:** According to the Wiktionary entry, the Sanskrit मरकत originates "from Semitic" languages. The document also notes a connection to "Ancient Greek σμάραγδος (smáragdos)," suggesting the word may have traveled through multiple linguistic traditions before reaching Sanskrit and its descendant languages.

**Key Descendants:**
The Sanskrit term evolved into numerous languages across Asia:
- Hindi: मरकत (markat)
- Tamil: மரகதம் (marakatam)
- Telugu: మరకతము (marakatamu)
- Thai: มรกต (mɔɔ-rá-gòt)
- Khmer: មរកត (mĕəʼrĕəʼkɑt)
- Tibetan: མར་གད (mar gad)

The word also appears in various Prakrit dialects, demonstrating its historical importance in Indo-Aryan linguistic development. The gemstone's name traveled alongside trade routes, reflecting the precious nature of emeralds in ancient commerce.
```


## [2026-09-04T14:28:56.154Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/margarine",
 "prompt": "Give the full etymology text for margarine (Chevreul, margaric acid, Greek margaron/margarites pearl) and, if on the page, related entries for Margaret and margarite."
}
```


### [2026-09-04T14:28:57.180Z] TOOL RESULT

```
# مروارید (Marvarid/Pearl)

## Meaning
The word مروارید means **pearl** or **margarite** in Persian and Ottoman Turkish.

## Etymology
According to the Wiktionary entry, the Persian term derives from "Middle Persian mwlwʾlyt' (morwārīd)" and traces back further to "Old Persian *margārīta-." Scholars propose it possibly originated from Proto-Iranian "*mŕ̥ga-ahri-ita-" meaning "oyster," literally "born from the shell of a bird," connected to the word for bird (*mr̥gáh).

## Historical Connections
The term shows related forms across multiple languages:
- **Parthian, Sogdian, Pashto, Khotanese** all have cognate versions
- **Greek μαργαρίτης (margarítēs)**, Armenian, and Georgian borrowings likely share the same Iranian root
- May connect to Sanskrit मञ्जरी (mañjarī)

## Modern Descendants
The word spread through languages that borrowed from Persian, including Azerbaijani, Turkish, Hindustani, Kazakh, and Tajik variants.

## Additional Use
Beyond the common noun, **مروارید** also functions as a female given name in Persian culture, with variants like Morvarid, Murwarid, and Murwareed.
```


## [2026-09-04T14:28:57.657Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Margaret",
 "prompt": "Give the full etymology text for Margaret, including Old French, Latin margarita, Greek margarites, Persian/Iranian source, and nicknames Maggie, Marjorie, Rita, Margarita."
}
```


## [2026-09-04T14:28:59.156Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mattus",
 "prompt": "For Latin mattus: full etymology (from *maditus / madeo? Pokorny mad-?), meaning, attestation, and descendants (French mat, Spanish matar?, Italian matto, English matte)."
}
```


### [2026-09-04T14:28:59.224Z] TOOL RESULT

```
# μαργαρίτης (margarite)

**Definition**: This Ancient Greek noun means "pearl" and also refers to a type of Egyptian plant whose exact nature remains uncertain.

**Etymology**: The word was borrowed from Indo-Iranian languages. According to linguistic scholar Beekes, it possibly derives from Proto-Iranian *mŕ̥ga-ahri-ita- (literally "born from the shell of a bird"), connecting it to words meaning "bird" across related languages like Avestan and Sanskrit.

**Language Connections**: The term appears related to Middle Persian forms and Persian مروارید (marvârid), as well as Sogdian and Sanskrit cognates, reflecting its journey through ancient trade routes and linguistic contact zones.

**Descendants**: The word's influence extended broadly:
- Modern Greek: μαργαρίτα (margaríta)
- Aramaic and Syriac: variants of marganita
- Latin: margarīta (which spawned numerous European descendants)
- English: margarite

**Grammatical Note**: In Ancient Greek, it functions as a masculine first-declension noun with the genitive form μαργαρίτου.
```


### [2026-09-04T14:29:00.315Z] TOOL RESULT

```
# Summary of مرجان (Marjān)

The word مرجان appears across multiple languages in this Wiktionary entry.

## Etymology

The term originates from **Classical Syriac** _margān_ ("pearl-like"), which derives from Syriac _margānīṯā_ ("pearl"). This traces back to **Ancient Greek** _margarítēs_ ("pearl"), identified as an Iranian language borrowing.

## Meanings

**Arabic**: The word denotes either "small pearls" or "corals" as a collective noun, with singular forms _marjāna_ or _murjāna_.

**Persian & Ottoman Turkish**: Both languages adopted the Arabic term to mean "coral" specifically.

## Descendants

The word spread widely across Turkic languages (Turkish, Kazakh, Tatar, Uyghur), Caucasian languages (Georgian, Armenian), Balkan languages (Romanian, Macedonian), and East African languages (Swahili, Hausa).

## Notable Detail

In Persian, مرجان also serves as a female given name (Marjan), derived from the Arabic root.
```


## [2026-09-04T14:29:00.657Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/checkmate",
 "prompt": "Give the full etymology text for checkmate (Old French eschec mat, Arabic shah mat, Persian shah mat 'the king is dead / left helpless', discussion of whether mat is Arabic 'died' or Persian), and also the entry for 'mate (v.2)' if shown."
}
```


## [2026-09-04T14:29:02.155Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/matte",
 "prompt": "Give the full etymology text for matte / mat (adj. dull), including French mat, Old French mat 'beaten down, defeated', Latin mattus, and the alternative from chess 'mate'."
}
```


### [2026-09-04T14:29:02.377Z] TOOL RESULT

```
# Etymology of Margarine

**Margarine (1873):** A butter substitute, the term comes from French *margarine*, invented in 1869 by French scientist Hippolyte Mège-Mouries. It was "made in part from edible fats and oils."

**Margarin (1836):** The chemical precursor term, from French *margarine*, coined by chemist Michel Eugène Chevreul (1786-1889) in 1813. The term derives from *(acide) margarique* meaning "margaric (acid)," which is "literally 'pearly,' from Greek *margaritēs* 'pearl'." The substance was named for "the luster of the crystals."

## Related Entries

**Margaret:** The page references this entry as etymologically connected through the Greek root meaning "pearl."

**Margarite:** Listed in nearby dictionary entries but full etymology not provided on this page.

The entire chain traces back to Greek *margaritēs* (pearl), reflecting the crystalline appearance of the original fatty substance Chevreul isolated and named.
```


## [2026-09-04T14:29:04.428Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/matar",
 "prompt": "For Spanish matar (and Portuguese/Catalan if present): full etymology (Vulgar Latin *mattare from mattus? Arabic/Persian mat 'checkmate'? Latin mactare?), meaning, and derivatives (matador)."
}
```


### [2026-09-04T14:29:04.632Z] TOOL RESULT

```
# Etymology of Margaret

**Origin Path:**
The name Margaret traveled from Oriental languages into English through multiple linguistic layers. It entered English around 1300 via Old French *Margaret* (French *Marguerite*), derived from Late Latin *Margarita*, which literally means "pearl."

**Greek Foundation:**
The Greek source is *margaritēs (lithos)*, meaning "pearl," though "its origin is unknown." Scholars propose the word came "from some Oriental language," most likely Iranian sources.

**Eastern Sources:**
The most credible theory traces it to Middle Persian *marvarit* meaning "pearl." An alternative suggestion points to Sanskrit *manjari* ("pearl; flowering bead"), though linguists note "the late and rare occurrence" makes direct connection uncertain. Iranian *mrga-ahri-ita-* ("born from the shell of a bird," essentially "oyster") represents another proposed origin.

**Folk Etymology:**
Germanic languages altered the word through "folk-etymology," creating Old English *meregrot*, reinterpreted as "sea-pebble."

**Related Names:**
Common nicknames and variants include Maggie, Madge, Meg, Peggy, Gretchen (German diminutive), Margery, and Margarita. The daisy flower was "said to have been originally a pet form of Margaret."
```


### [2026-09-04T14:29:05.411Z] TOOL RESULT

```
# Summary of "mattus" from Wiktionary

**Latin Adjective**: *mattus* means "drunk" or "intoxicated."

**Etymology**: The word derives from the Proto-Indo-European root *meh₂d- ("wet"). It comes through Proto-Italic *madēō, then Latin *maditus, which syncopated and underwent assimilation to become *mattus. The original source is "madēre" ("be drunk, be wet").

**Related Languages**: Sanskrit मत्त (mattá, "drunk") shares a common ancestor with this Latin term.

**Descendants**: The word evolved into modern Romance languages:
- French: *mat*
- Italian: *matto*

**Declension**: It functions as a first/second-declension adjective with masculine, feminine, and neuter forms that vary by case and number.

**Pronunciation** (Classical Latin): \[ˈmat.tʊs\]

The entry also notes an alternative spelling *mātus* and lists *ēbrius* as a synonym meaning "drunk."
```


## [2026-09-04T14:29:06.657Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AA",
 "prompt": "For Arabic مات (verb 'to die') and Persian مات entries: etymology, meanings (Persian: dead, stunned, dull, checkmated), and the chess term شاه مات / کیش مات. Also Persian موت, میت if any info."
}
```


### [2026-09-04T14:29:07.286Z] TOOL RESULT

```
# Etymology of Checkmate

## Checkmate (noun)

The term originated in the mid-14th century from Old French *eschec mat* (Modern French *échec et mat*), with parallels in Spanish *jaque y mate* and Italian *scacco-matto*. All derive from Arabic *shah mat*, meaning "the king died."

However, scholars debate the ultimate origin. According to Barnhart, there may be a misinterpretation involved: "the regular evolution of this Latin base would have yielded *\*meitar* in Portuguese and *\*mechar* in Spanish" where Arabic *mata* ("he died") was confused with Persian *mat* ("be astonished"). If Persian is the true source, *shah mat* would literally translate to "the king is left helpless, the king is stumped" rather than "the king died."

## Mate (v.2)

This verb meaning "to checkmate" dates to around 1300. It derives from Old French *mater*, meaning "to checkmate, defeat, overcome," which comes from *mat* ("checkmated"). The figurative verbal form emerged in the late 14th century with the sense "to thwart, frustrate," while its chess-specific usage dates to 1789.
```


## [2026-09-04T14:29:07.715Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/matador",
 "prompt": "Give the full etymology text for matador (Spanish matar, Latin mactare / mattus, Arabic mata, Persian mat) and the direction of borrowing into English and French."
}
```


### [2026-09-04T14:29:08.496Z] TOOL RESULT

```
# Etymology of Matte (Adjective - Dull)

The word "matte" meaning lusterless or dull originated in the 1640s from French *mat*, derived from Old French *mat* signifying "beaten down, withered, afflicted, dejected; dull."

Two possible etymological paths exist:

**Latin Origin Theory:**
The Old French term may derive from Latin *mattus*, meaning "maudlin with drink," which itself comes from *madere* meaning "to be wet or sodden, be drunk." This traces back to the Proto-Indo-European root *\*mad-* signifying "to be wet, drip."

**Chess Origin Theory:**
Alternatively, the French word might represent a transferred usage from chess of *mater*, meaning "to checkmate, defeat," which originated from Arabic.

The standardized spelling "matte" was uncommon before the late 19th century and wasn't normalized until the mid-20th century. Earlier print dictionaries simply listed the word as "mat."
```


### [2026-09-04T14:29:11.646Z] TOOL RESULT

```
# Matar: Etymology and Meaning

## Primary Meaning
**Matar** is a verb meaning "to kill" across Spanish, Portuguese, Catalan, and related Romance languages.

## Etymology
The word's origin is debated. The most common scholarly view traces it to Latin *mactāre* through a Vulgar Latin root *mattāre*. However, alternative theories propose:

- Derivation from Late Latin *mattus* ("drunk, intoxicated"), related to *madidus*
- Possible influence from Arabic *māta* ("to die")

The documentation notes: "Most likely from Latin *mactāre* (through a Vulgar Latin root *\*mattāre*). Alternatively, possibly from Vulgar Latin \*_mattāre_, from Late Latin _mattus_ ('drunk, intoxicated')."

## Derived Terms
Related words include:
- *matador* (killer/bullfighter)
- *matadouro/matadoiro* (slaughterhouse)
- *matança* (killing/slaughter)

## Extended Meanings
In Portuguese, the verb carries figurative senses: to destroy, to satisfy a desire, to commit suicide (reflexive), or colloquially to skip class or solve a mystery.
```


### [2026-09-04T14:29:12.944Z] TOOL RESULT

```
# Summary of مات (māt)

## Arabic
The primary meaning is **"to die."** The word derives from Proto-Semitic *mawut- and appears across Semitic languages. In classical Arabic, it's a Form I hollow verb with regular conjugations. A secondary, archaic meaning refers to land becoming "empty or unoccupied."

## Persian
**مات** functions as an adjective meaning "amazed" or "astonished." The etymology is debated—some scholars link it to the Arabic verb for dying, while others connect it to Sanskrit roots meaning "traversed" or "measured."

## Chess Term
In both Ottoman Turkish and Persian, مات signifies **checkmate**. The famous Persian phrase **شاه مات** (literally "the king is amazed/dead") refers to this chess position. This likely influenced the Persian adjective's meaning of being stunned or defeated.

## Language Variants
The word appears across multiple Arabic dialects (Egyptian, Moroccan, North and South Levantine) consistently meaning "to die," plus loanwords in Baluchi and Malay spelling variants.
```


### [2026-09-04T14:29:13.631Z] TOOL RESULT

```
# Etymology of Matador

**Origin Path:** The word entered English from Spanish in the 1670s.

**Spanish Source:** Spanish *matador* derives from *matar* ("to kill"), whose ultimate origin remains uncertain.

**Competing Theories:**

1. **Latin hypothesis:** Possibly from Latin *mactāre* ("to kill," originally "to honor by sacrifice"), though phonetic evolution presents difficulties—expected forms would be *meitar* (Portuguese) and *mechar* (Spanish).

2. **Semitic hypothesis:** Alternatively, the source may be Arabic *mata* ("he died"), borrowed from Persian.

**Direction of Borrowing:** The term passed from Spanish into English and French during the late 17th century, as both languages adopted the Spanish term for the bull-fighter who kills the bull. The feminine form is *matadora*.

**Related Connection:** The same Arabic-Persian root (*mata*) appears in "checkmate," suggesting a shared etymological pathway through Mediterranean trade and cultural exchange.
```


## [2026-09-04T14:29:34.298Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%91%D7%A8%D7%9B%D7%94",
 "prompt": "For Hebrew ברכה (berakhah, blessing): etymology (root ב-ר-ך, relation to ברך 'knee', Proto-Semitic), meaning, and cognates (Arabic بركة, Akkadian karābu?). Note any statement on the semantic link kneel > bless or the metathesis with Akkadian karābu."
}
```


## [2026-09-04T14:29:35.028Z] TOOL CALL #33: WebSearch

```json
{
 "query": "Akkadian karābu \"to bless\" metathesis Hebrew barak b-r-k etymology cherub kāribu"
}
```


## [2026-09-04T14:29:38.022Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D9%88%D8%A8%DB%8C",
 "prompt": "For Persian کروبی (karrubi): etymology (from Arabic كروبي, ultimately Hebrew), meaning (cherub/angel), plurals کروبیان, کروبیون, and any cited references."
}
```


### [2026-09-04T14:29:40.174Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:29:40.280Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%DA%A9%D8%AA#Persian",
 "prompt": "Report ONLY the Persian section of this page (برکت barakat): its etymology (borrowed from Arabic بركة?), meaning, and derived/related terms; and any references cited there."
}
```


### [2026-09-04T14:29:40.348Z] TOOL RESULT

```
# ברכה (Blessing) - Etymology and Meaning

## Primary Meaning
The Hebrew word **ברכה** (b'rakhá) means "blessing" or "congratulation." It appears across Hebrew, Ladino, and Yiddish.

## Etymological Root
The term derives from the Semitic root **ב־ר־ך** (b-r-k), which connects to related languages. According to the source, it is "Cognate with Arabic _بَرَكَة_ (baraka)."

## Linguistic Connections
The word shares roots with the Hebrew verb **ברך** (berékh), meaning "to bless." The root is also found in Arabic cognates, suggesting ancient Semitic origins for this concept of blessing.

## Language Distribution
Beyond Hebrew, this word has traveled into multiple languages:
- **Yiddish**: brokhe (blessing)
- **Ladino**: berahá (blessing)
- **English**: bracha (borrowed form)
- **Dutch**: brooche (via Yiddish)

The word remains religiously and culturally significant across Jewish communities in its various linguistic forms.
```


## [2026-09-04T14:29:41.777Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/barraqtu",
 "prompt": "For Akkadian barraqtu: meaning (emerald?), etymology (from barāqu 'to flash'), and related forms (Hebrew bareqet, Greek smaragdos, Sanskrit marakata)."
}
```


### [2026-09-04T14:29:43.469Z] TOOL RESULT

```
Web search results for query: "Akkadian karābu "to bless" metathesis Hebrew barak b-r-k etymology cherub kāribu"

Links: [{"title":"Cherub | The War of the Sword Wiki | Fandom","url":"https://the-war-of-the-sword.fandom.com/wiki/Cherub"},{"title":"Balashon - Hebrew Language Detective: kruv","url":"https://www.balashon.com/2007/07/kruv.html"},{"title":"Cherubim | The amazing word Cherubim: meaning and etymology","url":"https://www.abarim-publications.com/Meaning/Cherubim.html"},{"title":"Cherub - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/cherub"},{"title":"Cherubim – DANTE SISOFO","url":"https://dantesisofo.com/cherubim/"},{"title":"Cherub","url":"https://en.wikipedia.org/wiki/Cherub"},{"title":"Semantics of Ancient Hebrew Database","url":"https://sahd-online.com/words/krub/"},{"title":"Cherubo - Name Meaning, Origin, Popularity, and Related ...","url":"https://name-doctor.com/meaning/cherubo"}]

Based on the search results, here's what scholars have found about the etymology you inquired about:

The Hebrew word for cherub (כְּרוּב kərūḇ) is likely borrowed from a derived form of Akkadian karābu "to bless," such as kāribu meaning "one who blesses".

Regarding the metathesis connection with Hebrew barak (ברך), Dhorme argues that ברך is clearly a derivative of karābu, with 'b' switching with 'k' by means of metathesis. This means the consonants k-r-b in Akkadian karābu were rearranged to b-r-k in the Hebrew barak, both sharing the semantic field of "blessing."

Kāribu is the present participle of the verb karābu and has the meaning "one who prays" or "intercessor". More broadly, kāribu (diminutive kurību) refers to intercessory beings and statues of such beings that plead with the gods on behalf of humanity, which fits well with the biblical cherubim's role as divine intermediaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:29:43.872Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:29:43.971Z] TOOL RESULT

```
# Persian Section Not Available

The Wiktionary page provided does not contain a Persian section for برکت (barakat). 

The page shows that this entry exists in 10 languages including Persian (فارسی), as indicated by the language links at the top. However, only the Urdu language section is displayed in the content you've shared.

To access the Persian definition, meaning, and related terms, you would need to visit the Persian Wiktionary directly via the link: https://fa.wiktionary.org/wiki/برکت
```


## [2026-09-04T14:29:44.033Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D7%91%D7%A8%D7%A7%D7%AA",
 "prompt": "For Hebrew בָּרֶקֶת (bareqet): meaning, etymology (root b-r-q 'flash', Akkadian barraqtu), Bible attestation (Exodus 28:17), and relation to Greek σμάραγδος / Sanskrit marakata."
}
```


## [2026-09-04T14:29:45.527Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/smaragdus",
 "prompt": "For Latin smaragdus: etymology, meaning, and full descendants list (Old French esmeralde/esmeraude, Spanish esmeralda, English emerald, smaragdite, Middle English, etc.) and the Medieval/Vulgar Latin forms (smaralda, esmaraldus)."
}
```


## [2026-09-04T14:29:47.025Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/smaragdite",
 "prompt": "For English smaragdite: etymology (from French smaragdite? Latin smaragdus + -ite, Saussure 1796?), meaning (green mineral, actinolite/amphibole variety)."
}
```


## [2026-09-04T14:29:49.285Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/murw%C4%81r%C4%ABd",
 "prompt": "For Middle Persian murwārīd (pearl): spellings (Book Pahlavi mwlwʾlyt', Manichaean), etymology, meaning, references (MacKenzie), and descendants (Persian مروارید, Armenian margarit, Greek margarites?)."
}
```


### [2026-09-04T14:29:49.967Z] TOOL RESULT

```
# ברקת (Bareqet) - Hebrew Word Entry

Based on the Wiktionary page, **ברקת** (bareqet) is a Hebrew noun meaning "emerald" in Modern Israeli Hebrew.

## Key Information

**Etymology:** The word derives from Proto-Semitic *wVrrVḳānt- ("green gemstone"), stemming from the root *w-r-ḳ meaning "to be yellow/green" and referring generically to precious green stones, including green jasper.

**Grammatical Details:** It functions as a feminine noun with specific declension patterns for singular and plural forms, both in indefinite and construct states.

**Related Term:** The entry notes that אזמרגד (azmargad) serves as a synonym.

**Linguistic Reach:** The word has descendants in other languages, such as Samoan *pereketa*, demonstrating its cross-linguistic influence.

The entry includes audio pronunciation and references scholarly sources, including a 2024 academic work on identifying classical Hebrew gemstones by Ephraim S. Ayil.
```


### [2026-09-04T14:29:52.089Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:29:52.296Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DC%A1%DC%AA%DC%93%DC%A2%DC%9D%DC%AC%DC%90",
 "prompt": "For Classical Syriac ܡܪܓܢܝܬܐ (marganita, pearl): etymology (from Greek margarites? or directly from Iranian?), meaning, and descendants (Arabic مرجان, Armenian, Georgian, Hebrew/Aramaic מרגניתא)."
}
```


### [2026-09-04T14:29:52.343Z] TOOL RESULT

```
# Smaragdus: Etymology and Meaning

**Smaragdus** is a Latin noun meaning "emerald." According to the Wiktionary entry, it comes "From Ancient Greek σμάραγδος (smắrăgdos), itself from a Semitic source."

The word is classified as a second-declension noun that can be masculine or feminine. In Classical Latin, it's pronounced [smaˈraɡ.dʊs].

## Language Descendants

This Latin term produced widespread descendants across Romance and Germanic languages:

- **Romance languages**: Spanish *esmeralda*, French *émeraude*, Catalan *maragda*
- **Germanic languages**: Dutch, Danish, and Estonian all adopted *smaragd*
- **English path**: The term traveled through Old French (*esmeraude*) to Middle English (*emeraude*), eventually becoming the modern English "emerald"

The word subsequently spread to non-European languages, including Japanese (*エメラルド*, emerarudo) and Korean (*에메랄드*, emeraldeu), demonstrating how this ancient term for the precious stone achieved global linguistic reach.
```


### [2026-09-04T14:29:53.282Z] TOOL RESULT

```
# Smaragdite

Smaragdite is a mineral term defined in the Wiktionary entry as follows:

**Definition**: "A green foliated kind of amphibole, observed in eclogite and some varieties of gabbro."

**Etymology**: The word derives from its distinctive emerald-green coloring. The name connects to the French term *smaragdite* and ultimately traces back to *smaragd* (referring to emerald).

**Language Coverage**: The entry appears in English and French, with additional translations available in Greek, Malagasy, Tamil, Vietnamese, and Chinese.

**Source Note**: Much of the English definition was imported from Webster's Dictionary (1913 edition), which is now in the public domain.
```


## [2026-09-04T14:29:53.781Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/margarita#Latin",
 "prompt": "For Latin margarita: etymology (from Greek margarites), meaning (pearl), and descendants (Old French margarite/marguerite, English margarite, Margaret, Margery/Marjorie, Spanish Margarita, Old English meregrot, etc.)."
}
```


## [2026-09-04T14:29:55.282Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Marjorie",
 "prompt": "For English Marjorie: etymology (medieval variant of Margery, from Old French Margerie, from Margaret/margarita, influenced by marjoram?), and Rita / Maggie / Margarita if referenced."
}
```


## [2026-09-04T14:29:56.778Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/margarite",
 "prompt": "For English margarite: all senses (pearl (obsolete), mineral (calcium mica)), etymology (Middle English margarite from Old French margarite from Latin margarita), dates."
}
```


### [2026-09-04T14:29:58.966Z] TOOL RESULT

```
# ܡܪܓܢܝܬܐ (Marganita/Pearl)

This Wiktionary entry documents a word meaning "pearl" across two Aramaic languages:

## Assyrian Neo-Aramaic
The term **ܡܲܪܓܵܢܝܼܬ݂ܵܐ** (margānīṯā) denotes a pearl, with colloquial extension to mean jewel or gem. Biblical citations illustrate usage, such as in Matthew 7:6 about casting pearls before swine.

## Classical Syriac
**ܡܪܓܢܝܬܐ** (margānīṯā) carries broader meanings: "pearl, jewel, gem" plus figurative senses including relic and sacrificial offering.

## Etymology
Both derive from Aramaic, which inherited the term from Ancient Greek μαργαρίτης (margarítēs), itself an Indo-Iranian borrowing. The word spread widely into Arabic, Hebrew, Armenian, Georgian, and numerous other languages.

## Linguistic Legacy
The entry shows "descendants" spanning multiple language families—from Turkish to Swahili—demonstrating how this ancient pearl-related vocabulary dispersed through trade routes and cultural contact across centuries.
```


## [2026-09-04T14:29:59.102Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/mat#French",
 "prompt": "Report the French section(s) of 'mat': (1) adjective 'matte, dull' — etymology (Latin mattus? or from chess mat?), and (2) 'checkmate/mat' — etymology from Arabic شاه مات / Persian; also the phrase échec et mat. Also report the Old French section if present."
}
```


### [2026-09-04T14:29:59.541Z] TOOL RESULT

```
# Margarita: Etymology and Meanings

**The Cocktail:**
In English, a margarita is defined as "a cocktail made with tequila, an orange-flavoured liqueur, and lemon or lime juice, often served with salt encrusted on the rim of the glass."

**The Word's Origins:**
The term was borrowed from Spanish and traces back through Latin to Ancient Greek. The Latin *margarīta* derived from Greek *margarítēs*, ultimately possibly connecting to Proto-Iranian roots meaning bird or animal.

**Historical Meanings:**
Across Romance languages, margarita also refers to a daisy flower and a pearl. In Latin, *margarīta* specifically meant pearl and appears in classical texts like Jerome's Vulgate translation.

**Linguistic Descendants:**
The word spawned numerous related forms across European languages, including the personal names Margaret, Marguerite, and Margarita, as well as English terms like margarine and the archaic margarite mineral.
```


## [2026-09-04T14:30:01.279Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.cnrtl.fr/etymologie/mat",
 "prompt": "Give the full ETYMOL. ET HIST. section(s) for French 'mat' (adjective: terne/dull, and the chess sense 'échec et mat'): earliest attestations with dates, Latin mattus, Arabic šāh māt, Persian, and the editors' conclusion on which origin each sense has."
}
```


## [2026-09-04T14:30:02.806Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://dle.rae.es/matar",
 "prompt": "Give the etymology line given by the RAE for Spanish 'matar' (e.g. 'Quizá del lat. vulg. *mattare, de mattus ...' ) and also for 'matador' if present."
}
```


### [2026-09-04T14:30:03.713Z] TOOL RESULT

```
# Margarite: Definition and Etymology

**Margarite** has two primary meanings in English:

1. **Obsolete sense**: A pearl, derived from Ancient Greek *μαργαρίτης* (margarítēs)

2. **Mineralogical sense**: "A calcium-rich member of the mica group of phyllosilicates, forming white to pinkish or yellowish-gray masses or thin laminae."

The word comes from Ancient Greek roots meaning "pearl" and is a doublet of related terms including Margaret, margarita, and marguerite. Interestingly, it's also linguistically connected to margarine through its pearl-referencing origins.

The mineral definition carries the suffix *-ite*, commonly used in mineralogy to denote mineral species. Finnish translators refer to the mineral as *margariitti*.
```


### [2026-09-04T14:30:03.944Z] TOOL RESULT

```
# Marjorie: Etymology and Overview

According to Wiktionary, **Marjorie** is a female given name originating from Ancient Greek. The name's etymology traces back through several linguistic layers:

The English entry states that Marjorie is a "Variant of _Margery_, a medieval vernacular form of _Margaret_." This establishes the primary etymological pathway from the classic name Margaret down through its Middle English adaptation.

In French, the name represents "Variant of _Marguerite_," borrowed from English _Marjorie_. The Tagalog and Cebuano entries similarly indicate borrowing from the English form.

The page documents the name's use across multiple languages, with entries in 13 different language versions of Wiktionary, reflecting Marjorie's adoption as a given name internationally. The quotation provided shows historical usage, with Thomas Bailey Aldrich's 1869 story "Marjorie Daw" describing the name as having "a pleasing quaintness to it, something prim and violet-like."

While your note mentions possible marjoram influence, the Wiktionary content provided does not include that etymological connection—only the direct line from Margaret through medieval English vernacular forms.
```


## [2026-09-04T14:30:04.280Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/matador",
 "prompt": "Report etymology and dates for English matador (from Spanish), French matador (from Spanish), and any other language sections (Persian ماتادور? Turkish?)."
}
```


### [2026-09-04T14:30:05.269Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:30:06.300Z] TOOL RESULT

```
I appreciate your detailed request, but I need to be honest: the content provided to me consists only of a heading "Portail lexical" (Lexical Portal). There is no etymological section, no attestation dates, no discussion of Latin *mattus* or Arabic/Persian origins, and no editors' conclusions about the two senses of French 'mat'.

To properly answer your question about the ETYMOL. ET HIST. sections for French 'mat' (the adjective meaning "dull/terne" and the chess term "échec et mat"), I would need access to the actual dictionary or reference work content—likely from a comprehensive French etymological dictionary such as the TLF (Trésor de la Langue Française) or similar scholarly source.

If you have access to that content, I'd be happy to extract and summarize the etymological information following your specifications about character limits and citation format.
```


### [2026-09-04T14:30:06.306Z] TOOL RESULT

```
# French Section: "mat"

## Etymology 1 (Adjective - "matte, dull")
**Etymology:** From Old French _mat_, borrowed from Latin _mattus_ ("depressed"). The source notes this etymology is shared with the Dutch adjective meaning "matte, not reflecting light."

**Form:** Adjective with related terms listed.

## Etymology 2 (Noun - "checkmate")
**Etymology:** From Old French _mat_, ultimately from Persian _شاه مات_ (šâh mât, "the king is dead"). This is the chess term.

**Form:** Includes noun and adjective forms, plus derived terms like _mat_ (adjective) and compounds.

**Phrase:** The entry references _échec et mat_ (checkmate in chess).

## Old French Section
The document confirms an **Old French entry** exists with:
- **Adjective** _mat_ (listed under "Old French")
- Connection to both the chess term and the Latin-derived adjective meaning

Both modern French meanings trace to Old French, which borrowed from Romance/Mediterranean sources.
```


## [2026-09-04T14:30:06.560Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%AA",
 "prompt": "For Arabic موت (mawt) and Persian موت: etymology (Proto-Semitic *mawt-), meaning, and for Persian the pronunciation (mowt/mawt) and etymology (from Arabic). Also mention ممات if present."
}
```


## [2026-09-04T14:30:08.030Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%8A%D8%AA",
 "prompt": "For Arabic ميت (mayyit, dead) and Persian میت: etymology, meaning, pronunciation."
}
```


### [2026-09-04T14:30:10.492Z] TOOL RESULT

```
# Etymology Report: Matador

## English
**Etymology:** Borrowed from Spanish *matador* ("killer"). The word is used in English specifically for bullfighters, though Spain refers to them as *torero*.

## French
**Etymology:** Borrowed from Spanish *matador*.

## Spanish (Source Language)
**Etymology:** Derived through surface analysis from *matar* ("kill") + *-dor* (agent suffix). May correspond to Latin *mactātōrem* ("slayer, killer, slaughterer"), though the origin of the base verb *matar* remains disputed.

## Persian
**Etymology:** Not detailed in the provided content; listed as ماتادور (mâtâdor) among translations but no etymology section included.

## Turkish
**Etymology:** Turkish is listed as a descendant language in the Spanish section but lacks a dedicated entry with etymological information in this source document.

**Note:** The document shows matador has spread widely from Spanish origins, with most European languages borrowing directly or indirectly from the Spanish term.
```


## [2026-09-04T14:30:11.032Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/indoeurop.html",
 "prompt": "Find the Indo-European root 'mad-' (to be wet; also of various qualities of food) in the AHD appendix and report its full entry: meaning and derivatives (especially Latin mattus > matte/mat, madere, mast, meat, must). Also find 'baraq' or 'brk' if any Semitic roots appendix is linked (bless, emerald, cherub)."
}
```


### [2026-09-04T14:30:12.618Z] TOOL RESULT

```
# Summary of موت (Mawt)

## Etymology
The word traces back to **Proto-Semitic *mawt-** meaning "death." Cognates appear across Semitic languages including Akkadian, Hebrew, and Aramaic.

## Arabic (موت - mawt)
**Meaning:** "death" or "demise"

**Usage:** Functions as both a noun and verb. As a noun, it represents "the verbal noun of māta (to die)" and serves as the primary term for death. The antonym is حياة (life).

## Persian (موت - mowt/mawt)
**Etymology:** "Borrowed from Arabic mawt"

**Pronunciation:** Varies by dialect—Classical Persian uses /ˈmawt/, while Iranian Persian employs /mowt̪ʰ/

**Meaning:** Identical to Arabic, denoting death with multiple literary synonyms available in Persian vocabulary.

Both languages employ this etymologically shared term to express the concept of mortality, demonstrating the deep linguistic connections within the Semitic and broader Middle Eastern language families.
```


## [2026-09-04T14:30:13.280Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=cherub",
 "prompt": "Give the etymology given by the American Heritage Dictionary for 'cherub' (Hebrew kərūb, Akkadian karūbu/kāribu, Semitic root krb), and any linked Semitic root entry."
}
```


## [2026-09-04T14:30:14.030Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=griffin",
 "prompt": "Give the etymology given by the American Heritage Dictionary for 'griffin' (Greek grups, Latin gryphus, Old French grifon; any Semitic source suggestion)."
}
```


### [2026-09-04T14:30:14.442Z] TOOL RESULT

```
# Summary of ميت (mayyit)

**Primary Meaning:** The word ميت means "dead" across multiple Arabic dialects and related languages.

**Etymology:** In Modern Standard Arabic, ميت (mayyit) derives from the root م و ت (m w t). According to the entry, it's "a CaCīC-type adjective" that underwent phonetic changes from an original form *mawīt through assimilation to *mayīt, then to the final mayyit form.

**Key Uses:**
- As an adjective meaning "dead" or "subject to death; dying; mortal"
- In Egyptian Arabic, also means "a hundred" (from inherited مِئَة miʔat)
- In Urdu, primarily a noun referring to a "corpse" or "dead body," particularly in funeral contexts

**Language Spread:** The word has extensive descendants across languages including Turkish (meyyit), Malay (mayat), Swahili (maiti), and many others listed in the entry.

The Qur'an provides classical usage examples, demonstrating this term's longstanding presence in Arabic religious and literary tradition.
```


## [2026-09-04T14:30:15.472Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/search.html?q=emerald",
 "prompt": "Give the etymology given by the American Heritage Dictionary for 'emerald' (Old French esmeralde, Latin smaragdus, Greek smaragdos, Semitic source brq, Akkadian barraqtu, Sanskrit marakata), and any linked Semitic root entry brq."
}
```


### [2026-09-04T14:30:16.465Z] TOOL RESULT

```
# Search Results for Indo-European Roots

Based on the provided content from the American Heritage Dictionary's Indo-European Roots Appendix, I was unable to locate the entry for **'mad-'** (relating to wetness and food qualities).

The appendix excerpt provided contains roots beginning with letters A and B only, with entries running from "ad-" through "bheudh-" and partial content for "bheuə-". The document does not extend to the "M" section where "mad-" would appear.

Similarly, **no Semitic roots appendix** is referenced or linked in this documentation. The content focuses exclusively on Indo-European etymological roots using the standard scholarly notation system.

To access the "mad-" entry and any Semitic roots information, you would need to:
- Consult the complete digital version of the American Heritage Dictionary appendix
- Navigate to the M section for Indo-European roots
- Check if a separate Semitic roots section exists in the full dictionary

The guide references available at `/word/ieguide.html` may provide additional information about accessing all root entries.
```


### [2026-09-04T14:30:17.520Z] TOOL RESULT

```
# Etymology of "Cherub"

According to the American Heritage Dictionary, the entry for cherub provides this etymology:

"[Middle English, from Late Latin, from Hebrew _kərûb_; see **krb** in the Appendix of Semitic roots]."

The dictionary traces the word's origins through Middle English and Late Latin back to Hebrew, with a reference to the Semitic root **krb** available in their online appendices. However, the Akkadian forms you mentioned (karūbu/kāribu) are not included in the etymology presented on this page—only the Hebrew kərûb is explicitly cited.
```


### [2026-09-04T14:30:18.666Z] TOOL RESULT

```
# Etymology of "Griffin"

According to the American Heritage Dictionary, the word "griffin" traces back through several languages:

"[Middle English _griffoun_, from Old French _griffon_, from _grif_, from Latin _grȳpus, grȳphus_, variants of _grȳps__, grȳp-_, from Greek _grūps_.]"

The dictionary provides no Semitic source suggestion for this term. The etymological chain runs from Greek through Latin and Old French to Middle English.
```


### [2026-09-04T14:30:21.342Z] TOOL RESULT

```
# Etymology of "Emerald"

According to the American Heritage Dictionary, the word traces back through several languages. The entry states:

"Middle English _emeraude_, from Old French, from Medieval Latin _esmeralda, esmeraldus_, from Latin _smaragdus_, from Greek _smaragdos_"

The dictionary further notes connections to Sanskrit _marakatam_ and Semitic sources, specifically "akin to Akkadian _barraqtu_ and Hebrew _bāreqet_, a kind of gemstone (probably emerald)."

The entry references a Semitic root **brq** in the appendix but does not provide the actual linked content from that appendix entry in the material shown above. The page indicates such information exists in an "Appendix of Semitic roots," but the specific details of that brq entry are not included in this excerpt.
```


## [2026-09-04T14:30:44.034Z] AGENT (thinking)

I'll now look up the AHD Semitic-roots appendix entries for krb, brq, brk, and mwt, along with the SAHD cherub entry, Akkadian karābu/barraqtu, Middle Persian murwārīd, Old French esmeraude, and the Persian ماتادور page.


## [2026-09-04T14:30:44.591Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://ahdictionary.com/word/semitic.html",
 "prompt": "Find and quote in full the entries for the Semitic roots: brk (to kneel, bless), brq (to shine, lightning; emerald), krb (cherub), and mwt (to die). Give each entry's full text including derivatives (baraka, barq, cherub, griffin?, emerald, checkmate, matador etc.) and any notes about Akkadian karābu or metathesis."
}
```


## [2026-09-04T14:30:46.843Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://sahd-online.com/words/krub/",
 "prompt": "Summarize the etymology discussion for Hebrew kərūb (cherub): Akkadian karābu/kāribu/kurību, the proposed metathesis with b-r-k (Dhorme), which views are accepted or rejected by modern scholars, and any mention of griffin/Greek gryps."
}
```


## [2026-09-04T14:30:49.160Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.balashon.com/2007/07/kruv.html",
 "prompt": "Summarize what this post says about the etymology of Hebrew keruv (cherub): Akkadian karabu 'bless', karibu, the relation to barakh/b-r-k via metathesis, Klein's view, and griffin/gryps."
}
```


## [2026-09-04T14:30:50.660Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/karabu",
 "prompt": "Report any Akkadian entry for karābu/karabu: meaning, etymology, related words (kāribu, kurību, kirbu), and relation to Hebrew cherub or root b-r-k."
}
```


## [2026-09-04T14:30:51.411Z] TOOL CALL #59: WebSearch

```json
{
 "query": "Akkadian barraqtu emerald baraqu \"to flash\" smaragdos marakata etymology"
}
```


### [2026-09-04T14:30:51.460Z] TOOL RESULT

```
# Semitic Root Entries

## brk (to bless)
"West Semitic, to bless. Probably a metathesized variant of **krb.**" The entry lists broker, baruch, and notes the Arabic _bāraka_.

## brq (lightning/emerald)
"To flash (especially of lightning)." The sole example is emerald, traced through Greek _smaragdos_ to Akkadian _barraqtu_ and Hebrew _bāreqet_.

## krb (cherub)
"To praise. Common Semitic root, with West Semitic metathesized variant **brk.**" It connects cherub to Hebrew _kərûb_ and Akkadian _karābu_ (to praise, bless), with a cross-reference noting the brk variant.

## mwt (to die)
"To die." The entry provides checkmate and mate, derived from Arabic _māt_ (he has died), from earlier _māta_ (to die).
```


## [2026-09-04T14:30:52.165Z] TOOL CALL #60: WebSearch

```json
{
 "query": "Middle Persian murwārīd pearl MacKenzie \"mwlwʾlyt\" margarites Greek Iranian loanword"
}
```


### [2026-09-04T14:30:52.953Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:30:53.798Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/esmeraude",
 "prompt": "For Old French esmeraude (and variants esmeralde, esmeragde): etymology (Latin smaragdus, Medieval Latin smaralda/esmeraldus), meaning, attestation, and descendants (Middle English emeraude, English emerald, French émeraude)."
}
```


### [2026-09-04T14:30:54.422Z] TOOL RESULT

```
# Etymology of Hebrew כְּרוּב (kerūb)

## Akkadian Connection

The most widely supported theory links כְּרוּב to Akkadian terms. Scholars propose connections to _kāribu_ (present participle of _karābu_, meaning "one who prays" or "intercessor") and especially _kurību_ (a diminutive form). The Chicago Assyrian Dictionary distinguishes _kāribu_ as an adjective versus _kurību_ as a substantive referring to a specific divine being type. Evidence from Assyrian texts places _kurību_ statues among apotropaic figures, suggesting non-human form and guardian functions comparable to biblical cherubim.

## Rejected Theories

**Metathesis with בְּרָכָה (blessing):** Dhorme and Rinaldi proposed כְּרוּב derived from the root ברך through metathesis (switching first and third radicals). However, Mitchell's modern linguistic analysis definitively refutes this: "it is unlikely that the two are related; metathesis of the first and third radicals of a root is extremely rare."

**Greek γρύψ (griffin):** Brown's proposal connecting כְּרוּב to Greek gryphus through phonetic shift remains speculative and finds minimal scholarly acceptance.

The Akkadian _kurību_ etymology remains most plausible, though definitive proof remains elusive.
```


### [2026-09-04T14:30:55.091Z] TOOL RESULT

```
# Etymology of Hebrew Keruv (Cherub)

According to the post, Klein traces keruv to **Akkadian origins**: the word relates to "karabu (= to bless), karibu (= one who blesses)," an epithet for the bull-colossus. He further notes connection to the Hebrew verb ברך (barakh, meaning "to bless").

**Metathesis relationship**: Some scholars propose that the Akkadian "karâbu" represents a transposition of the Hebrew root, linking the two through sound reversal rather than direct descent.

**Griffin/Gryphon connection**: Klein suggests these mythological creatures may share a Semitic source "through the medium of the Hittites," citing Hebrew kerubh alongside Akkadian karibu as evidence. The Jewish Encyclopedia notes other scholars (like Delitzsch) connected Assyrian "kirubu" to "shedu" (the winged bull), offering similar cross-linguistic parallels for understanding the term's ancient origins.
```


## [2026-09-04T14:30:55.977Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D8%AA%D8%A7%D8%AF%D9%88%D8%B1",
 "prompt": "For Persian ماتادور (mâtâdor): etymology (from French matador? Spanish?), meaning, pronunciation, spelling variants (ماتادر)."
}
```


## [2026-09-04T14:30:58.978Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87_%D9%85%D8%A7%D8%AA",
 "prompt": "For Persian شاه مات (šâh mât, checkmate): etymology and literal meaning discussion (Arabic māta 'die' vs Persian māt 'helpless/astonished'), and descendants (Arabic شاه مات, Old French eschec mat, English checkmate). Also whether کیش مات is mentioned."
}
```


## [2026-09-04T14:31:00.134Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/mate",
 "prompt": "Give the full etymology text for 'mate (v.2)' / 'mate (n.2)' meaning checkmate/to overcome, and any dates; also 'mat' entries if shown."
}
```


### [2026-09-04T14:31:01.946Z] TOOL RESULT

```
Web search results for query: "Akkadian barraqtu emerald baraqu "to flash" smaragdos marakata etymology"

Links: [{"title":"Etymology of Emerald | WordReference Forums","url":"https://forum.wordreference.com/threads/etymology-of-emerald.3249997/"},{"title":"Emerald. : languagehat.com","url":"https://languagehat.com/emerald/"},{"title":"emerald - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/emerald"},{"title":"Balashon - Hebrew Language Detective: bareket and emerald","url":"https://www.balashon.com/2020/11/bareket-and-emerald.html"},{"title":"Emerald Definition & Meaning | YourDictionary","url":"https://www.yourdictionary.com/emerald"},{"title":"Translating Gemstones | Voices on Sefaria","url":"https://voices.sefaria.org/sheets/381719"},{"title":"σμάραγδος - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CF%83%CE%BC%CE%AC%CF%81%CE%B1%CE%B3%CE%B4%CE%BF%CF%82"},{"title":"THE KEY TO THE STONES OF HOSHEN: Bareqet. The Etymology of theWord","url":"https://glikman.blogspot.com/2015/07/bareqet-etymology-of-theword.html"},{"title":"Smaragdus (name)","url":"https://en.wikipedia.org/wiki/Smaragdus_(name)"},{"title":"Mons Smaragdus","url":"https://en.wikipedia.org/wiki/Mons_Smaragdus"}]

Based on the search results, here's what I found regarding the etymology connecting these terms:

Hebrew בָּרֶ֫קֶת is based on the common Semitic root brq, "to flash, shine," with attested cognates in Syriac (bārqā) as well as Neo-Babylonian Akkadian (barraqtu).

The Akkadian baraqu literally means "scintillation", and Hebrew baraq (בָּרָק) means "lightning," with bareḳet implying a "lightning-stone" or a stone with intense, flashing brilliance.

Regarding the Greek connection: Greek smaragdos "green gem" comes from Semitic baraq "shine", though Sanskrit marakata is a late loan from Greek σμάραγδος (in turn recognized by classicists as a loan into Greek from Semitic) and thus cannot be the origin of the Semitic forms.

However, there is an alternative theory: scholars have known that the Akkadian word was borrowed from the Sanskrit marakata, an "emerald" or gem of green corundum. This suggests some scholarly debate about the direction of borrowing, with some sources proposing Sanskrit marakata as the ultimate source rather than the Semitic root meaning "to flash."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:31:02.129Z] TOOL RESULT

```
# ماتادور (Persian)

Based on the Wiktionary entry, **ماتادور** (mâtâdor) is a Persian noun borrowed from Spanish. 

**Definition:** The term refers to "a person whose aim is to kill the bull in a bullfight."

**Etymology:** The word derives from the Spanish term *matador*, which was adopted into Persian vocabulary. The entry categorizes it as "Persian terms derived from Spanish," indicating this is a direct loanword rather than an independent development in the Persian language.
```


### [2026-09-04T14:31:03.081Z] TOOL RESULT

```
# esmeraude - Etymology and Meaning

**esmeraude** is an Old French word meaning both the color emerald and the precious stone itself.

## Etymology
The word traces back through several language layers: it derives from Vulgar Latin variants (*smaralda*, *smaraldus*, *smaraudus*), which came from the Latin *smaragdus* ("emerald"). This Latin term ultimately stems from Ancient Greek *σμάραγδος* (smáragdos) or *μάραγδος* (máragdos), with roots in Semitic languages.

## Linguistic Descendants
The word spawned several modern language variants:
- French: *émeraude*
- Middle English: *emeraude*
- English: *emerald*

## Variants
Old French had numerous spelling variations including *emeraude*, *esmeralde*, *esmeragde*, *smaralde*, and many others—reflecting the spelling inconsistencies common in medieval manuscripts.

The entry also notes that "esmeraude" appears as "an alternative form of *emeraude*" in Middle English usage.
```


### [2026-09-04T14:31:03.768Z] TOOL RESULT

```
Web search results for query: "Middle Persian murwārīd pearl MacKenzie "mwlwʾlyt" margarites Greek Iranian loanword"

Links: [{"title":"Greece xiii. Greek Loanwords in Middle Iranian Languages - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/greece-xiii/"},{"title":"مروارید - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF"},{"title":"μαργαρίτης - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82"},{"title":"Mordjene. : languagehat.com","url":"https://languagehat.com/mordjene/"},{"title":"Margarite - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/margarite"},{"title":"Pearl - Etymology, Origin & Meaning","url":"https://www.etymonline.com/word/pearl"},{"title":"Middle Persian literature","url":"https://en.wikipedia.org/wiki/Middle_Persian_literature"},{"title":"Margaret — Grokipedia","url":"https://grokipedia.com/page/Margaret"},{"title":"Iran (word)","url":"https://en.wikipedia.org/wiki/Iran_(word)"}]

I found relevant information about the etymology and linguistic relationship between Middle Persian and Greek terms for pearl. Here are the key findings:

## Middle Persian murwārīd and Related Forms

Middle Persian mwrwʾryd /morwārīd/ is documented in MacKenzie (1986, p. 56), and the Pahlavi form mwlwʾlyt also appears. The word likely derives from Old Persian *margārīta- and possibly from Proto-Iranian *mŕ̥ga-ahri-ita- ("oyster", literally "born from the shell of a bird").

## Relationship with Greek margarites

The Middle Persian word for 'pearl' was most probably not borrowed from Greek margarítēs, but the borrowing may rather have functioned the other way around. This contrasts with the traditional view, as Iranian scholars consider margarites a loanword from Greek; the Greek word is unlikely to have originated in Iranian.

## Related Forms Across Iranian Languages

Related forms appear across other Middle Iranian languages, including Manichaean Parthian mwrgʾryd /morγārīd/, Sogdian mrγʾrt(h), and Khotanese mrāhe 'pearl'.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:31:04.571Z] TOOL RESULT

```
# Response Based on Wiktionary Content

The page presents **شاه مات** (šāh māt) as a Persian entry. According to the dictionary, this term is classified as "an alternative form of شاه‌مات" and functions as a noun.

The entry indicates it is a "non-lemma form" and "noun form," suggesting it represents a variant spelling of the primary entry. The page notes this is a Persian language term, though it does not provide the full definition or detailed etymology on this particular page—instead directing readers to consult the corresponding main entry form for etymological information.

The term relates to the chess concept known in English as "checkmate," which has roots in Persian and Arabic linguistic traditions.
```


### [2026-09-04T14:31:07.852Z] TOOL RESULT

```
# Etymology of Mate (Chess Terms)

## mate (v.2)
"to checkmate," dating to around 1300, derives from Old French *mater* meaning "to checkmate, defeat, overcome," which comes from *mat* "checkmated" (see checkmate).

## mate (n.2)
In chess, this noun refers to "a condition of checkmate, the state of the king when he is in check and cannot move out of it," also from circa 1300. It originates from Old French *mat*, stemming from *mater* "to checkmate."

The entry includes historical examples like "Fool's mate" and "Scholar's mate," both documented chess strategies.

## mat (separate entry)
Regarding the general "mat" entry: it describes "an article plaited or woven of more or less coarse natural materials (rushes, straw, twine, etc.) used as bedding, floor-coverings, etc." This comes from Old English *matte*, derived from Late Latin *matta* "mat made of rushes" (4th century), likely from Punic or Phoenician origins.
```


## [2026-09-04T14:31:22.122Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/greece-xiii/",
 "prompt": "Quote what this article says about the word for 'pearl' (Middle Persian murwārīd / mwrwʾryd, Greek margarites): direction of borrowing, Old Persian reconstruction, and any other relevant remarks (also on zumurrud/smaragdos if present)."
}
```


### [2026-09-04T14:31:23.959Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-04T14:31:25.224Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87%E2%80%8C%D9%85%D8%A7%D8%AA",
 "prompt": "For Persian شاه‌مات: full etymology (شاه + مات; is مات Arabic 'died' or Persian 'helpless/astonished'? cited scholars), meaning, and descendants (Arabic, Old French eschec mat, Spanish jaque mate, English checkmate, Turkish)."
}
```


## [2026-09-04T14:31:27.380Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://languagehat.com/emerald/",
 "prompt": "Summarize the discussion of the etymology of emerald / smaragdos: direction of borrowing between Semitic (Akkadian barraqtu, Hebrew bareqet), Greek smaragdos, Sanskrit marakata, Prakrit maragada; Persian zumurrud route (Greek > Syriac/Middle Persian > Arabic?). Name the scholars cited."
}
```


## [2026-09-04T14:31:28.618Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/chess-a-board-game/",
 "prompt": "Quote what this article says about the term 'šāh māt' / checkmate: its literal meaning (is māt Persian 'helpless, at a loss' or Arabic 'dead'?), and the transmission of chess terminology to Arabic and Europe."
}
```


### [2026-09-04T14:31:31.848Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:31:32.890Z] TOOL RESULT

```
# شاه‌مات (Shahmat) - Etymology and Meaning

Based on the Wiktionary entry, this Persian word literally means **"the king is amazed."** It comprises two elements:

- **شاه** (šâh) = "king"
- **مات** (mât) = "stunned, amazed"

## Semantic Evolution

When the term entered Arabic before spreading to Romance languages, the second component underwent reinterpretation. Arabic speakers analyzed it as **مَاتَ** (māta), meaning "to die," fundamentally changing the semantic profile from "amazed" to "dead."

## Modern Usage

In Persian, the word denotes "checkmate" in chess contexts, though this usage is now rare. In Tajik, it has broadened to mean "chess" itself, functioning as a phono-semantic match with the Russian term **шахматы** (šaxmaty).

The entry documents how this single Persian expression generated the checkmate terminology found across multiple language families—from Arabic through Old French, Spanish, English, and Turkish—demonstrating significant cross-linguistic influence in chess vocabulary.
```


### [2026-09-04T14:31:39.091Z] TOOL RESULT

```
# Etymology of Emerald: Direction of Borrowing

## Primary Borrowing Direction

The consensus among most scholars is that the Semitic forms are the ultimate source. Hebrew *bareqet* and Akkadian *barraqtu* derive from a common Semitic root *brq* meaning "to flash, shine"—an appropriate etymology for a gemstone. Greek *smaragdos* borrowed from this Semitic source, not the reverse.

## Sanskrit's Secondary Role

Contrary to some earlier theories, Sanskrit *marakata* is a **late loan from Greek** *smaragdos*, not its origin. As one source notes, "Sanskrit *marakata* is a late loan from Greek σμάραγδος (in turn recognized by classicists as a loan into Greek from Semitic) and thus cannot be the origin of the Semitic forms."

## Transmission Routes

- **Greek → European languages**: Latin *smaragdus* → Medieval Latin *esmeraldus* → French *esmeraude* → English "emerald"
- **Greek → Asian languages**: Greek *smaragdos* appears in Pahlavi, New Persian *zumurrod*, and Arabic *zummurud* as later borrowings

## Scholars Cited

- Benjamin Noonan (2012 dissertation on Northwest Semitic loanwords)
- Philologos (Forward column)
- Klein and Online Etymology Dictionary
- Chantraine, Beekes, and Mayrhofer (on Greek phonetics)
- Sinkankas and Healy (on classical mineral descriptions)
```


## [2026-09-04T14:32:59.587Z] AGENT

I have enough source material. Writing both verification files now (via a Python script so the JSON is guaranteed valid).


## [2026-09-04T14:36:24.388Z] TOOL CALL #69: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write_101_345.py <<'PYEOF'\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\nAHD_SEM = \"https://ahdictionary.com/word/semitic.html\"\n\np101 = {\n  \"pdf_page\": 101, \"book_page\": 71,\n  \"verified_by\": \"claude-fable-5-1\", \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0, \"root\": \"B.r.k\", \"verdict\": \"confirmed\",\n      \"modern_form\": \"Semitic root b-r-k: Proto-Semitic *birk- 'knee' / West Semitic brk 'to kneel; to bless' (AHD Semitic roots brk)\",\n      \"note\": \"The root is real and its label 'Semitic' is right. Wiktionary reconstructs Proto-Semitic *birk- 'knee' (Akk. birkum, Heb. berekh, Ug. brk, Syr. burkā, Ge'ez bərk) with a metathetic variant *rukbat- (Ar. rukba). The 'kneel (of a camel) > bless' story is the traditional Gesenius/BDB account and matches Arabic baraka 'to kneel (camel)' / bāraka 'to bless'. The AHD Semitic appendix (Nourai's own AHD source) instead treats brk 'to bless' as 'probably a metathesized variant of krb' (Akk. karābu 'to praise, bless') — that is the hypothesis underlying Nourai's Akkadian/Hebrew cherub branch; it is accepted by AHD and Klein but rejected by recent Hebrew lexicography (SAHD, citing Mitchell: metathesis of first and third radicals is extremely rare). The griffin sub-branch is speculative (Klein) and not adopted by AHD's own griffin entry.\",\n      \"sources\": [W+\"Reconstruction:Proto-Semitic/birk-\", AHD_SEM, W+\"%D8%A8%D8%B1%D9%83%D8%A9\"],\n      \"nodes\": [\n        {\"id\": 1, \"lang\": \"Arabic\", \"words\": \"b.r.k; barakat\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Arabic root b-r-k: baraka 'to kneel (of a camel)' (verbal noun burūk), Form III bāraka 'to bless', Form II barraka, Form VI tabāraka 'be blessed'; the noun baraka(t) 'blessing, divine favour' is the maṣdar-type noun of the root, with tāʾ marbūṭa -at (hence the transliteration barakat). Cognate with Hebrew bērēkh 'to bless' / bərākhā 'blessing'. Wiktionary lists 11 Arabic derivatives of the root.\",\n         \"sources\": [W+\"%D8%A8%D8%B1%D9%83%D8%A9\", W+\"%D7%91%D7%A8%D7%9B%D7%94\"]},\n        {\"id\": 2, \"lang\": \"Persian\", \"words\": \"barekat\", \"verdict\": \"confirmed\",\n         \"derivation\": \"New Persian barakat برکت is a direct loan of Arabic baraka(t) with the Arabic construct/pausal -at preserved as -at (a regular treatment of Arabic feminine nouns in Persian, cf. رحمت, نعمت); Wiktionary derives Urdu barkat from Classical Persian barakat < Arabic. The extra forms are all Arabic derivatives of the same root borrowed into Persian: tabrīk تبریک (Form II maṣdar 'congratulation'), tabarruk تبرّک (Form V maṣdar 'seeking blessing; blessed object'), mubārak مبارک (Form III passive participle 'blessed').\",\n         \"sources\": [W+\"%D8%A8%D8%B1%DA%A9%D8%AA\", W+\"%D8%A8%D8%B1%D9%83%D8%A9\"]},\n        {\"id\": 3, \"lang\": \"Akkadian\", \"words\": \"karâbu\", \"verdict\": \"plausible\",\n         \"derivation\": \"Akkadian karābu 'to pray, bless, greet, praise' (participle kāribu 'one who blesses/intercedes', diminutive kurību, a protective genius) is a real word of root k-r-b. Its connection to b-r-k is the metathesis hypothesis (Dhorme; Klein 164; AHD Semitic roots: 'krb, to praise, common Semitic root, with West Semitic metathesized variant brk'). So Nourai's cited sources (KLN, AHD) do assert this, and AHD still does; but the Semantics of Ancient Hebrew Database (Mitchell) rejects it because metathesis of the first and third radicals is extremely rare, and Wiktionary's Proto-Semitic *birk- page lists no Akkadian karābu. Verdict: accepted by some, rejected by others.\",\n         \"sources\": [AHD_SEM, \"https://sahd-online.com/words/krub/\", E+\"cherub\"]},\n        {\"id\": 4, \"lang\": \"Hebrew\", \"words\": \"berâkah; kerŭbh\", \"verdict\": \"plausible\",\n         \"derivation\": \"bərākhā בְּרָכָה 'blessing' (root b-r-k, verb bērēkh 'to bless', berekh 'knee') is a straightforward member of the root and is confirmed (cognate with Arabic baraka). kərūḇ כְּרוּב 'cherub' (pl. kərūḇīm; Gen. 3:24, Ex. 25:18) is by the mainstream view a loan from Akkadian kāribu/kurību 'intercessor; protective winged genius' (root k-r-b, karābu 'to bless') — so it belongs with Akkadian karābu (node 3), and the chart's placing of it under b-r-k stands or falls with the krb/brk metathesis hypothesis: endorsed by Klein and AHD, rejected by SAHD/Mitchell. Robert Alter's alternative ('hybrid' or, by consonant inversion, rkb 'mount/steed') is also on the table. Worst verdict for the node: plausible.\",\n         \"sources\": [W+\"%D7%91%D7%A8%D7%9B%D7%94\", W+\"%D7%9B%D7%A8%D7%95%D7%91\", \"https://sahd-online.com/words/krub/\", \"https://ahdictionary.com/word/search.html?q=cherub\"]},\n        {\"id\": 5, \"lang\": \"Arabic\", \"words\": \"karŭbiyy\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Arabic karūbī كَرُوبِيّ 'cherub, archangel' (pl. karūbiyyūn, as in al-malāʾika al-karūbiyyūn) is, per Wiktionary, borrowed from Hebrew kərūḇ (in practice through Jewish Aramaic/Syriac kərūḇā, the vehicle of most biblical vocabulary into Arabic) with the Arabic nisba suffix -iyy added to form an adjective/noun of relation; the word appears in early Islamic tradition (hadith and tafsīr) for the highest angels. Not from the Akkadian directly.\",\n         \"sources\": [W+\"%D9%83%D8%B1%D9%88%D8%A8%D9%8A\", W+\"%D7%9B%D7%A8%D7%95%D7%91\"]},\n        {\"id\": 6, \"lang\": \"Persian\", \"words\": \"karrŭbî\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Persian karrūbī کرّوبی is Arabic karūbī taken over unchanged (Persian writers often geminate the r, karrūbī, as Nourai's spelling shows); the plurals karrūbiyān کروبیان (Persian -ān) and karrūbiyūn کروبیون (Arabic sound plural) are both used. Attested in classical poetry, e.g. Sa'di's Bustan (13th c.), as quoted in the chart. Gloss 'angel' is loose: the word means specifically 'cherub, one of the highest angels'. Nourai's source MON (Mo'in) is the standard Persian dictionary for this and Wiktionary's Arabic entry confirms the Arabic base; no independent Persian etymological page was found, but the Arabic loan is uncontroversial.\",\n         \"sources\": [W+\"%D9%83%D8%B1%D9%88%D8%A8%D9%8A\"]},\n        {\"id\": 7, \"lang\": \"English\", \"words\": \"cherub\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Hebrew kərūḇ was transliterated in the Septuagint (3rd–2nd c. BCE) as Greek χερούβ (pl. χερουβίμ), taken into Late Latin as cherub (pl. cherubim, Vulgate), and borrowed into Middle English in the late 14th c. as cherub 'an order of angels'; the sense 'winged child, putto' (the '(of love)' in Nourai's gloss) is Renaissance art usage, in English from c. 1705. The chart correctly draws it from Hebrew, not through Arabic. AHD's entry: 'from Late Latin, from Hebrew kərûb; see krb'.\",\n         \"sources\": [E+\"cherub\", \"https://ahdictionary.com/word/search.html?q=cherub\", W+\"%D7%9B%D7%A8%D7%95%D7%91\"]},\n        {\"id\": 8, \"lang\": \"Greek\", \"words\": \"gruphos, grups\", \"verdict\": \"plausible\",\n         \"derivation\": \"Greek γρύψ grȳps, gen. γρυπός grȳpós 'griffin' (Herodotus, Aeschylus) — the second form Nourai gives, 'gruphos', is not a Greek nominative but reflects the genitive grypos / Latin gryphus. Its origin is unsettled: one view links it to γρυπός 'hook-nosed, curved' (PIE *ger- 'to bend'); Klein (KLN:680, Nourai's source) and Beekes allow a Pre-Greek/Anatolian loan ultimately from Semitic (Akkadian karūbu/kāribu, Hebrew kərūḇ) 'through the medium of the Hittites', making it a doublet of χερούβ. Wiktionary reports both; AHD's own griffin entry gives no Semitic source, and SAHD notes Brown's kərūḇ–γρύψ link 'finds minimal scholarly acceptance'. So the edge Hebrew kerubh → Greek gryps is a respectable but minority hypothesis.\",\n         \"sources\": [W+\"%CE%B3%CF%81%CF%8D%CF%88\", E+\"griffin\", \"https://ahdictionary.com/word/search.html?q=griffin\", \"https://sahd-online.com/words/krub/\"]},\n        {\"id\": 9, \"lang\": \"Latin\", \"words\": \"gryphus\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Latin grȳps, grȳpis (Vergil, Pliny) was borrowed from Greek γρύψ; Late Latin created the thematic variants grȳpus and grȳphus (the -ph- is a hypercorrect spelling, etymonline: 'misspelling of grypus'), and it is the Late Latin gryphus/grifus that the Romance forms continue.\",\n         \"sources\": [E+\"griffin\", \"https://ahdictionary.com/word/search.html?q=griffin\"]},\n        {\"id\": 10, \"lang\": \"Old French\", \"words\": \"grifion\", \"verdict\": \"plausible\",\n         \"derivation\": \"Old French grifon / griffon (12th c.; Anglo-Norman grifun, griffoun) is Late Latin gryphus with the augmentative/derivational suffix -on (< Latin -ōnem), i.e. from a Late Latin *grifonem; AHD: 'Old French griffon, from grif, from Latin grypus, gryphus'. The edge Latin → Old French → English is certain. The spelling 'grifion' printed here is not a standard attested Old French form (expected grifon/griffon); it may be Nourai's or the scan's slip for grifon, but since Klein's page could not be checked it is left as plausible rather than transcription_suspect.\",\n         \"sources\": [E+\"griffin\", \"https://ahdictionary.com/word/search.html?q=griffin\"]},\n        {\"id\": 11, \"lang\": \"English\", \"words\": \"griffin\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Middle English griffoun, griffon (c. 1200 as a surname, 14th c. as the beast) from Old French grifon; the modern spelling griffin/gryphon settled in the 16th–17th c. (gryphon re-Latinised after Latin gryphus). Sense: the eagle-headed, lion-bodied guardian of Scythian gold in Greek legend.\",\n         \"sources\": [E+\"griffin\", W+\"%CE%B3%CF%81%CF%8D%CF%88\"]}\n      ]\n    },\n    {\n      \"entry\": 1, \"root\": \"B.r.q\", \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *baraḳ- 'lightning', root b-r-q 'to flash, shine' (AHD Semitic roots brq)\",\n      \"note\": \"Root, label and gloss are correct: Wiktionary reconstructs Proto-Semitic *baraḳ- 'lightning' (Akk. birqum, Heb. bārāq, Aram. barqā, Ar. barq, Ge'ez bärḳ), from Proto-Afroasiatic *bǐrk'-/*bǎrk'- 'to flash'; AHD Semitic appendix brq 'to flash (especially of lightning)' with emerald as its English derivative. The emerald branch (Semitic barraqtu/bāreqet → Greek smaragdos → Latin → Romance/English; Greek → Iranian/Arabic zumurrud) is standard (AHD, etymonline, Beekes, Noonan 2012). Two problems in this chart: the Greek form is misprinted/misread ('smaraldos' for smaragdos), and the Arabic → Persian direction for zumurrud is reversed relative to Wiktionary/MacKenzie (Middle Persian uzumburd is pre-Islamic).\",\n      \"sources\": [W+\"Reconstruction:Proto-Semitic/bara%E1%B8%B3-\", AHD_SEM, \"https://ahdictionary.com/word/search.html?q=emerald\"],\n      \"nodes\": [\n        {\"id\": 1, \"lang\": \"Arabic\", \"words\": \"b.r.q\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Arabic root b-r-q: baraqa 'to flash (of lightning), shine, glitter', noun barq 'lightning' (Qur'an 2:19–20 yakādu l-barqu yakhṭafu abṣārahum); Wiktionary: from Proto-Semitic *baraḳ-, noting the Arabic noun may be a deverbal formation rather than a direct inheritance. Derivatives barrāq 'glittering' (intensive faʿʿāl), bāriqa 'flash' (active participle).\",\n         \"sources\": [W+\"%D8%A8%D8%B1%D9%82\", W+\"Reconstruction:Proto-Semitic/bara%E1%B8%B3-\"]},\n        {\"id\": 2, \"lang\": \"Persian\", \"words\": \"barq\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Persian barq برق is borrowed from Arabic barq 'lightning' (Wiktionary: 'Persian borrowed the term directly from Arabic'); attested in Ferdowsi's Shahnameh (c. 1000 CE) in the sense 'lightning', as the chart's quotation shows. The sense 'electricity' is a 19th–20th-c. semantic extension in Persian (cf. barqī 'electric', barq-kār 'electrician'), paralleled by Arabic barq 'telegraph'. The extras barrāq برّاق 'glittering' and bāriqa بارقه 'flash, gleam' are further Arabic derivatives of the root borrowed into Persian.\",\n         \"sources\": [W+\"%D8%A8%D8%B1%D9%82\"]},\n        {\"id\": 3, \"lang\": \"Akkadian\", \"words\": \"baraqtu\", \"verdict\": \"plausible\",\n         \"derivation\": \"The Akkadian word for 'lightning' is birqu (Proto-Semitic *baraḳ-, Wiktionary lists Akkadian birqum); the form Nourai prints, baraqtu, corresponds to Neo-Babylonian barraqtu 'emerald, a flashing green stone' (AHD: 'akin to Akkadian barraqtu and Hebrew bāreqet, a kind of gemstone (probably emerald)'), a -t- derivative of barāqu 'to flash'. So the word is real and belongs to this root (KLN:514 s.v. emerald cites it), but the gloss 'lightning' is a conflation: barraqtu is the gem-name, and it is precisely the form from which Greek smaragdos is derived, so it ought to sit as the parent of the Greek node rather than as a sister.\",\n         \"sources\": [\"https://ahdictionary.com/word/search.html?q=emerald\", W+\"Reconstruction:Proto-Semitic/bara%E1%B8%B3-\", E+\"emerald\"]},\n        {\"id\": 4, \"lang\": \"Greek\", \"words\": \"smaraldos\", \"verdict\": \"transcription_suspect\",\n         \"derivation\": \"The Greek word is σμάραγδος smáragdos (also μάραγδος máragdos), 'emerald, green gem' (Herodotus, Theophrastus; Marcus Aurelius); 'smaraldos' with -ld- is not a Greek form and is almost certainly a misreading of the -gd- cluster (gd → ld) in the scan, since Klein (KLN:514) prints smaragdos. Etymology as drawn is confirmed: Wiktionary, AHD, etymonline and Beekes derive smaragdos from a Semitic source, Akkadian barraqtu / Hebrew bāreqet (Ex. 28:17) 'flashing gem', root b-r-q; the initial s- and the -agd- are the Greek adaptation of the Semitic b-r-q-t cluster (Noonan 2012 on Northwest Semitic loanwords). Old Armenian zmruxt also stems from it.\",\n         \"sources\": [W+\"%CF%83%CE%BC%CE%AC%CF%81%CE%B1%CE%B3%CE%B4%CE%BF%CF%82\", E+\"emerald\", \"https://ahdictionary.com/word/search.html?q=emerald\", \"https://languagehat.com/emerald/\"]},\n        {\"id\": 5, \"lang\": \"Arabic\", \"words\": \"\", \"verdict\": \"plausible\",\n         \"derivation\": \"Pass-through node: Arabic zumurrud زُمُرُّد 'emerald' does go back to Greek smaragdos, but not directly: Wiktionary derives Arabic zumurrud from Persian zumurrud (< Middle Persian ʾwzmbwlt /uzumburd/ < Greek), i.e. Persian is the intermediary into Arabic rather than the reverse; another route often cited is Syriac zmaragdā. Arabic zabarjad 'peridot' is a doublet. The chart's Greek → Arabic → Persian ordering reverses the direction Wiktionary/MacKenzie give, so the Arabic node's parent is right in substance (Greek origin) but its child edge is not.\",\n         \"sources\": [W+\"%D8%B2%D9%85%D8%B1%D8%AF\", W+\"%CF%83%CE%BC%CE%AC%CF%81%CE%B1%CE%B3%CE%B4%CE%BF%CF%82\"]},\n        {\"id\": 6, \"lang\": \"Persian\", \"words\": \"zomorrod\", \"verdict\": \"disputed\",\n         \"derivation\": \"Persian zumurrud/zomorrod زمرّد 'emerald' is, per Wiktionary, inherited from Middle Persian uzumburd (Book Pahlavi ʾwzmbwlt), itself borrowed from Greek σμάραγδος in the Sasanian period; the prothetic u-/i- (cf. Early New Persian uzmurud, Russian izumrud, Turkish zümrüt) reflects the un-Persian initial cluster sm- (s- > z- by voicing before m, -gd- > -rd/-rrd). Arabic zumurrud is then a loan FROM Persian (Wiktionary), not its source; etymonline likewise gives Persian zumurrud as the source of Turkish and Russian without an Arabic step. Modern sources therefore reverse the chart's Arabic → Persian edge; the ultimate origin (Semitic b-r-q via Greek), which KLN:514 also gives, is not in doubt.\",\n         \"sources\": [W+\"%D8%B2%D9%85%D8%B1%D8%AF\", E+\"emerald\", \"https://languagehat.com/emerald/\"]},\n        {\"id\": 7, \"lang\": \"Latin\", \"words\": \"smaragdus\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Latin smaragdus (m./f.), Pliny, Vulgate — a direct borrowing of Greek σμάραγδος with Greek -os rendered by the Latin 2nd-declension -us. In Vulgar/Medieval Latin it became smaralda, smaraldus, esmaraldus (with -gd- > -ld- by dissimilation and a prothetic e- before the s+consonant cluster), the source of all Romance forms.\",\n         \"sources\": [W+\"smaragdus\", E+\"emerald\"]},\n        {\"id\": 8, \"lang\": \"English\", \"words\": \"smaragdite\", \"verdict\": \"confirmed\",\n         \"derivation\": \"smaragdite 'a green foliated amphibole found in eclogite/gabbro' is a learned mineralogical coinage (French smaragdite, H.-B. de Saussure, 1796) from Latin smaragdus + the mineral suffix -ite (< Greek -ītēs), named for its emerald-green colour; English from French in the early 19th c. The Latin → English edge is via scientific French, with no Old French step.\",\n         \"sources\": [W+\"smaragdite\"]},\n        {\"id\": 9, \"lang\": \"Old French\", \"words\": \"esmeralde\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Old French esmeraude (12th c.), with the variants esmeralde, esmeragde, smaralde listed by Wiktionary, from Vulgar Latin *smaralda/*smaraldus (< Latin smaragdus): prothetic e- before s+C, -gd- > -ld- > -ud- (vocalisation of l before a consonant gives the standard esmeraude), so esmeralde is the conservative form; Modern French émeraude.\",\n         \"sources\": [W+\"esmeraude\", E+\"emerald\"]},\n        {\"id\": 10, \"lang\": \"English\", \"words\": \"emerald\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Middle English emeraude (c. 1300) from Old French esmeraude; the modern spelling emerald with -ld restored (after Medieval Latin esmaraldus / Old French esmeralde) appears from the 15th–16th c. AHD: 'Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos'.\",\n         \"sources\": [E+\"emerald\", \"https://ahdictionary.com/word/search.html?q=emerald\"]},\n        {\"id\": 11, \"lang\": \"Sanskrit\", \"words\": \"marakata\", \"verdict\": \"plausible\",\n         \"derivation\": \"Sanskrit marakata (n.) 'emerald' (Pali marakata, Prakrit maragaya; hence Tamil marakatam, Thai morakot, Tibetan mar gad) is a genuine word and, as the chart implies, ultimately of Semitic origin; Wiktionary labels it 'from Semitic', linking it with Greek σμάραγδος. But the immediate source is debated: Noonan and the classicists (Chantraine, Beekes, Mayrhofer) treat marakata as a late loan from Greek smaragdos (loss of initial s-, -gd- > -k-t-), i.e. Greek rather than the Semitic root directly; older scholarship (still echoed in some sources) even took Sanskrit as the source of the Semitic words, which is now rejected. So 'from the Semitic root' is right in ultimate origin but the direct edge Semitic → Sanskrit is uncertain.\",\n         \"sources\": [W+\"%E0%A4%AE%E0%A4%B0%E0%A4%95%E0%A4%A4\", \"https://languagehat.com/emerald/\", E+\"emerald\"]}\n      ]\n    }\n  ]\n}\n\np345 = {\n  \"pdf_page\": 345, \"book_page\": 315,\n  \"verified_by\": \"claude-fable-5-1\", \"verified_on\": \"2026-09-04\",\n  \"entries\": [\n    {\n      \"entry\": 0, \"root\": \"Murvârît\", \"verdict\": \"confirmed\",\n      \"modern_form\": \"Middle Persian murwārīd (Book Pahlavi mwlwʾlyt', Manichaean mwrwʾryd) 'pearl' < Old Persian *margārīta- < Proto-Iranian *mŕ̥ga-ahri-ita- 'born of the (sea-)bird's shell, oyster'\",\n      \"note\": \"Pahlavi murwārīd 'pearl' is real (MacKenzie 1971/1986; Nourai's -t reflects the Pahlavi spelling -yt'); gloss 'small pearl' is slightly narrow — MacKenzie simply 'pearl'. Modern scholarship (Wiktionary, Beekes s.v. μαργαρίτης, Encyclopaedia Iranica 'Greek loanwords in Middle Iranian') agrees the Iranian word is the SOURCE and Greek margaritēs the loan, so the chart's direction is right and the Borhan-e Qate' note (Persian from Greek) is rejected. One caveat: Greek margaritēs is already in Theophrastus (4th c. BCE), so the actual donor was Old Iranian *margārīta-, not Middle Persian proper; and the Aramaic/Arabic marjān branch runs through Greek (Syriac margānīṯā < Greek), not straight from Pahlavi. English margarine, Margarita and Rita do not pass through Old French.\",\n      \"sources\": [W+\"%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF\", W+\"%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82\", E+\"Margaret\"],\n      \"nodes\": [\n        {\"id\": 1, \"lang\": \"Persian\", \"words\": \"morvârîd\", \"verdict\": \"confirmed\",\n         \"derivation\": \"New Persian morvārīd مروارید continues Middle Persian murwārīd (mwlwʾlyt' / mwrwʾryd) unchanged apart from vowel adjustment; Parthian morγārīd, Sogdian mrγʾrt, Khotanese mrāhe are cognates, all from Old Iranian *margārīta-, which Beekes analyses as *mŕ̥ga-ahri-ita- 'oyster', literally 'born from the shell of a (sea-)bird' (*mr̥ga- 'bird', cf. Av. mərəγa-). Attested throughout classical poetry (Hafez, 14th c., in the chart). The NOTE that Borhan-e Qate' derives it from Greek is the reverse of the modern consensus: the Greek word is the borrowing (Wiktionary; Encyclopaedia Iranica 'Greece xiii': 'most probably not borrowed from Greek margarítēs, but the borrowing may rather have functioned the other way around').\",\n         \"sources\": [W+\"%D9%85%D8%B1%D9%88%D8%A7%D8%B1%DB%8C%D8%AF\", W+\"%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82\", E+\"Margaret\"]},\n        {\"id\": 2, \"lang\": \"Aramaic\", \"words\": \"\", \"verdict\": \"plausible\",\n         \"derivation\": \"Pass-through node: the Aramaic word is Jewish Aramaic מַרְגָּנִיתָא / Syriac ܡܪܓܢܝܬܐ margānīṯā 'pearl' (with -n- for the Greek/Iranian -r-; dissimilation r…r > r…n). Wiktionary derives it from Greek μαργαρίτης, which in turn is the Iranian loan, so the ultimate source is the Iranian word as the chart says, but the immediate parent should be Greek rather than Pahlavi (a direct Iranian → Aramaic borrowing in the Achaemenid/Parthian period is not excluded but is not what the sources give).\",\n         \"sources\": [W+\"%DC%A1%DC%AA%DC%93%DC%A2%DC%9D%DC%AC%DC%90\", W+\"%D9%85%D8%B1%D8%AC%D8%A7%D9%86\"]},\n        {\"id\": 3, \"lang\": \"Arabic\", \"words\": \"mardjân\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Arabic marjān مَرْجَان 'small pearls; coral' (collective; unit noun marjāna) is borrowed from Classical Syriac margān 'pearl-like' / margānīṯā 'pearl' (Wiktionary), with Syriac g > Arabic j regularly. It is Qur'anic (55:22, 55:58 lu'lu' wa-l-marjān), where commentators already waver between 'small pearls' and 'coral' — the source of the double gloss. So the edge Aramaic → Arabic is confirmed.\",\n         \"sources\": [W+\"%D9%85%D8%B1%D8%AC%D8%A7%D9%86\", W+\"%DC%A1%DC%AA%DC%93%DC%A2%DC%9D%DC%AC%DC%90\"]},\n        {\"id\": 4, \"lang\": \"Persian\", \"words\": \"marjân\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Persian marjān مرجان 'coral' (also the female name Marjan) is borrowed from Arabic marjān, keeping only the 'coral' sense (Wiktionary: Persian and Ottoman Turkish 'adopted the Arabic term to mean coral specifically'); attested in Hafez alongside lu'lu' 'pearl' as in the chart's line. This is an Iranian → Greek → Aramaic → Arabic → Persian round trip, so morvārīd and marjān are doublets in Persian.\",\n         \"sources\": [W+\"%D9%85%D8%B1%D8%AC%D8%A7%D9%86\"]},\n        {\"id\": 5, \"lang\": \"Greek\", \"words\": \"margarites\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Greek μαργαρίτης (λίθος) margarítēs 'pearl' (first in Theophrastus, De lapidibus 36, 4th c. BCE; also μάργαρον) is, per Wiktionary/Beekes, a loan from Indo-Iranian, specifically the Old Iranian ancestor (*margārīta-) of Middle Persian murwārīd, with the Greek agent/material suffix -ίτης substituted for the Iranian ending; etymonline: 'from some Oriental language, most likely Iranian; cf. Middle Persian marvarit'. The edge is right in direction; only the label 'Pahlavi' for the donor is anachronistic (the loan predates Middle Persian).\",\n         \"sources\": [W+\"%CE%BC%CE%B1%CF%81%CE%B3%CE%B1%CF%81%CE%AF%CF%84%CE%B7%CF%82\", E+\"Margaret\"]},\n        {\"id\": 6, \"lang\": \"Latin\", \"words\": \"\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Pass-through node: Latin margarīta 'pearl' (Cicero, Pliny; Vulgate Matt. 13:45–46 'pretiosa margarita'), a direct loan of Greek margarítēs with the Greek masculine -ítēs re-shaped as a Latin 1st-declension feminine -īta; Late Latin also as the female name Margarita.\",\n         \"sources\": [W+\"margarita\", E+\"Margaret\"]},\n        {\"id\": 7, \"lang\": \"Old French\", \"words\": \"\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Pass-through node: Old French margarite / marguerite 'pearl' and the name Margarete/Marguerite (12th–13th c.) from Latin margarīta (regular -a > -e, Latin g kept before a); Old French is the channel for English margarite, Margaret and Margery, but not for margarine, Margarita or Rita (see node 8).\",\n         \"sources\": [E+\"Margaret\", W+\"margarite\"]},\n        {\"id\": 8, \"lang\": \"English\", \"words\": \"margarite, margarine, Margaret, Marjorie, Margarita, Maggie, Rita\", \"verdict\": \"confirmed\",\n         \"derivation\": \"All seven go back to Greek margarítēs/Latin margarīta, but by different routes: margarite — Middle English 'pearl' (obsolete) from Old French margarite; the modern mineral sense (a calcium mica, 1820s) is a learned re-use with -ite. margarine — French margarine, coined by Chevreul (1813, acide margarique 'pearly acid', for the lustre of the crystals) from Greek margarítēs, then Mège-Mouriès' butter substitute (1869), English 1873: Greek → French → English, no Old French/Latin stage. Margaret — c. 1300 from Old French Margaret (Fr. Marguerite) < Late Latin Margarita. Marjorie — variant of Margery, the medieval vernacular (Old French Margerie) form of Margaret. Margarita — the Latin/Spanish form of the name (and the cocktail, from Spanish). Maggie — English pet form of Margaret; Rita — Spanish/Italian aphetic short form of Margarita/Margherita. So the chart's single Old French pass-through is right for margarite/Margaret/Marjorie/Maggie and only schematic for margarine, Margarita and Rita.\",\n         \"sources\": [E+\"Margaret\", E+\"margarine\", W+\"margarite\", W+\"Marjorie\", W+\"margarita\"]}\n      ]\n    },\n    {\n      \"entry\": 2, \"root\": \"M.v.t\", \"verdict\": \"confirmed\",\n      \"modern_form\": \"Proto-Semitic *mawt- 'death', root m-w-t 'to die' (Arabic māta, yamūtu; AHD Semitic roots mwt)\",\n      \"note\": \"The root is real (Proto-Semitic *mawt-; Akk. mūtu, Heb. māweṯ, Aram. mawtā, Ar. mawt) and is Common Semitic rather than specifically 'Arabic', though the Arabic reflex is what feeds Persian and Europe. The chart's two European branches diverge from modern scholarship: (a) Latin mattus 'drunk, sodden' cannot come from Arabic māt — it is attested in Petronius (1st c. CE) and is derived by Pokorny 694, de Vaan and Wiktionary from *maditus (madēre 'be wet'), PIE *meh₂d-; Nourai's own NOTE records this and modern scholarship sides with Pokorny/AHD; (b) the chess word French mat / échec et mat does come from Persian šāh māt via Arabic, but not through Latin mattus as drawn (its parent should be node 2/Arabic). Also, the māt of šāh māt is by Wiktionary's account native Persian 'stunned, at a loss', reinterpreted in Arabic as māta 'he died', so the whole Persian mât node sits awkwardly under an Arabic root. Spanish matar is of disputed origin (Latin mactāre or mattus preferred; Arabic/Persian māt is a competing minority view).\",\n      \"sources\": [W+\"%D9%85%D9%88%D8%AA\", AHD_SEM, W+\"mattus\", E+\"checkmate\"],\n      \"nodes\": [\n        {\"id\": 1, \"lang\": \"Arabic\", \"words\": \"maot\", \"verdict\": \"confirmed\",\n         \"derivation\": \"Arabic mawt مَوْت 'death' is the verbal noun (maṣdar) of the hollow verb māta / yamūtu 'to die', root m-w-t, from Proto-Semitic *mawt- (Wiktionary; cognates Akk. mūtu, Heb. māweṯ, Syr. mawtā). 'maot' is simply Nourai's rendering of mawt (aw diphthong).\",\n         \"sources\": [W+\"%D9%85%D9%88%D8%AA\", W+\"%D9%85%D8%A7%D8%AA\"]},\n        {\"id\": 2, \"lang\": \"Persian\", \"words\": \"mawt, mowt; mayyet; mât; kîš-mât\", \"verdict\": \"plausible\",\n         \"derivation\": \"mawt/mowt موت 'death' — borrowed from Arabic mawt, Iranian pronunciation mowt (Wiktionary); mamāt ممات is the Arabic maṣdar mīmī of the same verb, also borrowed: confirmed. mayyet میّت 'dead person' — Arabic mayyit, a CaCīC adjective of m-w-t (*mawīt > *mayīt > mayyit by assimilation), borrowed as a noun into Persian: confirmed. māt مات 'dead, dull; stunned, confused' — Wiktionary gives two views: Arabic māta 'he died' (the traditional one, Nourai's) or a native word connected with Sanskrit/Iranian 'measured, traversed', with the meaning 'stunned' reinforced by the chess use; unresolved. kīš-māt / šāh-māt کیش مات 'checkmate' — Wiktionary analyses šāh-māt as Persian 'the king is stunned/helpless', with Arabic speakers re-etymologising māt as 'died' before the phrase reached Europe; Barnhart and etymonline give the same alternative. So the Arabic derivation of māt/šāh-māt is the classical account but not the only modern one; node verdict follows the weakest word.\",\n         \"sources\": [W+\"%D9%85%D9%88%D8%AA\", W+\"%D9%85%D9%8A%D8%AA\", W+\"%D9%85%D8%A7%D8%AA\", W+\"%D8%B4%D8%A7%D9%87%E2%80%8C%D9%85%D8%A7%D8%AA\", E+\"checkmate\"]},\n        {\"id\": 3, \"lang\": \"Latin\", \"words\": \"mattus\", \"verdict\": \"disputed\",\n         \"derivation\": \"Latin mattus (also mātus) 'drunk, maudlin; sodden, dull' is attested in Petronius (Satyricon 41, 1st c. CE) — six centuries before any Arabic contact — so it cannot derive from Arabic/Persian māt. The standard etymology (Pokorny IEW 694 s.v. mad-, de Vaan, Wiktionary) is *maditus 'wetted' (past participle of madēre 'to be wet, be drunk', PIE *meh₂d-, cf. Skt. mattá- 'drunk') with syncope and assimilation -dt- > -tt-. Nourai's own NOTE ('POK:694 derives mattus from Mad: wet') records the correct view; modern scholarship is unanimous on Pokorny's side, and Nourai's FSD (Funk & Wagnalls) source is superseded. The parent edge Persian māt → Latin mattus is therefore rejected.\",\n         \"sources\": [W+\"mattus\", E+\"matte\", \"https://ahdictionary.com/word/indoeurop.html\"]},\n        {\"id\": 4, \"lang\": \"French\", \"words\": \"mat\", \"verdict\": \"plausible\",\n         \"derivation\": \"French mat 'matte, dull, without lustre' continues Old French mat 'beaten down, withered, dejected; dull' (12th c.), which Wiktionary and TLF derive from Latin mattus 'sodden, dull' — so the edge Latin mattus → French mat is the majority view and is right as drawn; etymonline adds the alternative that the Old French adjective is a transferred use of chess mat 'checkmated' (from Arabic šāh māt), in which case this word would after all descend from node 2 (but not through Latin). Either way it does not go back to Arabic through Latin.\",\n         \"sources\": [W+\"mat#French\", E+\"matte\", W+\"mattus\"]},\n        {\"id\": 5, \"lang\": \"English\", \"words\": \"mat 1\", \"verdict\": \"confirmed\",\n         \"derivation\": \"English mat/matte 'dull, lustreless' (1640s) is borrowed from French mat; the spelling matte was not standardised until the 20th c. AHD:805 (the chart's NOTE) refers it to the IE root mad- 'wet' via Latin mattus — which, as with node 3, is the modern consensus; the French → English edge itself is uncontroversial.\",\n         \"sources\": [E+\"matte\"]},\n        {\"id\": 6, \"lang\": \"French\", \"words\": \"mat; e'chec et mat\", \"verdict\": \"disputed\",\n         \"derivation\": \"Old French mat 'checkmated, defeated' (12th c.; verb mater 'to checkmate, overcome') and the phrase eschec mat > Modern French échec et mat are the chess term, from Arabic šāh māt (Persian šāh māt 'the king is stunned/helpless', re-read in Arabic as 'the king is dead'), which reached the Romance languages with chess itself through Muslim Spain and Sicily in the 10th–11th c. (Spanish jaque mate, Italian scacco matto, Medieval Latin scaccum mattum). The chart draws this French mat from Latin mattus 'drunk' — that edge is wrong: the checkmate word is an Arabic/Persian loan and should hang directly from node 2 (Persian/Arabic māt), as Nourai's own NOTE ('debatable paths') half-concedes. Its ultimate Semitic vs. Persian identity is the open question discussed at node 2.\",\n         \"sources\": [E+\"checkmate\", W+\"mat#French\", W+\"%D8%B4%D8%A7%D9%87%E2%80%8C%D9%85%D8%A7%D8%AA\", AHD_SEM]},\n        {\"id\": 7, \"lang\": \"English\", \"words\": \"mate 2; checkmate\", \"verdict\": \"confirmed\",\n         \"derivation\": \"English mate (v.2) 'to checkmate; to overcome, confound' (c. 1300) from Old French mater 'to checkmate, defeat' (< mat); mate (n.2) 'checkmate' likewise c. 1300 from Old French mat; checkmate (mid-14th c.) from Old French eschec mat, ultimately Arabic šāh māt. The figurative 'to thwart' sense is late-14th-c. AHD Semitic roots mwt lists exactly these two English derivatives.\",\n         \"sources\": [E+\"mate\", E+\"checkmate\", AHD_SEM]},\n        {\"id\": 8, \"lang\": \"Spanish\", \"words\": \"matar; matador\", \"verdict\": \"plausible\",\n         \"derivation\": \"Spanish matar 'to kill' (also Portuguese, Catalan) is of disputed origin. Wiktionary: 'most likely from Latin mactāre (through a Vulgar Latin *mattāre)', alternatively from Late Latin mattus 'drunk, stupefied' (*mattāre 'to stun'), or influenced by Arabic māta 'to die'; RAE likewise prefers Vulgar Latin *mattare < mattus. Etymonline notes the phonological difficulty of mactāre (expected *mechar) and gives Arabic māta (borrowed from Persian māt) as the alternative — the view Klein (KLN:946, Nourai's source) adopts and Corominas discusses via the chess word. So the Arabic derivation is a real scholarly option but not the preferred one. matador 'killer; the bullfighter who kills the bull' is transparently matar + agent suffix -dor (Latin -tōrem): confirmed as a derivative.\",\n         \"sources\": [W+\"matar\", E+\"matador\", W+\"matador\"]},\n        {\"id\": 9, \"lang\": \"French\", \"words\": \"matador\", \"verdict\": \"confirmed\",\n         \"derivation\": \"French matador is borrowed from Spanish matador in the late 17th–18th c. with the bullfighting vocabulary (Wiktionary: 'Borrowed from Spanish matador'); form unchanged.\",\n         \"sources\": [W+\"matador\", E+\"matador\"]},\n        {\"id\": 10, \"lang\": \"Persian\", \"words\": \"mâtâdor\", \"verdict\": \"plausible\",\n         \"derivation\": \"Persian mātādor ماتادور (the chart's spelling ماتادُر marks the short o) is a 20th-c. loan; Wiktionary labels it 'borrowed from Spanish matador', whereas Nourai (following Mo'in, MON:3678) routes it through French, which was the usual channel for European words into Persian in that period and is phonetically indistinguishable here. Both routes are compatible; the immediate donor cannot be decided from the form.\",\n         \"sources\": [W+\"%D9%85%D8%A7%D8%AA%D8%A7%D8%AF%D9%88%D8%B1\"]},\n        {\"id\": 11, \"lang\": \"English\", \"words\": \"matador\", \"verdict\": \"confirmed\",\n         \"derivation\": \"English matador (1670s) is borrowed directly from Spanish matador 'killer', agent noun of matar; also used from 1730s for the top trump cards in ombre/quadrille (Spanish card games).\",\n         \"sources\": [E+\"matador\", W+\"matador\"]}\n      ]\n    }\n  ]\n}\n\nfor page, data in ((101, p101), (345, p345)):\n    path = f\"/home/sfmqrb/git/rishe/data/verification/page-{page}.json\"\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        json.dump(data, f, ensure_ascii=False, indent=2)\n        f.write(\"\\n\")\n    print(path)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/write_101_345.py && for p in 101 345; do python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-$p.json > /dev/null && echo \"page-$p valid\"; done\npython3 - <<'EOF'\nimport json, collections\nfor p in (101, 345):\n    d = json.load(open(f\"/home/sfmqrb/git/rishe/data/verification/page-{p}.json\"))\n    src = json.load(open(f\"/home/sfmqrb/git/rishe/data/extracted/batch/page-{p}.json\"))\n    c = collections.Counter()\n    for e in d[\"entries\"]:\n        c[e[\"verdict\"]] += 1\n        ids = {n[\"id\"] for n in e[\"nodes\"]}\n        srcids = {n[\"id\"] for n in src[\"entries\"][e[\"entry\"]][\"nodes\"]}\n        assert ids == srcids, (p, e[\"entry\"], ids ^ srcids)\n        for n in e[\"nodes\"]: c[n[\"verdict\"]] += 1\n    print(p, dict(c))\nEOF",
 "description": "Write and validate verification JSON for pages 101 and 345"
}
```


### [2026-09-04T14:36:27.332Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/page-101.json
/home/sfmqrb/git/rishe/data/verification/page-345.json
page-101 valid
page-345 valid
101 {'confirmed': 15, 'plausible': 7, 'transcription_suspect': 1, 'disputed': 1}
345 {'confirmed': 14, 'plausible': 5, 'disputed': 2}
```


## [2026-09-04T14:36:41.693Z] AGENT

Both files written and validated with `python3 -m json.tool`; every node id in the source JSON is covered.

**page-101.json** (book p. 71; 2 roots + 22 nodes): confirmed 15, plausible 7, disputed 1, transcription_suspect 1
- transcription_suspect — B.r.q, Greek "smaraldos": Greek is σμάραγδος *smaragdos*; the -ld- is a misread of the -gd- cluster (Klein 514 prints smaragdos). Semitic origin itself is confirmed (AHD, Beekes, Wiktionary).
- disputed — B.r.q, Persian zomorrod (parent Arabic): Wiktionary/MacKenzie give Greek → Middle Persian *uzumburd* → NP zumurrud → Arabic; the chart's Arabic → Persian edge is reversed (MP form is pre-Islamic).
- Notable plausibles: Akkadian karâbu and Hebrew kerubh under b-r-k rest on the krb/brk metathesis (AHD and Klein endorse it; SAHD/Mitchell reject it); Greek gryps < kerubh is a Klein/Beekes minority view absent from AHD's griffin entry; Akkadian "baraqtu: lightning" is really barraqtu 'emerald' (lightning is birqu).

**page-345.json** (book p. 315; 2 roots + 19 nodes, redirect Mus skipped): confirmed 14, plausible 5, disputed 2
- disputed — M.v.t, Latin mattus (parent Persian māt): attested in Petronius, 1st c. CE; Pokorny 694/de Vaan/Wiktionary derive it from *maditus (madēre), PIE *meh₂d-. The chart's own NOTE is the correct side.
- disputed — M.v.t, French mat "defeated" / échec et mat (parent Latin mattus): the chess word is from Arabic šāh māt (Persian šāh-māt) via Muslim Spain, not from Latin; should hang from the Persian/Arabic node.
- Notable plausibles: Persian māt / kīš-māt — Wiktionary treats šāh-māt as native Persian 'the king is stunned', re-etymologised in Arabic as 'died'; Spanish matar — Latin mactāre/mattus preferred, Arabic māt a minority view; Aramaic marganita comes via Greek, not directly from Pahlavi. Root Murvârît confirmed: modern sources reverse BQT and make Greek margaritēs the loan from Iranian.
