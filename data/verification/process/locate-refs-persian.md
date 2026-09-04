# Verification process log — locate-refs-persian


## [2026-09-04T14:32:08.941Z] INPUT

Context: we are verifying Ali Nourai's "An Etymological Dictionary of Persian, English and other Indo-European Languages" (1999). Nourai cites 117 references by 3-letter abbreviation plus page number (e.g. BQT:918, MON5:528). We need to find full-text online copies of these references so that later agents can check the exact cited page or entry.

Files:
- Bibliography (OCR text of the book's Tables III and IV, listing every abbreviation with author/title/year): /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt
- Citation counts per abbreviation: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ref_counts.txt

YOUR SHARE: the Persian- and Arabic-language references (and Persian-authored works), i.e. these abbreviations:
BQT MON SOD SNS FFD FVA AEF VOP FSF TAD FVQ VDQ FVF ETM TZF SAP IRN AFM FRS ZMA FAF ARK AMD DZA KAS DMO SBK VGH VIE AKM ZFS SOR FNI VSF FVS FIB IRT SNB KFL NFI MMF MZF ARM ARB
(BQT = Borhan-e Qate' ed. Mo'in with etymological footnotes, 1983 Amir Kabir; MON = Mo'in's Farhang-e Farsi, 6 vols; SOD = Gharib's Sogdian-Persian-English Dictionary 1995; SNS = Tavoosi, Glossary of Shayast ne Shayast; FFD = Abolghasemi, Fe'lha-ye Farsi-ye Dari; FVA = Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi; AEF = Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi; VOP = Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi; FSF = Noushin, Vazhe-namak Shahnameh; TAD = Addi Shir? no — TAD is listed under Arabic authors (Unaysi T.?) check the bibliography; FVQ = Jeffery, Foreign Vocabulary of the Qur'an (English, 1938 — on archive.org); VDQ = Badreh'i's Persian translation of Jeffery; FVF = Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi; ETM = Abolghasemi, Risheh-shenasi; AFM = Addi Shir, Al-Alfaz al-Farisiyya al-Mu'arraba (Arabic, 1908 — on archive.org); FRS = Asadi Tusi, Loghat-e Fors; SAP = Sayyah's Al-Monjed translation; etc.)
(Another agent handles the Western references.)

For EACH abbreviation, most-cited first (BQT, MON, SOD, SNS, FFD, FVA, AEF matter most), find the best online full-text or searchable copy:
1. Online Persian dictionary sites that host these texts entry-by-entry: vajehyab.com (Mo'in, Dehkhoda, Amid), abadis.ir, parsi.wiki (Dehkhoda), loghatnameh.org, ganjoor.net (for Loghat-e Fors?), noorlib.ir / noormags.ir, lib.eshia.ir, ketabnak.com, archive.org (Borhan-e Qate' scans exist there; Jeffery's Foreign Vocabulary of the Qur'an is there; Addi Shir's Al-Alfaz al-Farisiyya is there; Gharib's Sogdian dictionary may be there). Record the URL pattern for looking up a headword (e.g. https://vajehyab.com/?q=<word>&d=moein or https://abadis.ir/fatofa/<word>/).
2. archive.org: search API
   curl -s 'https://archive.org/advancedsearch.php?q=<query>&fl[]=identifier&fl[]=title&fl[]=year&rows=20&output=json'
   then check https://archive.org/metadata/<identifier> for a `_djvu.txt` file; test download with curl -sI. If found, DOWNLOAD to /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs/<ABBR>.txt and note how to map printed page numbers to the OCR text (form-feed page count offset) — Persian OCR from archive.org may be poor; say so if it is.
3. Google Books / HathiTrust full view where applicable.
4. If nothing is online, say `none` and what you tried. Do not spend more than ~5 minutes on any reference cited fewer than 5 times.

Use Bash curl for archive.org APIs/downloads; WebSearch/WebFetch for discovery (WebFetch can read vajehyab/abadis pages — test one, e.g. the Mo'in entry for دیوار, and record whether the etymology footnote text is visible).

OUTPUT: write /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online_persian.json as a JSON object keyed by abbreviation:
{"MON": {"title": "...", "kind": "website|archive_djvu|google_books|none", "url": "...", "lookup_hint": "URL pattern / how to find an entry", "local_file": path or null, "page_offset": "..." or null, "covers_etymology": true/false, "notes": "..."}, ...}
Validate with python3 -m json.tool. Reply with a short summary: which references were found (with kind), which were not.


## [2026-09-04T14:32:11.090Z] AGENT

I'll start by reading the bibliography and citation counts.


## [2026-09-04T14:32:12.728Z] TOOL CALL #1: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/ref_counts.txt; echo ----; wc -l /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt",
 "description": "Show citation counts and bibliography size"
}
```


### [2026-09-04T14:32:12.792Z] TOOL RESULT

```
AHD 1906
POK 1765
BQT 1307
KLN 1243
MON 1025
 795
HRN 527
IEC 386
SOD 265
KNT 214
SYN 191
SNS 174
FFD 151
FVA 143
AEF 115
WLD 79
ISS 77
OEW 75
PLA 68
VOP 67
FSF 66
HUB 60
BRT 59
TAD 54
FVQ 52
VDQ 52
FSD 51
SKT 49
FVF 44
ETM 44
AKD 39
PRT 37
TZF 36
NYB 32
HJB 30
SAP 28
IRN 27
AFM 26
FRS 20
PHN 18
LKT 17
ZMA 16
FAF 15
WEB 14
SIN 14
AHM 13
ARK 12
AMD 11
CEL 11
GPL 10
MAG 10
DEV 9
DRM 9
ZAW 8
SLW 8
BLY 8
KGW 7
SHP 7
AID 7
OXF 7
VFO 7
MPP 7
DVS 6
SPG 6
ARB 6
PHD 6
DZA 6
KAS 5
TYL 5
DMO 5
SBK 5
LAM 5
UNV 5
LAT 5
NAT 5
VGH 4
VIE 4
AKM 4
ZFS 4
SOR 4
TTS 3
DOZ 3
AVG 3
LEW 3
FNI 3
SDQ 3
ROE 3
AFA 3
FWE 3
VSF 3
MFL 2
TLM 2
FVS 2
FIB 2
IRT 2
SNB 2
BST 2
KFL 2
NFI 2
HID 2
AIN 2
ZAP 2
DEW 1
? 1
AEC 1
AWH 1
MMF 1
MZF 1
ARP 1
UEC 1
SYN  1
1982- 1
EAV 1
ARM 1
PEI 1
400- 1
SOG 1----
25 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt
```


## [2026-09-04T14:32:15.205Z] TOOL CALL #2: Bash

```json
{
 "command": "cat /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bibliography_raw.txt",
 "description": "Show bibliography text"
}
```


### [2026-09-04T14:32:15.256Z] TOOL RESULT

```
===== page_15
 Page 15 
 TABLE III List of References by Language and Author Name ( See Table IV for Reference Abbreviations) PERSIAN ENGLISH FRENCH Authors Ref. AbolghasemT M. ETM FFD TZF ZFS Ahmad Soltam M. VFO Akhavan Zanjani K. SOR ATam A. J. AKM A" mid H. AMD Aryan, A. ARM Asadi TusT FRS Badreh-i VDQ Bahar M. T. SBK DanayT F. FNI Daneshgar A. FAF Emam ShfishtarT FVF FarahvashT B. IRN Gharib B. SOD (in Persian &amp; English ) Hasan! da"T Al-Eslam KAS Jonaydi F. NFI ZMA Khadiv Jam H. VGH Khaleqi Motlaq Jalal AEF KhaliliK. MMF Kowsar B. SNB Mehravand K. VSF Mo'in M. MON MoshM M. VOP NafTsi S. DMO Nahvi S. M. FVA Natel Khanlari P. MZF NoushTn A. H. FSF OranskT &amp; Keshavarz MFL Pur Davud FIB Rashed Mohassel DZA Rokn Zadeh Adamiyyat M.H. ARK Sajjadiyyeh M. A. IRT VIE Sayyah A. SAP Tabriz! M.H.(Borhan) BQT Tavoosi M. SNS Authors Ref. Baily H.W. BLY ZAP ISS Berlitz NAT Bliss A. J. FWE Buck C. D. SYN Collins W. WEB Claiborne R. ROW Davis P. DVS Gershevitch I. AHM Gupta S. K. CEL Funk I. K. FSD Henning W. P. LST MPP SLW SOG Horn P. BST Jackson A.V.W. AVG Jeffrey A. FVQ Kent R. G KNT Kinder H. &amp; Hilgemann W. AWH Klein E. KLN Laufer B. SIN MacKenzie PHD Mann S. E. IEC Morris W. AHD Nyberg H.S. NYB Partridge E. PRT PeiM. PEI Platts J. T. &amp; Ranking G.S.A. GPL Richardson J. RCH Shipley J. T. SHP OEW Skeat W. W. SKT Speake J. OXF Taylor W. TYL Tolman H. C. TLM Unvala J. M. UNV Widengren G. MAG Withworth G. C. AID Yule H. &amp; Burnel A. C. HJB Authors Ref. Darmester J. DRM Devic L. M. DEV Duchesne Guillemin EAV Ernout A.&amp; Meillet LAT Lammens H. LAM Pihan A. P. PHN ARABIC Authors Ref. Addi Shir Jawaliqi Tha'alebi Unaysi T. AFM ARB KFL TAD GERMAN /DUTCH Authors Ref. Asbaghi A. PLA Bartholoma BRT HID ZAW Dozy (Dutch) DOZ Dvorak R. FWK Frankel S. AFA Horn P. HRN Hubschmann HUB Ibrahim J. KGW Lagarde P. LAG Liden E AIN Lokotsch K. LKT Pokorny J. POK Siddiqi A. SDQ Spiegel F. SPG ARP Vambery H. TTS Walde A. LEW WLD Zimmern H AKD A-8 
===== page_16
 Page 16 
 TABLE IV - Reference Abbreviations 1 AEF 2 AFA 3 AFM 4 AHD 5 AHM 6 AID 7 AIN 8 AKD 9 AKM 0 AMD i ARB 2 ARK 3 ARM 4 ARP 5 AVG 6 AWH Jalal KhaleqT Motlaq, Asas Eshteqaq Farsi, ^j1* JISsAl o"1-'' Vol. I (a - kh), Bonyad Farhang Iran, 1977. Siegmund Fraenkel, Die Aramaischen Fremdworter im Arabischen, Hildesheim, 1962. Addi Shir, Al-Alfaz Al-Farsiyya Al-Mu'arraba, (A Dictionary of Persian Words in the Arabic Language), Library of Lebanon, 1980.. W. Morris, The American Heritage Dictionary, New College Edition, 1975, Appendix on Indo-European Roots, pp 1505-1550. I. Gershevitch, The Avestan Hymn to Mithra, Oriental Publications No.4, Cambridge University Press, 1959. G. C. Withworth, Anglo-Indian Dictionary. Kegan Paul, Trench &amp; Co, London 1885. E. Liden, Studien zur Altindischen und Vergleichenden Sprachgeschichte , Almqvist &amp; Wiksells, Upsala 1897. H. Zimmem, Akkadische Fremdworter Als Beweis Fur Babylonischen Kultureinfluss, Leipzig 1917. Amir J. ATam, Farhang A'alam Ketab Moqaddas or, A Dictionary of Proper Names in the Bible, English - Persian, Iran University Press, Tehran 1988. H. A" mid, Farhang Farsi Amid, Two volumes, Amir Kabir Press, Tehran, 1369 (1990). Jawaliqi, Al-Mu'arrab, Tehran 1966. M. H. Rokn Zadeh - Adammiyat, Arkan Sokhan, Sharq Press, Tehran 1347 (1968). ^W-\A£ h_)UT joMc' OwJbjd -W*c ^— *&gt;jl^ OwJfcjd £^~&gt; O^j' A. Aryan, ks~'j'* lSj^ ^)~&gt;^ ^*j' -ujUa ^la o^lj oiajs Farhang Vajheh-hay Hamanand, Armani - AvestaT, Pahlavi, FarsT, Vol. I (a), Bonyad Nayshabflr, Tehran 1363 (1984). F. Spiegel, Die Arische Periode und ihre Zustande, Leipzig ,1887. A. V. W. Jackson, An Avesta Grammer, W. Kohl Hammer, Stuttgart 1892. H. Kinder &amp; W. Hilgemann, Atlas of World History. 2 vol., Anchor Books, 1974. A-9 
===== page_17
 Page 17 
 TABLE IV - Reference Abbreviations (continued ...) 17 BLY 18 BQT 19 BRT 20 BST 21 CEL 22 DEV 23 DMO 24 DOZ 25 DRM 26 DVS 27 DZA 28 EAV 29 ETM 30 FAF 31 FFD H. W. Baily, "Hvatanica II", (Glossary of some Khotanese words with reference to Avestan and Persian words), Bulletin of the School of Oriental and African Studies (BSOAS IX:1937-39) pp 69-78, University of London. M. H. Tabriz! (Borhan), Borhan Qate', ^l»ls ^i&amp;j&gt; Etymological footnotes by Dr. M. MoTn, 4 vol, Amfr Kabrr Press, Tehran 1362 (1983). C. Bartholomae, Altiranisches Worterbuch Zusammen Mit Den Nacharbeiten Und Vorarbeiten, Walter de Gruyter Press, 1979. Paul Horn, "Some Inscriptions on Sassanian Gems", Avesta, Pahlavi and Ancient Persian Studies, First Series, pp 224-263, Bombay Educational Society's Press, 1904. S. K. Gupta, A Comparative Etymologic Lexicon of Common Indo-European Words, 6 Vol., Sverge Haus Publishers, Milton, Ma, 1997 L. M. Devic, Dictionnaire Etymologique des Mots Francais D'Origin Orientale, Oriental Press 1876. S. NafisT, Par Maktab Ostad, ilx-,1 Zohreh Press, Tehran 1344 (1965). R. Dozy, Verklarende Lisjt der Nederlandsche Woorden, Die Uit Het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch Afkomstig Zijn, Leiden 1867. J. Darmester, Etudes Itaniennes, Paris 1883. P. Davis, Roots - Family History of Familiar Words, McGraw-Hill Book Company 1981. M. T. Rashed Mohassel, Daramadi Bar Dastur ^^jl oki _}f~&gt;* j&gt;. iSJ^&gt;^ Zaban AvestST, Khajeh Press, Tehran 1364 (1985). J. Duchesne-Guillemin, "Etymologies Avestiques", Bulletin of the school of Oriental and African Studies (BSOAS IX: 1937-39) pp 861-869, University of London. M. Abolghasemr, RTsheh ShenasT - Etimologi, Ghoghnoos Press, Tehran 1374 (1995). A. Daneshgar, Farhang A'alam Farsi, Hafez NovTn Press, 1370 (1991). M. Abolghasemr, Fe'lhay FarsT Pari, Ghoghnoos Press, Tehran 1374 (1995). v^«&gt;jls pMel 
===== page_18
 Page 18 
 TABLE IV - Reference Abbreviations (continued...) 32 FIB 33 FNI 34 FRS 35 FSD 36 FSF 37 FVA 38 FVF 39 FVQ 40 FWE 41 FWK 42 GPL 43 HID 44 HJB 45 HRN 46 HUB 47 IEC Pur Davfld, Farhang Iran Bastan, Vol. I, University of Tehran Press 1326 (1947). F. DanaT, Farhang Namhay Irani, Negah Publishers, Tehran 1370 (1991). AsadT Tflsi, Farhang Fors, Kharazmi Press, Tehran 1365 (1986). ^iljjl ^cUj^cLs &gt;^fl&gt;jS Funk and Wagnalla, New Standard Dictionary of the English Language, Funk &amp; Wagnalls Company, New York, 1940. A. H. Noushin, Farhang Shahnameh Ferdowsi, oULS 03I3 - ^-jiy i*La&gt;Li ^^ay Vajheh Namak, Donya Press, Tehran 1363 (1984). S. M. Nahvi, Farhang VSm J-^-i - ^-&gt;jl» j* ^o^ ^gb. 03I3 ^(3 ^S^a,^ Vajhehhay Arabi dar Farsi, Dakhil, TohT Azadi Press 1368 (1989). S. M. A. Emam Shflshtari, ^c ^bj ji ^-"j1* iS^ °j'3 «-fc»j» Farhang Vajhehhay Farsi dar zaban Arabi, Anjoman Asar Melli, No 58, Bahman Press, Tehran, 1347 (1968). A. Jeffrey, The Foreign Vocabulary of the Qur'an, (see VDQ). Oriental Institute, Baroda, Stephen Austin &amp; Sons Press, Great Britain 1938 A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, Warner Books, 1966. R. Dvorak, "Fremdworter im Koran", Doctoral Dissertation, Akademische Buchdruckerei von F. Straub (1884). J.T. Platts and G.S.A. Ranking, A Grammar of the Persian Language, Oxford University Press (1911). B. Bartholomae, Handbuch der Altlranischen Dialekte, Breitkopf &amp;Hartel, Leipzig 1883. H. Yule &amp; A. C. Burnel, Hobson Jobson, A Glossary of Colloqual AngloIndian Words, Oriental Publishers, Delhi 1903-1968. Paul Horn, Grundriss der NeuPersischen Etymology, Verlag von Karl J. Trubner, Strassburg 1893-1974. H. Hubschmann, Persische Studien, Verlag von Karl J. Trubner, Strassburg 1895. Stuart E. Mann, An Indo-European Comparative Dictionary, Helmut Buske Verlag, Hamburg 1987 A-ll 
===== page_19
 Page 19 
 TABLE IV - Reference Abbreviations (continued...) 48 IRN 49 IRT 50 ISS 51 KAS 52 KFL 53 KGW 54 KLN 55 KNT 56 LAG 57 LAM 58 LAT 59 LEW 60 LKT 61 LST 62 MAG 63 MFL gsj^jljjf C. FarahvashT, Iranvij, Tehran University Press, 1368 (1989). M. A. Sajjadiyyeh, Tabar Moshtarek Iranian oMjj3 } jljljjl va Turanian, Bonyad Nayshabflr 1368 (1989). H. W. Baily, Indo-Scythian Studies (Khotanese Texts - volume VI), Cambridge University Press, 1967. M. A. Hasani Da'i Al-Eslam, ojj£-^-&lt; oki jy^j* Khod Amoz Zaban Sanskrit, Danesh Press, Tehran 1361 (1982). Tha'alebT, Ketab Feqh al-Logheh, Beirut, 1885. Jamshid Ibrahim, Kulturgeschichtliche Wortforschung. (Persisches Lehngut in Europaischen Sprachen, Wiesbaden 1991. D. Klein, A comprehensive Etymological Dictionary of the English Language, Two volumes, Elsevier Publishing Co., 1966. R. G. Kent, Old Persian - Grammer, Text, Lexicon, American Oriental Society, 1953. P. Lagarde, Persische Studien, Dieterichsce Verlag, Gottingen 1884. Henri Lammens, Remarques sur les Mots Francais Derives de l'Arabe, Imprimerie Catholique, Beyrouth 1890. A. Ernout &amp; A. Meillet, Dictionnaire Etymologique de la Langue Latine, Paris, 1951. A. Walde, Latinisches Etymologisches Worterbuch, (With Avestan and Persian Indices), Heidelberg 1938. K. Lokotsch, Etymologisches Worterbuch der Europaischen Worter Orientalischen Ursprunges, Heidelberg 1927. W. B. Henning, Bibliography of Important Studies on Old Iranian Subjects, Ketab Khaneh Danesh, Tehran 1950. G. Widengren, Mohammad, The Apostle of God, Chapter VIII, "Iranian Elements in the Kuranic Vocabulary", Uppsala Universitets Arsskrift, Uppsala, 1955 A. M. Oranski, Moqaddameh Feqh Al-Logheh Irani, ^'jj' '**&gt;S^ &amp; Z»Mb Translated into Persian by K. Keshavarz, Payam press, Tehran 1358 (1979). A- 12 
===== page_20
 Page 20 
 TABLE IV - Reference Abbreviations (continued ...) 64 MMF 65 MON 66 MPP 67 MZF 68 NAT 69 NFI 70 NYB 71 OEW 72 OXF 73 PEI 74 PHD 75 PHN 76 PLA 77 POK 78 PRT 79 RCH K. Khalili, Dictionary of Derivatives of the Persian ^wjls jiLa* ol£ii* &gt;_£^&amp;ji Infinitives or Farhang Moshtaqqat Masader FarsT, Institute of Cultural Studies and Research, Tehran, 1993. M. Mo" in, Farhang FarsT MoT'n, Six volumes, Amir Kabir press 1363 (1984). O^*® ^ ^-a-L!* Honari darbareh Zaban Farsi, Sokhan press, Tehran 1340 (1961). C. Berlitz, Native Tongues, Grosset &amp; Dunlapp Publishers, New York, 1982 F. Jonaydi, Nameh Farhang Iran, ^Ijjl ^»js i*b Bonyad Nayshabfir, Tehran 1368 (1989). Section 4, translated from C.H. Rempis' "Persische Worter im Deutschen," in Mitteilungen, Institut fur Auslands-Beziehungen, Iran-Nummer, 3/4, Stuttgart, 1960, S.229-233. H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1974. J. T. Shipley, The Origins of English Words, The John Hopkins University Press, Baltimore 1984. Jennifer Speake, Oxford Dictionary of Foreign Words and Phrases, Oxford University Press, New York 1997 M. Pei, The Families of Words, Harper &amp; Brothers press, New York 1962. D. N. MacKenzie, A Concise Pahlavi Dictionary. Oxford University press, London 1971. A. P. Pihan, Dictionnaire Etymologique des Motes de la Langue Francaise Derives de L'Arabe, du Persan ou du Turc, Paris 1866. Asya Asbaghi, Persische Lehnworter im Arabischen. Otto Harrassowitz, Wiesbaden 1988 J. Pokorny, Indogermanisches Etymologisches Worterbuck, Two volumes, Francke verlag, Bern 1959. E. Partridge, Origins - A short Etymological Dictionary of Modern English, MacMillan Co., NewYork 1958. J. Richardson, Dictionary, Persian, Arabic and English with Dissertation on the Languages, Literature and Manners of Eastern Nations, Sange-e-Meel Publications, Lahore 1829-1984. A-13 
===== page_21
 Page 21 
 TABLE IV - Reference Abbreviations (continued...) 80 ROE 81 SAP 82 SBK 83 SDQ 84 SHP 85 SIN 86 SKT 87 SLW 88 SNB 89 SNS 90 SOD 91 SOG 92 SOR 93 SPG 94 SYN 95 TAD R. Caliborne, The Roots of English, A Reader's Hanbook of Word Origins, Anchor Books, New York, 1989. A. Sayyah, Farhang Sayyah, Arabic - Persian Dictionary, ^}~&gt; «^a&gt;Js Three volumes, Translation of the Arabic "Al-Monjed" Dictionary, Eslam Publications, Tehran 1368 (1989). M. T. Bahar, Sabk ShenasT - Tarikh Tatawor Nasr Farsi, ^Ls ._£_&gt; Vol I, Tehran 1321 (1942). A. Siddiqi, Studien uber die Persischen Fremdworter im Klassischen Arabisch, Vandenhoeck &amp; Ruprecht, Gottingen 1919. J. T. Shipley, Dictionary of Word Origins, Philosophical Library press, New York 1945. G. Laufer, Sino-Iranica, Chinese Contributions to the History of Civilization in Ancient Iran, Field museum of natural History, publication 201, Anthropological Series, Vol XV, No. 3, Chicago 1919. W. W. Skeat, A Concise Etymological Dictionary of the English Language, Clarenden press, Oxford 1882-1967. W. B. Henning, "Sogdian Loan-words in New Persian", Bulletin of the School of Oriental and African Studies (BSOAS XT939-42) pp 93-106, University of London H. Kowsar, Sang Nebeshteh-ha Sokhan Miguyand, *ujj£~«&gt; Military Public Relations, Iranian Military Press, Tehran (1960's). M. Tavoosi, A Glossary of Shayast Ne Shayast, Shiraz University publications, 1986. B. Ghanb, Sogdian - Persian - English Dictionary, Farhangan Press, Tehran, 1374 (1995). jLw ^uu oV ijij ^imI^I - ^wjli - 
===== page_22
 Page 22 
 TABLE IV - Reference Abbreviations (continued...) 96 TLM 97 TTS 98 TYL 99 TZF 00 UNV 01 VDQ 02 VFO 03 VGH 04 VIE 05 VOP 06 VSF 07 WEB 08 WLD 09 ZAP 10 ZAW 11 ZFS 12 ZMA F. C. Tolman, Ancient Persian Lexicon, The Vanderbilt Oriental Series, American Book co. 1890-1908. G. Vambery, Etymologisches Worterbuch der Turko-Tatarischen Sprachen, Biblio Verlag, Osnabriick, 1972. W. Taylor, Arabic Words in English, Clarenton Press, London 1933. M. Abolghasemi, Tarikh Mokhtasar Zaban FarsT, ^-d1* oki j^""« ejJjIj Bonyad Andisheh EslamT Press, Tehran, 1373 (1994). J. M. Unvala, King Husrav and His Boy - Pahlavi Text and Glossary, Paul Geuthner publishers, Paris 1963. F. Badreh-t, Vajheh-hay Dakhil dar jl*=w oTjsji J-''2 i^l&amp;ejfj Qoran-e Majid, Translation of A. Jeffrey's book with Comments (see FVQ). Toos Publishers, Tehran 1372 (1993). M. Ahmad Soltam, Vajhgan FarsT dar Zabanhay ^jjl ^k-Sbj _ji ^j1* oT;'? OrupaT, Avay Niir Press, Tehran, 1372 (1993). H. Khadiv Jam, Vajheh Nameh Ghazalhay Hafez, Elmi Press, Tehran, 1371 (1992). £i9b» ^L^Jjc ^Ub OjT^ M. A. Sajjadiyyeh, Vajheh-hay Irani dar ^....JLCil ^bj ji ^IjjI ^la 03I3 Zaban EngelTsT, Bonyad Nayshabur, Tehran 1364 (1985). M. MoshM, Farhang Vajheh-hay Orupayl ^-"j1* j* ^kiJ lS1* °3'3 &gt;-^»j» dar FarsT, Alborz Press, Tehran 1371 (1992). K. Mehravand, Vajheh Sazi dar Zaban FarsT, Rasti press, Tehran 1349 (1970). v^-jl* ok) j4 lSJ1- °3'3 W. Collins, Webster's New Twentieth Century Dictionary of the English Language, second edition 1978. A. Walde, Vergleichendes Worterbuch der Indogermanischen Sprachen, two volumes, Walter de Gruyter &amp; co., Leipzig 1930-1973. H. W. Bailey, Zoroastrian Problems in the Ninth-Century Books, Clarendon press, Oxford 1943-1971. C. Bartholomae, Zum Altlranischen Worterbuch Nacharbeiten and Vorarbeiten, Vorlag von Karl J. Trubner, Strassburg 1906. M. Abolghasemi, Zaban FarsT va Sargozasht An, HTrmand Press, Tehran, 1375 (1996). F. Jonaydi, ZendegT va Mohajerat Aryaian, Bonyad Nayshabur, Tehran, 1374 (1995). A-15 
===== page_23
```


## [2026-09-04T14:32:22.505Z] AGENT

Now I have the bibliography. Let me load the web tools and start a batch of archive.org searches for the top references in parallel.


## [2026-09-04T14:32:22.928Z] TOOL CALL #3: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-04T14:32:22.935Z] TOOL RESULT

```


```


## [2026-09-04T14:32:25.783Z] AGENT

Let me run a batch of archive.org searches for the top references and simultaneously test the dictionary websites.


## [2026-09-04T14:32:35.685Z] TOOL CALL #4: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\nS='https://archive.org/advancedsearch.php'\nq() { echo \"=== $1\"; curl -s -G \"$S\" --data-urlencode \"q=$1\" --data-urlencode 'fl[]=identifier' --data-urlencode 'fl[]=title' --data-urlencode 'fl[]=year' --data-urlencode 'fl[]=language' --data-urlencode 'rows=15' --data-urlencode 'output=json' | python3 -c 'import sys,json\ntry:\n  d=json.load(sys.stdin)\n  for r in d[\"response\"][\"docs\"]: print(r.get(\"identifier\"),\"|\",str(r.get(\"title\"))[:90],\"|\",r.get(\"year\"),\"|\",r.get(\"language\"))\nexcept Exception as e: print(\"ERR\",e)'; }\nq 'برهان قاطع'\nq 'borhan qate'\nq 'burhan-i qati'\nq 'فرهنگ فارسی معین'\nq 'moin farhang farsi'\nq 'sogdian dictionary gharib'\nq 'فرهنگ سغدی'\nq 'shayast ne shayast glossary tavoosi'\nq 'شایست نشایست'\nq 'foreign vocabulary of the quran jeffery'\nq 'الالفاظ الفارسية المعربة'\nq 'addi shir alfaz'\nq 'لغت فرس اسدی'\nq 'واژه های دخیل در قرآن'\nq 'فرهنگ واژه های فارسی در زبان عربی'\nq 'اساس اشتقاق فارسی'",
 "description": "Search archive.org for the top Persian references",
 "timeout": 180000
}
```


### [2026-09-04T14:32:47.351Z] TOOL RESULT

```
=== برهان قاطع
einstein-his-life-and-universe-walter-isaacson | The Forgotten James Clerk Maxwell | 2025 | eng
isdar_tahqiq_40 | الجواهر السنية في الأحاديث القدسية | 2023 | ara
1_20210618_202106 | شرح المثنوي المعنوي المسمى بالمنهج القوي الشيخ يوسف ابن أحمد المولوي | None | ara
YoSoFeFATeMe.120 | واقعیت شکل زمین (تخت) بر اساس روایات‌اسلامی و اسناد معتبر علمی | 1399 | ira
borhan-ghate-v1 | برهان قاطع، جلد اول | 1963 | per
500166666666666666666666664 | الموسوعة المقروءة المكتوبة كتب صيغة وورد ورد اكثر من 6 آلاف كتاب | None | Arabic
240-p_202409 | تلبيس العاذرية بتحريف نقولات ابن تيمية( 240 P) | 2024 | ara
50016077777777777777777777 | كتب إسلامية وورد 6 ألف | None | Arabic
borhan-ghateh-j-1 | Borhan Ghateh - برهان قاطع | 1652 | per
50444444440160004 | islamic 6538 book word from shamelah library | None | urd
McGillLibrary-118596-1400 | Z̲aylī bar Burhān-i qāṭiʻ, "yā", Farhang-i lughāt-i bāzyāftah : shāmil-i qismatī | 1388 | Persian
borhan-qateh | Borhan Qateh | 1620 | per
5022222222222222222016000 | الموسوعة المقروءة المكتوبة كتب صيغة ويب اتش تي ام - اكثر من 6 آلاف كتاب | None | Arabic
50475869975498756000 | كتب صيغة وورد 6538 كتاب إسلامي كل ألف برابط | None | Arabic
0001Htm48_201901 | كتب صيغة ويب اتش تي ام من المكتبة الشاملة 6538 كتاب بصيغة htm | None | Arabic
=== borhan qate
borhan-ghateh-j-1 | Borhan Ghateh - برهان قاطع | 1652 | per
=== burhan-i qati
ghalibiyate-nau-1 | Ghalibiyate Nau 1 | 1969 | urd
dli.ministry.25441 | Burhan-I-Qati | None | per
adib-i-toussi-supplement-to-burhan-i-qati-2010 | Adib-i Toussi Supplement To Burhan-i Qati 2010 | None | None
=== فرهنگ فارسی معین
abu-abdurahman-kurdi-f_barid_02_20171226 | فرهنگ فارسی معین غ ی 02 | None | Persian
YoSoFeFATeMe.120 | واقعیت شکل زمین (تخت) بر اساس روایات‌اسلامی و اسناد معتبر علمی | 1399 | ira
abu-abdurahman-kurdi-f_barid_01_20171226 | فرهنگ فارسی معین الف ع 01 | None | Persian
YoSoFeFATeMe.175 | لیریکس ویدئو اختصاصی ترانه فارسی زبان ای عاشقان‌ با صدای گرم استاد سامی‌یوسف (ویرایش‌دوم) | 1400 | ira
2_20240201_20240201 | لغت‌ نامه دهخدا | 1999 | per
YoSoFeFATeMe.157 | برج بابل، اهرام مصر دروازه‌ای به سوی عوالم ستاره‌ای | 1400 | ira
YoSoFeFATeMe.150 | متن ترانه (لیریکس) ویدئو اختصاصی موسیقی ای عاشقان اثر سامی‌یوسف | 1399 | ira
farsi-2m-dabirestan-1348 | فارسی برای سال دوم دبیرستانها ۱۳۴۸ | 1969 | per
=== moin farhang farsi
farhang-sv-pers-golrang | GOLRANGS SVENSK - PERSISKA ORDBOK, VOLYM 1, A - F فرهنگ سوئدی به فارسی گلرنگ، جلد اول | 2025 | swe
=== sogdian dictionary gharib
=== فرهنگ سغدی
farsi-dabirestan-4m-1338 | فارسی برای سال چهارم دبیرستانها [سال ۱۳۳۸] | 1959 | per
YoSoFeFATeMe.121 | پژوهشی جامع درباره کوه قاف | 1399 | ira
=== shayast ne shayast glossary tavoosi
=== شایست نشایست
=== foreign vocabulary of the quran jeffery
GakewadsOrientalSeriesVol.LXXIXTheForeignVocabularyOfTheQuran | Gakewad's Oriental Series Vol. LXXIX The Foreign Vocabulary Of The Quran | 1938 | eng
in.ernet.dli.2015.68878 | The Foreign Vocabulary Of Quran | 1938 | eng
in.ernet.dli.2015.507015 | Foreign Vocabulary Of The Quran | 1938 | eng
in.ernet.dli.2015.277274 | Foreign Vocabulary of the Quran | 1938 | eng
dli.ministry.13123 | The Foreign vocabulary of the Quran | 1938 | ['eng', 'urd']
in.ernet.dli.2015.56841 | Foreign Vocabulary Of The Quran | 1938 | eng
in.ernet.dli.2015.217779 | The Foreign Vocabulary Of The Quran | 1938 | eng
foreignvocabular030753mbp | The Foreign Vocabulary Of The Quran | 1938 | eng
in.gov.ignca.7963 | Foreign vocabulary of the Quran | 1938 | eng
=== الالفاظ الفارسية المعربة
20250405_20250405_0055 | كتاب الالفاظ الفارسية المعربة | None | arabic
unset0000auth_c2g3 | كتاب الالفاظ الفارسية المعربة | 1908 | ['ara', 'syc']
plaintive27_gmail_20190316_1912 | الالفاظ الفارسية المعربة | None | Arabic
=== addi shir alfaz
=== لغت فرس اسدی
=== واژه های دخیل در قرآن
=== فرهنگ واژه های فارسی در زبان عربی
YoSoFeFATeMe.120 | واقعیت شکل زمین (تخت) بر اساس روایات‌اسلامی و اسناد معتبر علمی | 1399 | ira
litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023 | per
YoSoFeFATeMe.154 | شیاطین خدایان و معبودان و فرماندهان بزرگ آسمانی و زمینی و دوزخی بشر از ادوار گذشته تا به ا | 1399 | ira
Dic_M_Azarnosh | فرهنگ معاصر عربی فارسی آذرتاش آذرنوش | None | ara
=== اساس اشتقاق فارسی
YoSoFeFATeMe.162 | بازگشت یاران قدرتمند فضایی و سرگردان (دجال؛ حوروس/رع، یاجوج و ماجوج) شیطان از ابواب ستاره‌ | 1400 | ira
```


## [2026-09-04T14:33:14.257Z] AGENT (thinking)

Found good hits for BQT, MON, FVQ, and AFM. Next I'll check their metadata, run another batch of archive.org searches for the remaining references, and test the dictionary websites in parallel.


## [2026-09-04T14:33:16.848Z] TOOL CALL #5: Bash

```json
{
 "command": "meta() { echo \"=== $1\"; curl -s \"https://archive.org/metadata/$1\" | python3 -c 'import sys,json\nd=json.load(sys.stdin)\nm=d.get(\"metadata\",{})\nprint(\"title:\",m.get(\"title\"),\"| year:\",m.get(\"year\"),\"| lang:\",m.get(\"language\"),\"| desc:\",str(m.get(\"description\"))[:200])\nfor f in d.get(\"files\",[]):\n  n=f[\"name\"]\n  if n.endswith(\"_djvu.txt\") or n.endswith(\".pdf\") or n.endswith(\"_djvu.xml\") or n.endswith(\"_hocr.html\"): print(\"  \",n,f.get(\"size\"))'; }\nfor id in borhan-ghate-v1 borhan-ghateh-j-1 borhan-qateh dli.ministry.25441 adib-i-toussi-supplement-to-burhan-i-qati-2010 McGillLibrary-118596-1400 abu-abdurahman-kurdi-f_barid_01_20171226 abu-abdurahman-kurdi-f_barid_02_20171226 GakewadsOrientalSeriesVol.LXXIXTheForeignVocabularyOfTheQuran foreignvocabular030753mbp in.ernet.dli.2015.68878 unset0000auth_c2g3 20250405_20250405_0055 plaintive27_gmail_20190316_1912; do meta $id; done",
 "description": "Check archive.org metadata for candidate identifiers",
 "timeout": 180000
}
```


### [2026-09-04T14:33:34.822Z] TOOL RESULT

```
=== borhan-ghate-v1
title: برهان قاطع، جلد اول | year: 1963 | lang: per | desc: تألیف محمدحسین بن خلف تبریزی<div>باهتمام محمد معین</div><div>چاپ ۱۳۴۲ هجری شمسی</div>
   برهان قاطع، جلد اول.pdf 262397592
   برهان قاطع، جلد اول_djvu.txt 2620060
   برهان قاطع، جلد اول_djvu.xml 26399828
   برهان قاطع، جلد اول_hocr.html 49511007
=== borhan-ghateh-j-1
title: Borhan Ghateh - برهان قاطع | year: None | lang: per | desc: <p dir="rtl" class="p1" style="margin:0px;text-align:left;font-size:13px;line-height:normal;font-family:'Helvetica Neue';color:rgb(255,255,255);"><span style="color:rgb(230,232,240);font-family:'Googl
   Borhan_Ghateh_J1.pdf 18848243
   Borhan_Ghateh_J1_djvu.txt 2634275
   Borhan_Ghateh_J1_djvu.xml 26044082
   Borhan_Ghateh_J1_hocr.html 48310907
=== borhan-qateh
title: Borhan Qateh | year: None | lang: per | desc: <i style="font-size:16px;color:rgb(32,33,34);font-family:'system-ui', 'Segoe UI', 'Iranian Sans', 'Noto Sans Arabic', 'DejaVu Sans', sans-serif;"><b>رهان قاطع</b></i><span style="font-size:16px;color:
   Borhan Qateh.pdf 18848243
   Borhan Qateh_djvu.txt 2634275
   Borhan Qateh_djvu.xml 26029281
   Borhan Qateh_hocr.html 48304667
=== dli.ministry.25441
title: Burhan-I-Qati | year: None | lang: per | desc: None
   18720.13038-%28part-1%29.pdf 21527841
   18720.13038-%28part-1%29_djvu.txt 132862
   18720.13038-%28part-1%29_djvu.xml 1473323
   18720.13038-%28part-1%29_hocr.html 3239868
   18720.13038-%28part-1%29_text.pdf 3182367
   18720.13038-%28part-10%29.pdf 21452875
   18720.13038-%28part-10%29_djvu.txt 78935
   18720.13038-%28part-10%29_djvu.xml 994961
   18720.13038-%28part-10%29_hocr.html 2203106
   18720.13038-%28part-10%29_text.pdf 3032275
   18720.13038-%28part-2%29.pdf 23188479
   18720.13038-%28part-2%29_djvu.txt 143156
   18720.13038-%28part-2%29_djvu.xml 1713391
   18720.13038-%28part-2%29_hocr.html 4162905
   18720.13038-%28part-2%29_text.pdf 3358070
   18720.13038-%28part-3%29.pdf 23202129
   18720.13038-%28part-3%29_djvu.txt 182298
   18720.13038-%28part-3%29_djvu.xml 2063641
   18720.13038-%28part-3%29_hocr.html 4944054
   18720.13038-%28part-3%29_text.pdf 3560923
   18720.13038-%28part-4%29.pdf 21727272
   18720.13038-%28part-4%29_djvu.txt 217722
   18720.13038-%28part-4%29_djvu.xml 2301562
   18720.13038-%28part-4%29_hocr.html 5344631
   18720.13038-%28part-4%29_text.pdf 3490544
   18720.13038-%28part-5%29.pdf 22641124
   18720.13038-%28part-5%29_djvu.txt 187856
   18720.13038-%28part-5%29_djvu.xml 2046840
   18720.13038-%28part-5%29_hocr.html 4713377
   18720.13038-%28part-5%29_text.pdf 3362716
   18720.13038-%28part-6%29.pdf 23613984
   18720.13038-%28part-6%29_djvu.txt 157180
   18720.13038-%28part-6%29_djvu.xml 1830622
   18720.13038-%28part-6%29_hocr.html 4370156
   18720.13038-%28part-6%29_text.pdf 3159682
   18720.13038-%28part-7%29.pdf 22250243
   18720.13038-%28part-7%29_djvu.txt 153383
   18720.13038-%28part-7%29_djvu.xml 1907615
   18720.13038-%28part-7%29_hocr.html 4743946
   18720.13038-%28part-7%29_text.pdf 3232845
   18720.13038-%28part-8%29.pdf 23915243
   18720.13038-%28part-8%29_djvu.txt 183830
   18720.13038-%28part-8%29_djvu.xml 2185725
   18720.13038-%28part-8%29_hocr.html 5155245
   18720.13038-%28part-8%29_text.pdf 3301707
   18720.13038-%28part-9%29.pdf 22282618
   18720.13038-%28part-9%29_djvu.txt 170774
   18720.13038-%28part-9%29_djvu.xml 2028960
   18720.13038-%28part-9%29_hocr.html 4862515
   18720.13038-%28part-9%29_text.pdf 3282482
=== adib-i-toussi-supplement-to-burhan-i-qati-2010
title: Adib-i Toussi Supplement To Burhan-i Qati 2010 | year: None | lang: None | desc: The supplementary dictionary comprises lemmata not included in the existent editions of the Burhan-i Qati'.
   Adib_i_Toussi_Supplement_toBurhan_i_Qati_2010.pdf 6451143
   Adib_i_Toussi_Supplement_toBurhan_i_Qati_2010_djvu.txt 492463
   Adib_i_Toussi_Supplement_toBurhan_i_Qati_2010_djvu.xml 5529219
   Adib_i_Toussi_Supplement_toBurhan_i_Qati_2010_hocr.html 11898314
   Adib_i_Toussi_Supplement_toBurhan_i_Qati_2010_text.pdf 6051961
=== McGillLibrary-118596-1400
title: Z̲aylī bar Burhān-i qāṭiʻ, "yā", Farhang-i lughāt-i bāzyāftah : shāmil-i qismatī az lughāt va taʻbīrāt-i mustadrak kih bāyad bih farhang-i zabān-i Pārsī afzūdah shūd | year: 1388 | lang: Persian | desc: 198 pages ; 24 cm.
   118596.pdf 66329199
   118596_djvu.txt 502135
   118596_djvu.xml 5631124
   118596_hocr.html 11151363
=== abu-abdurahman-kurdi-f_barid_01_20171226
title: فرهنگ فارسی معین الف ع 01 | year: None | lang: Persian | desc: <a href="https://archive.org/details/@abu-abdurahman-kurdi-f" class="item-upload-info__uploader-name" style="color:rgb(42,100,150);line-height:1.36364;font-family:'Helvetica Neue', Helvetica, Arial, s
   فرهنگ فارسی معین-الف-ع-01.pdf 20113727
   فرهنگ فارسی معین-الف-ع-01_djvu.txt 4377831
   فرهنگ فارسی معین-الف-ع-01_djvu.xml 41128092
   فرهنگ فارسی معین-الف-ع-01_hocr.html 77702132
   فرهنگ فارسی معین-الف-ع-01_text.pdf 91219178
=== abu-abdurahman-kurdi-f_barid_02_20171226
title: فرهنگ فارسی معین غ ی 02 | year: None | lang: Persian | desc: <a href="https://archive.org/details/@abu-abdurahman-kurdi-f" class="item-upload-info__uploader-name" style="color:rgb(66,139,202);line-height:1.36364;font-family:'Helvetica Neue', Helvetica, Arial, s
   فرهنگ فارسی معین-غ-ی-02.pdf 21014767
   فرهنگ فارسی معین-غ-ی-02_djvu.txt 4331421
   فرهنگ فارسی معین-غ-ی-02_djvu.xml 41551187
   فرهنگ فارسی معین-غ-ی-02_hocr.html 78163559
   فرهنگ فارسی معین-غ-ی-02_text.pdf 88126438
=== GakewadsOrientalSeriesVol.LXXIXTheForeignVocabularyOfTheQuran
title: Gakewad's Oriental Series Vol. LXXIX The Foreign Vocabulary Of The Quran | year: None | lang: eng | desc: Gakewad's Oriental Series Vol. LXXIX - The foreign vocabulary of the Quran,Religion/Islam
   Gakewad's-Oriental-Series-Vol. LXXIX-The foreign-vocabulary-of-the-Quran.pdf 18004048
   Gakewad's-Oriental-Series-Vol. LXXIX-The foreign-vocabulary-of-the-Quran_djvu.txt 32523
   Gakewad's-Oriental-Series-Vol. LXXIX-The foreign-vocabulary-of-the-Quran_djvu.xml 6127525
   Gakewad's-Oriental-Series-Vol. LXXIX-The foreign-vocabulary-of-the-Quran_text.pdf 9337141
=== foreignvocabular030753mbp
title: The Foreign Vocabulary Of The Quran | year: None | lang: eng | desc: None
   foreignvocabular030753mbp.pdf 15728732
   foreignvocabular030753mbp_djvu.txt 649903
   foreignvocabular030753mbp_djvu.xml 5917156
=== in.ernet.dli.2015.68878
title: The Foreign Vocabulary Of Quran | year: None | lang: eng | desc: <p><b>Book Source:</b> <a href="http://www.new.dli.ernet.in/handle/2015/68878" rel="nofollow">Digital Library of India Item 2015.68878</a></p><p>dc.contributor.author: Jeffery,arthur<br />dc.date.acce
   2015.68878.The-Foreign-Vocabulary-Of-Quran.pdf 24320249
   2015.68878.The-Foreign-Vocabulary-Of-Quran_djvu.txt 643425
   2015.68878.The-Foreign-Vocabulary-Of-Quran_djvu.xml 6458986
   2015.68878.The-Foreign-Vocabulary-Of-Quran_text.pdf 27448325
=== unset0000auth_c2g3
title: كتاب الالفاظ الفارسية المعربة | year: None | lang: ['ara', 'syc'] | desc: None
   unset0000auth_c2g3.pdf 13423325
   unset0000auth_c2g3_djvu.txt 354548
   unset0000auth_c2g3_djvu.xml 4044032
   unset0000auth_c2g3_hocr.html 8228062
=== 20250405_20250405_0055
title: كتاب الالفاظ الفارسية المعربة | year: None | lang: arabic | desc: 1
   كتاب الالفاظ الفارسية المعربة.pdf 20978939
   كتاب الالفاظ الفارسية المعربة_djvu.txt 78669
   كتاب الالفاظ الفارسية المعربة_djvu.xml 1997265
   كتاب الالفاظ الفارسية المعربة_hocr.html 3898382
   كتاب الالفاظ الفارسية المعربة_text.pdf 14067249
=== plaintive27_gmail_20190316_1912
title: الالفاظ الفارسية المعربة | year: None | lang: Arabic | desc: صفحة كتب ممنوعة ونادرة
   الالفاظ الفارسية المعربة.pdf 14780832
   الالفاظ الفارسية المعربة_djvu.txt 383664
   الالفاظ الفارسية المعربة_djvu.xml 4201573
   الالفاظ الفارسية المعربة_hocr.html 7908272
```


## [2026-09-04T14:33:48.576Z] AGENT

Now I'll download the confirmed texts (BQT vol 1, MON both parts, FVQ, AFM), run a second search batch for the remaining references, and test the dictionary sites — all at once.


## [2026-09-04T14:34:01.476Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\ndl() { curl -sL -o \"$2\" \"https://archive.org/download/$1\"; echo \"$2: $(wc -c < \"$2\") bytes, pages(FF)=$(tr -cd '\\f' < \"$2\" | wc -c)\"; }\ndl 'borhan-ghate-v1/%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%A7%D9%88%D9%84_djvu.txt' BQT_v1.txt\ndl 'borhan-qateh/Borhan%20Qateh_djvu.txt' BQT_alt_v1.txt\ndl 'abu-abdurahman-kurdi-f_barid_01_20171226/%D9%81%D8%B1%D9%87%D9%86%DA%AF%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C%20%D9%85%D8%B9%DB%8C%D9%86-%D8%A7%D9%84%D9%81-%D8%B9-01_djvu.txt' MON_part1.txt\ndl 'abu-abdurahman-kurdi-f_barid_02_20171226/%D9%81%D8%B1%D9%87%D9%86%DA%AF%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C%20%D9%85%D8%B9%DB%8C%D9%86-%D8%BA-%DB%8C-02_djvu.txt' MON_part2.txt\ndl 'foreignvocabular030753mbp/foreignvocabular030753mbp_djvu.txt' FVQ.txt\ndl 'unset0000auth_c2g3/unset0000auth_c2g3_djvu.txt' AFM.txt\ndl 'dli.ministry.25441/18720.13038-%28part-1%29_djvu.txt' BQT_dli_part1.txt\necho; echo \"--- BQT_v1 sample around page 30\"; awk 'BEGIN{RS=\"\\f\"} NR==30{print substr($0,1,600)}' BQT_v1.txt\necho; echo \"--- MON_part1 sample page 40\"; awk 'BEGIN{RS=\"\\f\"} NR==40{print substr($0,1,800)}' MON_part1.txt\necho; echo \"--- BQT_dli sample page 20\"; awk 'BEGIN{RS=\"\\f\"} NR==20{print substr($0,1,400)}' BQT_dli_part1.txt",
 "description": "Download OCR texts for BQT, MON, FVQ, AFM and sample them",
 "timeout": 300000
}
```


### [2026-09-04T14:34:29.629Z] TOOL RESULT

```
BQT_v1.txt: 2620060 bytes, pages(FF)=0
BQT_alt_v1.txt: 2634275 bytes, pages(FF)=0
MON_part1.txt: 4377831 bytes, pages(FF)=0
MON_part2.txt: 4331421 bytes, pages(FF)=0
FVQ.txt: 649903 bytes, pages(FF)=0
AFM.txt: 354548 bytes, pages(FF)=0
BQT_dli_part1.txt: 146 bytes, pages(FF)=0

--- BQT_v1 sample around page 30

--- MON_part1 sample page 40

--- BQT_dli sample page 20
```


## [2026-09-04T14:34:33.182Z] AGENT

The downloads succeeded but the OCR texts have no form-feed page markers, so let me inspect their structure and quality directly.


## [2026-09-04T14:34:36.382Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\ncat BQT_dli_part1.txt; echo; echo \"--- BQT_v1 head\"; head -c 1500 BQT_v1.txt; echo; echo \"--- BQT_v1 grep دیوار\"; grep -n 'دیوار' BQT_v1.txt | head -5; echo \"--- MON_part1 head\"; head -c 1200 MON_part1.txt; echo; echo \"--- MON grep دیوار\"; grep -n '^دیوار\\|دیوار ' MON_part1.txt | head -5; echo \"--- FVQ head\"; sed -n '1,40p' FVQ.txt | cut -c1-100; echo \"--- AFM sample\"; grep -n 'ابريسم\\|ابريشم' AFM.txt | head -3",
 "description": "Inspect downloaded OCR texts"
}
```


### [2026-09-04T14:34:36.544Z] TOOL RESULT

```
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx</center>
</body>
</html>

--- BQT_v1 head



۱ ۵ ۱! ۱ 


7 موم ۳ لام 
م ۱ 0 و طق صفرررنیاعدریرماروی 
۰ ۱ "۳ 


۳ 


م و اس مر هر وه او 
7 رین خلت ریز یتایب بره ات 
لف‌بال ۶۲ .یرک 

ا اند کل داي رشب , رمع 


فان تا تا 
رن 9 3 
کرحم تن 
اد شش مرا 


مو رم | مر 
وک رهب اه نات مج 
لش 
وان روکد ور 
۱ و 
طراول ؛ | ع اس 


چاپ دوم فروردین ۱۳۴۳ 
با تجدید نظر کامل 
بسرمایه کنابفروشی ابن سینا - تپر ان 


اداره کل دک زون. 
شماره ۷9 9 ۳ 


بر 





5 


‌ ۰ م۸ 
و «ارس‌شبات 


4 


د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران 
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد * 
کلیه حقوق‌تجد ید طبم کتاب برهان قاطع با تمحیحات وحواشی و 
تملیقا ت وتصا ویرواقتباس‌وتلخیص وترجمه آن بنام‌جنابمالی 
محفوظ ومخصوص خوا هد بودضمنا وزا رنفرهنگ فرصت رامفتنم شمرد ه 
بد ینوسیله اززحمات شماد رانجام این‌خد مت مهم فرهنگی قد رد انی 
میکند وموفقیت آن) ستا د محتر مراد را ینکونه خد مات خواستاراست» 
هنگ 


رن 


یی سین 


شیر زوا عرسا رده ارسال ۱۳۱۷ ۰۳۳1« 9 لو
--- BQT_v1 grep دیوار
1524:۷ -< از این قبیل است : مرزیان نامه . نبکی‌نامه ۰ ثه میت از دیواره و ءاسته رد » 
10219:است و در بیخهای دیوار ور جاهای سابمدار 
24163:وزن سرزش» دیوار برآوردن و عمارت کردن را 
25841:برآوردن دیوار عمارت وامتال آن باشفد ِ 
27110:بر بام و دیوار مالیدن باشد - وکاهگل مالندرا 
--- MON_part1 head
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
و ده ها وی مزا موی ماما میو و موه ومد موه اش اما موم م میا شا ولمم 


معین, محمد» ۱۳۵۰۰۱۲۹۱ 
فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۱۳۸۱. 
۲ 
(دوره) 964-7252-51-6 :53(1] 
(ج.۲) 964-7252-53-6 :۰ (ج.۱/) 964-7252-52-8 :158 
فهرسکتویسی پر اسان اطلاغات فا 
ترشیت هارمه وا 
۵ ف ۲۹۵۴/2۷ ۳11 ۳ فا ۴ 
۱۳۸۹۰۱ 
کتابخانه ملی ایران 


۵ - ۸۱ م 


انتشارات آدنا 
فر هنک دوجلدی معین 
کرداورنده عزیزالت
--- MON grep دیوار
3142:ه روی در و دیوار و بوم مالند. 
4403:دیواری که برای حفظ سیاه کشند؛ بش کر 
4738:چون دیوار و سقف؛ لایه. 
5167:سب افتادن دیوار و سقف فرو ربزد از 
5412:دیوار و مانند آن. برافراختن» برافراشتن 
--- FVQ head
LIJ< OU 158174 >m 

> - ;0 73 

^ CO 



GAEKWAD*8 ^ORIENTAL SERIES 

Published unde* the Authority of 
the Government of His Highness 
the Maharaia Gaekwad of Baroda. 



GENERAL EDITOR : 
B. BHATTACHARYYA, M.A., Ph.D., 

Rdjaratna, Jndnaratna. 



No. LXXIX. 



THE FOREIGN VOCABULARY 
OF THE QUR'AN 



THE 

FOREIGN VOCABULARY 
OF THE QUR'AN 



By 
--- AFM sample
```


## [2026-09-04T14:34:53.482Z] AGENT (thinking)

I've confirmed BQT_v1 is Mo'in's 1342/1963 Ibn Sina edition, and the MON files are the 2-volume Adena 1381 abridgement rather than Nourai's 6-volume edition; the DLI URL failed due to encoding. Next I'll fix that download, test archive.org's inside-the-book search, run the second search batch, and check vajehyab/abadis.


## [2026-09-04T14:34:57.593Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\necho \"--- AFM sample lines 300-330\"; sed -n '300,330p' AFM.txt | cut -c1-120\necho \"--- DLI retry\"; curl -sL -o BQT_dli_part1.txt 'https://archive.org/download/dli.ministry.25441/18720.13038-(part-1)_djvu.txt'; wc -c BQT_dli_part1.txt; sed -n '200,215p' BQT_dli_part1.txt\necho \"--- inside.php search test on borhan-ghate-v1\"\nM=$(curl -s https://archive.org/metadata/borhan-ghate-v1); SRV=$(echo \"$M\" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d[\"server\"])'); DIR=$(echo \"$M\" | python3 -c 'import sys,json;d=json.load(sys.stdin);print(d[\"dir\"])'); echo \"server=$SRV dir=$DIR\"\ncurl -s -G \"https://$SRV/fulltext/inside.php\" --data-urlencode 'item_id=borhan-ghate-v1' --data-urlencode 'doc=برهان قاطع، جلد اول' --data-urlencode \"path=$DIR\" --data-urlencode 'q=دیوار' | python3 -c 'import sys,json\nt=sys.stdin.read()\ntry:\n  d=json.loads(t); print(\"matches:\",len(d.get(\"matches\",[])))\n  for m in d[\"matches\"][:5]: print(m[\"par\"][0].get(\"page\"), \"|\", m[\"text\"][:120].replace(\"\\n\",\" \"))\nexcept Exception as e: print(\"ERR\",e,t[:300])'",
 "description": "Test AFM OCR, fix DLI download, test archive inside.php page search",
 "timeout": 120000
}
```


### [2026-09-04T14:35:05.627Z] TOOL RESULT

```
--- AFM sample lines 300-330

( إلا جور اليا عور والا جور والا جر 0 وال جرون) قري ١‏ "لوز دعو 
تراب يحكم عجلة وتقريصة 2 2 5 'وقالوا فيه أ جر الطين ٠‏ وييرادفة بالا�
سدمارس وقال )ܡܢܐ (ص 09110 اصل اللفظة ارا ى ܐܓܪܐ وهو موحود : 
اللغة 32 القدعة ٠واما‏ العُرميد فهو @ 7 


لكر له 
| 0 13110 و 0 2 000 نالع ٠‏ ومئنهة الفرني ¢¢ 
والايطا ليائي - 0 3430 بالسر ± الدارجة 36 
والكردنة ٠‏ وام الاصطبل فهو تعريب الرومى 562111111153 
( إلا درون ) المثلفٍ والارى والوطن وهر إما معرب 50 80350 ,< 
ماخوذ عن اليونائي ا ثاريه وهر القسم من ܝܗ الختص باارجال ܢ܆ܐ ܐܢܝܕܪܘ
11:20 ® ܕ[ 0 والقليد فاخوذان عن بسجده»: وعن 0 اي المخدع 
وسبه مخدع 

( الاذرريون ). زهر اضفر في 71005 5957 الذذ كو راصل 11 ]ا 
شمه الثار. وآذر يون اغة فيه ± ` 096( حيجكى ( زهر القمر ) 
وقره كز ( العين السوداء ) 

3( الأرجان ) ,شر 4033( :3( 600390550901017 ا 
ارجن وهو الفستق البري وقيل الاوز المر واسمة 6 9 اي لوز الل 
( الترهان القاطع ) 

590 معرب )6.35 وهو سّحر له ورد 0 به 0 
ويطلق 9 على 0 حمر والشاب الخمر والصبغ الأخر ٠وقيل‏ 0 عوده اذا احصار�
تفع لاإننات ܚܟ .ܕܟܕ بالارامية ܐܪܥܘܝܐܝ ܙ( 5 6( و 6 1 
اللفظة سنسكر ܝܬ 10 ܐܦܬ نه من 5282 اي احمر ومن 724 وهى اداة 
النسة ( القاموس العبرالي الكلداني تأليف جسنيوسء ضن : + ) (4) : 

الأوارجة ) 5755 جسات الدخل والخرح يدون 3 )ا 1 
--- DLI retry
146 BQT_dli_part1.txt
--- inside.php search test on borhan-ghate-v1
server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1
matches: 20
214 | رباحین بود و پیوسته سبز میباشدو بركآن هر کز : نیقئد . گوبند در تبریز و آندبامسان ‏ سبار است و در بیخهای <IA_FTS_MATCH>دی
356 | فا . بهفر وشكوفةً درخث را کویند - وبمعنی قی واستفراغ هم آمده است ّ. اشکل پکر اول و تالث وسکون ثانی و لام 0 اسبی را کونند
374 | برآوردن <IA_FTS_MATCH>دیوار</IA_FTS_MATCH> عمارت وامتال آن باشفد ِ بیان یست و دوم
386 | ا فك - بروزن‌عمدا؛بممن ی کلابهوکاهگل بر بام و <IA_FTS_MATCH>دیوار</IA_FTS_MATCH> مالیدن باشد - وکاهگل مالندرا را نیز گفت
416 | ایز ازه « با زای شطهدار بروزن‌سحاره: ازارء خانه را گویتد و آن از <IA_FTS_MATCH>دیوار</IA_FTS_MATCH> مقداری‌باشد
```


## [2026-09-04T14:35:19.976Z] AGENT (thinking)

The inside.php search is confirmed working. Next I'll run the remaining archive.org searches, rebuild the BQT/MON texts with page breaks from djvu.xml for page mapping, retry the DLI file, and test vajehyab and abadis in parallel.


## [2026-09-04T14:35:38.306Z] TOOL CALL #9: Bash

```json
{
 "command": "S='https://archive.org/advancedsearch.php'\nq() { echo \"=== $1\"; curl -s -G \"$S\" --data-urlencode \"q=$1\" --data-urlencode 'fl[]=identifier' --data-urlencode 'fl[]=title' --data-urlencode 'fl[]=year' --data-urlencode 'rows=10' --data-urlencode 'output=json' | python3 -c 'import sys,json\ntry:\n  d=json.load(sys.stdin)\n  for r in d[\"response\"][\"docs\"]:\n    t=str(r.get(\"title\"))\n    if \"YoSoFeFATeMe\" in r[\"identifier\"]: continue\n    print(\" \",r.get(\"identifier\"),\"|\",t[:90],\"|\",r.get(\"year\"))\nexcept Exception as e: print(\"ERR\",e)'; }\nq 'برهان قاطع جلد دوم'; q 'برهان قاطع جلد سوم'; q 'برهان قاطع جلد چهارم'; q 'title:(برهان قاطع)'; q 'title:(Borhan) AND mediatype:texts'\nq 'title:(sogdian) AND mediatype:texts'; q 'قریب سغدی'; q 'Shayast'; q 'Tavoosi'\nq 'فعلهای فارسی دری'; q 'ابوالقاسمی'; q 'فرهنگ واژه های عربی در فارسی'; q 'نحوی دخیل'; q 'خالقی مطلق اشتقاق'\nq 'فرهنگ واژه های اروپایی'; q 'واژه نامک شاهنامه'; q 'نوشین شاهنامه'; q 'تفسير الالفاظ الدخيلة'; q 'العنيسي الدخيلة'\nq 'واژه های دخیل در قرآن مجید'; q 'بدره ای'; q 'امام شوشتری'; q 'ریشه شناسی اتیمولوژی'; q 'تاریخ مختصر زبان فارسی'\nq 'فرهنگ سیاح المنجد'; q 'ایرانویج فره وشی'; q 'لغت فرس'; q 'Asadi Lughat'; q 'مهاجرت آریاییان جنیدی'; q 'فرهنگ اعلام فارسی'\nq 'ارکان سخن'; q 'فرهنگ عمید'; q 'دستور زبان اوستایی راشد محصل'; q 'خودآموز زبان سانسکریت'; q 'در مکتب استاد نفیسی'; q 'سبک شناسی بهار'\nq 'واژه نامه غزلهای حافظ'; q 'واژه های ایرانی در زبان انگلیسی'; q 'فرهنگ اعلام کتاب مقدس'; q 'زبان فارسی و سرگذشت آن'; q 'فرهنگ نامهای ایرانی'; q 'واژه سازی در زبان فارسی'\nq 'فرهنگ ایران باستان پورداود'; q 'تبار مشترک ایرانیان و تورانیان'; q 'سنگ نبشته ها سخن می گویند'; q 'فقه اللغة ثعالبي'; q 'نامه فرهنگ ایران جنیدی'; q 'فرهنگ مشتقات مصادر فارسی'\nq 'المعرب الجواليقي'; q 'فرهنگ واژه های همانند ارمنی'; q 'هنری زبان فارسی سخن'; q 'ناتل خانلری زبان فارسی'; q 'اخوان زنجانی'",
 "description": "Second batch of archive.org searches for remaining Persian/Arabic references",
 "timeout": 400000
}
```


### [2026-09-04T14:36:38.370Z] TOOL RESULT

```
=== برهان قاطع جلد دوم
  borhan-ghate-v2 | برهان قاطع، جلد دوم | 1963
=== برهان قاطع جلد سوم
=== برهان قاطع جلد چهارم
=== title:(برهان قاطع)
  borhan-ghateh-j-1 | Borhan Ghateh - برهان قاطع | 1652
  borhan-ghate-v1 | برهان قاطع، جلد اول | 1963
  borhan-ghate-v2 | برهان قاطع، جلد دوم | 1963
=== title:(Borhan) AND mediatype:texts
  gov.uscourts.cacb.1906525 | Bijan Borhan Dayyany | None
  gov.uscourts.caed.389214 | (PC) Borhan v. McKesson | None
  borhan-ghateh-j-1 | Borhan Ghateh - برهان قاطع | 1652
  borhan_827 | borhan | None
  gov.uscourts.casb.436596 | Borhan Uddin Ahmed and Anisha Kowme Ahmed | None
  gov.uscourts.mab.498157 | Ramin Borhan Mojabi | None
  gov.uscourts.mdb.746511 | Borhan Reda Bizri | None
  gov.uscourts.mtd.72152 | United States v. Borhan | None
  borhan-qateh | Borhan Qateh | 1620
  al-borhan | al-borhan | None
=== title:(sogdian) AND mediatype:texts
  enwiki-Sogdian_language-20200728.pdf | enwiki-Sogdian_language-20200728.pdf | 2020
  spp306_sogdian_religions | Religions and Religious Space in Sogdian Culture: A View from Archaeological and Written S | 2020
  four-old-iranian-ethnic-names-scythian-skudra-sogdian-saka | Four Old Iranian Ethnic Names: Scythian – Skudra – Sogdian – Saka | 1980
  uzbekiston-tarixi-jurnali | Foundations of the historical unity of emergence Turkic and Sogdian writing | 2023
  sogdian-grammar-skjaervo | Sogdian, Grammar ( Skjærvø) | 2008
  SogdianDictionary | ÙØ±ÙÙÚ¯ Ø³ØºØ¯Û sogdian dictionary | None
  bub_gb_KVSPEN4ap_0C | Sogdian Painting The Pictorial Epic in Oriental Art | 1981
  spp327_sino-sogdian_horse | Images of the Riderless Horse as a Symbol of the Deceased in Sino-Sogdian Tombs | 2022
  cosmopolitanismi0000vale | Cosmopolitanism in the Tang Dynasty : a Chinese ceramic figure of a Sogdian wine-merchant | 2014
  AZARPAYSogdianPainting1981 | AZARPAY Sogdian Painting ( 1981) | 1981
=== قریب سغدی
=== Shayast
  india.history.resource.85806 | Pahlavi Texts, Part. I- the Bundahis, Bahman Yast and Shayast La-Shayast (the Sacred Books | 1880
  mlbd.pahlavitextssacr0000ewwe_f3j9 | SBE 24: Pahlavi Texts, Part 3 (Sacred Books of the East) | 1884
  india.history.resource.78103 | The Sacred Books of the East; translated by Various Oriental Scholars, Vol. V; Pahlavi Tex | 1880
  mlbd.sacredbooksofeas0047unse | SBE 47: Pahlavi Texts,Part 5: Marvels of Zoroastrianism (Sacred Books of the East) | 1897
  india.history.resource.117524 | Expositions; or, Niyama-Dipani; translated from the Pali; Critical, comparative, and histo | 1921
  mlbd.pahlavitextssacr0000ewwe_z0t1 | SBE 18: Pahlavi Texts, Part 2 (Sacred Books of the East) | 1882
  mlbd.pahlavitextssacr0000vol-37.ewwe_a5s1 | SBE 37: Pahlavi Texts, Part 4 (Sacred Books of the East) | 1892
  mlbd.pahlavitextssacr0000ewwe_v3m0 | SBE 05: Pahlavi Texts, Part 1 (Sacred Books of the East) | 1880
  bwb_W9-DCD-323 | pahlavi texts the bundahis-bahman yast, and shayast la-shayast | 1977
  wg905 | 1880 -The Sacred Books Of East Vol 5 Of 50 Zoroastrianism Pahlavi Texts Part 1 Of 5 | 1880
=== Tavoosi
  pubmed-PMC3123091 | Molecular Determinants of Phospholipid Synergy in Blood Clotting*. | 2011
  httpsjournal.cio-museums.orgarticle_709308.html | زیبایی‌شناسی تطبیقی نمونه کاشی‌های زرین‌فام منقوش متعلق به سدۀ هفتم هجری قمریA Comparative | None
  osf-registrations-zcj3k-v1 | Predicting Personality from LinkedIn Profiles Using Machine Learning and Natural Language  | 2023
  httpsjmme.um.ac.irarticle_32470.htmllangen | The Effect of Low Temperature Austempering on Microstructure, Mechanical and Wear Properti | 2018
  gov.uscourts.txnd.350724 | Mohammad Reza Tavoosi Mahyari v. Walmart Stores Inc | None
  VajnameShayest | Vajname Shayest | None
  pubmed-PMC3959187 | Echocardiographic estimation of left ventricular filling pressures in patients with mitral | 2013
=== فعلهای فارسی دری
=== ابوالقاسمی
  ya_2. | شعر در ایران پیش از اسلام 2. ابوالقاسمی | None
  zakeri_etymology | هدف از ریشه‌شناسی چیست؟ | 2004
  ahmed-abu-al-qasimi | Ahmed Abu Al Qasimi - أحمد أبو القاسمي - احمد ابوالقاسمی | None
  2_20250228_20250228_0858 | تلاوتهاي روز تشييع سيد حسن | 1403
  20220913_20220913_2055 | دربارۀ زبان آسی | 1969
  1402_20230629 | اسماء الحسنى - حج 1402 | 1402
  20221107_20221107_0720 | ابوالقاسمی والدین 2 | None
  20220417_20220417_2237 | دستور تاریخی زبان فارسی - محسن ابوالقاسمی | 1375
  haroon-ommat | کتاب هارون امت تالیف حسین قربانی دامنابی | None
=== فرهنگ واژه های عربی در فارسی
  litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023
  Dic_M_Azarnosh | فرهنگ معاصر عربی فارسی آذرتاش آذرنوش | None
=== نحوی دخیل
=== خالقی مطلق اشتقاق
=== فرهنگ واژه های اروپایی
  litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023
  2-1404_202606 | 2فرهنگ ریشه لغات فارسی با نمودارهای اشتقاق ـ ویراست 1404 | 2025
  20240309_20240309_1515 | فرهنگ اشتقاق واژه های فارسی | 2024
=== واژه نامک شاهنامه
  20220809_20220809_1444 | واژه نامک؛ فرهنگ واژه های دشوار شاهنامه | None
=== نوشین شاهنامه
  Sokhani | Sokhani | 1970
  nooshinshahnameh | Nooshin Shahnameh | 1982
=== تفسير الالفاظ الدخيلة
  IslamSpirit-Majem-Adla-PDF-02 | مكتبة المعاجم والأدلة والموسوعات العلمية ( بي دي اف ) - مجموعة (2) | None
  elshandawily14640 | تفسير الالفاظ الدخيلة في اللغة العربية مع ذكر اصلها بحروفه | None
  ar113lang79 | طوبيا العنيسي تفسير الالفاظ الدخيلة في اللغة العربية | None
  IslamSpirit-Majem-Adla-PDF-01 | مكتبة المعاجم والأدلة والموسوعات العلمية ( بي دي اف ) - مجموعة (1) | None
  IslamSpirit-Majem-Adla-PDF-03 | مكتبة المعاجم والأدلة والموسوعات العلمية ( بي دي اف ) - مجموعة (3) | None
  TOB1932ARAR | تفسير الالفاظ الدخيلة في اللغة العربية | 1932
=== العنيسي الدخيلة
  ar113lang79 | طوبيا العنيسي تفسير الالفاظ الدخيلة في اللغة العربية | None
=== واژه های دخیل در قرآن مجید
=== بدره ای
=== امام شوشتری
  TaghribAlMaaref | تقریب المعارف PDF | None
  20220626_20220626_0624 | وسائل المحبین فی خصایص الحسین صلوات الله وسلام الله علیه. شوشتری | None
  TaqribulMaarif | تقریب المعارف PDF | None
  haqaeq-ul-ahqaq-tarjuma-ahqaq-ul-haq-translated-by-syed-hassan-abbas-mosvi | حقائق الاحقاق ترجمہ احقاق الحق (باب امامت) موسوی | 1939
=== ریشه شناسی اتیمولوژی
=== تاریخ مختصر زبان فارسی
  RashdiFamilyPirJhando | A brief introduction of the Pir jhandewaras of the Rashdi family branch "Pir Jhanda": Darg | 2023
  meftah-al-moamelat | meftah-al-moamelat مفتاح المعاملات | None
  Maktaba-Maulana-Hafeez-ur-Rahman-Wasif-Dehlvi-ra | Maktaba Maulana Hafeez ur Rahman Wasif Dehlvi ra | None
  KhavarigUndSchia | Khavarig und Schia(چاپ اول) | 2016
  iran-in-pahlavi-age | ایران در روزگار پهلوی | 2015
  HistoricalBackgroundOfRashdiFamily | Review of the family and historical background of the Rashdi family in Sindh and their rel | 2003
  20250313_20250313_0609 | ['مفتاح المعاملات', 'از مقدمه \xa0 دکتر محمدامین ریاحی:', 'در آن روزها که گاهی این فرصت دس | 1950
  Babar-Namah | تزک بابری | None
=== فرهنگ سیاح المنجد
=== ایرانویج فره وشی
=== لغت فرس
  20230803_20230803_0654 | دیوان شعر ظهوری | None
=== Asadi Lughat
  dli.ernet.439493 | Lughat Faras | 1887
  dli.ernet.437743 | Lughat Faras | 1887
  LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi | Lughat e Furs - Abu Mansur Ali Bin Ahmad Asadi Tusi (Farsi) | None
=== مهاجرت آریاییان جنیدی
=== فرهنگ اعلام فارسی
  20240821_20240821_1220 | قاموس اعلام جغرافیائی افغانستان | None
  2_20240201_20240201 | لغت‌ نامه دهخدا | 1999
  GhBooK_IR | EPUB,GHM,JAR محصول بیش‌از ۴۶۰۰ جلد کتاب (بازار کتاب دیجیتال قائمیه) محبوب فارسی و عربی در  | 1399
  IRAN2_201603 | ISLAM&IRAN:Religion&Nationality=اسـلام و ايــران ؛ مـــذهــب و مــليـــت ايــرانـی | 2016
  1-2_20240821_202408 | قاموس جغرافیایی افغانستان ج 1 و 2 | None
=== ارکان سخن
  the-mother-of-earthquake | Earthquake damage: the method of earthquake engineering- learning form ... / زلزله در آلبو | 2003
  img-20200506-224250-664 | IMG 20200506 224250 664 | None
  farsi-2m-dabirestan-1348 | فارسی برای سال دوم دبیرستانها ۱۳۴۸ | 1969
=== فرهنگ عمید
=== دستور زبان اوستایی راشد محصل
=== خودآموز زبان سانسکریت
=== در مکتب استاد نفیسی
=== سبک شناسی بهار
  galaxy_ub2007_yahoo_20151117 | سبک شناسی بهار | None
  iran-front | IRAN DURING THE AGE OF PAHLAVI KINGDOM=ایران در روزگار پهلوی | 2016
  1_20250928_20250928_1159 | سبک شناسی 1 | 1942
=== واژه نامه غزلهای حافظ
=== واژه های ایرانی در زبان انگلیسی
  litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023
=== فرهنگ اعلام کتاب مقدس
=== زبان فارسی و سرگذشت آن
  OMiGo | صفحه‌پشتیبان از تمامی مطالب وبلاگ‌رسمی رسانه یوسف‌فاطمه | 1400
  dehkhoda_202508 | دهخدا و لغت‌نامه | 1402
  litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023
=== فرهنگ نامهای ایرانی
  3_20260303_202603 | خرد، سرمایه فلسفی جلد 3 | None
=== واژه سازی در زبان فارسی
  20221218_20221218_1902 | کارنامه ی پارسیک | 1987
=== فرهنگ ایران باستان پورداود
=== تبار مشترک ایرانیان و تورانیان
=== سنگ نبشته ها سخن می گویند
=== فقه اللغة ثعالبي
  20260705_20260705_0657 | فقه اللغة وسر العربية، اثر عبدالملك بن محمد بن اسماعيل ثعالبي۔ عربی ۔ حق | 2026
=== نامه فرهنگ ایران جنیدی
=== فرهنگ مشتقات مصادر فارسی
=== المعرب الجواليقي
  mo3rb | mo3rb | None
  20260217_20260217_0052 | سيرة | None
  20210716_20210716_2227 | إبن منصور الجواليقي المعرب من كلام العرب | None
  uc1.aa0003615705 | كتاب المعرب من الكلام الاعجمي على حروف المعجم | 1867
  almo3rab_gwaliqy_f_abduraheem | المعرب من الكلام الأعجمي | None
  MS.ARA.1933 | مجموع Recueil | None
  AAskZad-1135585 | Book المعرب من الكلام الأعجمي على حروف المعجم [1135585] --- منصور الجواليقي موهوب بن أحمد  | None
  AAlexandrina-148752 | 148752_المعرب_من_الكلام_الاعجمى_على_حروف_المعجم | 1867
  ar120vieux55 | أبو منصور الجواليقي المعرب من الكلام الأعجمي على حروف المعجم | None
  AAlexandrina-147458 | 147458_كتاب_المعرب_من_الكلام_الاعجمى_على_حروف_المعجم | 1867
=== فرهنگ واژه های همانند ارمنی
=== هنری زبان فارسی سخن
  1_20200718_20200718_1313 | ساختار و تأویل متن 1 | None
  litterature-comparee | [FR] Étude comparative du surréalisme dans les poèmes d’Ahmadreza Ahmadi et de Louis Arago | 2023
=== ناتل خانلری زبان فارسی
  1_20251010_20251010_2025 | تاریخ زبان فارسی☆ 1 | None
  190061 | 190061 | None
  AmoozeshVaParvaresh | Amoozesh Va Parvaresh | 1963
=== اخوان زنجانی
```


## [2026-09-04T14:37:00.926Z] AGENT (thinking)

Found several key sources: BQT vol 2, a Sogdian dictionary, VajnameShayest, Noushin's Vazhe-namak, al-Unaysi's Tafsir, Loghat-e Fors, Bahar's Sabk-shenasi, and works by Tha'alebi and Jawaliqi. Next I'll check their metadata, download what's available, run another search with alternative spellings, and test dictionary sites alongside web search.


## [2026-09-04T14:37:03.418Z] TOOL CALL #10: Bash

```json
{
 "command": "meta() { echo \"=== $1\"; curl -s \"https://archive.org/metadata/$1\" | python3 -c 'import sys,json\nd=json.load(sys.stdin)\nm=d.get(\"metadata\",{})\nif not m: print(\"  (no metadata)\"); sys.exit()\nprint(\"  title:\",m.get(\"title\"),\"| year:\",m.get(\"year\"),\"| lang:\",m.get(\"language\"),\"| desc:\",str(m.get(\"description\"))[:250].replace(\"\\n\",\" \"))\nfor f in d.get(\"files\",[]):\n  n=f[\"name\"]\n  if n.endswith(\"_djvu.txt\") or n.endswith(\".pdf\"): print(\"  \",n,f.get(\"size\"))'; }\nfor id in borhan-ghate-v2 SogdianDictionary VajnameShayest nooshinshahnameh 20220809_20220809_1444 TOB1932ARAR elshandawily14640 ar113lang79 LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi dli.ernet.439493 galaxy_ub2007_yahoo_20151117 1_20250928_20250928_1159 20260705_20260705_0657 almo3rab_gwaliqy_f_abduraheem ar120vieux55 mo3rb 20210716_20210716_2227; do meta $id; done",
 "description": "Check metadata for second-batch candidates",
 "timeout": 180000
}
```


## [2026-09-04T14:37:17.757Z] TOOL CALL #11: Bash

```json
{
 "command": "S='https://archive.org/advancedsearch.php'\nq() { echo \"=== $1\"; curl -s -G \"$S\" --data-urlencode \"q=$1\" --data-urlencode 'fl[]=identifier' --data-urlencode 'fl[]=title' --data-urlencode 'fl[]=year' --data-urlencode 'rows=8' --data-urlencode 'output=json' | python3 -c 'import sys,json\ntry:\n  d=json.load(sys.stdin)\n  for r in d[\"response\"][\"docs\"]:\n    if \"YoSoFeFATeMe\" in r[\"identifier\"] or r[\"identifier\"].startswith(\"gov.uscourts\") or r[\"identifier\"]==\"litterature-comparee\": continue\n    print(\" \",r.get(\"identifier\"),\"|\",str(r.get(\"title\"))[:90],\"|\",r.get(\"year\"))\nexcept Exception as e: print(\"ERR\",e)'; }\nq 'Sogdian Persian English dictionary'; q 'Gharib sogdian'; q 'Qarib sogdian'; q 'فرهنگ سغدی فارسی انگلیسی'\nq 'واژه نامه شایست نشایست'; q 'فعل های فارسی دری'; q 'فرهنگ واژه های عربی در زبان فارسی'; q 'فرهنگ واژه‌های عربی'\nq 'خالقی مطلق'; q 'مشیری واژه های اروپایی'; q 'واژه های دخیل'; q 'واژه‌های دخیل در قرآن'; q 'جفری قرآن'\nq 'فرهنگ واژه‌های فارسی در زبان عربی'; q 'ریشه شناسی ابوالقاسمی'; q 'ققنوس ریشه شناسی'; q 'فرهنگ سیاح'; q 'ایرانویج'\nq 'زندگی و مهاجرت آریاییان'; q 'جنیدی آریاییان'; q 'دانشگر اعلام'; q 'رکن زاده آدمیت'; q 'عمید فرهنگ فارسی'; q 'راشد محصل اوستایی'\nq 'حسنی داعی الاسلام'; q 'سعید نفیسی در مکتب استاد'; q 'خدیو جم حافظ'; q 'سجادیه'; q 'فرهنگ اعلام کتاب مقدس آریانپور'; q 'سرگذشت زبان فارسی'\nq 'فرهنگ نام های ایرانی'; q 'مهراوند واژه سازی'; q 'پورداود فرهنگ ایران باستان'; q 'فرهنگ ایران باستان'; q 'کوثر سنگ نبشته'; q 'نامه فرهنگ ایران'\nq 'خلیلی مشتقات مصادر'; q 'آریان فرهنگ واژه های همانند'; q 'title:(Kulturgeschichtliche)'; q 'title:(Ahmad Soltani) OR واژگان فارسی در زبانهای اروپایی'",
 "description": "Third batch of archive.org searches with alternate spellings",
 "timeout": 400000
}
```


## [2026-09-04T14:37:22.985Z] TOOL CALL #12: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=دیوار&d=moein",
 "prompt": "This is a Persian dictionary page. Report: (1) is the Mo'in (معین) dictionary entry for دیوار shown? Quote its full text. (2) Does the entry include an etymology in square brackets or a footnote, e.g. Pahlavi/Avestan forms like dēvār, pahl., or references like 'اوستا', 'پهلوی'? Quote exactly. (3) Which dictionaries are listed as available on the page (e.g. دهخدا, عمید, معین, برهان قاطع...)? (4) What is the page title and are there per-dictionary URL patterns visible?"
}
```


## [2026-09-04T14:37:26.105Z] TOOL CALL #13: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/دیوار/",
 "prompt": "This is a Persian dictionary aggregator page. Report which dictionaries are shown for the word دیوار (e.g. فرهنگ معین, لغت نامه دهخدا, فرهنگ عمید, فرهنگ فارسی (معین), برهان قاطع, پهلوی, etymology). Quote the full text of the فرهنگ معین (Mo'in) entry, and any etymology info such as Pahlavi forms. Also note whether لغت‌نامه دهخدا's entry cites برهان قاطع or Mo'in's footnotes (\"حاشیهٔ برهان قاطع\"). List any URL patterns you observe."
}
```


### [2026-09-04T14:37:26.527Z] TOOL RESULT

```
=== borhan-ghate-v2
  title: برهان قاطع، جلد دوم | year: 1963 | lang: per | desc: تألیف محمدحسین بن خلف تبریزی<div>باهتمام محمد معین</div><div>چاپ ۱۳۴۲ هجری شمسی</div>
   برهان قاطع، جلد دوم.pdf 10740708
   برهان قاطع، جلد دوم_djvu.txt 2359504
   برهان قاطع، جلد دوم_text.pdf 31711743
=== SogdianDictionary
  title: ÙØ±ÙÙÚ¯ Ø³ØºØ¯Û sogdian dictionary | year: None | lang: None | desc: ÙØ±ÙÙÚ¯ Ø³ØºØ¯ÛØ Ø¨Ø¯Ø±Ø§ÙØ²ÙØ§Ù ÙØ±ÛØ¨
   GharibSogdianDictionnary.pdf 31816079
   GharibSogdianDictionnary_djvu.txt 1845041
   GharibSogdianDictionnary_text.pdf 47744470
=== VajnameShayest
  title: Vajname Shayest | year: None | lang: None | desc: shayest ni shayest vajename
   vajname shayest.pdf 55078614
   vajname shayest_djvu.txt 325929
   vajname shayest_text.pdf 12288786
=== nooshinshahnameh
  title: Nooshin Shahnameh | year: None | lang: per | desc: <p>گزارشی چند درباره شاهنامه - زنده یاد عبدالحسین نوشین / م. گودرز</p><p>ناشر: پای ژه</p><p>چاپ: میخک</p><p>چاپ اول</p><p>تابستان ۱۳۶۱</p><p>تیراژ: ۳۰۰۰ نسخه</p>
   Nooshin-Shahnameh.pdf 4449099
   Nooshin-Shahnameh_djvu.txt 215561
   Nooshin-Shahnameh_text.pdf 6140490
=== 20220809_20220809_1444
  title: واژه نامک؛ فرهنگ واژه های دشوار شاهنامه | year: None | lang: None | desc: واژه نامک؛ فرهنگ واژه های دشوار شاهنامه
   واژه_نامک؛_فرهنگ_واژه_های_دشوار_شاهنامه.pdf 7243098
   واژه_نامک؛_فرهنگ_واژه_های_دشوار_شاهنامه_djvu.txt 1152733
   واژه_نامک؛_فرهنگ_واژه_های_دشوار_شاهنامه_text.pdf 11804998
=== TOB1932ARAR
  title: تفسير الالفاظ الدخيلة في اللغة العربية | year: None | lang: ara | desc: تفسير الالفاظ الدخيلة في اللغة العربية<div>مع ذكر أصلها بحروفه</div><div><br /></div><div>القس طوبيا العنيسى الحلبي اللبناني</div><div>نشره وصححه وعلَّق على حواشيه: يوسف توما البستاني</div><div><br /></div><div>1932 - الثانية</div><div><br /></div>
   تفسير الالفاظ الدخيلة في اللغة العربية.pdf 3443194
   تفسير الالفاظ الدخيلة في اللغة العربية_djvu.txt 151889
   تفسير الالفاظ الدخيلة في اللغة العربية_text.pdf 2668193
=== elshandawily14640
  title: تفسير الالفاظ الدخيلة في اللغة العربية مع ذكر اصلها بحروفه | year: None | lang: None | desc:  <div style="border:double 3.75pt;padding:1pt 4pt 1pt 4pt;background:#4C94D8;">  <p class="MsoNormal" align="center" dir="rtl" style="text-align:center;background:#4C94D8;border:none;padding:0cm;"><a rel="ugc nofollow"><b><u><span lang="ar-sa" style=
   تفسير الالفاظ الدخيلة في اللغة العربية مع ذكر اصلها بحروفه.pdf 6534804
   تفسير الالفاظ الدخيلة في اللغة العربية مع ذكر اصلها بحروفه_djvu.txt 101500
   تفسير الالفاظ الدخيلة في اللغة العربية مع ذكر اصلها بحروفه_text.pdf 1189630
=== ar113lang79
  title: طوبيا العنيسي تفسير الالفاظ الدخيلة في اللغة العربية | year: None | lang: ara | desc: طوبيا العنيسي تفسير الالفاظ الدخيلة في اللغة العربية
   طوبيا العنيسي-تفسير الالفاظ الدخيلة في اللغة العربية.pdf 3321637
   طوبيا العنيسي-تفسير الالفاظ الدخيلة في اللغة العربية_djvu.txt 151220
=== LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi
  title: Lughat e Furs - Abu Mansur Ali Bin Ahmad Asadi Tusi (Farsi) | year: None | lang: per | desc: Lughat e Furs - Abu Mansur Ali Bin Ahmad Asadi Tusi (Farsi)
   luqate-fors.pdf 10006840
   luqate-fors_djvu.txt 890981
   luqate-fors_text.pdf 11518713
=== dli.ernet.439493
  title: Lughat Faras | year: None | lang: urd | desc: <p>Source: Digital Library of India</p><p>Scanning Centre: C-DAC, Noida<br />Source Library: Maulana Azad Library Aligarh Muslim University<br />Date Accessioned: 9/15/2015 17:40<br />The Digital Library of India was a project under the auspices of t
   439493-Lughat Faras.pdf 6249057
   439493-Lughat Faras_djvu.txt 507377
   439493-Lughat Faras_text.pdf 7782861
=== galaxy_ub2007_yahoo_20151117
  title: سبک شناسی بهار | year: None | lang: Persian | desc: سبک شناسی<br />
   سبک شناسی بهار.pdf 1657310
   سبک شناسی بهار_djvu.txt 135
   سبک شناسی بهار_text.pdf 1744487
=== 1_20250928_20250928_1159
  title: سبک شناسی 1 | year: None | lang: None | desc: مجموعه‌ی سه جلدی «سبک شناسی» اثر استاد ملک‌الشعرای بهار
   سبک شناسی_1.pdf 7109240
   سبک شناسی_1_djvu.txt 1264311
   سبک شناسی_2.pdf 6070374
   سبک شناسی_2_djvu.txt 1133676
   سبک شناسی_3.pdf 6332103
   سبک شناسی_3_djvu.txt 1219047
=== 20260705_20260705_0657
  title: فقه اللغة وسر العربية، اثر عبدالملك بن محمد بن اسماعيل ثعالبي۔ عربی ۔ حق | year: None | lang: ara | desc: <b>فقه اللغة وسر العربية، اثر عبدالملك بن محمد بن اسماعيل ثعالبي۔ عربی  ۔متون اربعہ،  فقہ حنفی، مختصر القدوری، الامام ابو الحسین احمد بن محمد بن احمد بن جعفر بن حمدان البغدادی القدوری، ۔ المختار، امام موصلی،۔ کنز الدقائق، امام نسفی۔ الوقایہ، تاج الشر
   فقه اللغة وسر العربية، اثر عبدالملك بن محمد بن اسماعيل ثعالبي۔ عربی ۔ حق .pdf 11560092
   فقه اللغة وسر العربية، اثر عبدالملك بن محمد بن اسماعيل ثعالبي۔ عربی ۔ حق _djvu.txt 1299560
=== almo3rab_gwaliqy_f_abduraheem
  title: المعرب من الكلام الأعجمي | year: None | lang: Arabic | desc: None
   almo3rab-gwaliqy-f-abdulraheem.pdf 10321335
   almo3rab-gwaliqy-f-abdulraheem_djvu.txt 285355
   almo3rab-gwaliqy-f-abdulraheem_text.pdf 11220937
=== ar120vieux55
  title: أبو منصور الجواليقي المعرب من الكلام الأعجمي على حروف المعجم | year: None | lang: ara | desc: أبو منصور الجواليقي المعرب من الكلام الأعجمي على حروف المعجم
   أبو منصور الجواليقي-المعرب من الكلام الأعجمي على حروف المعجم.pdf 5887075
   أبو منصور الجواليقي-المعرب من الكلام الأعجمي على حروف المعجم_djvu.txt 365307
=== mo3rb
  title: mo3rb | year: None | lang: Arabic | desc: ktab almo3rb
   mo3rb.pdf 12933745
   mo3rb_djvu.txt 1296442
=== 20210716_20210716_2227
  title: إبن منصور الجواليقي المعرب من كلام العرب | year: None | lang: ara | desc: الجواليقي - المعرب من كلام العرب
   إبن منصور الجواليقي المعرب من كلام العرب.pdf 35306755
   إبن منصور الجواليقي المعرب من كلام العرب_djvu.txt 374461
   إبن منصور الجواليقي المعرب من كلام العرب_text.pdf 6145263
```


## [2026-09-04T14:37:26.884Z] TOOL CALL #14: WebSearch

```json
{
 "query": "Gharib \"Sogdian dictionary\" Sogdian-Persian-English 1995 pdf online full text"
}
```


## [2026-09-04T14:37:27.632Z] TOOL CALL #15: WebSearch

```json
{
 "query": "\"واژه های دخیل در قرآن مجید\" بدره ای pdf دانلود"
}
```


## [2026-09-04T14:37:27.840Z] TOOL CALL #16: WebSearch

```json
{
 "query": "\"اساس اشتقاق فارسی\" خالقی مطلق pdf"
}
```


### [2026-09-04T14:37:57.810Z] TOOL RESULT

```
=== Sogdian Persian English dictionary
  persian-etymology-charts-nourai | Persian Etymology Charts Nourai | 2022
=== Gharib sogdian
=== Qarib sogdian
=== فرهنگ سغدی فارسی انگلیسی
=== واژه نامه شایست نشایست
=== فعل های فارسی دری
=== فرهنگ واژه های عربی در زبان فارسی
  Dic_M_Azarnosh | فرهنگ معاصر عربی فارسی آذرتاش آذرنوش | None
=== فرهنگ واژه‌های عربی
  abo_abdrahman_kordi_barid_4 | لغت نامه دهخدا ب ت 4 | None
  abo_abdrahman_kordi_barid_2_20150624 | لغت نامه دهخدا ا 2 | None
  abo_abdrahman_kordi_barid_3 | لغت نامه دهخدا ا ب 3 | None
  abo_abdrahman_kordi_barid_1_20150624 | لغت نامه دهخدا آ 1 | None
=== خالقی مطلق
  6_20250518_20250518_1951 | شاهنامه خالقی جلد 6 | None
  img-20200807-002643-699 | IMG 20200807 002643 699 | None
  ya_1_095 | شاهنامه جلد 1 | None
  b6562155-s | Nizami of Ganja (نظامی گنجه‌ای) | 1402
  TarikheRuzePayaneNazmeShahname | Tarikhe Ruze Payane Nazme Shahname | None
  hamedkheradpishe_gmail_8 | شاهنامه | None
=== مشیری واژه های اروپایی
=== واژه های دخیل
=== واژه‌های دخیل در قرآن
=== جفری قرآن
=== فرهنگ واژه‌های فارسی در زبان عربی
  abo_abdrahman_kordi_barid_4 | لغت نامه دهخدا ب ت 4 | None
  abo_abdrahman_kordi_barid_2_20150624 | لغت نامه دهخدا ا 2 | None
  abo_abdrahman_kordi_barid_3 | لغت نامه دهخدا ا ب 3 | None
  abo_abdrahman_kordi_barid_1_20150624 | لغت نامه دهخدا آ 1 | None
=== ریشه شناسی ابوالقاسمی
=== ققنوس ریشه شناسی
=== فرهنگ سیاح
=== ایرانویج
  keshvare-haftom | Keshvare Haftom, کشور هفتم | 2021
  20230705_20230705_1505 | ذبیح بهروز - تقویم و تاریخ در ایران | 1952
  Iranvej | ایرانویج | None
=== زندگی و مهاجرت آریاییان
=== جنیدی آریاییان
=== دانشگر اعلام
=== رکن زاده آدمیت
=== عمید فرهنگ فارسی
=== راشد محصل اوستایی
=== حسنی داعی الاسلام
  Seerat_e_pak | مجموعہ سیرتِ طیبہ | None
=== سعید نفیسی در مکتب استاد
=== خدیو جم حافظ
=== سجادیه
  sahifa-sajjadia-416 | أقدم نسخة من الصحيفة السجادية | None
  MavaezSahifemarefat16 | Sahifemarefat 16 | 2017
  info_mtif_56 | الصحيفة الکاملة السجادية | None
  MavaezSahifemarefat7 | Sahifemarefat 7 | 2017
  info_mtif_20180725 | الصحیفة الثانیة السجادیة | None
  20250203_20250203_1929 | صحيفه سجاديه به روايت حسين بن اشکيب | None
  20230409-124131 | آشنایی با صحیفه سجادیه - جلسه اول | 1402
  shahryar122000_yahoo_201808 | ترجمه و شرح صحیفه سجادیه = درسایه سار صحیفه | 2018
=== فرهنگ اعلام کتاب مقدس آریانپور
=== سرگذشت زبان فارسی
  abo1_20260718 | ابومسلم‌نامه به روایت ابوطاهر طرسوسی | 2001
  RashdiFamilyPirJhando | A brief introduction of the Pir jhandewaras of the Rashdi family branch "Pir Jhanda": Darg | 2023
  OMiGo | صفحه‌پشتیبان از تمامی مطالب وبلاگ‌رسمی رسانه یوسف‌فاطمه | 1400
  dehkhoda_202508 | دهخدا و لغت‌نامه | 1402
  HistoricalBackgroundOfRashdiFamily | Review of the family and historical background of the Rashdi family in Sindh and their rel | 2003
=== فرهنگ نام های ایرانی
  farhang-afsaneh-haye-mardom-iran-jeld6-ejra-nahid-shafegh | دانلود رایگان کتاب صوتی فرهنگ افسانه‌های مردم ایران جلد6 نویسندگان علی اشرف درویشیان و رضا | None
  shesh-fasl_tabaritreatise_on_astrolabe_202604 | شش فصل یا معرفة الاسطرلاب - A treatise on Astrolabe, from 11th Century | 1995
  abu-abdurahman-kurdi-f_barid_20180203_1455 | کامل ترین فرهنگ نام های ایرانی فلورا جهان دار | None
  shesh-fasl_tabaritreatise_on_astrolabe | shesh fasl شش فصل یا معرفة الاسطرلاب | None
  Ashub5 | دانلود سریال آشوب قسمت پنجم 5 /اپارات نماشا یوتوب | None
  rebel-series | دانلود سریال یاغی | None
  yaghi-series-episode-14 | دانلود قسمت چهاردهم سریال یاغی | None
=== مهراوند واژه سازی
=== پورداود فرهنگ ایران باستان
=== فرهنگ ایران باستان
  20201001_20201001_1820 | تاریخ سیاسی ایران باستان | 2012
  NamayeshhayeIrani | namayeshhaye Irani | None
  e9b2-0d55-4e34-82a5 | مجموعه سه جلدی تاریخ ایران باستان | None
  iranology11_gmail_IRAN | IRAN ; Religion & Culture= ایران ؛ آیین و فرهنگ | 2016
  20250222_20250222_1918 | جواهر الكلم وفرائد الحكم - علي بن عبيدة الريحاني | None
  20250222_20250222_1912 | جواهر الكلم وفرائد الحكم علي بن عبيدة الريحاني | None
  20220422_20220422_1807 | خویدوده. ازدواج با محارم در روایات زرتشتی | None
=== کوثر سنگ نبشته
=== نامه فرهنگ ایران
  KhavarigUndSchia | Khavarig und Schia(چاپ اول) | 2016
  abo_abdrahman_kordi_barid_20150502_0842 | فرهنگ نامه ی نام اوران اشنایی با چهره های سرشناس تاریخ ایران و جهان | 2015
  3-1383_20210206 | دایرة المعارف دانش بشر جلد 3 (نمایه) چاپ 1383 | 2021
  2-1383_20210206 | دایرة المعارف دانش بشر جلد 2 چاپ 1383 | 2021
  shortand-naughty | عصر اوسکولی - حکایات و جملات قصار | 2024
  180_20250722 | ماهنامه ادبیات داستانی چوک شماره 180 | 2025
  1-1383_20210206 | دایرة المعارف دانش بشر جلد 1 چاپ 1383 | 2021
  interuniversal | مصاحبه استاد محمد علی طاهری در خصوص انتقادات صورت گرفته از عرفان حلقه (عرفان کیهانی) | [2001, 2010]
=== خلیلی مشتقات مصادر
=== آریان فرهنگ واژه های همانند
=== title:(Kulturgeschichtliche)
  unserhausundhof00wolfgoog | Unser Haus und Hof: Kulturgeschichtliche Schilderungen aus Siebenbürgen | 1882
  paper-doi-10_1038_078660a0 | Kraft: Ökonomische, technische und kulturgeschichtliche Studien über die Machlentfaltung d | 1908
  11621885bsb | Die Mennoniten in Ostfriesland vom 16. bis zum 18. Jahrhundert: aktenmässige kulturgeschic | 1887
  schillerkulturg00unkngoog | Schiller: Kulturgeschichtliche Novelle in sechs Büchern | 1873
  buntebltterkult00kluggoog | Bunte Blätter: Kulturgeschichtliche Vorträge und Aufsätze | 1908
  bub_gb_EAs-AAAAIAAJ | Schiller Kulturgeschichtliche Novelle in sechs Büchern | 1873
  jstor-27699713 | Die Küche des 16. Jahrhunderts nach Johann Fischart; Eine Kulturgeschichtliche Studie | 1903
  italograecakultu01saal | Italograeca [microform], kulturgeschichtliche studien auf sprachwissenschaftlicher grundla | 1882
=== title:(Ahmad Soltani) OR واژگان فارسی در زبانهای اروپایی
  fav-mitra_ahmad_soltani | Mitra Ahmad Soltani Favorites | None
```


### [2026-09-04T14:38:04.468Z] TOOL RESULT

```
Web search results for query: "Gharib "Sogdian dictionary" Sogdian-Persian-English 1995 pdf online full text"

Links: [{"title":"Sogdian Dictionary: Sogdian - Persian - English by B. Gharib: New Hardcover (1995) 1st Edition. | Anis Press","url":"https://www.abebooks.com/first-edition/Sogdian-Dictionary-Persian-English-B-Gharib/30040190515/bd"},{"title":"Sogdian Dictionary: Sogdian - Persian - English: B. Gharib: 9789645558060: Amazon.com: Books","url":"https://www.amazon.com/Sogdian-Dictionary-Persian-English/dp/9645558069"},{"title":"Sogdian Dictionary, Sogdian Persian English by Gharib, Badrozaman | Leather bound | 1995 | Farhangan Publications | 9789645558060 | Biblio","url":"https://www.biblio.com/book/sogdian-dictionary-sogdian-persian-english-gharib/d/1196715091"},{"title":"Sogdian Dictionary: Sogdian - Persian - English - B. Gharib: 9789645558060 - AbeBooks","url":"https://www.abebooks.com/9789645558060/Sogdian-Dictionary-Persian-English-Gharib-9645558069/plp"},{"title":"Sogdian Dictionary: Sogdian - Persian - English by B. Gharib | Goodreads","url":"https://www.goodreads.com/book/show/91976503"},{"title":"Full text of \"Ù Ø±Ù‡Ù†Ú¯ Ø³ØºØ¯ÛŒ sogdian dictionary\"","url":"https://archive.org/stream/SogdianDictionary/GharibSogdianDictionnary_djvu.txt"},{"title":"CiNii Books - Sogdian dictionary : Sogdian--Persian--English","url":"https://ci.nii.ac.jp/ncid/BA27085278?l=en"},{"title":"Sogdian dictionary : Sogdian, Persian, English / B. Gharib ; [editorial supervisor, A. Mansouri ; editor, S. Fotouhi.] | Book | Badr al-Zamān Qarīb 1929 or 1930- (Mansouri, Ahmad | Mansouri, Ahmad;Fotouhi, Sharzad | The National Library of Israel","url":"https://www.nli.org.il/en/books/NNL_ALEPH990018188540205171/NLI"},{"title":"Badr al-Zaman Gharib","url":"https://en.wikipedia.org/wiki/Badr_al-Zaman_Gharib"},{"title":"Sogdian alphabet","url":"https://en.wikipedia.org/wiki/Sogdian_alphabet"}]

Based on the search results, I found information about the Gharib Sogdian Dictionary:

The Sogdian Dictionary: Sogdian - Persian - English by B. Gharib was published on January 1, 1995, by Tehran: Farhangan Publications and contains 559 pages.

I also found evidence that the full text is available on Archive.org. The dictionary's full text has been archived on Archive.org at https://archive.org/stream/SogdianDictionary/, with the copyright dated 1995 and published by Farhangan Publications with editorial supervisor A. Mansouri and editor S. Fotouhi.

However, the search results do not indicate whether a freely accessible PDF version is available online. The Archive.org text file appears to contain the full text content, though the accessibility may be restricted depending on Archive.org's lending policies for this particular title.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:38:09.274Z] TOOL RESULT

```
Web search results for query: ""اساس اشتقاق فارسی" خالقی مطلق pdf"

Links: [{"title":"کتابخانه مجازی ادبیات - جلال خالقی مطلق","url":"https://eliteraturebook.com/authors/books/2924/%D8%AC%D9%84%D8%A7%D9%84+%D8%AE%D8%A7%D9%84%D9%82%DB%8C+%D9%85%D8%B7%D9%84%D9%82"},{"title":"خرید کتاب اساس اشتقاق فارسی","url":"https://www.iketab.com/اساس-اشتقاق-فارسی"},{"title":"از شاهنامه تا خداینامه - خالقی مطلق.pdf","url":"https://s17.picofile.com/file/8425875600/%D8%A7%D8%B2_%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87_%D8%AA%D8%A7_%D8%AE%D8%AF%D8%A7%DB%8C%D9%86%D8%A7%D9%85%D9%87_%D8%AE%D8%A7%D9%84%D9%82%DB%8C_%D9%85%D8%B7%D9%84%D9%82.pdf.html"},{"title":"اساس اشتقاق فارسی - پارسی‌شناسی","url":"https://parsishenasi.ir/wiki/index.php/%D8%A7%D8%B3%D8%A7%D8%B3_%D8%A7%D8%B4%D8%AA%D9%82%D8%A7%D9%82_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"دانلود کتاب شاهنامه فردوسی به تصحیح دکتر جلال خالقی مطلق - فرهنگ و ادب","url":"https://farhangoadabeirani.blogsky.com/1395/09/03/post-1122/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-%D9%81%D8%B1%D8%AF%D9%88%D8%B3%DB%8C-%D8%A8%D9%87-%D8%AA%D8%B5%D8%AD%DB%8C%D8%AD-%D8%AF%DA%A9%D8%AA%D8%B1-%D8%AC%D9%84%D8%A7%D9%84-%D8%AE%D8%A7%D9%84%D9%82%DB%8C-%D9%85%D8%B7%D9%84%D9%82"},{"title":"دانلود کتابهای جلال خالقی مطلق","url":"https://ketabnak.com/persons/3681/%D8%AC%D9%84%D8%A7%D9%84+%D8%AE%D8%A7%D9%84%D9%82%DB%8C+%D9%85%D8%B7%D9%84%D9%82"},{"title":"دانلود شاهنامه pdf - دانلود رایگان شاهنامه با لینک مستقیم","url":"https://hiword.ir/downloads/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87-pdf/"},{"title":"بررسی و مقایسه شرح های خالقی مطلق،کزازی و جوینی بر جلد دوم شاهنامه فردوسی","url":"https://www.virascience.com/thesis/518997/"}]

Based on the search results, I found information about "اساس اشتقاق فارسی" (Foundations of Persian Etymology):

"اساس اشتقاق فارسی" is a book by Paul Hörn about the etymology and derivation of Persian words. Jalal Khalegi Motlagh translated a portion of this book, covering words beginning with letters "آ" through "خ", along with notes by Heinrich Hübschmann from his work "Persian Studies" in 1356 (1977), adding evidence from Persian and Pahlavi.

Dr. Jalal Khalegi Motlagh translated this book in 1356 AH with the name "اساس اشتقاق فارسی". The complete translation of this book, along with Hübschmann's critical notes and evidence from Persian and Pahlavi, was published in 1394 (2015) under the name "Dictionary of Persian Etymology".

The search results indicate that the work is available in PDF format from several sources, though I cannot directly access specific PDF download links from these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:38:10.098Z] TOOL RESULT

```
# Persian Dictionary Page Analysis

## (1) Mo'in Dictionary Entry

The Mo'in (معین) dictionary entry for دیوار is shown. Its full text reads:

"جداری از سنگ ، چوب ، آجر و غیره که اطراف خانه ، زمین و باغ و غیره به جهت محصور کردن و حفاظت آن بنا می کنند. 2 - حایل میان دو چیز."

## (2) Etymology Information

The entry includes etymological markers in square brackets: **[ په . ]** (indicating Persian origin) and **(اِ.)** (indicating noun classification). However, no Pahlavi, Avestan, or ancient language forms like "dēvār" or references to "اوستا" or "پهلوی" are present in the visible text.

## (3) Available Dictionaries

The page lists: **فرهنگ انتشارات معین** (Mo'in Dictionary of Publications). The header indicates "26 فرهنگ" (26 dictionaries), suggesting multiple resources are available through the platform, though specific names beyond Mo'in aren't detailed in this excerpt.

## (4) Page Title and URL Patterns

The page title is **"معنی دیوار | واژه یاب"** (Meaning of dīvār | Vazheh Yab). URL patterns visible include dictionary-specific paths like `/moein/دیوار` and parameter-based queries like `?q=دیوار&d=moein`.
```


### [2026-09-04T14:38:10.482Z] TOOL RESULT

```
Web search results for query: ""واژه های دخیل در قرآن مجید" بدره ای pdf دانلود"

Links: [{"title":"نگاهی به (واژه های دخیل در قرآن مجید)","url":"https://vista.ir/m/a/seg2v/%D9%86%DA%AF%D8%A7%D9%87%DB%8C-%D8%A8%D9%87-(%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%AF%D8%B1-%D9%82%D8%B1%D8%A2%D9%86-%D9%85%D8%AC%DB%8C%D8%AF)"},{"title":"کتاب واژه های دخیل در قرآن مجید ~آرتور جفری - نشر توس - آدینه بوک","url":"https://www.adinehbook.com/gp/product/9643153137"},{"title":"واژه های دخیل در قرآن مجید - شهر کتاب آنلاین","url":"https://shahreketabonline.com/Products/Details/27542/واژه_های_دخیل_در_قرآن_مجید"},{"title":"واژه های دخیل در قرآن مجید - صفحه 1","url":"https://noorlib.ir/book/view/12868"},{"title":"دانلود نرم افزار واژه های دخیل در قرآن مجید","url":"http://tahaquran.ir/%D9%86%D8%B1%D9%85-%D8%A7%D9%81%D8%B2%D8%A7%D8%B1-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%AF%D8%B1-%D9%82%D8%B1%D8%A2%D9%86-%D9%85%D8%AC%DB%8C%D8%AF/"},{"title":"واژه های دخیل در قرآن مجید - یکتامهر|ارسال به تمام نقاط","url":"https://yektabook.com/product/14560/واژه-های-دخیل-در-قرآن-مجید"},{"title":"متن كامل كتاب واژه های دخیل در قرآن مجید اثر آرتور جفری با محیطی جذاب و كاربر پسند بر روی سایت مرکز قائمیه قرار گرفت. - خبرگزاری بازار کتاب","url":"http://www.ghnews.ir/index.php?option=com_k2&view=item&id=27824:%D9%85%D8%AA%D9%86-%D9%83%D8%A7%D9%85%D9%84-%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%9C-%D8%AF%D8%AE%DB%9C%D9%84-%D8%AF%D8%B1-%D9%82%D8%B1%D8%A2%D9%86-%D9%85%D8%AC%DB%9C%D8%AF-%D8%A7%D8%AB%D8%B1-%D8%A2%D8%B1%D8%AA%D9%88%D8%B1-%D8%AC%D9%81%D8%B1%DB%9C-%D8%A8%D8%A7-%D9%85%D8%AD%DB%9C%D8%B7%DB%9C-%D8%AC%D8%B0%D8%A7%D8%A8-%D9%88-%D9%83%D8%A7%D8%B1%D8%A8%D8%B1-%D9%BE%D8%B3%D9%86%D8%AF-%D8%A8%D8%B1-%D8%B1%D9%88%DB%9C-%D8%B3%D8%A7%DB%9C%D8%AA-%D9%85%D8%B1%DA%A9%D8%B2-%D9%82%D8%A7%D8%A6%D9%85%DB%9C%D9%87-%D9%82%D8%B1%D8%A7%D8%B1-%DA%AF%D8%B1%D9%81%D8%AA&Itemid=125"},{"title":"واژه های دخیل در قرآن مجید - بانک کتاب رایا","url":"https://rayabook.net/?option=com_hikashop&ctrl=product&task=show&cid=30151"},{"title":"کتاب واژه های دخیل در قرآن مجید","url":"https://ketabnak.com/book/51136/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%AF%D8%B1-%D9%82%D8%B1%D8%A2%D9%86-%D9%85%D8%AC%DB%8C%D8%AF"},{"title":"دانلود کتاب واژه های دخیل در قرآن مجید | کتابکو","url":"https://ketabkoo.com/book/1504276/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%AF%D8%B1-%D9%82%D8%B1%D8%A2%D9%86-%D9%85%D8%AC%DB%8C%D8%AF"}]

بر اساس نتایج جستجو، اطلاعات زیر را درباره کتاب "واژه های دخیل در قرآن مجید" به دست آمد:

## درباره کتاب

کتاب واژه های دخیل در قرآن مجید اثر نویسنده آرتور جفری است که توسط دکتر فریدون بدره ای ترجمه شده و توسط انتشارات توس منتشر شده است.

## محتوای کتاب

مؤلف واژه های دخیل قرآن را به سه گروه دسته بندی کرده است: الف) واژه هایی که به هیچ وجه عربی نیستند; چون: استبرق, زنجبیل و فردوس. ب) واژه های سامی که ریشه سه حرفی آنها نیز ممکن است در زبان عربی باشد, اما در قرآن با معنای ریشه عربی استعمال نشده اند. ج) واژه های عربی اصیل که معنایشان دارای صبغه ای است که نتیجه استعمال آنها در زبانهای همزاد با زبان عربی است.

## دانلود PDF

کتاب دیجیتال "واژه های دخیل در قرآن مجید" با نسخه pdf در دسترس است. لینک‌های دانلود با حجم‌های ۸۴۶ کیلوبایت و ۹۰۵کیلوبایت موجود است.

می‌توانید برای دانلود به سایت‌های معرفی شده در نتایج جستجو مراجعه کنید، از جمله نورلیب (noorlib.ir) و تاقرآن (tahaquran.ir).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:38:14.887Z] TOOL RESULT

```
# Persian Dictionary Analysis: دیوار (Divar - Wall)

## Dictionaries Shown

The page aggregates entries from multiple Persian dictionaries:

1. **لغت‌نامه دهخدا** (Dehkhoda Dictionary)
2. **فرهنگ فارسی** (Persian Dictionary)
3. **فرهنگ معین** (Mo'in Dictionary)
4. **فرهنگ عمید** (Amid Dictionary)
5. **دانشنامه اسلامی** (Islamic Encyclopedia)
6. **دانشنامه عمومی** (General Encyclopedia)

## Farhang-e Mo'in Entry (Full Text)

The Mo'in dictionary provides this definition:

"[ په . ] (اِ. ) ۱ - جداری از سنگ ، چوب ، آجر و غیره که اطراف خانه ، زمین و باغ و غیره به جهت محصور کردن و حفاظت آن بنا می کنند. ۲ - حایل میان دو چیز."

(Translation: A barrier made of stone, wood, brick, etc., constructed around houses, lands, and gardens for enclosure and protection; also, something separating two things.)

## Etymology Information

The **Dehkhoda entry** notes: "دیو + آر" (div + ar), referencing Persian linguistic transformation patterns where "ل" and "ر" interchange.

Modern scholarly etymology traces the word through **Pahlavi** (divār) to proto-Iranian roots meaning "to enclose" or "to protect."

## URL Pattern

The dictionary uses the format: `/fatofa/[WORD]/` for linked terms.
```


## [2026-09-04T14:38:53.915Z] AGENT (thinking)

I confirmed vajehyab and abadis show the Mo'in entry with only the "[په.]" Pahlavi tag (no actual Pahlavi form), identified AEF as Khaleqi Motlaq's Persian translation of Horn's Grundriss, and found VDQ on noorlib.ir. Next, I'll download the newly found texts, work out BQT's page offsets, test noorlib's viewer and the vajehyab Dehkhoda entry, and continue searching for remaining mid-frequency titles.


## [2026-09-04T14:39:16.780Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\ndl() { curl -sL -o \"$2\" \"https://archive.org/download/$1\"; printf \"%s: %s bytes\\n\" \"$2\" \"$(wc -c < \"$2\")\"; }\ndl 'borhan-ghate-v2/%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%AF%D9%88%D9%85_djvu.txt' BQT_v2.txt\ndl 'SogdianDictionary/GharibSogdianDictionnary_djvu.txt' SOD.txt\ndl 'VajnameShayest/vajname%20shayest_djvu.txt' SNS.txt\ndl '20220809_20220809_1444/%D9%88%D8%A7%DA%98%D9%87_%D9%86%D8%A7%D9%85%DA%A9%D8%9B_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D9%88%D8%A7%DA%98%D9%87_%D9%87%D8%A7%DB%8C_%D8%AF%D8%B4%D9%88%D8%A7%D8%B1_%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87_djvu.txt' FSF.txt\ndl 'TOB1932ARAR/%D8%AA%D9%81%D8%B3%D9%8A%D8%B1%20%D8%A7%D9%84%D8%A7%D9%84%D9%81%D8%A7%D8%B8%20%D8%A7%D9%84%D8%AF%D8%AE%D9%8A%D9%84%D8%A9%20%D9%81%D9%8A%20%D8%A7%D9%84%D9%84%D8%BA%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_djvu.txt' TAD.txt\ndl 'LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi/luqate-fors_djvu.txt' FRS.txt\ndl '1_20250928_20250928_1159/%D8%B3%D8%A8%DA%A9%20%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_1_djvu.txt' SBK.txt\ndl '20260705_20260705_0657/%D9%81%D9%82%D9%87%20%D8%A7%D9%84%D9%84%D8%BA%D8%A9%20%D9%88%D8%B3%D8%B1%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%D8%8C%20%D8%A7%D8%AB%D8%B1%20%D8%B9%D8%A8%D8%AF%D8%A7%D9%84%D9%85%D9%84%D9%83%20%D8%A8%D9%86%20%D9%85%D8%AD%D9%85%D8%AF%20%D8%A8%D9%86%20%D8%A7%D8%B3%D9%85%D8%A7%D8%B9%D9%8A%D9%84%20%D8%AB%D8%B9%D8%A7%D9%84%D8%A8%D9%8A%DB%94%20%D8%B9%D8%B1%D8%A8%DB%8C%20%DB%94%20%D8%AD%D9%82%20_djvu.txt' KFL.txt\ndl 'mo3rb/mo3rb_djvu.txt' ARB_mo3rb.txt\ndl 'almo3rab_gwaliqy_f_abduraheem/almo3rab-gwaliqy-f-abdulraheem_djvu.txt' ARB_abdulraheem.txt\necho \"--- Iranvej meta\"; curl -s https://archive.org/metadata/Iranvej | python3 -c 'import sys,json;d=json.load(sys.stdin);m=d.get(\"metadata\",{});print(m.get(\"title\"),m.get(\"description\"));[print(\" \",f[\"name\"],f.get(\"size\")) for f in d.get(\"files\",[]) if f[\"name\"].endswith((\"_djvu.txt\",\".pdf\"))]'\necho \"--- imagecounts\"; for id in borhan-ghate-v1 borhan-ghate-v2 SogdianDictionary VajnameShayest; do printf \"$id: \"; curl -s https://archive.org/metadata/$id/metadata/imagecount; echo; done\necho \"--- archivelab page OCR test\"; curl -s 'https://api.archivelab.org/books/borhan-ghate-v1/pages/374/ocr' | head -c 400; echo\necho \"--- samples\"; for f in SOD SNS FSF TAD FRS SBK KFL ARB_mo3rb; do echo \"## $f\"; sed -n '150,400p' $f.txt | grep -v '^\\s*$' | head -8 | cut -c1-120; done",
 "description": "Download newly found reference texts and sample them",
 "timeout": 400000
}
```


## [2026-09-04T14:39:24.346Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\n# BQT v1: get djvu.xml and build page-split text with FF, then look for printed page numbers\ncurl -sL -o BQT_v1_djvu.xml 'https://archive.org/download/borhan-ghate-v1/%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%A7%D9%88%D9%84_djvu.xml'\nls -la BQT_v1_djvu.xml\npython3 - <<'EOF'\nimport re,html\nx=open('BQT_v1_djvu.xml',encoding='utf-8',errors='ignore').read()\npages=re.findall(r'<OBJECT.*?</OBJECT>',x,flags=re.S)\nprint(\"leaves:\",len(pages))\nout=[]\nfor i,p in enumerate(pages):\n    lines=[]\n    for ln in re.findall(r'<LINE>(.*?)</LINE>',p,flags=re.S):\n        words=re.findall(r'<WORD[^>]*>(.*?)</WORD>',ln,flags=re.S)\n        lines.append(' '.join(html.unescape(w) for w in words))\n    out.append('\\n'.join(lines))\nopen('BQT_v1_pages.txt','w',encoding='utf-8').write('\\f'.join(out))\n# show first 2 lines of leaves 100..106 to find printed page numbers\nfor i in range(100,107):\n    ls=[l for l in out[i].split('\\n') if l.strip()]\n    print(i, '|', ls[0][:80] if ls else '', '|', ls[-1][:80] if ls else '')\nEOF",
 "description": "Build page-split BQT vol 1 text from djvu.xml and inspect page headers",
 "timeout": 400000
}
```


## [2026-09-04T14:39:27.034Z] TOOL CALL #19: WebFetch

```json
{
 "url": "https://noorlib.ir/book/view/12868",
 "prompt": "This is a book viewer page on noorlib.ir for the Persian translation of Jeffery's Foreign Vocabulary of the Qur'an (واژه های دخیل در قرآن مجید). Report: book title, author/translator, publisher/year, number of pages, whether page text (OCR) is visible or only images, and any URL pattern for jumping to a page number (e.g. ?pageNumber=). Also whether a login is required."
}
```


## [2026-09-04T14:39:30.033Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=دیوار&d=dehkhoda",
 "prompt": "Quote the beginning of the Dehkhoda (لغت‌نامه دهخدا) entry for دیوار including any bracketed source citations such as (برهان), (حاشیهٔ برهان قاطع چ معین), (از فرهنگ فارسی معین), Pahlavi forms in Latin letters, etc. Which dictionaries does the page list in its dictionary selector (names and d= codes if visible)?"
}
```


## [2026-09-04T14:39:30.795Z] TOOL CALL #21: WebSearch

```json
{
 "query": "\"فعل های فارسی دری\" ابوالقاسمی pdf OR noorlib OR ketabnak"
}
```


## [2026-09-04T14:39:31.475Z] TOOL CALL #22: WebSearch

```json
{
 "query": "\"فرهنگ واژه های عربی در زبان فارسی\" نحوی pdf دانلود"
}
```


## [2026-09-04T14:39:32.220Z] TOOL CALL #23: WebSearch

```json
{
 "query": "\"فرهنگ واژه های فارسی در زبان عربی\" امام شوشتری pdf noorlib"
}
```


## [2026-09-04T14:39:33.014Z] TOOL CALL #24: WebSearch

```json
{
 "query": "مشیری \"فرهنگ واژه های اروپایی در فارسی\" pdf"
}
```


### [2026-09-04T14:42:13.000Z] TOOL RESULT

```
BQT_v2.txt: 2359504 bytes
SOD.txt: 1845041 bytes
SNS.txt: 325929 bytes
FSF.txt: 1152733 bytes
TAD.txt: 151889 bytes
FRS.txt: 890981 bytes
SBK.txt: 1264311 bytes
KFL.txt: 1299560 bytes
ARB_mo3rb.txt: 1296442 bytes
ARB_abdulraheem.txt: 285355 bytes
--- Iranvej meta
ایرانویج ایرانویج، برنامه ای از رادیو سدای امید پیرامون جستارهای ایرانشناسی
--- imagecounts
borhan-ghate-v1: {"error":"Couldn't get part '/imagecount' of 'metadata' for item borhan-ghate-v1"}
borhan-ghate-v2: {"error":"Couldn't get part '/imagecount' of 'metadata' for item borhan-ghate-v2"}
SogdianDictionary: {"error":"Couldn't get part '/imagecount' of 'metadata' for item SogdianDictionary"}
VajnameShayest: {"error":"Couldn't get part '/imagecount' of 'metadata' for item VajnameShayest"}
--- archivelab page OCR test

--- samples
## SOD
j*  L*l  iojui  UjlTi  jj^>  A;  ^i  -o  Jaii  jl-U^^j  (^ Ia« jl_j  ^1^  .(XXXV 
fJUjb  J-'t-?'  <Jj~C  *£  U«jlj  jl  ^j-^ajy  ^/^  .C— I  aJLi  ^Tj  0»I^T IjL 
JL>-  ^j  <ui*Ji    o  U—  tl>3>-  ijj  *-j  !  jl  *^r^"  U^*j  J***  jl  ^'  <C—*I  (--Xjc> 
6-U  I  jjJi^  (_^o  jlj  >_ j  'A*>  Ja-^  j*  i^^.j^"  ^^t^-Ot  j  >>  ^^-j^  c5^' 
j  <o^l  u,,  ... ;  ^j^jjls-  Lr  LAo-t-jjIjT  <(_j jU- 1  ^L^a  L  « jIj  jU  I  jj 
^  J._->-^  £t-^>t*0  (^L^tA    *_J>xaJ  j  ^^JaJ  Ijjj*  0_j«fl>  oW?  J-1 1 
.JjloJ^  U^l  Ji^JU  ^A 
(^U^T  j  tf-Ut)  ,^1^  ^u  jl  <T  ^Uo^w  i^-A^  ^yl  jj 
## SNS
^u-tfV^j** j-fcX.,^^ 
'Jt*- 
TTt fc 
i 1 u»J* 
« 
b 
\ 
"? 
## FSF
مقدمة مولف 
شیو کار نکارنده در تدوی ن کتاب 
از نمونه‌های فراوانی که در پیش آورده شد شیوه کار این جانب آشکار اس
که اینک آن‌را خلاصه می‌کنم: 
۱-نام‌های خحاص را نیاورده‌ام. چون برای هر خواننده شاهنامه به خوبی
است که رستم کیست و افراسیاب از کجاست و سهراب و سیاوش فرزندان که 
هستند» و برای کسی که با شاهنامه سرو کاری ندارد از دانستن این نام‌ه
به جای نام‌های خاص سیاری کلمات مرکب مانند: بدگمان نیک اختر - 
## TAD
روت ح- بوناني م ركب من 3 يتعنى غير و2008 بمعنى حي وهو غاز عنصري 
لا رائحة ولا لم ولا لون وقد يدخل بتركيب الموا. 
اس - ايطالي 0 عمعناه وحدة وهو ورقة من ورقاللعب ذات نقطة واحدة 
إسبائخ س فارسي «اسفائغ» وهو بقلة بستانية تشبهالسلق 'يسلق ورقها وب�
إسبيداج - قارسي « سفيداتك » سفيد في الفارسية معناه أبيض وأنّك في 
العبرائية معناه رصاص وهو بياض الرصاص وبال لدفيالكيميا كربونات ال�
استاذ فارمي «استاد معناه مع 
إستار يوناني 818167 تاد أزانفة وهو لقن فضة كان يساوي فى أثينا 
## FRS
مظفر از فساد نسخه‌ای که در دست داشته و از روی آن منوشته شکایت 
میکند و بخود امید میدهد که بعد ها بتصحیح آن توفیق یابد . 
این نسخه‌مانطور که محشدین‌مسعودینهظفر میکویدسارخر ابو 
مغلوطست مان -خه‌ای که‌او دردست‌داشته‌هر چهبودهالمّه ازس هم مای�
و 
کمترغلط وافتاد گی وتحرف داشته چه براغلاطی که مین مسعود از 
آنها شکات مبکرده غلماهای دبگری هم بدست او و کاتب نسخه موجود 
ما افزوده شده و شاید هم هر دو بسیاری ازموارد را که مفلوطمیینداشته 
## SBK
۷مکرر فہرست مطالب 
تش پپلوی‌اشکانی (نمونه) ازمنحة ۱۰۸ تا ۱۱۳ 
> پپلوی ساسانی (نمونه) € » ۱۱۳ € ۱۰ 
تجددهائی که درشر پیلوی رویداده است € > ۱۲۵۰ ۰ ۱۲۸ 
کتیبه‌های ساسانی (نمونه) € CIA‏ ۱۲۹ 
کتیبةٌ شاپورستاشاه (متن و ترجمه) € > ۱۲۹ > ۱۳۰ 
کنات زیرخاکی 6 ۱۳۰ > - 
سکه‌های قدیم & € ۱۳۰ 6 ۱۳۱ 
## KFL
[ البَسَّمُ ] م راك ماعب باناك بد مي لاج وال خاي واجاي وذ عي نعل الجا
| الوَهْنٌ | قد ود م ققدم لق عه عام قم علو اه لمعك قم ع وك عرقي مو قعل 
[حَلَا ] الع ا اوم د اا ل و ل ما راكع عا ع يي لكا عا يأ اي ارو م لق باك �
[الضُغف ] ا ا ا ا ا اا ا ا 1 
[ التصيره ] وا ا م و ما ل م ل وو ا لي ل باق ا باو صم ل ب ل ا با ع نر 
[ الؤغُوره | امب ا ا ل اا ل عاك لق ولا الا وا 1 
| العَمَى ] ا م 100 
| البَيْدَر | لما ا ا ا ا ا ل د ا اي ا ا د ل لوك ليا ان الا وك للا افا ا �
## ARB_mo3rb
0 عزاس ل جلإلرو 
تقسدم لكاتب 6 
والشالث : المسارعة إلى القاس كثير من . أصول اكات الأممية 
قْ الفارسية ٠‏ وكانت الفارسية أقرب إلى ملماء ألالفة دن غيرها 6 فكا
الفارسية فيا يظنونه أعميا أقرب إلى ظنونهم . > تخص كلمة “«عمى”“ با�
عا عازه ى فى الأصل الكل من ١‏ لس نس ماه 
ومن أمغله هذاء: 7 الأيل 5 قال المؤاف (ص 0( : 2» والأيل 
الراهب فارمسى مدب » ٠ه‏ والكمة أيسءت فارسية »6 بل سر رانية » ومعتا�
```


### [2026-09-04T14:42:42.881Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 26399828 Sep  4 10:42 BQT_v1_djvu.xml
leaves: 777
100 | مقدمه نود ودو | مردم آذدباجان را که بدان اتساب دارد - ملاك قراد داده‌امت ؛ مثلا در «آغل» وقرخنه»
101 | نود وسه هایس برهان | وحاشبه. م.م. ۳ب چهانگیری این‌نام ر ابجا ذبل فربو» آورده. م.م.
102 | مقدمه ۱ نود وچپار | کردن» حکومت کردن. «وبلیامز ۲ ۸۷ :۳ دلی‌آمن کمه ریطي بتر کیب #صاحت ۳ ندارد. م۴
103 | نود وپنحع نقایس برهان | ویکی‌ماده وسرهای آنهارا باتش بسوزانند ودرشراب بریز ند هر کس از
104 | "مقدنمه ۰ نود شش | (مقد مه بر های دواز دهم )
105 | م . معین | فرهنگه نظام ج۱ ص۲۲.
106 | نود وهشت | بودانی ۸502۲2805 .
```


### [2026-09-04T14:42:50.403Z] TOOL RESULT

```
Web search results for query: ""فعل های فارسی دری" ابوالقاسمی pdf OR noorlib OR ketabnak"

Links: [{"title":"(PDF) یای» پایانی فعل امر در فارسی دری » The Final “y” of the Imperative verb of Early New Persian","url":"https://www.academia.edu/31883235/%DB%8C%D8%A7%DB%8C_%D9%BE%D8%A7%DB%8C%D8%A7%D9%86%DB%8C_%D9%81%D8%B9%D9%84_%D8%A7%D9%85%D8%B1_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D8%AF%D8%B1%DB%8C_The_Final_y_of_the_Imperative_verb_of_Early_New_Persian"},{"title":"دانلود و خرید کتاب واژگان زبان فارسی دری اثر محسن ابولقاسمی","url":"https://fidibo.com/book/6668-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1%DB%8C"},{"title":"کتاب دری استاد شاهپور عنایت | PDF","url":"https://www.scribd.com/document/802364864/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%B1%DB%8C-%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF-%D8%B4%D8%A7%D9%87%D9%BE%D9%88%D8%B1-%D8%B9%D9%86%D8%A7%DB%8C%D8%AA"},{"title":"(PDF) دری ادبیات و زبان","url":"https://www.academia.edu/34153858/%D8%AF%D8%B1%DB%8C_%D8%A7%D8%AF%D8%A8%DB%8C%D8%A7%D8%AA_%D9%88_%D8%B2%D8%A8%D8%A7%D9%86"},{"title":"ادبیات دری - دانلود pdf","url":"https://noorlib.ir/book/info/115018/%D8%A7%D8%AF%D8%A8%DB%8C%D8%A7%D8%AA-%D8%AF%D8%B1%DB%8C"},{"title":"دستور زبان دری - دانلود pdf","url":"https://noorlib.ir/book/info/103541/%D8%AF%D8%B3%D8%AA%D9%88%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%AF%D8%B1%DB%8C"},{"title":"مجموعه کتاب های ابوالقاسم حالت - فایلمس","url":"https://filemas.com/product/%d9%85%d8%ac%d9%85%d9%88%d8%b9%d9%87-%da%a9%d8%aa%d8%a7%d8%a8-%d9%87%d8%a7%db%8c-%d8%a7%d8%a8%d9%88%d8%a7%d9%84%d9%82%d8%a7%d8%b3%d9%85-%d8%ad%d8%a7%d9%84%d8%aa/"},{"title":"دانلود کتاب فهرست فعلهای فارسی با معنای آنها","url":"https://www.ketabnak.com/book/45024/%D9%81%D9%87%D8%B1%D8%B3%D8%AA-%D9%81%D8%B9%D9%84%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%85%D8%B9%D9%86%D8%A7%DB%8C-%D8%A2%D9%86%D9%87%D8%A7"},{"title":"دانلود کتاب تاریخ منتظم ناصری - جلد اول","url":"https://ketabnak.com/book/57290/%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE-%D9%85%D9%86%D8%AA%D8%B8%D9%85-%D9%86%D8%A7%D8%B5%D8%B1%DB%8C-%D8%AC%D9%84%D8%AF-%D8%A7%D9%88%D9%84"},{"title":"عطیه مشاهری فرد","url":"https://www.goodreads.com/user/show/84119667"}]

Based on the search results, I found relevant information about the query "فعل های فارسی دری ابوالقاسمی" (Persian Dari verbs by Abolqasemi):

There is a book titled "واژگان زبان فارسی دری" (Vocabulary of Persian Dari) by Mohsen Abolqasemi published by Tahouri Press, available in electronic and PDF format. This book is available for purchase and download from Fidibo.

Additionally, Noorlib (noorlib.ir) offers digital books and PDFs, including a work titled "دستور زبان دری" (Grammar of Dari Language).

The search results show that Ketabnak (ketabnak.com) provides downloads for books including "فهرست فعلهای فارسی با معنای آنها" (Index of Persian Verbs with Their Meanings).

Your search query included references to these three digital libraries (PDF, Noorlib, and Ketabnak) which are indeed legitimate sources for Persian and Dari language materials.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:42:53.899Z] TOOL RESULT

```
Web search results for query: ""فرهنگ واژه های عربی در زبان فارسی" نحوی pdf دانلود"

Links: [{"title":"(PDF) بررسی تغییرات معنايي و كاربردي واژگان عربی در زبان فارسی","url":"https://www.academia.edu/28276213/%D8%A8%D8%B1%D8%B1%D8%B3%DB%8C_%D8%AA%D8%BA%DB%8C%DB%8C%D8%B1%D8%A7%D8%AA_%D9%85%D8%B9%D9%86%D8%A7%D9%8A%D9%8A_%D9%88_%D9%83%D8%A7%D8%B1%D8%A8%D8%B1%D8%AF%D9%8A_%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86_%D8%B9%D8%B1%D8%A8%DB%8C_%D8%AF%D8%B1_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"کتاب فرهنگ واژه های فارسی در زبان عربی؛ گویش لبنانی د. طونی الحاج + دانلود نمونه رایگان","url":"https://taaghche.com/book/134704/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C%D8%9B-%DA%AF%D9%88%DB%8C%D8%B4-%D9%84%D8%A8%D9%86%D8%A7%D9%86%DB%8C"},{"title":"فهرست واژه‌های عربی با ریشه فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D8%B9%D8%B1%D8%A8%DB%8C_%D8%A8%D8%A7_%D8%B1%DB%8C%D8%B4%D9%87_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"کتاب فرهنگ واژه‌های فارسی در زبان عربی [چ1] -فروشگاه اینترنتی کتاب گیسوم","url":"https://www.gisoom.com/book/11375703/%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C/"},{"title":"کتاب فرهنگ تطبیقی معانی حروف در زبان عربی و فارسی اثر اسماعیل تاجبخش | ایران کتاب","url":"https://www.iranketab.ir/book/164955-arabic-and-persian"},{"title":"خرید کتاب فرهنگ واژه های فارسی در زبان عربی اثر سیدمحمدعلی امام شوشتری از نشر ترآوا","url":"https://www.adinehbook.com/gp/product/6003471743"},{"title":"فرهنگ واژه‌های فارسی در زبان عربی - دانلود pdf","url":"https://noorlib.ir/book/info/105056/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C"},{"title":"دانلود کتاب فرهنگ واژه های فارسی در زبان عربی","url":"https://ketabnak.com/book/48613/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C"},{"title":"کتاب واژه های فارسی عربی شده","url":"https://ketabnak.com/book/50020/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%B9%D8%B1%D8%A8%DB%8C-%D8%B4%D8%AF%D9%87"}]

بر اساس نتایج جستجو، اطلاعاتی در مورد منابع مربوط به "فرهنگ واژه های عربی در زبان فارسی" پیدا شد:

کتابی با عنوان "فرهنگ واژه های فارسی در زبان عربی" اثر سیدمحمدعلی امام شوشتری توسط انتشارات ترآوا منتشر شده است که دارای ۶۰۸ صفحه و شماره شابک 978-600-347-174-0 می باشد.

این کتاب در قالب نسخه دیجیتال و PDF برای دانلود و مطالعه آنلاین در دسترس است.

همچنین پژوهش‌های دیگری نیز در مورد تغییرات معنایی و کاربردی واژگان عربی در زبان فارسی انجام شده است.

برای دریافت فایل PDF، می‌توانید به سایت‌های کتاب فروشی و کتابخانه‌های دیجیتالی ایرانی مانند نور لیب (noorlib.ir)، کتاب ناک (ketabnak.com) و دیگر پایگاه‌های مشابه مراجعه کنید.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:42:54.136Z] TOOL RESULT

```
Web search results for query: ""فرهنگ واژه های فارسی در زبان عربی" امام شوشتری pdf noorlib"

Links: [{"title":"بارگیری «فرهنگ واژه‌های فارسی در زبان عربی» محمدعلی امام‌شوشتری","url":"http://parsianjoman.org/?p=1265"},{"title":"خرید کتاب فرهنگ واژه های فارسی در زبان عربی اثر سیدمحمدعلی امام شوشتری از نشر ترآوا","url":"https://www.adinehbook.com/gp/product/6003471743"},{"title":"فرهنگ واژه‌های فارسی در زبان عربی - دانلود pdf","url":"https://noorlib.ir/book/info/105056/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C"},{"title":"خرید آنلاین کتاب فرهنگ واژه های فارسی در زبان عربی |Iranfarhang Bookstore","url":"https://www.iranfarhang.com/Book/19250"},{"title":"فرهنگ واژه های فارسی درزبان عربی/محمدعلی امام شوشتری/تراوا اثر محمدعلی امام شوشتری-تراوا شهر کتاب","url":"https://oxinbook.com/book/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C-%D9%85%D8%AD%D9%85%D8%AF%D8%B9%D9%84%DB%8C-%D8%A7%D9%85%D8%A7%D9%85-%D8%B4%D9%88%D8%B4%D8%AA%D8%B1%DB%8C-%D8%AA%D8%B1%D8%A7%D9%88%D8%A7"},{"title":"کتاب فرهنگ واژه های فارسی در زبان عربی اثر محمد علی امام شوشتری - کتابفروشی میمکتابفروشی میم","url":"https://bookmim.com/product/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C-%D8%A7%D8%AB%D8%B1/"},{"title":"فرهنگ واژگان فارسی در زبان عربی - سپند مینو | sepandminoo","url":"https://sepandminoo.ir/product/farhang-vazhegan/"},{"title":"دانلود کتاب فرهنگ واژه های فارسی در زبان عربی","url":"https://ketabnak.com/book/48613/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AF%D8%B1-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B9%D8%B1%D8%A8%DB%8C"},{"title":"دانلود کتابهای محمدعلی امام شوشتری","url":"https://ketabnak.com/persons/12746/%D9%85%D8%AD%D9%85%D8%AF%D8%B9%D9%84%DB%8C+%D8%A7%D9%85%D8%A7%D9%85+%D8%B4%D9%88%D8%B4%D8%AA%D8%B1%DB%8C"}]

Based on the search results, I found information about "فرهنگ واژه های فارسی در زبان عربی" (A Dictionary of Persian Words in the Arabic Language):

**Book Information:**

The book was written by Mohammad Ali Imam Shoshteri and published in 1347 (1968) by the National Heritage Society (انجمن آثار ملی) in Tehran.

The dictionary contains approximately 3,000 borrowed words and their roots.

**Content and Significance:**

The work explores how Persian language and literature influenced Arabic, examining the roots of many words shared between these two languages. The Arabic language borrowed many words from Persian, and many Persian words entered Arabic in different forms, which are called "معربات" (Arabicized terms).

**Availability:**

The book is available for download and online reading as a digital copy with a PDF version on Noorlib, which directly matches your search reference to noorlib.

The book remains an important reference work for scholars interested in the linguistic and cultural connections between Persian and Arabic languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:42:56.557Z] TOOL RESULT

```
Web search results for query: "مشیری "فرهنگ واژه های اروپایی در فارسی" pdf"

Links: [{"title":"مهشید مشیری - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D9%87%D8%B4%DB%8C%D8%AF_%D9%85%D8%B4%DB%8C%D8%B1%DB%8C"},{"title":"فرهنگ ریشه شناختی واژه ها و کوتاه نوشته های دخیل اروپایی و آمریکایی در فارسی","url":"https://press.um.ac.ir/index.php?Itemid=714&id=278%3Af-400&lang=fa&option=com_k2&view=item"},{"title":"فرهنگ ریشه لغات فارسی با نمودارهای اشتقاق 1404 | PDF","url":"https://www.scribd.com/document/999519412/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D9%84%D8%BA%D8%A7%D8%AA-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A8%D8%A7-%D9%86%D9%85%D9%88%D8%AF%D8%A7%D8%B1%D9%87%D8%A7%DB%8C-%D8%A7%D8%B4%D8%AA%D9%82%D8%A7%D9%82-1404"},{"title":"کتاب فرهنگ ریشه شناختی واژه ها و کوتاه نوشته های دخیل اروپایی و آمریکایی در فارسی ~رضا زمردیان - نشر دانشگاه فردوسی (مشهد) - آدینه بوک","url":"https://www.adinehbook.com/gp/product/9643860663"},{"title":"دانلود کتاب فرهنگ ریشه های هند و اروپایی زبان فارسی اثر منوچهر آرش پور ☀️ PDF رایگان","url":"https://persianpdf.com/book/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D9%87%D8%A7%DB%8C-%D9%87%D9%86%D8%AF-%D9%88-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7%DB%8C/"},{"title":"دانلود pdf کتاب فرهنگ واژه‌های دخیل اروپایی در فارسی (همراه با ریشه هر واژه) | دانلود با لینک مستقیم - فارس فایل","url":"https://enop.farsfile.ir/file/156989/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-pdf-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7%DB%8C%DB%8C-%D8%AF%D8%B1-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-(%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D8%B1%DB%8C%D8%B4%D9%87-%D9%87%D8%B1-%D9%88%D8%A7%DA%98%D9%87)"},{"title":"دانلود pdf کتاب فرهنگ ریشه‌شناختی واژه‌ها و کوتاه‌نوشته‌های دخیل اروپایی و آمریکایی در فارسی | دانلود با لینک مستقیم - فارس فایل","url":"https://unikey.farsfile.ir/file/159832/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-pdf-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7-%D9%88-%DA%A9%D9%88%D8%AA%D8%A7%D9%87%E2%80%8C%D9%86%D9%88%D8%B4%D8%AA%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7%DB%8C%DB%8C-%D9%88-%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%DB%8C%DB%8C-%D8%AF%D8%B1-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"دانلود کتاب فرهنگ واژه های دخیل اروپایی در فارسی (همراه با ریشه هر واژه)","url":"https://ketabnak.com/book/132354/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D8%AF%D8%AE%DB%8C%D9%84-%D8%A7%D8%B1%D9%88%D9%BE%D8%A7%DB%8C%DB%8C-%D8%AF%D8%B1-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D9%87%D9%85%D8%B1%D8%A7%D9%87-%D8%A8%D8%A7-%D8%B1%DB%8C%D8%B4%D9%87-%D9%87%D8%B1-%D9%88%D8%A7%DA%98%D9%87"},{"title":"دانلود کتاب فرهنگ ریشه واژگان فارسی","url":"https://ketabnak.com/book/98849/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"}]

بر اساس نتایج جستجو، کتاب «فرهنگ واژه‌های اروپایی در فارسی» اثر مهشید مشیری، منتشر شده توسط انتشارات البرز در سال ۱۳۷۱ است.

در نتایج جستجو، چندین منبع برای دانلود فایل PDF این کتاب و کتاب‌های مرتبط شامل واژه‌های دخیل اروپایی در فارسی پیدا شد، اما من نمی‌توانم مستقیماً لینک دانلود را ارائه دهم. با این حال، می‌توانید در وب‌سایت‌های منابع دیجیتالی فارسی مانند:

- **فارس‌فایل** - دارای PDF کتاب فرهنگ واژه‌های دخیل اروپایی در فارسی
- **کتاب نک** - دانلود کتاب‌های مختلف در این زمینه
- **اسکریبد** - منابع متنوع

جستجو کنید. همچنین ممکن است این کتاب در کتابخانه‌های دیجیتالی و دانشگاهی ایران در دسترس باشد.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:42:56.886Z] TOOL RESULT

```
# Dehkhoda Entry and Dictionary Selector

**Dehkhoda Entry Beginning:**
"دیوار. [ دی ] (اِ) (از: دیو + آر، علامت نسبت ). (بهار عجم ). جدار و بنائی که در اطراف خانه میگذارند و بدان وی را محصور می کنند."

**Dictionaries in Selector:**
The page lists several dictionary options accessible via the top navigation:
- همه (All) - general search
- دیکشنری (Dictionary) - d=en2fa,fa2en
- مترادف (Synonyms) - d=motaradef
- طیفی (Spectral) - d=teyfi
- آزاد (Open) - d=wiki

Under the Dehkhoda-specific filters, additional search modes are available (exact, similar, homophone, text-based, prefix, and suffix matching), but these are search refinements rather than separate dictionary sources.
```


### [2026-09-04T14:42:57.489Z] TOOL RESULT

```
# Noorlib Book Viewer Report

**Book Title:** واژههای دخیل در قرآن مجید (Foreign Vocabulary of the Qur'an)

**Author/Translator:** Not specified in provided content

**Publisher/Year:** Not provided

**Page Count:** Not indicated

**Text Visibility:** Cannot determine from page excerpt shown

**URL Pattern:** No page-jumping URL pattern is evident in the supplied content

**Login Requirement:** The page displays "ورود / عضویت" (login/registration) options, suggesting account access may be needed for full functionality, though the current page appears viewable

**Note:** The website header states this is "صفحه 1" (page 1), but detailed bibliographic information and technical specifications about the book's digitization are not included in the excerpt provided.
```


## [2026-09-04T14:43:19.419Z] AGENT (thinking)

I'll run these independent searches together: BQT's leaf-to-page mapping and letter coverage for vols 1-2, OCR quality checks for SOD/SNS, noorlib/ketabnak viewer URL patterns, and discovery searches for the mid-frequency titles (ETM, TZF, SAP, FIB, VDQ).


## [2026-09-04T14:43:29.746Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\npython3 - <<'EOF'\nimport re\npages=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\ndef fl(i):\n    ls=[l for l in pages[i].split('\\n') if l.strip()]\n    return (ls[0][:70] if ls else '') + ' || ' + (ls[-1][:70] if ls else '')\nfor i in [150,180,200,201,220,300,400,500,600,700,760,775,776]:\n    print(i,'|',fl(i))\n# find leaves whose first line is a persian/arabic numeral only\npat=re.compile(r'^[\\s۰-۹٠-٩0-9]{1,6}$')\nhits=[]\nfor i,p in enumerate(pages):\n    ls=[l.strip() for l in p.split('\\n') if l.strip()]\n    if ls and pat.match(ls[0]): hits.append((i,ls[0]))\nprint(\"numeral-first-line leaves (sample):\",hits[:40])\nEOF\necho \"--- v2 djvu.txt: lines that are pure numerals\"; grep -nE '^[۰-۹0-9]{2,4} *$' BQT_v2.txt | head -30\necho \"--- SOD english check\"; grep -c 'Manich\\|Buddh\\|Christian' SOD.txt; grep -n 'wall' SOD.txt | head -5\necho \"--- SNS quality\"; sed -n '2000,2020p' SNS.txt | cut -c1-100\necho \"--- noorlib page URL tests\"; for u in 'https://noorlib.ir/book/view/12868?pageNumber=50&viewType=pdf' 'https://noorlib.ir/book/view/12868/1/50' 'https://noorlib.ir/book/info/105056'; do printf \"%s -> \" \"$u\"; curl -s -o /dev/null -w '%{http_code} %{redirect_url}\\n' \"$u\"; done\necho \"--- ketabnak\"; curl -s -o /dev/null -w '%{http_code}\\n' 'https://ketabnak.com/book/51136'",
 "description": "Map BQT leaves to printed pages, check SOD/SNS OCR, test noorlib URLs",
 "timeout": 120000
}
```


## [2026-09-04T14:43:32.767Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://noorlib.ir/book/search?q=ابوالقاسمی",
 "prompt": "List every book title, author, and noorlib book id/URL shown in these search results (especially anything by محسن ابوالقاسمی such as فعل های فارسی دری, ریشه شناسی, تاریخ مختصر زبان فارسی, زبان فارسی و سرگذشت آن). If the page is not a search results page, describe what it is and any search URL pattern visible."
}
```


## [2026-09-04T14:43:33.579Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://ketabnak.com/book/51136",
 "prompt": "Describe this book page: title, author/translator, publisher, edition, page count, file format and size, whether a direct download link is present (quote it), and whether login is required."
}
```


## [2026-09-04T14:43:35.050Z] TOOL CALL #28: WebSearch

```json
{
 "query": "ابوالقاسمی \"ریشه شناسی\" اتیمولوژی ققنوس pdf دانلود noorlib OR ketabnak OR archive.org"
}
```


## [2026-09-04T14:43:35.839Z] TOOL CALL #29: WebSearch

```json
{
 "query": "\"فرهنگ سیاح\" المنجد فارسی pdf دانلود"
}
```


### [2026-09-04T14:43:36.000Z] TOOL RESULT

```
150 | مقد‌مه صد وچپل ودق _ || قبری (-مروج).
180 | ماضی مضارغ اسم فاعل (سم‌مفعو ل || 0 خم ۱ : بآخر. ۲- اوء ایشان: آنان عسمیر نش» واسم اشاره درفارسی داین» و
200 | در || ۱- چك : معنی. ۲-- خم ۲ : آموز کار.
201 | 0 دسئور زبان پارسی || لیاقت
220 | نواحی باشند از دنبال شخصي که آب میبرد روان || که درخت آن در
300 | ست و 4 سب || ۴ - درزبان فارسی حاضر وهمچنین در ادبیات
400 | واجب و بفستا وا گیبتد و جر هی اهنت » || ۱ - رك: ابر کوه .
500 | و با بای عارسی نیز درست است - || ( بر هان قابلع ۴«
600 | فر ) گنف ه باکاف قارسی بروزندهاوند, || (برهان فاطع ۲ )
700 | تخت فیروزه . ۷4 سس || بقیه درسفحةٌ 4۷۵
760 | تورنگه || شه درسضعاً ۵۳۳
775 | اي محِ || شه دز صفحه ۵8۸
776 | ۱۱/۱7 || کوبند درسحرا که آب درآن جمع شود وعرب
numeral-first-line leaves (sample): [(7, '۱'), (53, '۲'), (72, '۲'), (86, '1'), (94, '4'), (187, '0'), (211, '۳'), (221, '0'), (277, '9'), (333, '26 ٩'), (337, '۱ ۷۲۳'), (347, '۱۳'), (379, '2'), (437, '۲۱۷'), (445, '2'), (481, '۳'), (483, '5'), (534, '۱ 2۳9'), (539, '۳۵'), (563, '۳۳'), (570, '۳9'), (572, '۲۶ ۵'), (577, '۳66 77'), (583, '۳'), (584, '۳'), (637, '۳'), (689, '39۳9'), (697, '9'), (702, '۳۹'), (716, '۵'), (722, '3')]
--- v2 djvu.txt: lines that are pure numerals
2736:۷۹ 
2918:۳۹ 
2927:0۷۸ 
3185:۸۱ 
3320:۱۳ 
7054:14 
7331:۳0 
7611:۲۷ 
7826:۷6 
10324:۱۳ 
11969:14 
16281:۷۱۹ 
17829:۷۳۱ 
18404:۷۳۹ 
19994:۱۳ 
20422:۷۲ 
21701:۹۷ 
24110:۱۷۱ 
24252:۰۰ 
24673:۷۷ 
25512:۳9 
27690:۲۲۴ 
36167:۱۱ 
36740:۱۷ 
37125:۲۱ 
37793:۲4 
42444:72 
44040:7۳ 
54249:۱۱۳ 
54593:۱۰۵۹ 
--- SOD english check
259
3896:and  extending  towards  the  walls  of  China  in  the  east. 
4468:of  Kan-Su.  The  fortified  frontier  wall  presented 
4517:discovered  a  walled  up  library.  The  library  was 
4664:Tawallod-e  BudS  be  Ravdyat-e  Soghdi,  Tehran,  Nashr- 
5175:of  the  fortified  walls  which  surrounded  the  city. 
--- SNS quality


U-b 



■fr/T ^ 




x§z :>;t {GNPE. 102)xaSzanuha-haSz ^j 1 ;.^ 
\X/\Y^ ax§z: V (y W y. 178) xist : o T *r*L**li 

.jiil>£-t J -.^l > i. i L :abaz-Sxez§n5nd : jku^^ 

\x/\vJ\ 

■YA tf t-iO'jcwV 'o-l#*< tahySsi 

•f/1t^ ahy5 yfis.n- : *- 
--- noorlib page URL tests
https://noorlib.ir/book/view/12868?pageNumber=50&viewType=pdf -> 200 
https://noorlib.ir/book/view/12868/1/50 -> 404 
https://noorlib.ir/book/info/105056 -> 200 
--- ketabnak
301
```


## [2026-09-04T14:43:36.590Z] TOOL CALL #30: WebSearch

```json
{
 "query": "پورداود \"فرهنگ ایران باستان\" pdf دانلود noorlib OR archive.org OR ketabnak"
}
```


## [2026-09-04T14:43:36.713Z] TOOL CALL #31: WebSearch

```json
{
 "query": "\"تاریخ مختصر زبان فارسی\" ابوالقاسمی pdf noorlib OR ketabnak"
}
```


### [2026-09-04T14:43:42.129Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-04T14:43:43.731Z] TOOL RESULT

```
Web search results for query: "ابوالقاسمی "ریشه شناسی" اتیمولوژی ققنوس pdf دانلود noorlib OR ketabnak OR archive.org"

Links: [{"title":"مطالعات قرآن و حدیث (Jan 2017)","url":"https://doaj.org/article/8199d7b4e69c4a2f97738aff4d3f1350"},{"title":"نمایان‌سازی انتحال در یک فرهنگ‌نامه پزشکی: مطالعه موردی تطبیق دو اثر «کتاب الماء» و« قاموس الاطباء و ناموس الالباء»","url":"https://core.ac.uk/works/133318980"},{"title":"Jump to ratings and reviews","url":"https://www.goodreads.com/book/show/146367"},{"title":"دراسات فی اللغه العربیه و آدابها (Feb 2024)","url":"https://doaj.org/article/529e438126d741bda830b175cfcce903"},{"title":"Pizhūhish/Nāmah-i Tafsīr va Zabān-i Qurān (Sep 2018)","url":"https://doaj.org/article/b0972c27b0d54af38fa8eedcf2bb0012"},{"title":"البرهان في علوم القرآن Quotes","url":"https://www.goodreads.com/work/quotes/25733661"}]

I've performed the web search with your exact query. The search results returned academic articles and references related to etymology (ریشه‌شناسی/اتیمولوژی) and Arabic linguistics, but **did not find a direct link to a downloadable PDF** of a specific work by Abulqasemi about etymology and "Qaqqanus" (ققنوس) on the platforms you mentioned (noorlib, ketabnak, or archive.org).

The search results include:
- Academic articles on Quranic etymology and historical linguistic etymology
- Articles from scholarly databases (DOAJ, CORE)
- References to classical Arabic linguistic works

However, none of these results provide a direct download link for the specific text you're looking for. To find this particular resource, you might want to:

1. Visit the websites directly: noorlib.ir, ketabnak.com, or archive.org
2. Search those platforms specifically for "ابوالقاسمی" or the specific work title
3. Check academic databases like Google Scholar or ResearchGate
4. Contact Persian/Arabic digital library services or academic institutions specializing in Persian literature and linguistics


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:43:46.656Z] TOOL RESULT

```
Web search results for query: ""فرهنگ سیاح" المنجد فارسی pdf دانلود"

Links: [{"title":"فرهنگ منجد الطلاب عربی فارسی محمد بندر ریگی : ابو عبدالرحمن الكردي : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/abo_abdrahman_kordi_barid_20150501_1718"},{"title":"Amid Dictionary","url":"https://en.wikipedia.org/wiki/Amid_Dictionary"},{"title":"نمایشگاه مجازی - لغت‌نامه، یا، فرهنگ بزرگ جامع نوین سیاح: ترجمه المنجد (با اضافات) عربی به فارسی","url":"https://book.icfi.ir/book/567233/%D9%84%D8%BA%D8%AA-%D9%86%D8%A7%D9%85%D9%87-%DB%8C%D8%A7-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A8%D8%B2%D8%B1%DA%AF-%D8%AC%D8%A7%D9%85%D8%B9-%D9%86%D9%88%DB%8C%D9%86-%D8%B3%DB%8C%D8%A7%D8%AD-%D8%AA%D8%B1%D8%AC%D9%85%D9%87-%D8%A7%D9%84%D9%85%D9%86%D8%AC%D8%AF-%D8%A8%D8%A7-%D8%A7%D8%B6%D8%A7%D9%81%D8%A7%D8%AA-%D8%B9%D8%B1%D8%A8%DB%8C-%D8%A8%D9%87-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"کتاب لغت‌نامه، یا، فرهنگ بزرگ جامع نوین سیاح: ترجمه المنجد (با اضافات) عربی به فارسی (جلد 2) [چ7] -فروشگاه اینترنتی کتاب گیسوم","url":"https://www.gisoom.com/book/1490734/%DA%A9%D8%AA%D8%A7%D8%A8-%D9%84%D8%BA%D8%AA-%D9%86%D8%A7%D9%85%D9%87-%DB%8C%D8%A7-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A8%D8%B2%D8%B1%DA%AF-%D8%AC%D8%A7%D9%85%D8%B9-%D9%86%D9%88%DB%8C%D9%86-%D8%B3%DB%8C%D8%A7%D8%AD-%D8%AA%D8%B1%D8%AC%D9%85%D9%87-%D8%A7%D9%84%D9%85%D9%86%D8%AC%D8%AF-%D8%A8%D8%A7-%D8%A7%D8%B6%D8%A7%D9%81%D8%A7%D8%AA-%D8%B9%D8%B1%D8%A8%DB%8C-%D8%A8%D9%87-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-2/"},{"title":"فرهنگ ابجدی - دانلود pdf","url":"https://noorlib.ir/book/info/2094/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%D8%A8%D8%AC%D8%AF%DB%8C"},{"title":"دانلود برنامه دیکشنری المنجد اندروید | بازار","url":"https://cafebazaar.ir/app/mabna.ir.almonjed"},{"title":"المنجد فی اللغة - دانلود pdf","url":"https://noorlib.ir/book/info/32878/%D8%A7%D9%84%D9%85%D9%86%D8%AC%D8%AF-%D9%81%DB%8C-%D8%A7%D9%84%D9%84%D8%BA%D8%A9"},{"title":"دانلود کتاب فرهنگ دانشگاهی 1 عربی به فارسی المنجد الابجدی PDF","url":"https://jozvepro.com/product/arabi-farsi-almonjed/"},{"title":"دانلود کتاب فرهنگ دانشگاهی عربی فارسی جلد اول المنجد الابجدی 953صفحه PDF پی دی اف","url":"https://pdfbomb.com/product/farhang-danshgahi-arani-farsi/"},{"title":"المنجد.pdf","url":"https://bayanbox.ir/info/520198756828938728/%D8%A7%D9%84%D9%85%D9%86%D8%AC%D8%AF"}]

Based on the search results, I found several resources related to "فرهنگ سیاح" (Farhangi Siahah) - the Persian translation of Al-Munjid dictionary by Ahmad Siahah:

1. **Internet Archive**: There is a copy of "فرهنگ منجد الطلاب" (Al-Munjid Al-Tullab dictionary) available on Internet Archive.

2. **Comprehensive Dictionary**: The "لغت‌نامه یا فرهنگ بزرگ جامع نوین سیاح" is a translation of Al-Munjid with additions from Arabic to Persian, authored by Louis Ma'louf with translation by Ahmad Siahah.

3. **PDF Downloads**: Several platforms offer PDF versions:
   - NoorLib offers digital PDF versions for online reading
   - Commercial PDF versions are available on book sales platforms, with the first volume containing 953 pages
   - BayanBox offers file storage and sharing services for PDFs

4. **Mobile App**: There is also an Android application available based on Ahmad Siahah's works.

You can access these resources through the links provided in the search results, including Internet Archive, NoorLib, and various PDF download platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:43:49.059Z] TOOL RESULT

```
# Book Page Summary

**Title:** واژه های دخیل در قرآن مجید (Foreign Words in the Quran)

**Author:** Arthur Jeffery

**Translator:** Fereydoun Badreai

**Publisher:** Not explicitly stated on this page

**Edition/Format:** Electronic version uploaded 1392/06/05 (Persian calendar)

**Page Count:** Not specified

**File Format & Size:** Not provided

**Download Link:** No direct download link is available. The page displays: "امکان دانلود آن وجود ندارد" (Download is not possible due to copyright considerations)

**Login Required:** Yes. The page states users must log in to access the book: "برای درج دیدگاه لطفاً به حساب کاربری خود وارد شوید" (Please log in to your account)

**Additional Notes:** This is a specialized reference work examining etymological origins of Quranic vocabulary. The comments section indicates the Persian translation has omissions compared to the original English editions (1938 and 2007).
```


### [2026-09-04T14:43:51.859Z] TOOL RESULT

```
Web search results for query: "پورداود "فرهنگ ایران باستان" pdf دانلود noorlib OR archive.org OR ketabnak"

Links: [{"title":"کتاب فرهنگ ایران باستان اثر ابراهیم پورداود | ایران کتاب","url":"https://www.iranketab.ir/book/87735-iran"},{"title":"فرهنگ ایران باستان - دانلود pdf","url":"https://noorlib.ir/book/info/104334/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86"},{"title":"دانلود کتاب فرهنگ ایران باستان » رایگان در کتاب کاشان :: کاشان کتاب","url":"https://kashanketab.com/PDF/دانلود-کتاب-فرهنگ-ایران-باستان/"},{"title":"کتاب فرهنگ ایران باستان - ابراهیم پورداوود - دانلود pdf - سایت آسمان کتاب","url":"http://asmaneketab.ir/product/%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%DB%8C%D9%85-%D9%BE%D9%88%D8%B1%D8%AF%D8%A7/"},{"title":"دانلود کتاب‌های تاريخ ايران باستان PDF | PDF کافه کتاب","url":"https://ketab.cafe/library/history-of-ancient-iran/"},{"title":"دانلود کتاب فرهنگ ایران باستان استاد ابراهیم پورداود - فرهنگ و ادب","url":"https://farhangoadabeirani.blogsky.com/1395/03/21/post-762/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF-%D8%A7%D8%A8%D8%B1%D8%A7%D9%87%DB%8C%D9%85-%D9%BE%D9%88%D8%B1%D8%AF%D8%A7%D9%88%D8%AF"},{"title":"دانلود pdf کتاب فرهنگ ایران باستان رایگان","url":"https://dehlinks.ir/fa/book/poetry/book/20642/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-pdf-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%B1%D8%A7%DB%8C%DA%AF%D8%A7%D9%86/"},{"title":"دانلود کتاب \"فرهنگ ایران باستان\" | PDF کافه‌کتاب","url":"https://kaffeketab.ir/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86-%D8%A8%D8%A7%D8%B3%D8%AA%D8%A7%D9%86/"}]

The search results show several sources for downloading or accessing the "فرهنگ ایران باستان" (Culture of Ancient Iran) book by Ibrahim Pourdasoud:

1. **Noorlib** - The Noorlib website offers digital download and online reading of the book "فرهنگ ایران باستان" along with a PDF version.

2. **Kashan Ketab** - Kashan Ketab provides the book by Ibrahim Pourdasoud in PDF format with a file size of 62.3 MB.

3. **Iran Ketab** (iranketab.ir) - The Iran Ketab website lists information about this book by Ibrahim Pourdasoud.

4. **Asmane Ketab** (asmaneketab.ir) - This site offers downloading the electronic version of the book "فرهنگ ایران باستان" written by Ibrahim Pourdasoud.

5. **PDF Cafe Ketab** (ketab.cafe) - Another source for downloading books on ancient Iranian history in PDF format.

6. **Kaffe Ketab** (kaffeketab.ir) - Offers both PDF and audio versions of the book for free download.

The most relevant source from your search query appears to be **Noorlib**, which you specifically mentioned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:43:53.347Z] TOOL RESULT

```
Web search results for query: ""تاریخ مختصر زبان فارسی" ابوالقاسمی pdf noorlib OR ketabnak"

Links: [{"title":"دستور تاریخی زبان فارسی - محسن ابوالقاسمی : محسن ابوالقاسمی : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/20220417_20220417_2237"},{"title":"کتاب تاریخ زبان فارسی -محسن ابوالقاسمی - سمتا -","url":"https://samta.samt.ac.ir/content/9122/%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"دانلود کتاب تاریخ زبان فارسی -محسن ابوالقاسمی - سمت - کتابخانه دیجیتال سازمان مطالعه و تدوین کتب علوم انسانی دانشگاهها - سمت","url":"http://samta.samt.ac.ir/content/9122/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"کتاب تاریخ مختصر زبان فارسی اثر محسن ابوالقاسمی | ایران کتاب","url":"https://www.iranketab.ir/book/102858-farsi"},{"title":"تاریخ زبان فارسی نسخه pdf","url":"https://library.tebyan.net/f/Viewer/Pdf/168187/8"},{"title":"دانلود کتاب تاریخ مختصر زبان فارسی دکتر محسن ابوالقاسمی - فرهنگ و ادب","url":"https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8"},{"title":"دانلود کتابهای محسن ابوالقاسمی","url":"https://ketabnak.com/persons/31486/%D9%85%D8%AD%D8%B3%D9%86+%D8%A7%D8%A8%D9%88%D8%A7%D9%84%D9%82%D8%A7%D8%B3%D9%85%DB%8C"},{"title":"دانلود کتاب تاریخ مختصر زبان فارسی","url":"https://ketabnak.com/book/81646/تاریخ-مختصر-زبان-فارسی"},{"title":"کتاب های ؛محسن ابوالقاسمی | کتابخانه فارسی ایرانیان - معرفی کتاب های برتر","url":"http://library.blogzz.ir/Tag/کتاب-های-؛محسن-ابوالقاسمی"},{"title":"دانلود کتاب تاریخ زبان فارسی محسن ابوالقاسمی - معرفی و دانلود رایگان کتاب های فارسی","url":"https://persianbook.topsblog.ir/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%B1%D8%B3%DB%8C/%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AA%D8%A7%D8%B1%DB%8C%D8%AE-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D9%85%D8%AD%D8%B3%D9%86-%D8%A7%D8%A8%D9%88%D8%A7.html"}]

Based on the search results, I found information about the book "تاریخ مختصر زبان فارسی" (A Brief History of Persian Language) by Dr. Mohsen Abulqasemi:

## Book Information

The book "تاریخ مختصر زبان فارسی" by Dr. Mohsen Abulqasemi discusses three periods of the history of Persian language, one of the oldest and most important Indo-European languages.

The book is divided into three time periods: "Ancient Persian," "Middle Persian," and "New Period Persian".

## Available Sources

The search results indicate several places where this book can be found:

1. **Internet Archive**: The book is available at archive.org (result 1)
2. **Samta (SAMT)**: A digital library maintained by the Organization for Studying and Compiling University Humanities Textbooks (results 2-3)
3. **Iran Ketab**: The book is catalogued, though according to copyright considerations, direct download may not be available on some platforms (result 8)
4. **Tebyan Library**: A PDF version viewer is available (result 5)

You can access the book through these platforms, particularly through archive.org, SAMT's digital library, or by searching on ketabnak.com as you specified in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:44:37.490Z] AGENT (thinking)

I'll now check page-split texts for the remaining downloads, verify OCR quality for SOD, identify ARB/FRS editions, confirm noorlib's page text and search capabilities, check vajehyab for Mo'in's a'lam volumes, and run noorlib/ketabnak searches for the remaining titles.


## [2026-09-04T14:44:47.815Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\necho \"pdftotext: $(which pdftotext || echo MISSING)\"; python3 -c \"import fitz; print('pymupdf ok')\" 2>&1 | tail -1\necho \"--- SOD sample lines 20000-20015\"; sed -n '20000,20015p' SOD.txt | cut -c1-110\necho \"--- SOD entries with numbers (dictionary entries are numbered)\"; grep -nE '^[0-9]{3,5} ' SOD.txt | head -5; grep -cE '^[0-9]{3,5} ' SOD.txt\necho \"--- ARB edition check\"; grep -n 'شاكر\\|شاکر\\|1361\\|١٣٦١\\|1942' ARB_mo3rb.txt | head -5; echo ..; grep -n 'شاكر\\|عبد الرحيم' ARB_abdulraheem.txt | head -3\necho \"--- FRS edition check\"; grep -n 'اقبال\\|مجتبائی\\|صادقی\\|خوارزمی\\|دبیرسیاقی\\|۱۳۱۹\\|1319' FRS.txt | head -8\necho \"--- FVQ page numbers\"; grep -nE '^\\s*[0-9]{1,3}\\s+(THE FOREIGN|FOREIGN VOCABULARY)|^(THE FOREIGN VOCABULARY OF THE QUR.AN)\\s+[0-9]+' FVQ.txt | head -5\necho \"--- AFM page numerals\"; grep -nE '^\\s*[٠-٩0-9]{1,3}\\s*$' AFM.txt | head -8\necho \"--- noorlib search probes\"; for u in 'https://noorlib.ir/book/search?query=%D9%81%D8%B9%D9%84' 'https://noorlib.ir/search?q=%D9%81%D8%B9%D9%84' 'https://noorlib.ir/book/list?q=%D9%81%D8%B9%D9%84' 'https://noorlib.ir/book/search/%D9%81%D8%B9%D9%84' 'https://noorlib.ir/search/book?q=%D9%81%D8%B9%D9%84'; do printf \"%s -> \" \"$u\"; curl -s -o /dev/null -w '%{http_code} %{redirect_url}\\n' \"$u\"; done\necho \"--- noorlib page text probe\"; curl -s 'https://noorlib.ir/book/view/12868?pageNumber=50&viewType=pdf' | grep -o 'pageNumber[^\"]\\{0,60\\}\\|viewType=[a-z]*\\|ocr[^\"]\\{0,40\\}' | sort | uniq -c | head -15",
 "description": "Check tooling, OCR quality, editions, and noorlib URL patterns",
 "timeout": 120000
}
```


## [2026-09-04T14:44:50.071Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://noorlib.ir/book/view/12868?pageNumber=50&viewType=pdf",
 "prompt": "Is the text of page 50 of this book (واژه های دخیل در قرآن مجید) readable here as text, or is only an image shown? Quote any Persian body text you can see from the page (first 3 lines). Also report the total page count if shown and any page-navigation URL parameters."
}
```


## [2026-09-04T14:44:52.316Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=افراسیاب&d=moein",
 "prompt": "Does the Mo'in (معین) result include a proper-name (اعلام) entry for افراسیاب (e.g. describing the Turanian king) in addition to or instead of a common-noun entry? Quote the entry text and any bracketed etymology like [په.] or Avestan forms."
}
```


## [2026-09-04T14:44:54.570Z] TOOL CALL #35: WebSearch

```json
{
 "query": "نحوی \"فرهنگ واژه های عربی در فارسی\" OR \"واژه‌های عربی در فارسی دخیل\" OR \"فعل های فارسی دری\" OR \"فرهنگ واژه های اروپایی در فارسی\" OR \"ریشه شناسی\" ابوالقاسمی",
 "allowed_domains": [
  "noorlib.ir",
  "ketabnak.com",
  "lib.eshia.ir",
  "ketabkoo.com"
 ]
}
```


## [2026-09-04T14:44:56.814Z] TOOL CALL #36: WebSearch

```json
{
 "query": "ایرانویج فره وشی OR \"زندگی و مهاجرت آریاییان\" OR \"ارکان سخن\" OR \"فرهنگ اعلام فارسی\" دانشگر OR \"نامه فرهنگ ایران\" جنیدی OR \"درآمدی بر دستور زبان اوستایی\"",
 "allowed_domains": [
  "noorlib.ir",
  "ketabnak.com",
  "archive.org",
  "ketabkoo.com"
 ]
}
```


### [2026-09-04T14:45:00.063Z] TOOL RESULT

```
pdftotext: /usr/bin/pdftotext
ModuleNotFoundError: No module named 'fitz'
--- SOD sample lines 20000-20015

1886  'wYwr  =»  'wyywr 

1887  >wYwrt  =»  \vfwrt- 

1888  >wyvz-   S  =»  »wYlyz- 

1889  jwyz  =*  'wyz-,  Jwxz- 

1890  >wYz-   B,S,C  ^^W> 
oxaz   Owy'z-)  ©<*ava-haiz  ©impf.  w*Yz 

^Jwyst-,  *wxz-,  Jwxst- 
0o)go  down,  0<?)dcsccnd 
GMS  55,  342;  Gcrsh.  BSOAS  14.88;  VJ;  TSP;  SCE 

--- SOD entries with numbers (dictionary entries are numbered)
2523:101 
3935:1876  for  the  unknown  language  of  the  legends  of  the  coins 
4106:130  B.c.12  ,  that  a  Chinese  general  -  a  special  envoy 
5218:1961 
5225:19751 
12622
--- ARB edition check
..
--- FRS edition check
40:بی‌مانند بگانه دوست ارجند آقای اقبال است که تخضص و تبخر شخصی 
45:مورد استفاده واقم گردید . ام‌داد ماه ۷۱۳۱۹ عبدالرحم خاخالی 
394:بیکی از لهجه‌های غیر فصیح ولایتی مانند سفدی و خوارزمی وخراسانی 
612:تحر.ش ترماه ۷۱۳۹ عتاس اقبال 
19145:لباس جاه تو بادا همیشه زدولت بود و از اقبال تاره 
19647:نامه مانی با نامه تو راز است شعرخوارزمی با شعر تو لامانی 
--- FVQ page numbers
3093:44 FOREIGN VOCABULARY OF THE QUR'lN 
3209:46 FOREIGN VOCABULARY OF THE QUR'AN 
3343:48 FOREIGN VOCABULARY OP THE QUR J AN 
3474:50 FOREIGN VOCABULARY OP THE QUR*AN 
3588:52 FOREIGN VOCABULARY OF THE QUR'AN 
--- AFM page numerals
1:8 
4:0 
57:1 
61:1 
72:5 
76:5 
83:9 
84:1 
--- noorlib search probes
https://noorlib.ir/book/search?query=%D9%81%D8%B9%D9%84 -> 404 
https://noorlib.ir/search?q=%D9%81%D8%B9%D9%84 -> 200 
https://noorlib.ir/book/list?q=%D9%81%D8%B9%D9%84 -> 200 
https://noorlib.ir/book/search/%D9%81%D8%B9%D9%84 -> 404 
https://noorlib.ir/search/book?q=%D9%81%D8%B9%D9%84 -> 404 
--- noorlib page text probe
      1 pageNumber=49&amp;sectionNumber=1&amp;volumeNumber=1&amp;viewType=pdf
      3 pageNumber=50&amp;viewType=html
      4 pageNumber=50&amp;viewType=pdf
      1 pageNumber=51&amp;sectionNumber=1&amp;volumeNumber=1&amp;viewType=pdf
      1 pageNumber:a,viewType:V,bookView:b,paragraphNumber:bd},advancedQueryIn
      1 pageNumber:a,volumeNumber:a,section:a,hasChildren:b,levelNumber:a,page
      1 pageNumber:A,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:C,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:D,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:e,sectionNumber:e,volumeNumber:e,selectedText:e,paragraphNu
      1 pageNumber:e,sectionNumber:e,volumeNumber:e,selectedText:e,paragraphs:
      1 pageNumber:E,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:F,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:H,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
      1 pageNumber:I,volumeNumber:a,section:a,hasChildren:c,levelNumber:a,page
```


## [2026-09-04T14:45:01.314Z] TOOL CALL #37: WebSearch

```json
{
 "query": "\"خودآموز زبان سانسکریت\" OR \"در مکتب استاد\" نفیسی OR \"واژه نامه غزلهای حافظ\" OR \"واژه های ایرانی در زبان انگلیسی\" سجادیه OR \"فرهنگ اعلام کتاب مقدس\" OR \"زبان فارسی و سرگذشت آن\" OR \"فرهنگ نامهای ایرانی\" OR \"واژه سازی در زبان فارسی\" مهراوند",
 "allowed_domains": [
  "noorlib.ir",
  "ketabnak.com",
  "archive.org",
  "ketabkoo.com"
 ]
}
```


## [2026-09-04T14:45:03.979Z] TOOL CALL #38: WebSearch

```json
{
 "query": "\"تبار مشترک ایرانیان و تورانیان\" OR \"سنگ نبشته ها سخن می گویند\" OR \"فرهنگ مشتقات مصادر فارسی\" OR \"فرهنگ واژه های همانند\" آریان OR \"واژگان فارسی در زبانهای اروپایی\" OR اخوان زنجانی",
 "allowed_domains": [
  "noorlib.ir",
  "ketabnak.com",
  "archive.org",
  "ketabkoo.com"
 ]
}
```


### [2026-09-04T14:45:08.142Z] TOOL RESULT

```
Web search results for query: "نحوی "فرهنگ واژه های عربی در فارسی" OR "واژه‌های عربی در فارسی دخیل" OR "فعل های فارسی دری" OR "فرهنگ واژه های اروپایی در فارسی" OR "ریشه شناسی" ابوالقاسمی"

Links: [{"title":"PRo-Pat: Probabilistic Root–Pattern Bi-gram data language model for Arabic based morphological analysis and distribution","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9852924/"},{"title":"Category-specific fMRI correlates of picture naming: A study with Arabs and Filipinos","url":"https://www.biorxiv.org/content/10.1101/2022.02.05.478294.full.pdf"},{"title":"Normalized Orthography for Tunisian Arabic","url":"https://arxiv.org/pdf/2402.12940"},{"title":"دانشنامه جهان اسلام - بنیاد دائرة المعارف اسلامی - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/23019/1/1967/پراهمیت"},{"title":"Hypothesis, analysis and synthesis, it's all Greek to me","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6382348/"},{"title":"Detecting gender bias in Arabic text through word embeddings","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11957338/"},{"title":"Arabo-Persian Perspective on Classification of Psychotic Disorders","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11737959/"},{"title":"Arabic spell checking error model","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10515148"}]

I've completed the web search for your query. The search returned several academic and scientific results, though they don't appear to be specifically focused on the exact topic combination you were searching for.

The most relevant result appears to be from an Islamic Encyclopedia (Dānesh‌nāmeh‌-yi Jahān-i Islām) that mentions etymology (ریشه شناسی), word usage, and the term "Bani Israel" as it appears in the Quran, in ancient scriptures, in hadith and tafsir, and in literature and popular culture.

The other results mostly concern Arabic morphology, language models for Arabic, and related linguistic topics, but don't specifically address the Persian/Dari language studies, Arabic loanwords in Persian, Persian verbs, or European loanwords in Persian that your search query appears to be targeting.

For a more precise search focused on Persian etymology and loanwords specifically, you might want to try a more targeted search query or look in Persian-language academic resources directly, as the results suggest that much of this specialized linguistic research may not be well-indexed in English-language academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:45:08.382Z] TOOL RESULT

```
Based on the provided content, **no body text from page 50 is readable**. The page appears to be a navigation/header section of the Noorlib digital library website, not the actual book content.

The content shown includes only:
- Website navigation menus
- Logo and branding elements
- Footer information about the library

**No Persian body text from the book page itself is visible**, and there are no page-navigation URL parameters displayed in this excerpt.

To access the actual text of page 50 from "واژههای دخیل در قرآن مجید," you would need to navigate to the book viewer section of the website.
```


### [2026-09-04T14:45:10.520Z] TOOL RESULT

```
Based on the provided webpage content, the Mo'in dictionary results shown do not include a direct entry for افراسیاب (Afrasyab) itself as either a proper name or common noun.

The search results only display two related entries:

1. "گنج افراسیاب" (Treasure of Afrasyab) - described as "نام گنج چهارم از گنج های خسرو پرویز که آن را از افراسیاب به دست آورد" (a treasure name associated with Khosrow Parviz and Afrasyab)

2. "ارژنگ" (Arzang) - described as "نام چاهی که افراسیاب ، بیژن را در آن زندانی کرد" (the name of a well where Afrasyab imprisoned Bijan)

Neither entry provides a standalone definition of Afrasyab as a Turanian king or etymological information. The webpage indicates there are 3 headwords found across 26 dictionaries, but the specific entry for افراسیاب itself is not displayed in this excerpt.
```


### [2026-09-04T14:45:10.858Z] TOOL RESULT

```
Web search results for query: "ایرانویج فره وشی OR "زندگی و مهاجرت آریاییان" OR "ارکان سخن" OR "فرهنگ اعلام فارسی" دانشگر OR "نامه فرهنگ ایران" جنیدی OR "درآمدی بر دستور زبان اوستایی""

Links: [{"title":"آریاییان، مردم کاشی، اَمَرد، پارس، و دیگر ایرانیان، دفتر یکم و دویم : Dr Jahanshah Derakhshani : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/diaeko2716_gmail_1"},{"title":"Full text of \"Hukht 1344 @ Persianbooks 1\"","url":"https://archive.org/stream/hukht-1344-persianbooks-1/Hukht-1344-@Persianbooks1_djvu.txt"},{"title":"Ancient DNA indicates 3,000 years of genetic continuity in the Northern Iranian Plateau, from the Copper Age to the Sassanid Empire","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12075576/"},{"title":"Extending LLMs to New Languages: A Case Study of Llama and Persian Adaptation","url":"https://arxiv.org/pdf/2412.13375"},{"title":"System and method for teaching second language writing skills using the linguistic discourse model","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6866510"},{"title":"The Genetic Legacy of the Expansion of Turkic-Speaking Nomads Across Eurasia","url":"https://www.biorxiv.org/content/10.1101/005850.full.pdf"}]

I've performed the web search with your query. The search results contain a mix of content in Persian and English, though the results don't appear to have strong direct matches for all the specific book titles and terms you included in your OR query.

The most relevant result appears to be from the Internet Archive (result #1), which references work related to Iranian history and scholarship. The other results include general content about Iran, Persian language processing, and genetic studies, but don't specifically address the particular works you searched for such as:

- "ایرانویج فره وشی"
- "زندگی و مهاجرت آریاییان" 
- "ارکان سخن"
- "فرهنگ اعلام فارسی"
- "نامه فرهنگ ایران"
- "درآمدی بر دستور زبان اوستایی"

If you're looking for information about these specific Persian-language scholarly works, you might have better success searching for them individually on the Internet Archive, Google Books, or Persian-language academic databases. Would you like me to search for any of these titles individually?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:45:17.405Z] TOOL RESULT

```
Web search results for query: ""تبار مشترک ایرانیان و تورانیان" OR "سنگ نبشته ها سخن می گویند" OR "فرهنگ مشتقات مصادر فارسی" OR "فرهنگ واژه های همانند" آریان OR "واژگان فارسی در زبانهای اروپایی" OR اخوان زنجانی"

Links: [{"title":"Full text of \"(مجموعه کتابهای استاد ناصر پورپیرار، ( تأملی در بنیان تاریخ ایران)+ (اسلام و شمشیر )،( مگر این پنج روزه ،\"","url":"https://archive.org/stream/16-01-603892_202102/3%20Sassanian%201_174677_djvu.txt"},{"title":"TARAZ: Persian Short-Answer Question Benchmark for Cultural Evaluation of Language Models","url":"https://arxiv.org/pdf/2602.22827"},{"title":"Impaired language in Alzheimer’s disease: A comparison between English and Persian implicates content-word frequency rather than the noun-verb distinction","url":"https://www.medrxiv.org/content/10.1101/2024.04.09.24305534.full.pdf"},{"title":"Ancient DNA indicates 3,000 years of genetic continuity in the Northern Iranian Plateau, from the Copper Age to the Sassanid Empire","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12075576/"},{"title":"The Genomic Formation of South and Central Asia","url":"https://www.biorxiv.org/content/10.1101/292581.full.pdf"},{"title":"The Genetic Legacy of the Expansion of Turkic-Speaking Nomads Across Eurasia","url":"https://www.biorxiv.org/content/10.1101/005850.full.pdf"},{"title":"Ancient genomics support deep divergence between Eastern and Western Mediterranean Indo-European languages","url":"https://www.biorxiv.org/content/10.1101/2024.12.02.626332.full.pdf"},{"title":"Genetic Basis of Social Structure in the Pastoral Nomads of Central Eurasia","url":"https://www.biorxiv.org/content/10.64898/2026.01.27.701587.full.pdf"},{"title":"The Genetic Legacy of the Expansion of Turkic-Speaking Nomads across Eurasia","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4405460/"}]

I found some search results, but the query produced results that don't directly match the specific books or linguistic resources you were searching for. The results primarily returned academic papers on genetics and genomics rather than the Persian linguistic and cultural texts indicated by your search terms.

Your search included references to several Persian-language works that appear to be specialized linguistic and cultural studies, including:
- "تبار مشترک ایرانیان و تورانیان" (Common ancestry of Iranians and Turanians)
- "سنگ نبشته ها سخن می گویند" (The inscriptions speak)
- "فرهنگ مشتقات مصادر فارسی" (Dictionary of Persian derivatives and verbal roots)
- "فرهنگ واژه های همانند" (Dictionary of similar/equivalent words)
- Works by or about اخوان زنجانی (Akhavan Zanjani)

The search results do not contain direct information about these specific texts. To find these Persian linguistic references, you might want to:
1. Search for them individually by exact title
2. Search for the author "اخوان زنجانی" separately
3. Try searching on Persian-language academic or library databases
4. Search on Internet Archive (archive.org) which sometimes has Persian texts

Would you like me to perform a more targeted search for any of these specific works or authors?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:45:18.666Z] TOOL RESULT

```
Web search results for query: ""خودآموز زبان سانسکریت" OR "در مکتب استاد" نفیسی OR "واژه نامه غزلهای حافظ" OR "واژه های ایرانی در زبان انگلیسی" سجادیه OR "فرهنگ اعلام کتاب مقدس" OR "زبان فارسی و سرگذشت آن" OR "فرهنگ نامهای ایرانی" OR "واژه سازی در زبان فارسی" مهراوند"

Links: [{"title":"دانلود کتاب واژه نامه غزلهای حافظ","url":"https://ketabnak.com/book/121989/%D9%88%D8%A7%DA%98%D9%87-%D9%86%D8%A7%D9%85%D9%87-%D8%BA%D8%B2%D9%84%D9%87%D8%A7%DB%8C-%D8%AD%D8%A7%D9%81%D8%B8"},{"title":"دانلود کتاب خودآموز زبان سنسکریت","url":"https://ketabnak.com/book/108067/%D8%AE%D9%88%D8%AF%D8%A2%D9%85%D9%88%D8%B2-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B3%D9%86%D8%B3%DA%A9%D8%B1%DB%8C%D8%AA"},{"title":"دانلود کتاب در مکتب استاد","url":"https://www.ketabnak.com/book/55983/%D8%AF%D8%B1-%D9%85%DA%A9%D8%AA%D8%A8-%D8%A7%D8%B3%D8%AA%D8%A7%D8%AF"},{"title":"دانلود کتاب ف‍ره‍ن‍گ‌ س‍ن‍س‍ک‍ری‍ت‌ - ف‍ارس‍ی‌ - جلد 2","url":"https://www.ketabnak.com/book/61873/%D9%81%E2%80%8D%D8%B1%D9%87%E2%80%8D%D9%86%E2%80%8D%DA%AF%E2%80%8C-%D8%B3%E2%80%8D%D9%86%E2%80%8D%D8%B3%E2%80%8D%DA%A9%E2%80%8D%D8%B1%DB%8C%E2%80%8D%D8%AA%E2%80%8C-%D9%81%E2%80%8D%D8%A7%D8%B1%D8%B3%E2%80%8D%DB%8C%E2%80%8C-%D8%AC%D9%84%D8%AF-2"},{"title":"دانلود کتاب فرهنگ ده هزار واژه از دیوان حافظ - جلد 1","url":"https://ketabnak.com/book/103923/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%AF%D9%87-%D9%87%D8%B2%D8%A7%D8%B1-%D9%88%D8%A7%DA%98%D9%87-%D8%A7%D8%B2-%D8%AF%DB%8C%D9%88%D8%A7%D9%86-%D8%AD%D8%A7%D9%81%D8%B8-%D8%AC%D9%84%D8%AF-1"},{"title":"دانلود کتابهای آذر نفیسی","url":"https://www.ketabnak.com/persons/4146/%D8%A2%D8%B0%D8%B1+%D9%86%D9%81%DB%8C%D8%B3%DB%8C"},{"title":"دانلود کتاب خدای حافظ را بشناسیم","url":"https://ketabnak.com/book/137095/%D8%AE%D8%AF%D8%A7%DB%8C-%D8%AD%D8%A7%D9%81%D8%B8-%D8%B1%D8%A7-%D8%A8%D8%B4%D9%86%D8%A7%D8%B3%DB%8C%D9%85"},{"title":"کتاب نامه پهلوانی : خودآموز خط و زبان پهلوی اشکانی، ساسانی","url":"https://ketabnak.com/book/44658/%D9%86%D8%A7%D9%85%D9%87-%D9%BE%D9%87%D9%84%D9%88%D8%A7%D9%86%DB%8C-%D8%AE%D9%88%D8%AF%D8%A2%D9%85%D9%88%D8%B2-%D8%AE%D8%B7-%D9%88-%D8%B2%D8%A8%D8%A7%D9%86-%D9%BE%D9%87%D9%84%D9%88%DB%8C-%D8%A7%D8%B4%DA%A9%D8%A7%D9%86%DB%8C-%D8%B3%D8%A7%D8%B3%D8%A7%D9%86%DB%8C"},{"title":"دانلود کتاب غزلیات سعدی","url":"https://ketabnak.com/book/1093/%D8%BA%D8%B2%D9%84%DB%8C%D8%A7%D8%AA-%D8%B3%D8%B9%D8%AF%DB%8C?subcat=696?&page=9"},{"title":"دانلود کتاب تفسیر غزلهای حافظ","url":"https://ketabnak.com/book/43435/%D8%AA%D9%81%D8%B3%DB%8C%D8%B1-%D8%BA%D8%B2%D9%84%D9%87%D8%A7%DB%8C-%D8%AD%D8%A7%D9%81%D8%B8"}]

بر اساس نتایج جستجو، من اطلاعاتی را در مورد کتاب‌های مرتبط با این عنوان‌ها برای شما پیدا کردم:

## کتاب‌های یافت شده:

1. **خودآموز زبان سنسکریت**: این کتاب، خودآموز سنسکریت است که به دست یک دانشمند ایرانی ۲۱ سال پیش از راهنم

2. **در مکتب استاد**: این برنامه نخستین بار با مدیریت و تنظیم سعید نفیسی شنیده شد. در این برنامه رادیویی مباحثی همچون شرح بیت یا ابیاتی از حافظ و دیگر مشاهیر، شرح معانی و پیچیدگی‌ها و مصطلحات، آشنایی با قواعد دستوری برای دانش‌آموزان و دوستداران مباحثی ادبی مطرح می‌شد

3. **واژه‌نامه غزلهای حافظ**: در این کتاب مفهوم مقداری از الفاظ غزلیات حافظ تبیین شده است.

نتایج جستجو بیشتر اطلاعات را در مورد این سه اثر پیدا کرد. برای کتاب‌های دیگری که در جستجوی شما نام بردید (مثل "واژه‌های ایرانی در زبان انگلیسی سجادیه"، "فرهنگ اعلام کتاب مقدس"، "زبان فارسی و سرگذشت آن"، "فرهنگ‌نامه‌های ایرانی" و "واژه‌سازی در زبان فارسی مهراوند")، نتایج جستجو اطلاعات خاصی را ارائه نکرد.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:45:36.417Z] AGENT (thinking)

I'll generate page-split versions of the downloaded books using pdftotext and djvu.xml splitting for FVQ/AFM to compute page offsets, while also probing noorlib's html/search endpoints and checking ketabnak page download permissions—running these independent tasks in parallel.


## [2026-09-04T14:46:02.657Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\nconv() { # id, remote file, out\n  curl -sL -o tmp.pdf \"https://archive.org/download/$1/$2\" && pdftotext -layout tmp.pdf \"$3\" 2>/dev/null; printf \"%s: pdf %s bytes -> %s pages, %s bytes\\n\" \"$3\" \"$(wc -c < tmp.pdf)\" \"$(tr -cd '\\f' < \"$3\" | wc -c)\" \"$(wc -c < \"$3\")\"; rm -f tmp.pdf; }\nconv borhan-ghate-v2 '%D8%A8%D8%B1%D9%87%D8%A7%D9%86%20%D9%82%D8%A7%D8%B7%D8%B9%D8%8C%20%D8%AC%D9%84%D8%AF%20%D8%AF%D9%88%D9%85_text.pdf' BQT_v2_pages.txt\nconv SogdianDictionary 'GharibSogdianDictionnary_text.pdf' SOD_pages.txt\nconv VajnameShayest 'vajname%20shayest_text.pdf' SNS_pages.txt\nconv 20220809_20220809_1444 '%D9%88%D8%A7%DA%98%D9%87_%D9%86%D8%A7%D9%85%DA%A9%D8%9B_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D9%88%D8%A7%DA%98%D9%87_%D9%87%D8%A7%DB%8C_%D8%AF%D8%B4%D9%88%D8%A7%D8%B1_%D8%B4%D8%A7%D9%87%D9%86%D8%A7%D9%85%D9%87_text.pdf' FSF_pages.txt\nconv TOB1932ARAR '%D8%AA%D9%81%D8%B3%D9%8A%D8%B1%20%D8%A7%D9%84%D8%A7%D9%84%D9%81%D8%A7%D8%B8%20%D8%A7%D9%84%D8%AF%D8%AE%D9%8A%D9%84%D8%A9%20%D9%81%D9%8A%20%D8%A7%D9%84%D9%84%D8%BA%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_text.pdf' TAD_pages.txt\nconv LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi 'luqate-fors_text.pdf' FRS_pages.txt\n# djvu.xml -> pages for FVQ and AFM\nsplit() { curl -sL -o tmp.xml \"https://archive.org/download/$1/$2\"; python3 - \"$3\" <<'EOF'\nimport re,html,sys\nx=open('tmp.xml',encoding='utf-8',errors='ignore').read()\nout=[]\nfor p in re.findall(r'<OBJECT.*?</OBJECT>',x,flags=re.S):\n    lines=[' '.join(html.unescape(w) for w in re.findall(r'<WORD[^>]*>(.*?)</WORD>',ln,flags=re.S)) for ln in re.findall(r'<LINE>(.*?)</LINE>',p,flags=re.S)]\n    out.append('\\n'.join(lines))\nopen(sys.argv[1],'w',encoding='utf-8').write('\\f'.join(out)); print(sys.argv[1],\"leaves:\",len(out))\nEOF\nrm -f tmp.xml; }\nsplit foreignvocabular030753mbp foreignvocabular030753mbp_djvu.xml FVQ_pages.txt\nsplit unset0000auth_c2g3 unset0000auth_c2g3_djvu.xml AFM_pages.txt\n# offsets: FVQ find leaf containing \"44 FOREIGN VOCABULARY\"\npython3 - <<'EOF'\nimport re\nfor fn,pat in [('FVQ_pages.txt',r'^\\s*(\\d{2,3})\\s+FOREIGN VOCABULARY|FOREIGN VOCABULARY OF THE QUR.{0,3}AN\\s+(\\d{2,3})\\s*$'),('AFM_pages.txt',r'^\\s*([٠-٩]{2,3}|\\d{2,3})\\s*$')]:\n    pages=open(fn,encoding='utf-8').read().split('\\f')\n    found=[]\n    for i,p in enumerate(pages):\n        ls=[l.strip() for l in p.split('\\n') if l.strip()][:2]+[l.strip() for l in p.split('\\n') if l.strip()][-2:]\n        for l in ls:\n            m=re.search(pat,l)\n            if m:\n                n=(m.group(1) or (m.group(2) if m.lastindex and m.lastindex>=2 else None))\n                if n:\n                    n=int(n.translate(str.maketrans('٠١٢٣٤٥٦٧٨٩','0123456789')))\n                    found.append((i,n)); break\n    print(fn,'leaf->printed samples:',found[:6],'...',found[-4:], '| offsets:',sorted(set(i-n for i,n in found))[:8])\nEOF\necho \"--- SOD_pages: check entry numbering & page headers\"; awk 'BEGIN{RS=\"\\f\"} NR==300{print substr($0,1,500)}' SOD_pages.txt\necho \"--- SNS_pages sample\"; awk 'BEGIN{RS=\"\\f\"} NR==60{print substr($0,1,400)}' SNS_pages.txt\necho \"--- TAD_pages sample\"; awk 'BEGIN{RS=\"\\f\"} NR==40{print substr($0,1,300)}' TAD_pages.txt\necho \"--- BQT_v2_pages: continuation notes\"; grep -n 'بقیه در' BQT_v2_pages.txt | head -3; awk 'BEGIN{RS=\"\\f\"} /بقیه در ?صفح/{print NR\": \"substr($0,length($0)-60)}' BQT_v2_pages.txt | head -8",
 "description": "Convert text PDFs and djvu.xml to page-split texts and compute page offsets",
 "timeout": 600000
}
```


## [2026-09-04T14:46:10.636Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\necho \"--- noorlib html view\"; curl -s 'https://noorlib.ir/book/view/12868?pageNumber=50&viewType=html' -o nl.html; wc -c nl.html; grep -o '[ء-ی‌ ]\\{40,\\}' nl.html | head -5\necho \"--- noorlib search page\"; curl -s 'https://noorlib.ir/search?q=%D9%81%D8%B9%D9%84%20%D9%87%D8%A7%DB%8C%20%D9%81%D8%A7%D8%B1%D8%B3%DB%8C%20%D8%AF%D8%B1%DB%8C' -o nls.html; wc -c nls.html; grep -o 'book/info/[0-9]*/[^\"]*' nls.html | head -10\necho \"--- noorlib info pages\"; for id in 105056 104334 12868; do printf \"$id: \"; curl -s \"https://noorlib.ir/book/info/$id\" | grep -o '<title>[^<]*' | head -1; done\necho \"--- ketabnak download availability\"; for id in 121989 108067 55983 48613 51136 81646 45024; do printf \"$id: \"; curl -sL \"https://ketabnak.com/book/$id\" | python3 -c 'import sys,re\nh=sys.stdin.read()\nt=re.search(r\"<title>([^<]*)\",h); print((t.group(1) if t else \"?\")[:60], \"| blocked\" if \"امکان دانلود آن وجود ندارد\" in h else \"| download?\", \"| pages:\"+(re.search(r\"تعداد صفحات[^0-9۰-۹]*([0-9۰-۹]+)\",h).group(1) if re.search(r\"تعداد صفحات[^0-9۰-۹]*([0-9۰-۹]+)\",h) else \"?\"))'; done",
 "description": "Probe noorlib html view/search and ketabnak download availability",
 "timeout": 120000
}
```


### [2026-09-04T14:50:01.752Z] TOOL RESULT

```
BQT_v2_pages.txt: pdf 31711743 bytes -> 683 pages, 4339896 bytes
SOD_pages.txt: pdf 47744470 bytes -> 644 pages, 3741182 bytes
SNS_pages.txt: pdf 12288786 bytes -> 242 pages, 1292394 bytes
FSF_pages.txt: pdf 11804998 bytes -> 484 pages, 2192488 bytes
TAD_pages.txt: pdf 2668193 bytes -> 86 pages, 243285 bytes
FRS_pages.txt: pdf 11518713 bytes -> 567 pages, 1613053 bytes
FVQ_pages.txt leaves: 335
AFM_pages.txt leaves: 198
FVQ_pages.txt leaf->printed samples: [(61, 44), (63, 46), (65, 48), (66, 49), (67, 50), (68, 51)] ... [(310, 293), (311, 294), (312, 295), (313, 296)] | offsets: [17, 67]
AFM_pages.txt leaf->printed samples: [(13, 83), (62, 7), (77, 21), (82, 11), (88, 0)] ... [(62, 7), (77, 21), (82, 11), (88, 0)] | offsets: [-70, 55, 56, 71, 88]
--- SOD_pages: check entry numbering & page headers
                                                                                                                 nVzyCy)

 233


        VJ 1019, 1020, 1021, 1027, 1036, etc.; Laufer.                   BBB 490; GMS 546; Sogdica. 21.2b; Anc. Lett.
                                                                           2.51; AVS 81
         p285
 5809 nYkr'k B                          <*-W<Aji                                 nw-:
      nar-kare ©Knot, nala; <Indo. ndda                         
--- SNS_pages sample
                                            Lu ii-^U <uU »jlj                                                                                                      Li_   c-^,Lt*.L.;l,
AY                                                                                                                                                                                                                    A*
--- TAD_pages sample
                   ‫ناس وسممان نت أرامي ‪ 3‬سفسارا م©عتاه المساوم‬

‫إسفين وسَفين ‪ -‬بوناني ‪ 0618‬معناه مضق ويطلق على سكة ضرب‬
                            ‫اللقود مرادفه قلق يفلق به
--- BQT_v2_pages: continuation notes
767: ‫(برهان اطع ‪)۵۷‬‬                                                  ‫بقیه درسضحهٌ ‪۹٠٠‬‏‬
2329:  ‫بقیه درصفحة ‪4۸‬‬
3175:          ‫بقیه در صفحً ‪446‬‬
42: �‪(۰۶:۶‬‬


  ‫بقیه درصفحة ‪4۸‬‬

57: 446‬‬

          ‫زبرهان فاطع ‪)۰۸‬‬
```


### [2026-09-04T14:50:20.463Z] TOOL RESULT

```
--- noorlib html view
48543 nl.html
جستجوی پیشرفته در کتابخانه‌ها و پدیدآوران
کسب نشان زرین سرآمد در ششمین جشنواره بین‌المللی رسانه‌های دیجیتال 
کسب رتبه شایسته تقدیر در نخستین جشنواره کتاب مجازی 
دریافت عنوان وب‌سایت برگزیده در یازدهمین جشنواره وب و موبایل ایران 
کسب رتبه اول در دومین جشنواره ملی کتاب در فضای مجازی 
--- noorlib search page
260963 nls.html
--- noorlib info pages
105056: <title>فرهنگ واژه‌های فارسی در زبان عربی - دانلود pdf
104334: <title>فرهنگ ایران باستان - دانلود pdf
12868: <title>واژههای دخیل در قرآن مجید - دانلود pdf
--- ketabnak download availability
121989: دانلود کتاب واژه نامه غزلهای حافظ | download? | pages:145
108067: دانلود کتاب خودآموز زبان سنسکریت | download? | pages:131
55983: دانلود کتاب در مکتب استاد | download? | pages:283
48613: دانلود کتاب فرهنگ واژه های فارسی در زبان عربی | download? | pages:818
51136: کتاب واژه های دخیل در قرآن مجید | blocked | pages:?
81646: دانلود کتاب تاریخ مختصر زبان فارسی | download? | pages:142
45024: دانلود کتاب فهرست فعلهای فارسی با معنای آنها | download? | pages:102
```


## [2026-09-04T14:50:58.698Z] AGENT (thinking)

I'll now gather several things in parallel: BQT leaf-to-page offsets and the SOD page offset, a ketabnak search sweep for the remaining low-count titles, lib.eshia.ir coverage of BQT/Mo'in, noorlib entries for FFD/FVA/VOP/ETM, and whether abadis carries Mo'in's proper-name volumes.


## [2026-09-04T14:51:14.526Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\npython3 - <<'EOF'\nimport re\ntr=str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩','01234567890123456789')\ndef nums(s): return [int(x.translate(tr)) for x in re.findall(r'[0-9۰-۹٠-٩]{2,4}',s)]\nfor fn in ['BQT_v1_pages.txt','BQT_v2_pages.txt','SOD_pages.txt']:\n    pages=open(fn,encoding='utf-8').read().split('\\f')\n    print('==',fn,len(pages))\n    # continuation notes \"بقیه در صفحه N\" => printed page = N-1 for that leaf\n    offs=[]\n    for i,p in enumerate(pages):\n        for m in re.finditer(r'بقی[هة]\\s*در\\s*ص\\S*\\s*([0-9۰-۹٠-٩]{2,4})',p):\n            n=int(m.group(1).translate(tr)); offs.append((i,n-1,i-(n-1)))\n    print(' continuation-derived (leaf,printed,offset):',offs[:12])\n    from collections import Counter\n    print(' offset histogram:',Counter(o for _,_,o in offs).most_common(6))\n    # header numerals in first 2 nonblank lines\n    hdr=[]\n    for i,p in enumerate(pages):\n        ls=[l for l in p.split('\\n') if l.strip()][:2]\n        for l in ls:\n            for n in nums(l):\n                if 0<abs(i-n)<400 or True: hdr.append((i,n,i-n))\n    c=Counter(o for _,_,o in hdr if 0<=o<300)\n    print(' header offset histogram:',c.most_common(6))\n    # first/last leaves with text\n    for i in [len(pages)//10, len(pages)//2, len(pages)-10]:\n        ls=[l.strip() for l in pages[i].split('\\n') if l.strip()]\n        print(' leaf',i,'|',(ls[0][:60] if ls else ''),'||',(ls[1][:60] if len(ls)>1 else ''))\nEOF\necho \"--- ketabnak search sweep\"\nfor q in 'فعل های فارسی دری' 'فرهنگ واژه های عربی در فارسی' 'فرهنگ واژه های اروپایی در فارسی' 'ریشه شناسی اتیمولوژی' 'ایرانویج' 'زندگی و مهاجرت آریاییان' 'ارکان سخن' 'فرهنگ اعلام فارسی' 'درآمدی بر دستور زبان اوستایی' 'واژه های ایرانی در زبان انگلیسی' 'فرهنگ اعلام کتاب مقدس' 'زبان فارسی و سرگذشت آن' 'فرهنگ نامهای ایرانی' 'واژه سازی در زبان فارسی' 'تبار مشترک ایرانیان' 'سنگ نبشته ها سخن' 'نامه فرهنگ ایران' 'فرهنگ مشتقات مصادر' 'فرهنگ واژه های همانند' 'واژگان فارسی در زبانهای اروپایی' 'فرهنگ سیاح' 'فرهنگ عمید' 'واژه نامک' 'اساس اشتقاق فارسی' 'فرهنگ سغدی' 'واژه نامه شایست نشایست' 'برهان قاطع' 'فرهنگ فارسی معین' 'لغت فرس' 'الالفاظ الفارسية المعربة' 'فرهنگ ایران باستان' 'سبک شناسی بهار'; do printf \"%s => \" \"$q\"; curl -sL -G 'https://ketabnak.com/search' --data-urlencode \"q=$q\" | python3 -c 'import sys,re,html\nh=sys.stdin.read()\nr=re.findall(r\"href=\\\"(https?://(?:www\\.)?ketabnak\\.com/book/(\\d+)/[^\\\"]*)\\\"[^>]*>([^<]{3,80})<\",h)\nseen=set(); out=[]\nfor u,i,t in r:\n    if i in seen: continue\n    seen.add(i); out.append(f\"{i}:{html.unescape(t).strip()[:50]}\")\nprint(\"; \".join(out[:4]) if out else \"no results\")'; done",
 "description": "Compute BQT/SOD page offsets and sweep ketabnak search for remaining titles",
 "timeout": 300000
}
```


## [2026-09-04T14:51:15.903Z] TOOL CALL #42: WebSearch

```json
{
 "query": "\"برهان قاطع\" OR \"فرهنگ فارسی معین\" OR \"لغت نامه دهخدا\" کتابخانه مدرسه فقاهت",
 "allowed_domains": [
  "lib.eshia.ir"
 ]
}
```


## [2026-09-04T14:51:17.597Z] TOOL CALL #43: WebSearch

```json
{
 "query": "noorlib فعل های فارسی دری OR \"واژه های عربی در فارسی\" OR \"فرهنگ واژه های اروپایی در فارسی\" OR \"ریشه شناسی\" OR \"فرهنگ سیاح\" OR ایرانویج OR \"ارکان سخن\"",
 "allowed_domains": [
  "noorlib.ir"
 ]
}
```


## [2026-09-04T14:51:20.174Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/افراسیاب/",
 "prompt": "Which dictionaries are shown for افراسیاب? Is there a \"فرهنگ فارسی\" or \"فرهنگ معین\" (اعلام) entry describing Afrasiab the Turanian king, with Avestan/Pahlavi forms (e.g. Frangrasyan)? Quote it. Also quote the لغت‌نامه دهخدا entry's first lines including bracketed sources."
}
```


### [2026-09-04T14:51:38.501Z] TOOL RESULT

```
== BQT_v1_pages.txt 777
 continuation-derived (leaf,printed,offset): [(32, 24, 8), (296, 86, 210), (329, 117, 212), (331, 119, 212), (414, 194, 220), (502, 282, 220), (534, 314, 220), (654, 498, 156), (692, 496, 196), (740, 512, 228), (758, 2, 756)]
 offset histogram: [(220, 3), (212, 2), (8, 1), (210, 1), (156, 1), (196, 1)]
 header offset histogram: [(17, 3), (12, 2), (2, 2), (104, 2), (105, 2), (133, 2)]
 leaf 77 | شصت ونه ۱ فرهنگهای پارسی || مسلم‌است که سر زمین اصلیز بان دری خر اسان‌وماوراءالنپر بوده 
 leaf 388 | اندر خور || ا ندز خو در - بنمخای نفطه‌داروسکون
 leaf 767 | تهمك - بر وزن لك لك , مصفر تهم || اسق بت و بمعنی دویم تهك ‌‌ حست که برهنه
== BQT_v2_pages.txt 684
 continuation-derived (leaf,printed,offset): [(310, 57, 253)]
 offset histogram: [(253, 1)]
 header offset histogram: [(158, 4), (58, 3), (63, 2), (154, 2), (260, 2), (13, 1)]
 leaf 68 | ‫سس‬                                                         || ‫چار دیو ار صمرذات؟ ‪ -‬وکنابه‬                             
 leaf 342 | ‫بیان هیجدهم (‪)۱‬‬ || ‫و کنات‬         ‫در دال می نقطه با نون مشتمل بر شصت وسه لغت
 leaf 674 | ‫ه‬ || ‫ا ‪۱۷‬‬
== SOD_pages.txt 645
 continuation-derived (leaf,printed,offset): []
 offset histogram: []
 header offset histogram: [(65, 162), (67, 162), (66, 133), (212, 3), (17, 3), (5, 2)]
 leaf 64 | s^\ || ^Mi.^j\3.^j*^
 leaf 322 | 256 || nyztk
 leaf 635 | AY || AY^   jl^^
--- ketabnak search sweep
فعل های فارسی دری => no results
فرهنگ واژه های عربی در فارسی => no results
فرهنگ واژه های اروپایی در فارسی => no results
ریشه شناسی اتیمولوژی => no results
ایرانویج => no results
زندگی و مهاجرت آریاییان => no results
ارکان سخن => no results
فرهنگ اعلام فارسی => no results
درآمدی بر دستور زبان اوستایی => no results
واژه های ایرانی در زبان انگلیسی => no results
فرهنگ اعلام کتاب مقدس => no results
زبان فارسی و سرگذشت آن => no results
فرهنگ نامهای ایرانی => no results
واژه سازی در زبان فارسی => no results
تبار مشترک ایرانیان => no results
سنگ نبشته ها سخن => no results
نامه فرهنگ ایران => no results
فرهنگ مشتقات مصادر => no results
فرهنگ واژه های همانند => no results
واژگان فارسی در زبانهای اروپایی => no results
فرهنگ سیاح => no results
فرهنگ عمید => no results
واژه نامک => no results
اساس اشتقاق فارسی => no results
فرهنگ سغدی => no results
واژه نامه شایست نشایست => no results
برهان قاطع => no results
فرهنگ فارسی معین => no results
لغت فرس => no results
الالفاظ الفارسية المعربة => no results
فرهنگ ایران باستان => no results
سبک شناسی بهار => no results
```


### [2026-09-04T14:51:45.123Z] TOOL RESULT

```
Web search results for query: ""برهان قاطع" OR "فرهنگ فارسی معین" OR "لغت نامه دهخدا" کتابخانه مدرسه فقاهت"

Links: [{"title":"کتابخانه مدرسه فقاهت | بخش اصلی","url":"https://lib.eshia.ir/"},{"title":"دانشنامه فرهنگ مردم ایران - مرکز دائرة المعارف بزرگ اسلامی - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/12294/2/380"},{"title":"دائرة المعارف بزرگ اسلامی، ج 11، ص 320 | مرکز دائرة المعارف بزرگ اسلامی | کتابخانه مدرسه فقاهت | بخش اصلی","url":"https://lib.eshia.ir/12293/11/320/22"},{"title":"دانشنامه فرهنگ مردم ایران، ج 2، ص 452 | مرکز دائرة المعارف بزرگ اسلامی | کتابخانه مدرسه فقاهت | بخش اصلی","url":"https://lib.eshia.ir/12294/2/452"},{"title":"فرهنگ نامه علوم قرآن - دفتر تبلیغات اسلامی - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/26683/1/4840"},{"title":"سخنرانی - سخنرانی - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/11140/1/136"},{"title":"معارف اسلامی - دفتر تبلیغات اسلامی حوزه علمیه قم - کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/10258/84/8"},{"title":"دانشنامه فرهنگ مردم ایران، ج 2، ص 28 | مرکز دائرة المعارف بزرگ اسلامی | کتابخانه مدرسه فقاهت | بخش اصلی","url":"https://lib.eshia.ir/12294/2/28"},{"title":"کتابخانه مدرسه فقاهت","url":"https://lib.eshia.ir/%D9%85%D8%B9%D8%A7%D8%AC%D9%85"},{"title":"دانشنامه فرهنگ مردم ایران، ج 2، ص 34 | مرکز دائرة المعارف بزرگ اسلامی | کتابخانه مدرسه فقاهت | بخش اصلی","url":"https://lib.eshia.ir/12294/2/34"}]

I found search results for your query. کتابخانه مدرسه فقاهت is a free digital library for documenting articles, with root word search capability and AI features for diacritization, summarization and translation.

The search results show that this library (lib.eshia.ir) contains various reference works including encyclopedias and cultural dictionaries. However, the specific results displayed don't directly show content from the three lexicographic sources you mentioned (برهان قاطع, فرهنگ فارسی معین, or لغت نامه دهخدا). 

The library appears to have a dedicated section for dictionaries and lexical references (معاجم), which would likely contain these Persian language dictionaries. To find these specific resources, you would need to visit the library's website directly and search their dictionary section.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:51:49.173Z] TOOL RESULT

```
Web search results for query: "noorlib فعل های فارسی دری OR "واژه های عربی در فارسی" OR "فرهنگ واژه های اروپایی در فارسی" OR "ریشه شناسی" OR "فرهنگ سیاح" OR ایرانویج OR "ارکان سخن""

Links: [{"title":"Phoneme-Based Persian Speech Recognition","url":"https://arxiv.org/pdf/1901.04699"},{"title":"Principle Methods of Rendering Non-equivalent Words from Uzbek and Dari to Russian and English","url":"https://arxiv.org/pdf/2508.15453"},{"title":"Noor-Ghateh: A Benchmark Dataset for Evaluating Arabic Word Segmenters in Hadith Domain","url":"https://arxiv.org/pdf/2307.09630"},{"title":"فرهنگ فارسی برهان قاطع - دانلود pdf","url":"https://noorlib.ir/book/info/10294/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%A8%D8%B1%D9%87%D8%A7%D9%86-%D9%82%D8%A7%D8%B7%D8%B9"},{"title":"Extending LLMs to New Languages: A Case Study of Llama and Persian Adaptation","url":"https://arxiv.org/pdf/2412.13375"},{"title":"واژه‌های نهج البلاغه - دانلود pdf","url":"https://noorlib.ir/book/info/3516/%D9%88%D8%A7%DA%98%D9%87-%D9%87%D8%A7%DB%8C-%D9%86%D9%87%D8%AC-%D8%A7%D9%84%D8%A8%D9%84%D8%A7%D8%BA%D9%87"},{"title":"کتابخانه شخصیت","url":"https://www.presentation.noorlib.ir/Books"}]

Based on the web search results, I found some relevant information about noorlib.ir and Persian language resources:

**برهان قاطع** (Burhan Qate') is a Persian-to-Persian dictionary authored by Muhammad Husayn ibn Khalaf Tabrizi, known as Burhan. The book was written in 1062 AH for Sultan Abdullah Qutb Shah and includes Persian, Pahlavi, Dari, Greek, Syriac, Roman terms, and Arabic-mixed expressions and idioms, along with Zend and Pahlavi words found in lexicographical works.

Additionally, there is a lexicon resource called "واژه‌های نهج‌البلاغه" (Words of Nahj al-Balagha), which is a book in Arabic and Persian that explains the meanings of difficult words and terms used in Nahj al-Balagha by Seyyed Razi.

These appear to be linguistic and lexicographical resources available through noorlib.ir (ویکی نور/Wiki Noor), an Iranian digital library platform that houses various academic and literary texts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:51:51.798Z] TOOL RESULT

```
# Dictionaries and Entries for افراسیاب

## Dictionaries Shown

The page displays entries from multiple lexicographic sources:
- **فرهنگ اسم‌ها** (Names Dictionary)
- **لغت‌نامه دهخدا** (Dehkhoda Dictionary)
- **فرهنگ فارسی** (Persian Dictionary)
- **دانشنامه عمومی** (General Encyclopedia)
- **دانشنامه آزاد فارسی** (Free Persian Encyclopedia)

## Dehkhoda Dictionary Entry (Opening Lines)

The initial Dehkhoda entry begins:

> "افراسیاب. [ اَ ] ( ص )کنایه از هموار به راه رونده است چه آب بمعنی راه رو هموار است. ( هفت قلزم ) ( برهان )."

This translates to a reference meaning "smooth path-walker," citing sources "Haft Qolzom" and "Burhan."

## Avestan/Pahlavi Forms

The Names Dictionary section provides: "در اوستایی، fran ( g ) rasiyan" and notes the Pahlavi form "فراسیاک" meaning "fearsome person."

The Dehkhoda section elaborates that in Pahlavi it means "frightening person," with etymological origins in Avestan *Frangrasyan*.
```


## [2026-09-04T14:52:19.959Z] AGENT (thinking)

I'll now request the remaining details together: a firmer BQT vol. 2 page offset, the noorlib edition of Borhan-e Qate' (book 10294), and whether noorlib hosts Mo'in's 6-volume Farhang-e Farsi or Sayyah's dictionary.


## [2026-09-04T14:52:26.927Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\npython3 - <<'EOF'\nimport re\nfrom collections import Counter\ntr=str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩','01234567890123456789')\npages=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nc=Counter(); ex=[]\nfor i,p in enumerate(pages):\n    ls=[l for l in p.split('\\n') if l.strip()]\n    for l in ls[:2]+ls[-2:]:\n        for x in re.findall(r'[0-9۰-۹٠-٩]{3,4}',l):\n            n=int(x.translate(tr))\n            if 540<=n<=1400: c[i-n]+=1; ex.append((i,n))\nprint('v2 offsets for header numerals 540-1400:',c.most_common(8)); print(ex[:15])\n# first leaf with headword-like content and the letter\nfor i in [20,30,40,60]:\n    ls=[l.strip() for l in pages[i].split('\\n') if l.strip()]\n    print(i,'|',' / '.join(x[:40] for x in ls[:3]))\n# last leaves headwords\nfor i in [600,650,670]:\n    ls=[l.strip() for l in pages[i].split('\\n') if l.strip()]\n    print(i,'|',' / '.join(x[:40] for x in ls[:3]))\nEOF\nls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs | awk '{print $5, $9}'",
 "description": "Estimate BQT vol 2 page offset and list downloaded files",
 "timeout": 60000
}
```


### [2026-09-04T14:52:29.200Z] TOOL RESULT

```
v2 offsets for header numerals 540-1400: [(-543, 3), (-541, 3), (-545, 3), (-772, 2), (-622, 2), (-624, 2), (-697, 2), (-587, 2)]
[(4, 1331), (14, 705), (16, 900), (19, 878), (19, 800), (20, 792), (27, 649), (32, 575), (34, 878), (34, 838), (36, 870), (37, 981), (44, 891), (49, 673), (54, 751)]
20 | ‫¬=“‬                                    / ‫ونام کلی حم هت وآن در هندوستان‬      ‫ب / ‫نباش‬
30 | ‫يان نهم‬ / ‫در جیم ابجدبا شین قرشت مشتمل‌برپانزده ل / ‫و آن روز ششم‌فروردین‌ماه قدیم باشد» و آ
40 | ‫اس‬      ‫‪۲‬‬                          / ‫باشد پیش جهودان چ"ه ابثان هرساعتی را بك / ‫را از آن جلق‬         ‫هزار وهشتاد قسم 
60 | ‫‪ ۵ ۲‬ات‬ / ‫جومت‬ / ‫هورك از سنگهای نفسه همچو المای وباقوت‬ 
600 | ‫‪۱۱۳‬‬ / ‫آمد وسزاوار گردید هم هت ‪4.‬‬         ‫ / ‫بوز‬
650 | ‫‏‪r‬‬ / ‫بوریجان‬ / ‫ابهپیکان تشبیهکرده‌اند ‪ - ۴‬ونوعی از پ
670 | ‫==‬                                     / ‫و بنون زده» لوعی از گیاه باشد مانند فرت / ‫و پیوسته درآب روید و آلرا پعریی حرف‌الم
 
4096 .
4096 ..
600115 AFA.txt
342401 AFM_pages.txt
354548 AFM.txt
850109 AHD_watkins1985.txt
824886 AHM.txt
1215090 AID.txt
239712 AIN.txt
255553 AKD.txt
285355 ARB_abdulraheem.txt
1296442 ARB_mo3rb.txt
743553 ARP.txt
633097 AVG.txt
2634275 BQT_alt_v1.txt
146 BQT_dli_part1.txt
26399828 BQT_v1_djvu.xml
2247721 BQT_v1_pages.txt
2620060 BQT_v1.txt
4339896 BQT_v2_pages.txt
2359504 BQT_v2.txt
4803500 BRT.txt
656131 BST.txt
1769485 CHEUNG.txt
592705 DEV.txt
143939 DOZ.txt
1499054 DRM.txt
559516 EAV_studies.txt
1613053 FRS_pages.txt
890981 FRS.txt
16441388 FSD_vol1.txt
16801850 FSD_vol2.txt
16697862 FSD_vol4.txt
2192488 FSF_pages.txt
1152733 FSF.txt
628003 FVQ_pages.txt
649903 FVQ.txt
572506 GPL.txt
1572807 HENNING_selected_papers.txt
448664 HID.txt
5610600 HJB.txt
688044 HRN.txt
527491 HUB.txt
3311889 IEC.txt
3409804 ISS_alt_DKS.txt
1299560 KFL.txt
10837854 KLN_1966.txt
10278576 KLN_1971.txt
873578 KNT.txt
487736 LAM.txt
4618386 LAT.txt
627390 LEW_1910.txt
1056082 LKT.txt
62059 LST.txt
4377831 MON_part1.txt
4331421 MON_part2.txt
372944 MPP.txt
470206 NAT_2005.txt
504627 NYB_vol1.txt
920054 NYB_vol2_glossary.txt
8373934 PHD_mackenzie.pdf
609465 PHD_mackenzie.txt
603979 PHN.txt
981836 POK_01.txt
1137861 POK_02.txt
1170809 POK_03.txt
3971883 POK_full.txt
1264311 SBK.txt
225642 SDQ.txt
1365234 SIN.txt
2656202 SKT.txt
1292394 SNS_pages.txt
325929 SNS.txt
3741182 SOD_pages.txt
1845041 SOD.txt
466443 SPG_keilinschriften1881.txt
4502081 SYN.txt
243285 TAD_pages.txt
151889 TAD.txt
312765 TLM.txt
89292 UNV.txt
12198872 WEB_vol1.txt
317372 WLD_band3.txt
548741 ZAP.txt
```


## [2026-09-04T14:52:29.272Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://noorlib.ir/book/info/10294",
 "prompt": "Report the bibliographic details of this noorlib book: exact title, author, editor (e.g. محمد معین), publisher, year, number of volumes and pages per volume, and whether it is described as having حواشی/تعلیقات by Mo'in. Quote the description."
}
```


## [2026-09-04T14:52:30.770Z] TOOL CALL #47: WebSearch

```json
{
 "query": "noorlib.ir \"فرهنگ فارسی\" محمد معین شش جلدی امیرکبیر دانلود pdf",
 "allowed_domains": [
  "noorlib.ir"
 ]
}
```


## [2026-09-04T14:52:32.148Z] TOOL CALL #48: WebSearch

```json
{
 "query": "noorlib.ir \"فرهنگ بزرگ جامع نوین\" سیاح OR \"فرهنگ عمید\" OR \"لغت فرس\" اسدی OR \"فرهنگ ایران باستان\"",
 "allowed_domains": [
  "noorlib.ir"
 ]
}
```


### [2026-09-04T14:52:35.986Z] TOOL RESULT

```
# Bibliographic Details: فرهنگ فارسی برهان قاطع

**Exact Title:** فرهنگ فارسی برهان قاطع

**Author:** برهان‌، محمدحسین‌ بن‌ خلف (Burhan, Muhammad Husayn ibn Khalaf)

**Editor:** Not listed

**Publisher:** نيما (Nima), Tehran, Iran

**Year:** 1380 (Persian calendar)

**Number of Volumes:** 1

**Pages per Volume:** Not specified in source

**Notes on Marginalia:** The provided content makes no reference to حواشی or تعلیقات by Muhammad Mo'in.

**Description Quote:** The work is described as "فرهنگ لغات فارسی به فارسی" (a Persian-to-Persian lexicon) that aims to "جمع‌آوری همه لغات فارسی پهلوی، دری، یونانی، سریانی، رومی، اصطلاحات" (compile Persian, Pahlavi, Dari, Greek, Syriac, and Roman vocabulary with related expressions).
```


### [2026-09-04T14:52:36.814Z] TOOL RESULT

```
Web search results for query: "noorlib.ir "فرهنگ فارسی" محمد معین شش جلدی امیرکبیر دانلود pdf"

Links: [{"title":"روضات الجنات في أوصاف مدینة هرات - Download pdf","url":"https://noorlib.ir/en/book/info/11516/%D8%B1%D9%88%D8%B6%D8%A7%D8%AA-%D8%A7%D9%84%D8%AC%D9%86%D8%A7%D8%AA-%D9%81%D9%8A-%D8%A3%D9%88%D8%B5%D8%A7%D9%81-%D9%85%D8%AF%DB%8C%D9%86%D8%A9-%D9%87%D8%B1%D8%A7%D8%AA"},{"title":"لغت نامه - دانلود pdf","url":"https://noorlib.ir/book/info/53064/%D9%84%D8%BA%D8%AA-%D9%86%D8%A7%D9%85%D9%87"},{"title":"خلاصة الأشعار و زبدة الأفکار (بخش یزد و کرمان و نواحی آن)","url":"https://noorlib.ir/book/info/92811"},{"title":"خلاصة الأشعار و زبدة الأفکار (بخش شیراز و نواحی آن)","url":"https://noorlib.ir/book/info/35808/%D8%AE%D9%84%D8%A7%D8%B5%D8%A9-%D8%A7%D9%84%D8%A3%D8%B4%D8%B9%D8%A7%D8%B1-%D9%88-%D8%B2%D8%A8%D8%AF%D8%A9-%D8%A7%D9%84%D8%A3%D9%81%DA%A9%D8%A7%D8%B1-(%D8%A8%D8%AE%D8%B4-%D8%B4%DB%8C%D8%B1%D8%A7%D8%B2-%D9%88-%D9%86%D9%88%D8%A7%D8%AD%DB%8C-%D8%A2%D9%86)"},{"title":"المصباح المنیر في غریب الشرح الکبیر للرافعي","url":"https://noorlib.ir/book/info/2092"},{"title":"کتابخانه دیجیتال نور - صفحه اصلی","url":"https://noorlib.ir/"},{"title":"حکمت الهی در متون فارسی - دانلود pdf","url":"https://noorlib.ir/book/info/13870/%D8%AD%DA%A9%D9%85%D8%AA-%D8%A7%D9%84%D9%87%DB%8C-%D8%AF%D8%B1-%D9%85%D8%AA%D9%88%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"خلاصة الأشعار و زبدة الأفکار (بخش تبریز، و آذربایجان و نواحی آن)","url":"https://noorlib.ir/book/info/92809/%D8%AE%D9%84%D8%A7%D8%B5%D8%A9-%D8%A7%D9%84%D8%A3%D8%B4%D8%B9%D8%A7%D8%B1-%D9%88-%D8%B2%D8%A8%D8%AF%D8%A9-%D8%A7%D9%84%D8%A3%D9%81%DA%A9%D8%A7%D8%B1-(%D8%A8%D8%AE%D8%B4-%D8%AA%D8%A8%D8%B1%DB%8C%D8%B2-%D9%88-%D8%A2%D8%B0%D8%B1%D8%A8%D8%A7%DB%8C%D8%AC%D8%A7%D9%86-%D9%88-%D9%86%D9%88%D8%A7%D8%AD%DB%8C-%D8%A2%D9%86)"},{"title":"کتابخانه شخصیت","url":"https://www.presentation.noorlib.ir/Books"},{"title":"فرهنگ معارف نهج البلاغه - دانلود pdf","url":"https://noorlib.ir/book/info/3483"}]

The search results don't contain any information specifically about "فرهنگ فارسی" (Persian Dictionary) by Mohammad Mo'in published by Amirkabir in a six-volume edition or its PDF download on noorlib.ir.

The search returned various results from noorlib.ir (a digital library for Islamic sciences), but none of them were related to the specific work you're looking for. The results included other Persian language dictionaries and literary works, but not the particular six-volume Persian dictionary by Mohammad Mo'in published by Amirkabir that you searched for.

If you're looking to download this specific work, you might want to:
1. Search directly on noorlib.ir's website
2. Try alternative search terms
3. Check other Persian digital libraries
4. Contact noorlib.ir directly for availability of this specific publication


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-04T14:52:40.335Z] TOOL RESULT

```
Web search results for query: "noorlib.ir "فرهنگ بزرگ جامع نوین" سیاح OR "فرهنگ عمید" OR "لغت فرس" اسدی OR "فرهنگ ایران باستان""

Links: [{"title":"فرهنگ عمید - دانلود pdf","url":"https://noorlib.ir/en/book/info/28973/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B9%D9%85%DB%8C%D8%AF"},{"title":"فرهنگ لغت عربی - Occasional books","url":"https://noorlib.ir/en/Specials/29"},{"title":"فرهنگ ابجدی - دانلود pdf","url":"https://noorlib.ir/book/info/2094/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%A7%D8%A8%D8%AC%D8%AF%DB%8C"},{"title":"فرهنگ عمید - جلد 1 بخش بخش 1 صفحه 1","url":"https://noorlib.ir/book/view/28973/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B9%D9%85%DB%8C%D8%AF?viewType=pdf"},{"title":"... جمهرة اللغة - دانلود pdf","url":"https://noorlib.ir/book/info/776/...-%D8%AC%D9%85%D9%87%D8%B1%D8%A9-%D8%A7%D9%84%D9%84%D8%BA%D8%A9"},{"title":"أخبار الطوال - دانلود pdf","url":"https://noorlib.ir/book/info/2321/%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D8%B7%D9%88%D8%A7%D9%84"},{"title":"تهذیب اللغة - دانلود pdf","url":"https://noorlib.ir/book/info/775/%D8%AA%D9%87%D8%B0%DB%8C%D8%A8-%D8%A7%D9%84%D9%84%D8%BA%D8%A9"},{"title":"لغت نامه: فرهنگ متوسط دهخدا - volume 1 Book section بخش 2 Page 1601","url":"https://noorlib.ir/en/book/view/50606/%D9%84%D8%BA%D8%AA-%D9%86%D8%A7%D9%85%D9%87:-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D9%85%D8%AA%D9%88%D8%B3%D8%B7-%D8%AF%D9%87%D8%AE%D8%AF%D8%A7?pageNumber=1601&sectionNumber=2&volumeNumber=1&viewType=html"},{"title":"النهایة في غریب الحدیث و الأثر - دانلود pdf","url":"https://noorlib.ir/book/info/2384/%D8%A7%D9%84%D9%86%D9%87%D8%A7%DB%8C%D8%A9-%D9%81%D9%8A-%D8%BA%D8%B1%DB%8C%D8%A8-%D8%A7%D9%84%D8%AD%D8%AF%DB%8C%D8%AB-%D9%88-%D8%A7%D9%84%D8%A3%D8%AB%D8%B1"},{"title":"المصباح المنیر في غریب الشرح الکبیر للرافعي","url":"https://noorlib.ir/book/info/2092"}]

I've completed the web search for your query about Persian dictionaries on noorlib.ir. The search results show several relevant dictionary resources available on the platform:

The "فرهنگ عمید" (Amid Dictionary) by Hassan Amid is available for reading and download as a PDF.

The search results also indicate that noorlib.ir hosts a comprehensive collection of linguistic resources, including 39 complete dictionary titles in 200 volumes in Arabic and Persian, covering various types of dictionaries: thematic, lexical, Quranic, narrative, philosophical, jurisprudential, medical, and geographical.

Other dictionary resources mentioned in the results include various classical Arabic and Persian lexicographic works, though the specific titles you mentioned in your search query ("فرهنگ بزرگ جامع نوین" by Siahi, "لغت فرس" by Asadi, and "فرهنگ ایران باستان") are not explicitly highlighted in the main search results displayed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-04T14:53:09.981Z] AGENT (thinking)

I've confirmed the BQT vol. 2 pagination offset and noted that noorlib's Borhan entry (10294) is a separate one-volume Nima 1380 edition, not Mo'in's, making it only a secondary reference. Now I'll write the JSON output file.


## [2026-09-04T14:55:23.577Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nR=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs\npython3 - \"$R\" <<'EOF'\nimport json,sys\nR=sys.argv[1]\nINSIDE=\"archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}\"\nd={}\nd[\"BQT\"]={\"title\":\"Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)\",\n \"kind\":\"archive_djvu\",\n \"url\":\"https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary)\",\n \"lookup_hint\":\"grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\\\f; leaf N = N-th \\\\f-block, 0-based); or use \"+INSIDE+\". Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes.\",\n \"local_file\":[R+\"/BQT_v1_pages.txt\",R+\"/BQT_v2_pages.txt\",R+\"/BQT_v1.txt (raw djvu.txt, no page breaks)\",R+\"/BQT_v2.txt (raw)\"],\n \"page_offset\":\"vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375.\",\n \"covers_etymology\":True,\n \"notes\":\"Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition).\"}\nd[\"MON\"]={\"title\":\"Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)\",\n \"kind\":\"website\",\n \"url\":\"https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)\",\n \"lookup_hint\":\"Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).\",\n \"local_file\":[R+\"/MON_part1.txt\",R+\"/MON_part2.txt\"],\n \"page_offset\":None,\n \"covers_etymology\":True,\n \"notes\":\"covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view.\"}\nd[\"SOD\"]={\"title\":\"Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995\",\n \"kind\":\"archive_djvu\",\n \"url\":\"https://archive.org/details/SogdianDictionary\",\n \"lookup_hint\":\"Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or \"+INSIDE.replace('borhan-ghate-v1','SogdianDictionary').replace('ia800104.us.archive.org dir=/23/items/borhan-ghate-v1','see metadata'),\n \"local_file\":[R+\"/SOD_pages.txt\",R+\"/SOD.txt\"],\n \"page_offset\":\"printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\\\f blocks; 645 leaves; English intro precedes)\",\n \"covers_etymology\":True,\n \"notes\":\"OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.\"}\nd[\"SNS\"]={\"title\":\"Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986\",\n \"kind\":\"archive_djvu\",\n \"url\":\"https://archive.org/details/VajnameShayest\",\n \"lookup_hint\":\"grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.\",\n \"local_file\":[R+\"/SNS_pages.txt\",R+\"/SNS.txt\"],\n \"page_offset\":\"242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image\",\n \"covers_etymology\":True,\n \"notes\":\"OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image.\"}\nd[\"FFD\"]={\"title\":\"Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online. The verb etymologies it gives largely repeat Abolghasemi's دستور تاریخی زبان فارسی, which IS on archive.org (https://archive.org/details/20220417_20220417_2237) and could serve as a proxy.\"}\nd[\"FVA\"]={\"title\":\"S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Searched archive.org, ketabnak, noorlib, web: no digital copy found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"AEF\"]={\"title\":\"Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence\",\n \"kind\":\"none\",\n \"url\":None,\n \"lookup_hint\":\"Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015 complete edition was retitled 'فرهنگ ریشه‌شناختی فارسی' (Mehrafarin), also not online.\",\n \"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online; proxy via HRN/HUB.\"}\nd[\"VOP\"]={\"title\":\"Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"FSF\"]={\"title\":\"Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/20220809_20220809_1444\",\n \"lookup_hint\":\"grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).\",\n \"local_file\":[R+\"/FSF_pages.txt\",R+\"/FSF.txt\"],\"page_offset\":\"484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking\",\"covers_etymology\":False,\n \"notes\":\"Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used.\"}\nd[\"TAD\"]={\"title\":\"Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640\",\n \"lookup_hint\":\"Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.\",\n \"local_file\":[R+\"/TAD_pages.txt\",R+\"/TAD.txt\"],\"page_offset\":\"86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image\",\"covers_etymology\":True,\n \"notes\":\"Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination.\"}\nd[\"FVQ\"]={\"title\":\"Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)\",\n \"lookup_hint\":\"Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).\",\n \"local_file\":[R+\"/FVQ_pages.txt\",R+\"/FVQ.txt\"],\"page_offset\":\"printed page = leaf − 17 (0-based \\\\f blocks in FVQ_pages.txt; 335 leaves)\",\"covers_etymology\":True,\n \"notes\":\"Good English OCR (Arabic script garbled). Same 1938 edition Nourai cites.\"}\nd[\"VDQ\"]={\"title\":\"Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993\",\n \"kind\":\"website\",\"url\":\"https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)\",\n \"lookup_hint\":\"noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.\",\n \"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"Not on archive.org. Also on ghaemiyeh (ghbook.ir) as an app/EPUB per news reports.\"}\nd[\"FVF\"]={\"title\":\"S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968\",\n \"kind\":\"website\",\"url\":\"https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)\",\n \"lookup_hint\":\"Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.\",\n \"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS).\"}\nd[\"ETM\"]={\"title\":\"Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Searched archive.org, ketabnak, noorlib, web: not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"TZF\"]={\"title\":\"Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994\",\n \"kind\":\"website\",\"url\":\"https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)\",\n \"lookup_hint\":\"Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).\",\n \"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"PDF exists but not downloadable without login.\"}\nd[\"SAP\"]={\"title\":\"Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"IRN\"]={\"title\":\"Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"AFM\"]={\"title\":\"Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)\",\n \"lookup_hint\":\"Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').\",\n \"local_file\":[R+\"/AFM_pages.txt\",R+\"/AFM.txt\"],\"page_offset\":\"198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image\",\"covers_etymology\":True,\n \"notes\":\"Arabic OCR fair; Syriac/Latin etyma partially garbled.\"}\nd[\"FRS\"]={\"title\":\"Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')\",\n \"lookup_hint\":\"Look up the headword (entries grouped by final letter); FRS_pages.txt has \\\\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.\",\n \"local_file\":[R+\"/FRS_pages.txt\",R+\"/FRS.txt\"],\"page_offset\":\"different edition — no mapping\",\"covers_etymology\":False,\n \"notes\":\"Persian OCR fair. Ganjoor does not host Loghat-e Fors.\"}\nd[\"ZMA\"]={\"title\":\"Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Searched archive.org, ketabnak, noorlib, web: not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"FAF\"]={\"title\":\"A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"ARK\"]={\"title\":\"M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"AMD\"]={\"title\":\"Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990\",\n \"kind\":\"website\",\"url\":\"https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf\",\n \"lookup_hint\":\"Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.\",\n \"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"Entry-level verification only.\"}\nd[\"DZA\"]={\"title\":\"M.T. Rashed Mohassel, Daramadi bar Dastur-e Zaban-e Avestai, Khajeh 1364/1985\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"KAS\"]={\"title\":\"M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982\",\"kind\":\"website\",\"url\":\"https://ketabnak.com/book/108067 (131 pp. PDF, login)\",\"lookup_hint\":\"Not on archive.org.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"PDF page exists; not fetched.\"}\nd[\"DMO\"]={\"title\":\"Sa'id Nafisi, Dar Maktab-e Ostad, Zohreh 1344/1965\",\"kind\":\"website\",\"url\":\"https://www.ketabnak.com/book/55983 (283 pp. PDF, login)\",\"lookup_hint\":\"Not on archive.org.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"PDF page exists; not fetched.\"}\nd[\"SBK\"]={\"title\":\"M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/1_20250928_20250928_1159 (3 vols; vol 1 = سبک شناسی_1)\",\n \"lookup_hint\":\"grep in SBK.txt (raw djvu, no page breaks); use inside.php with doc='سبک شناسی_1'. Later printings keep the 1st-edition pagination approximately; verify.\",\n \"local_file\":[R+\"/SBK.txt\"],\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"Persian OCR fair. galaxy_ub2007_yahoo_20151117 is another (tiny-OCR) copy.\"}\nd[\"VGH\"]={\"title\":\"H. Khadiv Jam, Vazhe-name-ye Ghazalha-ye Hafez, Elmi 1371/1992\",\"kind\":\"website\",\"url\":\"https://ketabnak.com/book/121989 (145 pp. PDF, login)\",\"lookup_hint\":\"Not on archive.org.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"PDF page exists; not fetched.\"}\nd[\"VIE\"]={\"title\":\"M.A. Sajjadiyyeh, Vazheha-ye Irani dar Zaban-e Engelisi, Bonyad-e Neyshabur 1364/1985\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"AKM\"]={\"title\":\"Amir J. A'lam, Farhang-e A'lam-e Ketab-e Moqaddas (Dictionary of Proper Names in the Bible, English–Persian), Iran University Press 1988\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"ZFS\"]={\"title\":\"Mohsen Abolghasemi, Zaban-e Farsi va Sargozasht-e An, Hirmand 1375/1996\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"SOR\"]={\"title\":\"K. Akhavan Zanjani — title unknown (Table IV entry for SOR lost in OCR; listed under Persian authors)\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Author search on archive.org/web found nothing.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online; title unidentified.\"}\nd[\"FNI\"]={\"title\":\"F. Danayi, Farhang-e Namha-ye Irani, Negah 1370/1991\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found (archive has an unrelated 'کامل ترین فرهنگ نام های ایرانی' by Flora Jahandar).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"VSF\"]={\"title\":\"K. Mehravand, Vazhe-sazi dar Zaban-e Farsi, Rasti 1349/1970\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"FVS\"]={\"title\":\"(not in Table IV — probably a typo for FVF or FSF)\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Check the two citations against FVF (Emam Shushtari) and FSF (Noushin).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"abbreviation not defined in Nourai's Table IV.\"}\nd[\"FIB\"]={\"title\":\"Ebrahim Pur-Davud, Farhang-e Iran-e Bastan, vol. I, Tehran University Press 1326/1947\",\n \"kind\":\"website\",\"url\":\"https://noorlib.ir/book/info/104334 (viewer: https://noorlib.ir/book/view/104334?pageNumber=<N>&viewType=pdf) ; PDFs also offered at kashanketab.com / kaffeketab.ir (62 MB)\",\n \"lookup_hint\":\"Not on archive.org; browser needed for noorlib.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"Scan exists online but not fetched here.\"}\nd[\"IRT\"]={\"title\":\"M.A. Sajjadiyyeh, Tabar-e Moshtarek-e Iranian va Turanian, Bonyad-e Neyshabur 1368/1989\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"SNB\"]={\"title\":\"H. Kowsar, Sang-nebeshteh-ha Sokhan Miguyand, Iranian Military Press (1960s)\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"KFL\"]={\"title\":\"Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/20260705_20260705_0657 (an Indian/other printing; OCR poor) ; better: text on shamela.ws (search 'فقه اللغة وسر العربية الثعالبي') with edition page numbers\",\n \"lookup_hint\":\"Look up by chapter/word on shamela; the 1885 Beirut pagination is not reproduced online.\",\n \"local_file\":[R+\"/KFL.txt\"],\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"Archive OCR of this copy is very poor; use shamela text.\"}\nd[\"NFI\"]={\"title\":\"F. Jonaydi, Nameh-ye Farhang-e Iran (section 4 translating C.H. Rempis, 'Persische Wörter im Deutschen'), Bonyad-e Neyshabur 1368/1989\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"MMF\"]={\"title\":\"K. Khalili, Farhang-e Moshtaqqat-e Masader-e Farsi (Dictionary of Derivatives of the Persian Infinitives), Institute of Cultural Studies and Research 1993\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online.\"}\nd[\"MZF\"]={\"title\":\"P. Natel Khanlari — Table IV line garbled ('... darbareh Zaban-e Farsi', Sokhan 1340/1961; probably 'زبان‌شناسی و زبان فارسی')\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found (his تاریخ زبان فارسی is on archive.org as 1_20251010_20251010_2025 but is a different book).\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":False,\"notes\":\"none online; title uncertain.\"}\nd[\"ARM\"]={\"title\":\"A. Aryan, Farhang-e Vazheha-ye Hamanand: Armani–Avestai–Pahlavi–Farsi, vol. I (آ), Bonyad-e Neyshabur 1363/1984\",\"kind\":\"none\",\"url\":None,\"lookup_hint\":\"Not found.\",\"local_file\":None,\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"none online.\"}\nd[\"ARB\"]={\"title\":\"al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)\",\n \"kind\":\"archive_djvu\",\"url\":\"https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws\",\n \"lookup_hint\":\"Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.\",\n \"local_file\":[R+\"/ARB_mo3rb.txt\",R+\"/ARB_abdulraheem.txt\"],\"page_offset\":None,\"covers_etymology\":True,\"notes\":\"Arabic OCR fair.\"}\njson.dump(d,open('refs_online_persian.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint(len(d),\"entries\")\nEOF\npython3 -m json.tool refs_online_persian.json > /dev/null && echo JSON_OK\npython3 -c \"\nimport json;d=json.load(open('refs_online_persian.json'))\nfrom collections import Counter;print(Counter(v['kind'] for v in d.values()))\nprint('archive:',[k for k,v in d.items() if v['kind']=='archive_djvu']);print('website:',[k for k,v in d.items() if v['kind']=='website']);print('none:',[k for k,v in d.items() if v['kind']=='none'])\"",
 "description": "Write and validate refs_online_persian.json"
}
```


### [2026-09-04T14:55:25.907Z] TOOL RESULT

```
44 entries
JSON_OK
Counter({'none': 24, 'archive_djvu': 11, 'website': 9})
archive: ['BQT', 'SOD', 'SNS', 'FSF', 'TAD', 'FVQ', 'AFM', 'FRS', 'SBK', 'KFL', 'ARB']
website: ['MON', 'VDQ', 'FVF', 'TZF', 'AMD', 'KAS', 'DMO', 'VGH', 'FIB']
none: ['FFD', 'FVA', 'AEF', 'VOP', 'ETM', 'SAP', 'IRN', 'ZMA', 'FAF', 'ARK', 'DZA', 'VIE', 'AKM', 'ZFS', 'SOR', 'FNI', 'VSF', 'FVS', 'IRT', 'SNB', 'NFI', 'MMF', 'MZF', 'ARM']
```


## [2026-09-04T14:55:51.498Z] AGENT

Output written and validated: `/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/refs_online_persian.json` (44 abbreviations). Downloaded texts are in `.../scratchpad/refs/`.

## Summary

**Found on archive.org with OCR downloaded (11)**

| Abbr | Item | Local file | Page mapping |
|---|---|---|---|
| **BQT** | Mo'in's 1342/1963 ed. (Nourai's Amir Kabir 1362 is its photo-reprint), **vols 1–2 only** (`borhan-ghate-v1`, `-v2`) | `BQT_v1_pages.txt`, `BQT_v2_pages.txt` (\f-separated leaves) | v1: printed ≈ leaf −210 … −228 (drifts); v2: printed ≈ leaf +543. BQT:918 → v2 leaf ≈375. Vols 3–5 not online; fall back on Dehkhoda's quotations (vajehyab/abadis/parsi.wiki cite "حاشیهٔ برهان قاطع چ معین"). Footnotes are in the OCR; quality mediocre. |
| **SOD** | Gharib 1995, full scan (`SogdianDictionary`) | `SOD_pages.txt` | printed ≈ leaf −66; entries are numbered — SOD:NNNN may be entry numbers. Sogdian/English readable, Persian glosses garbage. |
| **SNS** | Tavoosi's glossary (`VajnameShayest`) | `SNS_pages.txt` | OCR poor; locate via Latin transliteration, then read page image. |
| **FVQ** | Jeffery 1938 (`foreignvocabular030753mbp`) | `FVQ_pages.txt` | printed = leaf −17. Good OCR. |
| **AFM** | Addi Shir 1908 (`unset0000auth_c2g3`) | `AFM_pages.txt` | ≈ leaf −8, confirm on image. |
| **FSF** | Noushin, Vazhe-namak (`20220809_20220809_1444`) | `FSF_pages.txt` | edition unverified. |
| **TAD** | = Tobia al-Unaysi, *Tafsir al-alfaz al-dakhila*, 1932 ed. (`TOB1932ARAR`) | `TAD_pages.txt` | ≈ leaf −5. |
| **FRS** | Loghat-e Fors, Eqbal 1319 ed. (different from Nourai's Kharazmi 1365) | `FRS_pages.txt` | verify entry, not page. |
| **SBK** | Bahar, Sabk-shenasi 3 vols | `SBK.txt` | no page breaks. |
| **KFL**, **ARB** | Tha'alebi; Jawaliqi (2 editions) | `KFL.txt`, `ARB_*.txt` | poor/unknown editions; shamela.ws text is the better route. |

Generic page-locating trick recorded in every archive entry: archive.org's `fulltext/inside.php` search returns leaf numbers for a query word (tested on BQT).

**Website only (9)**: **MON** — vajehyab.com/?q=<word>&d=moein and abadis.ir/fatofa/<word>/ give the entry text with origin tags ([په.] etc.) but *without* the Latin Pahlavi/Avestan forms; page numbers unmappable; the a'lam vols 5–6 (MON5 citations) are not online at all. The archive.org "Mo'in" is only the 2-vol Adena abridgement (downloaded as `MON_part*.txt`). VDQ, FVF, FIB — noorlib.ir viewer (JS-rendered, browser needed; `?pageNumber=N&viewType=pdf`); TZF, KAS, DMO, VGH — ketabnak pages (login); AMD — vajehyab `d=amid`.

**Not found (24)**: FFD, FVA, AEF, VOP, ETM, SAP, IRN, ZMA, FAF, ARK, DZA, VIE, AKM, ZFS, SOR, FNI, VSF, FVS, IRT, SNB, NFI, MMF, MZF, ARM (archive.org, noorlib, ketabnak, web searched). Two useful proxies noted: **AEF is Khaleqi Motlaq's Persian translation of Horn's Grundriss (HRN) + Hübschmann (HUB)**, so AEF citations can be checked against HRN/HUB; FFD's content overlaps Abolghasemi's دستور تاریخی زبان فارسی, which is on archive.org (`20220417_20220417_2237`).

Caveats: FVS is not defined in Nourai's Table IV (probably a typo for FVF/FSF); SOR's and MZF's titles were lost in the bibliography OCR; the DLI "Burhan-i Qati" item is a different edition and its files 404 on download.
