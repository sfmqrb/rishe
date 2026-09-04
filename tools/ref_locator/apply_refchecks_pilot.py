#!/usr/bin/env python3
"""Add ref_check arrays (and archived web URLs to sources) to pages 101, 126, 311, 345."""
import json, collections

VER = "/home/sfmqrb/git/rishe/data/verification/page-%d.json"

def rc(ref, status, note):
    return {"ref": ref, "status": status, "note": note}

NC = lambda ref, why: rc(ref, "not_checked", why)
NONE = lambda extra="": rc("none", "not_checked", "Nourai cites no reference for this node." + (" " + extra if extra else ""))

no_FVA = "FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi) has no digital copy (refs_online.json)."
no_SOR = "SOR (K. Akhavan Zanjani) unidentified/not online (refs_online.json)."
no_PLA = "PLA (Asbaghi, Persische Lehnwörter im Arabischen) is not online in full text (HathiTrust search-only)."
no_VDQ = "VDQ (Badreh'i's Persian translation of Jeffery) is only on noorlib's JavaScript viewer; not readable here. Its substance = FVQ."
no_MAG = "MAG (Widengren, Muhammad the Apostle of God, 1955) has no full text online."
no_KGW = "KGW (Ibrahim, Kulturgeschichtliche Wortforschung, 1991) is in copyright; Google Books preview only."
no_MON5 = "MON vol. 5 (a'lam / proper names) is not online; vajehyab/abadis carry only the lexicon volumes."
no_BQT3 = "Borhan-e Qate' (Mo'in ed.) vols 3-5 are not online in full text (only vols 1-2 on archive.org)."
no_CEL = "CEL3 is not in refs_online.json (no online copy located)."

# URLs archived with tools/fetch_source.py in this session
U_MON = lambda w: f"https://vajehyab.com/?q={w}&d=moein"
U_AHD = lambda w: f"https://ahdictionary.com/word/search.html?q={w}"
U_SEM = "https://ahdictionary.com/word/semitic.html"

KLN_BERAKAH = ("KLN_1966.txt leaf 98 (printed pp. ~160-164), s.v. 'berakah': 'Heb. berākhāh, blessing, from the stem of bērākh, "
               "he blessed, which is rel. to Aram. bārākh, Arab. bāraka, Ethiop. bārāka, he blessed, Akkad. karābu (a metathesis form), "
               "to bless, Ethiop. mekrab (metath.), temple. Cp. cherub, griffin.'")
KLN_CHERUB = ("KLN_1966.txt leaf 155 (printed pp. 274-275), s.v. 'cherub': 'Heb. kerūbh, winged angel, prob. rel. to Akkad. karābu, "
              "to bless, karibu, one who blesses, epithet of the bull-colossus, and to Heb. bērēkh, he blessed, berākhāh, blessing. "
              "See berakah and cp. griffin.'")
KLN_GRIFFIN = ("KLN_1966.txt leaf 367 (printed p. 681), s.v. 'griffin, griffon, gryphon': 'ME. griffon, fr. OF. grifoun (F. griffon), "
               "fr. Late L. gryphus ..., fr. Gk. grūps, gen. grūpos, which was prob. borrowed from the Semites through the medium of the "
               "Hittites. Cp. Heb. kerūbh, a winged angel, Akkad. karibu, epithet of the bull-colossus, lit. one who blesses, and see cherub.'")
KLN_EMERALD = ("KLN_1966.txt leaf 280 (printed pp. 514-515), s.v. 'emerald': 'ME. emeraude, fr. OF. esmeralde, esmeraude (F. émeraude), "
               "fr. L. smaragdus (whence also It. smeraldo, Sp. esmeralda), fr. Gk. smaragdos, maragdos, emerald, which is of Sem. origin. "
               "Cp. Heb. bāreqeth, Akkad. barraqtu, emerald, lit. something flashing, a derivative of Heb. bārāq, resp. Akkad. birqu, "
               "lightning, which are rel. to Aram. beraq, barqā, Arab. barq, lightning, Heb. bāraq, Aram. beraq, Arab. baraqa, Ethiop. "
               "baraqa, it flashed, glistened, Akkad. barāqu, to flash. Cp. OI. marakatam, Pers. zumurrud (whence Turk. zümrüd, whence "
               "Russ. izumrud), emerald, which are also Sem. loan words. Cp. also smaragd, which is a doublet of emerald.'")
KLN_DIXIE = ("KLN_1966.txt leaf 256 (printed pp. 468-469), s.v. 'dixie, dixy' (mess tin): 'Hind. degchī, a small kettle, fr. Pers. "
             "degcha, dimin. of deg, pot, which is rel. to Pahlavi dēg, pot, Arm. dez, heap, and to OI. dihmi, I smear, anoint, fr. I.-E. "
             "base *dheigh-, *dhoigh-, *dhigh-, to form out of clay, to knead, form. See dough and cp. next word [dizdar, fr. Pers. diz, castle].'")
KLN_LIBERAL = ("KLN_1966.txt leaf 476 (printed pp. 884-885), s.v. 'liberal': 'fr. liber, free, fr. I.-E. base *leudhero-s, whence also "
               "Gk. eleutheros, free. This base prob. meant orig. belonging to the people ... and derives fr. base *leudho-, *leudhi-, people, "
               "whence also OSlav. ljudŭ ... OE. lēod ... G. Leute ... I.-E. base *leudho-, *leudhi-, people, is a derivative of base *leudh-, "
               "to grow, rise. This latter appears in OI. rōdhati, grows, rises, climbs, Avestic raoδa-, growth, authority, Toch. A lut-k, to "
               "cause to grow. Cp. liberate, liberty, liege, livery ...'")
KLN_MAT = ("KLN_1966.txt leaf 508 (printed pp. 948-949; Nourai's 946 = previous leaf), s.v. 'mat, adj., dull': 'F., dull, lusterless, "
           "unpolished, fr. OF. mat, defeated, afflicted, depressed, dejected; dull, fr. Arab. māt in the sentence māt ash-shāh, the king has "
           "died. The word mat, orig. used only as a term of chess, gradually developed also the meanings faint, feeble, dull-colored. See "
           "checkmate and cp. matador, mate, adj.'; s.v. 'matador': 'Sp., killer, murderer, fr. matar, to kill, murder, fr. Arab. māta, he "
           "died. Cp. checkmate. Cp. also mat, dull'; s.v. 'mate, tr. v.' (checkmate): 'ME. maten, fr. OF. mater, to defeat, overcome, fr. "
           "mat, checkmated; defeated, overcome'; 'mate, n., checkmate. — ME. mat, fr. MF., fr. OF.' Same leaf.")
KLN_CHECK = ("KLN_1966.txt leaf 154 (printed pp. 272-273), s.v. 'check' (chess): '... fr. Pers. shāh, king (in the Arab.-Pers. phrase "
             "shāh māt, the king is dead) ... cp. checkmate, chess, checker, exchequer'; 'checkmate' on the same leaf ends '(cp. also It. "
             "scaccomatto). See check, a sudden stop, and cp. mate, checkmate.'")
FVQ_BARAKA = ("FVQ_pages.txt leaf 92 (Jeffery p. 75), s.v. Baraka: 'To bless. ... The primitive verb b-r-k, which is not used in the "
              "Qur'an, means to kneel, used specially of the camel, so that baraka is the technical word for making a camel kneel. In this "
              "primitive sense it is common Semitic ... It was in the N. Semitic area, however, that the root seems to have developed the "
              "sense of to bless, and from thence it passed to the S. Semitic area. Thus we have Heb. bērēk, and Phon. brk to bless; Aram. "
              "brk to bless or praise; Syr. barrek ... From this N. Semitic sense we find derived the Sab. brk, Eth. bāraka to bless, "
              "celebrate the praises of, and Ar. bāraka as above.'")
FVQ_MARJAN = ("FVQ_pages.txt leaf 278 (Jeffery p. 261), s.v. Marjān: 'Small pearls. The word occurs only in a description of Paradise, "
              "and was early recognized as borrowed from Persia, but it is certain that it did not come directly from Iranian into Arabic. "
              "We find in Phlv. murvārīt, a pearl used, e.g. in the Gōsht-i-Fryānō, ii, 13 ... From Middle Persian the word was borrowed "
              "widely, e.g. Gk. margarites; Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic. It would have "
              "come at an early date for it is used in the old poetry ...' (fn. 5: 'In spite of Addai Sher, 144, and his attempted "
              "derivation from ...'; fn. 6 cites Horn, Grundriss 218 n.).")
POK_DHEIGH = ("POK_01.txt leaves 255-256 (IEW pp. 244-245), s.v. dheiĝh-: 'Lehm kneten und damit mauern oder bestreichen (Mauer, Wall; "
              "Töpferei; dann auch von anderweitigem Bilden); auch vom Teig kneten (Bäckerei)'; dheiĝho-s, dhoiĝho-s 'Gebilde, Wall' ... "
              "'ai. dēhmi bestreiche ... dehī f. Wall, Damm, Aufwurf, av. pairi-daēzayeiti mauert ringsum ... uz-daēza- m. Aufhäufung, "
              "Wall, pairi-daēza- m. Umfriedigung (daraus gr. paradeisos), apers. didā Festung (aus *dizā-, Wurzelnom. auf -ā), npers. "
              "diz, dez ds.; ... gr. teichos n., toichos m. Mauer, Wand; ... lat. fingō ... figūra Bildung, Gestalt, Figur, fictiō ...; "
              "got. daigs m. Teig (*dhoighos), anord. deig, ags. dāg, ahd. teig ds.'")
POK_LEUDH = ("POK_02.txt leaf 345 (IEW pp. 684-685), s.v. 1. leudh-: 'emporwachsen, hochkommen; leudho-, leudhi- Nachwuchs, Volk; "
             "leudhero- zum Volk gehörig, frei. Ai. rōdhati, rōhati steigt, wächst, av. raoδaiti wächst, ... av. raoδa- m. Wuchs, Ansehen, "
             "npers. rōi Gesicht; gr. eleutheros frei aus *leudhero-s = lat. līber frei; ... got. liudan, ahd. liotan, as. liodan, ags. "
             "lēodan wachsen ... got. ludja Antlitz (vgl. np. rōi) ... ahd. liut, ags. lēod Volk, mhd. liute Leute ...'")
POK_MAD = ("POK_02.txt leaf 355 (IEW pp. 694-695), s.v. mad-: 'naß, triefen; auch von Fett triefen, vollsaftig, fett, gemästet' ... "
           "'lat. madeō, -ēre naß sein, von Nässe triefen, reifen, voll sein, mattus trunken (*madi-to-s)'.")
AHD_DHEIGH = ("AHD_watkins1985.txt line 377 s.v. dheigh-: 'To form, build. 1. Germanic *daigjōn in Old English dǣge, bread kneader: "
              "DAIRY. 2. Germanic *-dig- in Old English compound hlǣfdige, mistress of a household (< bread kneader; hlāf, bread, loaf): "
              "LADY. 3. Extended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dāg, dough: DOUGH ... 4. Suffixed zero-grade "
              "form *dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE ... 5. Nasalized zero-grade form *dhi-n-gh- in "
              "Latin fingere, to shape: FEIGN, FICTION, FIGMENT; EFFIGY ... 7. Suffixed o-grade form *dhoigh-o- in Avestan daēza-, wall "
              "(originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.]' (same list online at "
              "ahdictionary.com/word/indoeurop.html#dheigh-).")
AHD_PARADISE = ("AHD online (archived) s.v. paradise: '[Middle English paradis, from Old French, from Late Latin paradīsus, from Greek "
                "paradeisos, garden, enclosed park, paradise, from Avestan pairidaēza-, enclosure, park : pairi-, around; see per1 ... + "
                "daēza-, wall; see dheigh- ...]'. Nourai's AHD:950 is the 1976 page of this same entry.")
AHD_MARGAR = ("AHD_watkins1985.txt line 725: '[margarītēs. Pearl. Greek noun of Oriental origin (probably immediately from Iranian). "
              "Greek margarītēs, margaron, pearl: MARGARIC, MARGARIC ACID, (MARGARINE), MARGARITE1, MARGARITE2.]' Online AHD s.v. "
              "margarite (archived): 'Ultimately from Greek margarītēs, pearl, perhaps of Iranian origin; perhaps akin to Avestan "
              "mərəγa-, bird'.")
HRN_DIVAR = ("HRN.txt leaf 154 (Horn p. 133), No. 599: 'dīvār Mauer, Wand. ap. *deghavāra- (vergl. gr. teichos, osk. feíhúss). "
             "Nöldeke (mündliche Mitteilung), unter der Voraussetzung, dass die np. Grundform *dēvār lautete ...; kurd. LW. dīwār; "
             "wax. LW. dival, sar. delvūl Mauer, Wand, Umwallung.' Cf. No. 563 (leaf 146, p. 125): 'diz, dez Burg ... ap. didā Festung; "
             "aw. daēza-; phlv. d(i)z ... Ascoli's Erklärung von np. dīvār Mauer aus ap. *didavara- Stadtwall ist daher nicht "
             "wahrscheinlich'.")
HUB_DEG = ("HUB.txt leaf 75 (Hübschmann p. 65), No. 594: 'Wenn dēz, dēza Kochtopf zu got. deigan kneten, aus Thon formen (Wzl. "
           "dheigh) gehört, ist es verwandt mit Nr. 563 diz, dēz Burg. Ob auch dēg Kochtopf dazu gehört, ist fraglich, da 1) idg. dhigh "
           "durch skr. dēgdhi, digdha- nicht gesichert ist und 2) idg. dhoigho- im Neup. zu *dēy werden müsste. Np. dēg (afgh. LW. dēg "
           "Kessel) setzt ap. *daika- voraus. Phl. dēg Kessel (Gl. and Ind. 288) kann eine junge Form sein.' No. 599 (same page): "
           "'Besser *daidavara- (Festungsmauer) als *daigavara- anzusetzen ... Falls dīvār (mit ī) die ursprüngliche Form ist ..., wäre "
           "dīvār über *diyvār = *did-vār auf ap. *dida-vara- zurückzuführen. Alles unsicher.'")
KNT_DIDA = ("KNT.txt leaf 214 (Kent p. 191): 'didā- sb. wall, stronghold, fortress: NPers. diz, pIE *dhiĝhā-, cf. Skt. dehī- wall, "
            "Gk. teichos, NEng. dike, ditch ... Cf. also paradayadām. didā nsf. DB 1.58; 2.39, 44; 3.61, 72; DSe 46; DSf 42. didām asf. "
            "DB 2.78; DSe 48; DSf 54.'")
IEC_DHEIGH = ("IEC.txt leaf 112 (Mann cols ~193-194), s.v. dheigh-: 'shape, earth up; form, wall ... Cf. dhoigh- Skt. dehah "
              "shape, body; Av. (pairi-)daēzō surrounding fence beside diz- earth up, cover; LW in Arm. dez mound, dizem pile up; Gk. "
              "teikhos outer wall, dam; Osc. feíhúss, acc.pl. walls; Go. digan (z-gde) shape, mould ... For Cz. díže kneading-trough and "
              "OHG teic, E dough, etc. see dhoiĝh-.'")
SOD_DYZ = ("SOD_pages.txt leaf 216 (Gharib p. 151), entry 3825: 'δyz' M — δiza (dyz') < OP didā, f. n., stronghold, fort. BBB f 57; "
           "STii 3.27'; entry 3826 'dyz' C = δyz''.")
SOD_RWD = ("SOD_pages.txt leaf 411 (Gharib p. 344), entry 8562: 'rwδ- B, M, S — rōδ < Av. raod-; *fraud-; Parth. rōd-; Khot. rw-; "
           "Yaghn. ur-; inf. -y; (to) grow. BBB 580; GMS 586; TSP 2.10, 18 ...'; entry 8563 'rwd C = rwδ-'.")
SYN_874 = ("SYN.txt leaf 946 (Buck p. 875; leaf 945 = p. 874), in 12.51 FORM/SHAPE (OCR garbled): '... OS liodan spring up, grow, "
           "Skt. rudh-, Av. raod- grow (12.53). Walde-P. 2.416. Feist 323.' Buck lists the Avestan word only as 'grow'; the 'face' "
           "gloss and the raoδa-taxma compound are not on this page.")
BQT_DEZ = ("BQT_v2_pages.txt leaf 311 (printed p. ~854; Nourai 851): 'دژ = بکسر اول و سکون ثانی، قلعه و حصار باشد' with footnote "
           "marker ۱; Mo'in's footnote (Pahlavi/Avestan forms) is not legible in the OCR of this leaf.")
BQT_DIG = ("BQT_v2_pages.txt leaves 371-372 (printed pp. ~914-915): the دیگ entry area; leaf 371 footnote cites 'Henning, Two "
           "Central Asian words, Hertford 1946' and leaf 372 mentions «دیگه» and دیزی (فرهنگ اسدی); Mo'in's Latin-script Pahlavi/Old "
           "Persian forms are not legible in the OCR.")
BQT_PALIZ = ("BQT_v1_pages.txt leaf 581 (printed p. ~361; Nourai 359): 'پالیز ۱ - بر وزن کاریز، بمعنی باغ و بوستان و کشتزار باشد "
             "عموماً و خربزه‌زار و خیارزار و هندوانه‌زار را گویند خصوصاً'; Mo'in's etymological footnote ۱ is not legible in the OCR.")
BQT_RAZ = ("BQT_v2_pages.txt leaf 404 (printed p. ~947; Nourai 944): 'رز = بفتح اول و سکون ثانی، درخت انگور باشد و به عربی کرم خوانند "
           "... و باغ را گویند و بمعنی انگور هم آمده است'; Mo'in's footnote on this leaf is illegible (only a Henning BSOS reference "
           "survives), so the claimed link to rūy/rustan cannot be confirmed here.")
BQT_ROSTAM = ("BQT_v2_pages.txt leaf 408 (printed p. ~951), Mo'in's footnote s.v. رستم: 'رستم = رستهم: رو (بالش، نمو) [رستن و "
              "روییدن از همین ریشه است] + تهم = tahm در پارسی باستان، گاتها و دیگر بخشهای اوستا بمعنی دلیر و پهلوان؛ تهمتن نیز از "
              "همین ریشه است بمعنی بزرگ‌پیکر و قوی‌اندام ... رستم یعنی کشیده‌بالا و بزرگ‌تن و قوی‌پیکر (یشتها ۲ ص ۱۳۹) ... مارکوارت "
              "تصور کرده است که رئوتس‌تخم (اوستا) عنوان و صفتی برای ... ' — i.e. Mo'in derives Rostam from rō 'growth' + tahm "
              "'strong', exactly Nourai's raoδa-taxma.")
FSF_RAZ = ("FSF_pages.txt leaf 265 (page numeral illegible; Nourai p. 199), s.v. 'رز (با زبر اول): ۱- باغ. ۲- انگور: چو ببرید رستم "
           "تن شاخ گز / بیامد ز دریا به ایوان و رز'. A Shahnameh glossary: confirms the word and glosses (garden, vine), gives no etymology.")
AFM_RAWNAQ = ("AFM_pages.txt leaf 75 (Addi Shir p. ~74): '(الرونق) حسن كل شيء، معرب رو أي وجه ومن نيك أي صبيح' — i.e. rawnaq is an "
              "Arabicized compound of Persian rū 'face' + nīk 'fair', exactly Nourai's arrow.")
AFM_RAWDA = ("AFM_pages.txt leaf 76 (Addi Shir p. ~75): '(الروضة) من الرمل والعشب مستنقع الماء ... وهي من ريختن أي صبّ، أخذتها العرب "
             "وتصرفت بها' — Addi Shir derives rawḍa from Persian rīxtan 'to pour', not from raz.")
FSD_MAT = ("FSD_vol3.txt leaf 51 (printed p. ~1517; Nourai 1526), s.v. mat (dull surface) — OCR badly garbled, but the etymology "
           "bracket reads '[< F. mat(t), dull, < L. mattus; see MATE2]'. Funk & Wagnalls thus takes French mat from Latin mattus and "
           "refers the reader to the checkmate word (mate2) for the Arabic origin.")
FSD_526 = ("FSD_vol1.txt: printed p. 526 (leaf ~575) is in the C's ('coerce' etc.) and has no 'mat'; the checkmate entry is at p. 457 "
           "(leaf 511): 'check'mate, v. ... Chess. To put (an opponent's king) in a check from which no escape is possible ... 2. Hence, to "
           "discomfit or defeat'. Nourai's 526 is probably a misprint for 1526 (vol. 3, the mat entry).")
PHN_MAT = ("PHN.txt leaf 288 (Pihan p. 257): 'MAT, adj. m. (p.) [māt] défait, réduit à l'extrémité. — Faire mat ou mater veut dire, au "
           "jeu d'échecs, mettre le roi dans l'impossibilité de changer de place, ce qui termine la partie. Voyez Échec. — Par extension, "
           "le verbe mater s'emploie aussi au figuré, dans le sens de dompter, humilier, affaiblir, abattre'. Pihan tags the word '(p.)' "
           "= Persian.")
DEV_MAT = ("DEV.txt leaf 192 (Devic p. 159): 'Mat. Terme du jeu des échecs. (Voy. Échec.) Mat, adjectif, au sens de terne, vient du "
           "mat des échecs. « Dans les anciens auteurs, dit M. Littré, mat signifie las, humilié; c'est de ce sens qu'on est allé au sens "
           "de terne, qui paraît très-récent. » ... Il est remarquable qu'en hindoustani le terme māt, importé du persan, a aussi les "
           "deux sens'.")
LKT_MAT = ("LKT.txt leaf 142 (Lokotsch p. 115), No. 1443: 'Ar. māt(a): Er ist gestorben, tot; als Fachausdruck der Schachspieler šāh "
           "māt vom pers. šāh König [Horn NpEt S. 170, Nr. 772]: Der König ist tot; hieraus ist mit dem Schachspiele selbst der Ausdruck "
           "international geworden, vor allem it. scacco matto schachmatt, prov. mat, frz. échec et mat, sp. jaque y mate ..., pg. "
           "chaque e mate, rum. mat; dtsch. schachmatt, engl. checkmate ... Dazu die Vb. it. mattare, frz. mater, prov. kat. sp. pg. "
           "matar mattsetzen, überwinden, besiegen und schließlich sp. pg. matar töten [und nicht etwa < lat. mactare ...]'.")
SKT_EMERALD = ("SKT.txt leaf 156 (Skeat 1911 p. ~136; Nourai's 163 is another printing), s.v. Emerald: '(F. — L. — Gk.) M.E. emeraude "
               "— O.F. esmeraude — L. smaragdum, acc. of smaragdus — Gk. smaragdos, an emerald. Cf. Skt. marakata (the same).'")
MON_ZOMORROD = ("vajehyab.com (Mo'in) s.v. زمرد: '(زُ مُ رُّ) [معر - یو.] (اِ.) یکی از سنگ های قیمتی به رنگ سبز' — Mo'in tags it "
                "'Arabicized, from Greek' (page numbers of the print edition cannot be mapped online).")

def add_sources(node, urls):
    for u in urls:
        if u not in node["sources"]:
            node["sources"].append(u)

# ------------------------------------------------------------------ page 101
P101 = {
    (0, "root"): [
        rc("FVQ:75", "supports", FVQ_BARAKA + " — exactly Nourai's 'kneel (of the camel) → bless' story."),
    ],
    (0, 1): [
        rc("KLN:164", "supports", KLN_BERAKAH + " Gives Arab. bāraka 'he blessed' under the Semitic root and the Akkadian metathesis, as the chart does."),
        rc("FVQ:75", "supports", "Same page as the root: 'Ar. bāraka as above' derived from the N. Semitic sense 'to bless' (FVQ_pages.txt leaf 92)."),
    ],
    (0, 2): [NC("FVA:45", no_FVA)],
    (0, 3): [
        rc("KLN:164", "supports", KLN_BERAKAH + " Klein calls Akkad. karābu 'a metathesis form' of b-r-k — Nourai's 'letters are interchanged'."),
        rc("AHD:579", "partial", "AHD:579 is the 1976 dictionary page (griffin); the current AHD griffin entry (archived, " + U_AHD("griffin") + ") derives griffin only 'from Greek grūps' with no Semitic link, but the AHD Semitic-roots appendix (archived, " + U_SEM + ") s.v. krb: 'Common Semitic root, with West Semitic metathesized variant brk. cherub, from Hebrew kərûb, cherub; akin to Akkadian karābu, to praise, bless. Compare also brk' and s.v. brk: 'West Semitic, to bless. Probably a metathesized variant of krb.' — so AHD supports the Akkadian karābu ~ brk metathesis."),
    ],
    (0, 4): [
        rc("KLN:274", "supports", KLN_CHERUB + " Klein connects kerūbh with Heb. bērēkh/berākhāh via Akkad. karābu, i.e. the reversed consonants Nourai notes."),
        rc("KLN:164", "supports", KLN_BERAKAH),
    ],
    (0, 5): [
        rc("MON:2958", "supports", "vajehyab.com (Mo'in) s.v. کروبی: '(کَ یّ) [ع.] (اِ.) فرشتة مقرب درگاه. ج. کروبیون' — tagged Arabic; Mo'in's page numbers cannot be mapped online. Archived " + U_MON("کروبی") + "."),
    ],
    (0, 6): [
        rc("MON:2958", "supports", "vajehyab.com (Mo'in) s.v. کروبی [ع.] 'فرشتة مقرب درگاه، ج. کروبیون'; also کروبیان 'فرشتگان مقرب درگاه' and کروبیون 'جِ کروبی' — the Persian word is marked as an Arabic loan, as the arrow says (archived " + U_MON("کروبی") + ")."),
    ],
    (0, 7): [
        rc("AHD:231", "supports", "AHD online s.v. cherub (archived, " + U_AHD("cherub") + "): '[Middle English, from Late Latin, from Hebrew kərûb; see krb in the Appendix of Semitic roots.]' — Hebrew → (Latin →) English as in the chart; AHD:231 is the 1976 page of this entry."),
    ],
    (0, 8): [
        rc("KLN:680", "supports", KLN_GRIFFIN + " — Klein does derive Gk. grūps from the Semitic kerūbh/karibu word (via Hittite), Nourai's arrow."),
        rc("AHD:579", "partial", "AHD online s.v. griffin (archived, " + U_AHD("griffin") + "): '[Middle English griffoun, from Old French griffon, from grif, from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps.]' — the chain below Greek is there, but AHD does not derive Greek grūps from Hebrew kerūbh; the Semitic appendix s.v. krb lists only cherub."),
    ],
    (0, 9): [
        rc("AHD:579", "supports", "AHD online s.v. griffin (archived, " + U_AHD("griffin") + "): 'from Latin grȳpus, grȳphus, variants of grȳps, grȳp-, from Greek grūps' — Latin gryphus from Greek."),
    ],
    (0, 10): [
        rc("KLN:680", "supports", KLN_GRIFFIN + " Klein: 'ME. griffon, fr. OF. grifoun (F. griffon), fr. Late L. gryphus' — OF from Latin; the OF spelling grifion in the chart is Nourai's/OCR's."),
    ],
    (0, 11): [
        rc("AHD:579", "supports", "AHD online s.v. griffin (archived, " + U_AHD("griffin") + "): '[Middle English griffoun, from Old French griffon ...]' — English from Old French."),
    ],
    (1, "root"): [
        rc("KLN:514", "supports", KLN_EMERALD + " Klein gives the whole Semitic b-r-q 'flash, lightning' family under 'emerald'."),
    ],
    (1, 1): [
        rc("KLN:514", "supports", KLN_EMERALD + " Lists 'Arab. barq, lightning ... Arab. baraqa, it flashed, glistened'."),
    ],
    (1, 2): [NC("FVA:45", no_FVA), NC("SOR:35", no_SOR)],
    (1, 3): [
        rc("KLN:514", "partial", KLN_EMERALD + " Klein has Akkad. barraqtu but glosses it 'emerald, lit. something flashing' (a derivative of Akkad. birqu 'lightning'); Nourai's gloss 'lightning' belongs to birqu, not to baraqtu."),
    ],
    (1, 4): [
        rc("KLN:514", "supports", KLN_EMERALD + " 'Gk. smaragdos, maragdos, emerald, which is of Sem. origin. Cp. Heb. bāreqeth, Akkad. barraqtu' — the Greek form in Klein is smaragdos (with -gd-), which confirms that the chart's 'smaraldos' is a transcription slip."),
    ],
    (1, 5): [
        rc("MON:1746", "supports", MON_ZOMORROD + " Mo'in's tag [معر - یو.] = Arabicized (mu'arrab) from Greek, i.e. Greek → Arabic → Persian, which is the route drawn through this empty Arabic node. Archived " + U_MON("زمرد") + "."),
    ],
    (1, 6): [
        rc("MON:1746", "supports", MON_ZOMORROD + " Archived " + U_MON("زمرد") + "."),
        rc("KLN:514", "partial", KLN_EMERALD + " Klein: 'Cp. OI. marakatam, Pers. zumurrud (whence Turk. zümrüd, whence Russ. izumrud), emerald, which are also Sem. loan words' — Klein treats zumurrud as a direct Semitic loan and does not route it through Greek/Arabic as Nourai does."),
    ],
    (1, 7): [
        rc("KLN:514", "supports", KLN_EMERALD + " 'fr. L. smaragdus ..., fr. Gk. smaragdos'."),
    ],
    (1, 8): [
        rc("AHD:427", "partial", "AHD:427 is the 1976 page of 'emerald'; the current AHD emerald entry (archived, " + U_AHD("emerald") + ") reads '[Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos; akin to Sanskrit marakatam, probably of Semitic origin; akin to Akkadian barraqtu and Hebrew bāreqet, a kind of gemstone ...; see brq in the Appendix of Semitic roots.]' — it confirms Latin smaragdus < Greek but does not treat smaragdite (the AHD search for smaragdite, archived " + U_AHD("smaragdite") + ", returned no entry). Klein (KLN_1966.txt leaf 280-281 s.v. smaragdite): 'F., formed with subst. suff. -ite fr. Gk. smaragdos, emerald'."),
    ],
    (1, 9): [
        rc("KLN:514", "supports", KLN_EMERALD + " 'ME. emeraude, fr. OF. esmeralde, esmeraude (F. émeraude), fr. L. smaragdus'."),
    ],
    (1, 10): [
        rc("AHD:427", "supports", "AHD online s.v. emerald (archived, " + U_AHD("emerald") + "): 'Middle English emeraude, from Old French, from Medieval Latin esmeralda, esmeraldus, from Latin smaragdus, from Greek smaragdos ... probably of Semitic origin; akin to Akkadian barraqtu and Hebrew bāreqet' — the whole chain of this branch, including the Semitic b-r-q root."),
    ],
    (1, 11): [
        rc("KLN:514", "supports", KLN_EMERALD + " 'Cp. OI. marakatam ... which are also Sem. loan words' — Klein makes Skt. marakata a Semitic loan, as the arrow says."),
        rc("SKT:163", "partial", SKT_EMERALD + " Skeat only compares Skt. marakata with the Greek word; he does not say it is a Semitic loan."),
    ],
}

# ------------------------------------------------------------------ page 126
P126 = {
    (0, "root"): [
        rc("POK:244", "supports", POK_DHEIGH),
        rc("KNT:191", "supports", KNT_DIDA + " Kent puts OP didā- under pIE *dhiĝhā- with Skt. dehī-, Gk. teichos."),
        NC("CEL3:203", no_CEL),
    ],
    (0, 1): [
        rc("HRN:133", "supports", HRN_DIVAR + " Nourai's 'děğa-vâra' is Horn's *deghavāra-; his 'didâ' is Horn's/Kent's ap. didā. (Horn himself, No. 563, rejects deriving dīvār from *dida-vara-.)"),
        rc("KNT:191", "supports", KNT_DIDA),
        rc("IEC:191", "partial", IEC_DHEIGH + " Mann gives the root and Av. (pairi-)daēza- but does not list Old Persian didā- or *daiga-vāra-."),
    ],
    (0, 2): [
        rc("BQT:918", "not_found", "BQT_v2_pages.txt leaves 375-378 (printed pp. ~918-921) are the دیو- entries, but the دیوار headword and Mo'in's footnote are not recoverable from the OCR (only the following entry 'دیوال = با لام، بر وزن و معنی دیوار است، چه در فارسی را و لام بهم تبدیل می‌یابند' on leaf 378 is legible). Mo'in's online text (vajehyab) tags دیوار [په.] = Pahlavi (refs_online.json note)."),
    ],
    (0, 3): [
        rc("SOD:151", "supports", SOD_DYZ + " Gharib derives Sogdian δyz' 'stronghold, fort' from OP didā — exactly the arrow drawn from node #1."),
    ],
    (0, 4): [
        rc("POK:244", "supports", POK_DHEIGH + " Pokorny: 'uz-daēza- m. Aufhäufung, Wall, pairi-daēza- m. Umfriedigung' under dheiĝh-."),
    ],
    (0, 5): [
        rc("BQT:851", "partial", BQT_DEZ),
        NC("MON5:528", no_MON5),
    ],
    (0, 6): [
        rc("POK:244", "supports", POK_DHEIGH + " 'pairi-daēza- m. Umfriedigung (daraus gr. paradeisos)'."),
    ],
    (0, 7): [
        rc("BQT:359", "partial", BQT_PALIZ + " The gloss (garden, melon field) matches; the derivation from pairi-daēza- is in Mo'in's note, which the OCR does not preserve."),
        rc("MON:680", "partial", "vajehyab.com (Mo'in) s.v. پالیز: '(اِ.) ۱- باغ، بوستان. ۲- کشتزار. ۳- زمینی که در آن خربزه، خیار و مانند آن بکارند' — meaning confirmed; the online text carries no origin tag or Avestan form for this entry. Archived " + U_MON("پالیز") + "."),
    ],
    (0, 8): [NC("BQT:1455", no_BQT3)],
    (0, 9): [
        rc("AHD:950", "supports", AHD_PARADISE),
    ],
    (0, 10): [NONE("The AHD paradise entry checked at node #9 (archived " + U_AHD("paradise") + ") gives 'Middle English paradis, from Old French, from Late Latin paradīsus, from Greek paradeisos'.")],
    (0, 11): [
        rc("HUB:65", "partial", HUB_DEG + " Hübschmann does posit ap. *daika- for np. dēg (Nourai's 'daika'), but he explicitly doubts that dēg belongs to the root dheigh- ('ist fraglich')."),
        rc("KLN:469", "supports", KLN_DIXIE + " Klein derives Pers. deg 'pot' (Pahlavi dēg) from I.-E. *dheigh- 'to form out of clay' — the arrow from the root; he does not give an Old Persian form."),
    ],
    (0, 12): [
        rc("BQT:912,914", "partial", BQT_DIG),
        rc("KLN:469", "supports", KLN_DIXIE),
    ],
    (0, 13): [
        rc("AHD", "supports", AHD_DHEIGH + " Germanic *daigaz 'dough' and OE dǣge 'bread kneader' (DAIRY), hlǣfdige (LADY) are items 1-3."),
    ],
    (0, 14): [NONE("Covered by the AHD dheigh- entry checked at node #13: DAIRY, LADY, DOUGH.")],
    (0, 15): [
        rc("AHD", "supports", AHD_DHEIGH + " Item 4: '*dhigh-ūrā, in Latin figūra, form, shape (< result of kneading): FIGURE'."),
    ],
    (0, 16): [NONE("Covered by the AHD dheigh- entry checked at node #15: FIGURE; FICTION (item 5, Latin fingere).")],
}

# ------------------------------------------------------------------ page 311
P311 = {
    (0, "root"): [
        rc("POK:684", "supports", POK_LEUDH + " Pokorny's 1. leudh- 'emporwachsen' with av. raoδa- 'Wuchs' and npers. rōi 'Gesicht' is the root Nourai draws (his second name 'Rei' is not in Pokorny under this root)."),
        rc("KLN:885", "supports", KLN_LIBERAL),
        rc("SYN:874", "partial", SYN_874),
        NC("VDQ:39", no_VDQ),
    ],
    (0, 1): [
        rc("KLN:885", "supports", KLN_LIBERAL + " 'Avestic raoδa-, growth, authority' under base *leudh- 'to grow, rise'."),
        rc("SYN:874", "partial", SYN_874),
    ],
    (0, 2): [
        rc("BQT:944", "partial", "The روییدن/روی entries (BQT_v2_pages.txt leaves ~400-403, printed pp. ~944-946) are not legible in the OCR; but Mo'in's footnote s.v. رستم (leaf 408) states 'رو (بالش، نمو) [رستن و روییدن از همین ریشه است]', i.e. rūyīdan and rustan come from rō 'growth'. Pokorny 684 (checked at the root) gives 'npers. rōi Gesicht' under leudh-, the 'face' word of this node."),
    ],
    (0, 3): [
        rc("BQT:944", "partial", BQT_RAZ),
        rc("FSF:199", "partial", FSF_RAZ),
    ],
    (0, 4): [
        NC("PLA:138", no_PLA),
        rc("AFM:75", "contradicts", AFM_RAWDA + " Cited by Nourai only in his NOTE as the dissenting view; it does not support the arrow raz → rawḍa."),
    ],
    (0, 5): [
        rc("MON", "supports", "vajehyab.com (Mo'in) s.v. روضه: '(رَ ض) [ع. روضة] (اِ.) ۱- باغ، گلزار. ج. ریاض، روضات. ۲- مطالب و اشعاری که هنگام عزا ... می‌خوانند' — Persian rowzeh marked as Arabic rawḍa, as the arrow says. Archived " + U_MON("روضه") + "."),
    ],
    (0, 6): [NONE("Addi Shir's rawnaq entry checked at node #7 presupposes Persian rū + nīk.")],
    (0, 7): [
        rc("AFM:74", "supports", AFM_RAWNAQ),
    ],
    (0, 8): [
        rc("MON:1694", "supports", "vajehyab.com (Mo'in) s.v. رونق: '(رُ نَ) [ع.] (اِمص.) ۱- فروغ، روشنایی. ۲- زیبایی، جمال. ۳- رواج' — tagged Arabic. Archived " + U_MON("رونق") + "."),
    ],
    (0, 9): [
        rc("MON:1689", "partial", "vajehyab.com (Mo'in) s.v. روستا: '(اِ.) ده، قریه' — the online Mo'in text gives the meaning only; the print edition's Pahlavi form (rōstāk) is stripped online, so the Pahlavi → Persian arrow cannot be confirmed from it. Archived " + U_MON("روستا") + "."),
    ],
    (0, 10): [
        rc("IEC:1103", "not_found", "IEC.txt leaves 604-607 (Mann cols ~1097-1104) contain the roudh-/rudh- 'red, rust' entries; no rōstāk/rūstā 'village' is there. Mann does list 'Per. cf. rustan, rostan, inf. grow; rust, rost growth' under ordhos (1) 'erect; growth; grow, rise' (IEC.txt line 12277), i.e. under a different root."),
        rc("MON:1689", "partial", "vajehyab.com (Mo'in) s.v. روستا: 'ده، قریه' — meaning only, no origin tag online. Archived " + U_MON("روستا") + "."),
    ],
    (0, 11): [
        rc("KLN:885", "partial", KLN_LIBERAL + " Klein has Avestic raoδa- 'growth' but not the compound raoδa-taxma / Rostam."),
        rc("SYN:874", "partial", SYN_874),
    ],
    (0, 12): [
        rc("BQT", "supports", BQT_ROSTAM),
    ],
    (0, 13): [NC("VDQ:39", no_VDQ), NC("MAG:186", no_MAG)],
    (0, 14): [NC("MAG:186", no_MAG), NC("VDQ:39", no_VDQ)],
    (0, 15): [NC("VDQ:39", no_VDQ), NC("MAG:186", no_MAG)],
    (0, 16): [
        rc("MON:1378", "supports", "vajehyab.com (Mo'in) s.v. حور: '[ع.] (اِ.) ۱- زن سیاه چشم. ۲- زن زیباروی'; حوری '[ع - فا.] زن بهشتی' — Persian ḥūr marked as Arabic. Archived " + U_MON("حور") + "."),
    ],
    (0, 17): [
        rc("SOD:344", "supports", SOD_RWD + " Gharib derives Sogdian rwδ- 'to grow' from Av. raod-, the root of this chart."),
    ],
    (0, 18): [
        rc("KLN:885", "supports", KLN_LIBERAL + " '*leudhero-s ... derives fr. base *leudho-, *leudhi-, people ... a derivative of base *leudh-, to grow, rise' — both of Nourai's forms."),
    ],
    (0, 19): [NONE("Klein s.v. liberal (checked at #18): 'fr. liber, free, fr. I.-E. base *leudhero-s'; Pokorny 684 (root): 'gr. eleutheros frei aus *leudhero-s = lat. līber frei'.")],
    (0, 20): [NONE("Klein (KLN_1966.txt leaf 231, s.v. deliver): 'OF. delivrer ... fr. VL. dēlīberāre, fr. de- and līberāre, to set free, fr. līber, free'; Klein s.v. Latvia (leaf 467): 'the country of the Letts', which he does not connect with *leudh-.")],
}

# ------------------------------------------------------------------ page 345
P345 = {
    (0, "root"): [
        NC("PLA:247", no_PLA),
        rc("FVQ:261", "supports", FVQ_MARJAN + " Jeffery's Phlv. murvārīt is Nourai's root form."),
    ],
    (0, 1): [
        NC("BQT:1997", no_BQT3 + " (BQT:1997 would be vol. 4)."),
        rc("FVQ:261", "supports", FVQ_MARJAN + " (Persian morvārīd is the NP continuation of the Phlv. murvārīt Jeffery quotes; fn. 6 cites Horn, Grundriss 218 n.)"),
        NC("KGW:112", no_KGW),
    ],
    (0, 2): [
        rc("FVQ:261", "supports", FVQ_MARJAN + " 'From Middle Persian the word was borrowed widely, e.g. ... Aram. margānītā; Syr. margānītā, and from some Aram. form it came into Arabic' — the Aramaic intermediary of this empty node."),
    ],
    (0, 3): [
        rc("FVQ:261", "supports", FVQ_MARJAN + " Arabic marjān 'small pearls' from an Aramaic form of the Middle Persian word."),
        NC("PLA:247", no_PLA),
    ],
    (0, 4): [NC("BQT:1981", no_BQT3 + " (BQT:1981 would be vol. 4).")],
    (0, 5): [
        rc("AHD:1527", "supports", AHD_MARGAR + " AHD:1527 is the 1976 appendix page of this same entry."),
        NC("KGW:111", no_KGW),
        rc("FVQ:261", "supports", FVQ_MARJAN + " 'From Middle Persian the word was borrowed widely, e.g. Gk. margarites' (fn. 7: 'Also margaris ..., from which comes the Arm. margarit and the European forms')."),
    ],
    (0, 6): [NONE("Klein (KLN_1966.txt leaf 504, s.v. margarite): 'ME., fr. OF. margarite (F. marguerite), fr. L. margarita, fr. Gk. margarites'.")],
    (0, 7): [NONE("Klein (KLN_1966.txt leaf 504, s.v. margarite/Margaret): 'OF. margarite (F. marguerite), fr. L. margarita'; 'Margaret ... OF. Margaret, fr. L. margarita, pearl'.")],
    (0, 8): [NONE("AHD_watkins1985.txt line 725 lists MARGARIC, MARGARINE, MARGARITE under margarītēs; Klein (leaf 504) s.v. Margaret 'fr. L. margarita, pearl' and s.v. margarine 'F.; ... fr. margarique ... fr. Gk. margaron, pearl'.")],
    (2, "root"): [
        NC("FVA:384", no_FVA),
        rc("KLN:946", "supports", KLN_MAT + " Klein derives mat, matador, mate (checkmate) from Arab. māt/māta 'he died'."),
    ],
    (2, 1): [NC("FVA:387", no_FVA)],
    (2, 2): [
        NC("FVA:387", no_FVA),
        rc("MON:3678,4421", "supports", "vajehyab.com (Mo'in) s.v. موت: '(مَ) [ع.] (اِ.) مرگ' (tagged Arabic; archived " + U_MON("موت") + "); s.v. مات: '(ص.) ۱- حیران، سرگشته. ۲- (اِ.) وضعیتی در بازی شطرنج که شاه قادر به هیچ حرکتی نیست و بازی به اتمام می‌رسد' and 'شاه مات: هنگامی که شاه شطرنج مات شود' (no origin tag shown online; archived " + U_MON("مات") + ")."),
    ],
    (2, 3): [
        rc("FSD:1526", "partial", FSD_MAT + " It gives Latin mattus as the source of French mat, but does not itself derive mattus from Arabic māt."),
        rc("POK:694", "contradicts", POK_MAD + " Pokorny derives Latin mattus 'drunk' from *madi-to-s (root mad- 'wet'), not from Arabic — the dissent Nourai records in his NOTE."),
    ],
    (2, 4): [
        rc("FSD:1526", "supports", FSD_MAT + " French mat 'dull' from Latin mattus, as the arrow says."),
    ],
    (2, 5): [
        rc("FSD:526", "not_found", FSD_526),
        rc("AHD:805", "contradicts", "AHD online s.v. mat 2 (archived, " + U_AHD("mat") + "): '[From French, dull, from Old French, defeated, withered, perhaps from Latin mattus, stupefied, senseless, possibly from *maditus, past participle of madēre, to be wet.]' — English mat from French mat is confirmed, but AHD traces the word to Latin madēre (root mad-), not to Arabic māt; Nourai's NOTE acknowledges this. (AHD s.v. matte 2, archived " + U_AHD("matte") + ": 'from Old French, dull, from Latin mattus, stupefied; see MAT2'.)"),
    ],
    (2, 6): [
        rc("PHN:257", "supports", PHN_MAT),
        rc("DEV:159", "supports", DEV_MAT),
    ],
    (2, 7): [
        rc("LKT:115", "supports", LKT_MAT),
        rc("KLN:946", "supports", KLN_MAT + " Also KLN s.v. check (" + KLN_CHECK + ")."),
    ],
    (2, 8): [
        rc("KLN:946", "supports", KLN_MAT + " 'matador ... fr. matar, to kill, murder, fr. Arab. māta, he died' — Nourai's arrow. (AHD s.v. matador, archived " + U_AHD("matador") + ", prefers 'possibly from Vulgar Latin *mattāre, to beat senseless, perhaps from Latin mattus'; Lokotsch 1443 sides with Klein: 'sp. pg. matar töten' from the chess word.)"),
    ],
    (2, 9): [
        rc("MON:3678", "supports", "vajehyab.com (Mo'in) s.v. ماتادور: '(دُ) [فر.] (اِ.) کسی که در میدان عمومی با گاو مبارزه می‌کند، گاوباز' — Mo'in marks the Persian word as a French loan, i.e. the French node is the immediate source. Archived " + U_MON("ماتادور") + "."),
    ],
    (2, 10): [
        rc("MON:3678", "supports", "vajehyab.com (Mo'in) s.v. ماتادور [فر.] 'گاوباز' — French → Persian as drawn. Archived " + U_MON("ماتادور") + "."),
    ],
    (2, 11): [
        rc("KLN:946", "supports", KLN_MAT + " 'matador, n. ... Sp., killer, murderer' — English from Spanish."),
    ],
}

# web URLs to append to sources, per (page, entry, node)
WEB = {
    (101, 0, 3): [U_AHD("griffin"), U_SEM],
    (101, 0, 5): [U_MON("کروبی")],
    (101, 0, 6): [U_MON("کروبی")],
    (101, 0, 7): [U_AHD("cherub")],
    (101, 0, 8): [U_AHD("griffin")],
    (101, 0, 9): [U_AHD("griffin")],
    (101, 0, 11): [U_AHD("griffin")],
    (101, 1, 5): [U_MON("زمرد")],
    (101, 1, 6): [U_MON("زمرد")],
    (101, 1, 8): [U_AHD("emerald"), U_AHD("smaragdite")],
    (101, 1, 10): [U_AHD("emerald")],
    (126, 0, 7): [U_MON("پالیز")],
    (126, 0, 9): [U_AHD("paradise")],
    (126, 0, 10): [U_AHD("paradise")],
    (311, 0, 5): [U_MON("روضه")],
    (311, 0, 8): [U_MON("رونق")],
    (311, 0, 9): [U_MON("روستا")],
    (311, 0, 10): [U_MON("روستا")],
    (311, 0, 16): [U_MON("حور")],
    (345, 2, 2): [U_MON("موت"), U_MON("مات")],
    (345, 2, 5): [U_AHD("mat"), U_AHD("matte")],
    (345, 2, 8): [U_AHD("matador")],
    (345, 2, 9): [U_MON("ماتادور")],
    (345, 2, 10): [U_MON("ماتادور")],
}

def insert_after(d, key_after, newkey, value):
    """Return an OrderedDict-like dict with newkey inserted right after key_after (or at end)."""
    out = {}
    done = False
    for k, v in d.items():
        if k == newkey:
            continue
        out[k] = v
        if k == key_after:
            out[newkey] = value; done = True
    if not done:
        out[newkey] = value
    return out

def apply(page, table):
    path = VER % page
    v = json.load(open(path, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    seen = set()
    new_entries = []
    for e in v["entries"]:
        ei = e["entry"]
        assert (ei, "root") in table, (page, ei)
        e2 = insert_after(e, "sources", "ref_check", table[(ei, "root")]); seen.add((ei, "root"))
        nodes = []
        for n in e2["nodes"]:
            key = (ei, n["id"])
            assert key in table, (page, key)
            n2 = dict(n)
            for u in WEB.get((page, ei, n["id"]), []):
                if u not in n2["sources"]:
                    n2["sources"] = list(n2["sources"]) + [u]
            n2 = insert_after(n2, "sources", "ref_check", table[key]); seen.add(key)
            nodes.append(n2)
        e2["nodes"] = nodes
        new_entries.append(e2)
    missing = set(table) - seen
    assert not missing, (page, missing)
    v["entries"] = new_entries
    json.dump(v, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(path, "a", encoding="utf-8").write("\n")
    cnt = collections.Counter()
    for e in v["entries"]:
        for r in e["ref_check"]: cnt[r["status"]] += 1
        for n in e["nodes"]:
            for r in n["ref_check"]: cnt[r["status"]] += 1
    print(page, dict(cnt))

apply(101, P101); apply(126, P126); apply(311, P311); apply(345, P345)
