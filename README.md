<div align="center">

# Rishe · ریشه

**The roots of Persian & English, laid out like a night sky.**

[**Live site**](https://sfmqrb.github.io/rishe/) · [**نسخهٔ فارسی این سند ← README.fa.md**](README.fa.md)

<a href="https://sfmqrb.github.io/rishe/"><img src="docs/demo.gif" alt="A tour of Rishe: the constellation map, a root chart, the pathfinder, borrowing flows, a word's journey, and the research notes" width="850"></a>

</div>

*Rishe* (ریشه, Persian for *root*) is an interactive rendition of **Ali Nourai's**
*An Etymological Dictionary of Persian, English and other Indo-European Languages* —
a remarkable reference charting over 1,600 shared roots of some 4,700 Persian and
3,300 English words. The book exists only as a scan of hand-drawn charts; this
project turned all 541 of them into structured, open data and built a bilingual
website on top: a zoomable constellation of every root family, the charts as
interactive trees with the book's poetry citations under the words they attest,
a pathfinder that walks the road between any two words (*šâh* ↔ *checkmate*,
*pardîs* ↔ *paradise*), and an animated map of each word's journey across lands
and centuries.

The data turned out to be good for more than browsing. A research section computes
quantitative studies straight from the charts — borrowing rates by semantic field,
the sound laws of Arabic-mediated re-borrowing recovered from doublets, the poets'
purism gradient from Rŭdakî to Hâfez — and then crosses the dictionary with
8.5 million words of Persian poetry from the [Ganjoor](https://ganjoor.net) corpus
to retest those findings against 56 poets' complete divans spanning a millennium.
Every number regenerates from open scripts in this repository, and the whole site
is a single self-contained HTML file: no backend, no build framework, no external
libraries. It works offline.

## Demo

| | |
|---|---|
| [![Map](docs/shots/map.png)](https://sfmqrb.github.io/rishe/#map) **Map** — every root family as a star, clustered by origin | [![Roots](docs/shots/roots.png)](https://sfmqrb.github.io/rishe/#roots) **Roots** — the book's charts as interactive bilingual trees |
| [![Pathfinder](docs/shots/path.png)](https://sfmqrb.github.io/rishe/#path) **Pathfinder** — *pardîs* → *pairi-daêza* → *paradeisos* → *paradise* | [![Flows](docs/shots/flows.png)](https://sfmqrb.github.io/rishe/#flows) **Flows** — how words entered Persian, as a Sankey |
| [![Journey](docs/shots/journey.png)](https://sfmqrb.github.io/rishe/#journey) **Journey** — a word's family fanning out across an old map | [![Research](docs/shots/research.png)](https://sfmqrb.github.io/rishe/#research) **Research** — quantitative studies with methods stated |

The whole site is bilingual — the header toggle (or
[`?lang=fa`](https://sfmqrb.github.io/rishe/?lang=fa)) switches every label, chart
gloss, and note into Persian and mirrors the entire layout right-to-left:

<div align="center">
<a href="https://sfmqrb.github.io/rishe/?lang=fa"><img src="docs/shots/fa.png" alt="The site in Persian, fully right-to-left" width="700"></a>
</div>

## What's inside

- **English / فارسی** — the ~7,100 English glosses and margin notes from the book
  were translated into Persian (`data/translations/fa.json`) and are baked into
  the same single file; the layout mirrors right-to-left.
- **Map** — every root family as a star in a zoomable constellation, clustered by
  origin (Indo-European, Semitic, Iranian, Turkic), sized by its descendants.
  Hover a root to light up its cross-referenced neighbors.
- **Roots** — the book's charts as interactive trees: bilingual search
  (برق or *barq* or *emerald*), collapsible branches, the poetry citations
  (Ferdowsî, Hâfez, Sa'dî…) under the words they attest, and a
  *View scanned page* button showing the original printed page.
- **Pathfinder** — pick any two words and walk the road between them.
  Kinship means a genuinely shared root; the book's ☞ margin notes are shown
  separately and honestly.
- **Flows** — a Sankey of how words entered Persian: inherited directly,
  via Arabic, via European languages, via Turkic — plus headline numbers
  (719 roots shared by Persian and English, and counting).
- **Journey** — an animated old-map of a word's family fanning out across
  lands and centuries, your word's own road drawn in gold.
- **Research** — quantitative studies computed from the charts, with methods
  stated on the page: borrowing rates by WOLD semantic field (double-annotated),
  the sound laws of Arabic-mediated re-borrowing recovered from doublets,
  round-trip words, the poets' purism gradient (Rŭdakî → Hâfez), the topology
  of the ☞ cross-reference network, "nine degrees of etymology", and how badly
  surface similarity predicts real relatedness (false friends included).
  All numbers regenerate via `tools/research.py`.
- **Ganjoor corpus studies** — the dictionary crossed with 8.5 million words
  of Persian poetry from the official [Ganjoor](https://ganjoor.net) database:
  the purism gradient retested on 56 poets' complete divans (Ferdowsî → Sîmîn
  Behbahânî, 900–1975), first-attestation dates for every charted word (the
  Greek layer vs. the modern European wave), and types-vs-tokens — only ~4% of
  running verse is borrowed even though ~28% of the charted vocabulary is.
  Regenerate via `tools/ganjoor.py`.

## Source & credit

All the scholarship belongs to **Ali Nourai**. The book is freely available at the
[Internet Archive](https://archive.org/details/AnEtymologicalDictionaryOfPersianEnglishAndOtherIndo-europeanLanguages).
This project is a non-commercial homage; rights to the dictionary's content remain
with its author.

## How the data was made

The scan has no digital text, and ordinary OCR destroys the charts. Extraction was
done by a fleet of **Claude** (Anthropic) vision-model agents working page by page:
each chart page rendered at 200 DPI, every box read with the Perso-Arabic script
transcribed character by character from magnified crops, the drawn arrows traced to
reconstruct each derivation tree, and the results validated structurally
(`tools/validate.py`) — with disputed glyphs re-read against the classical verses
the book quotes. Details and known source defects are in
[`data/ANOMALIES.md`](data/ANOMALIES.md) (notably: book page 92 is missing from the
scan itself).

## Repository layout

```
data/EXTRACTION_SPEC.md      # the schema & rules the extraction agents followed
data/extracted/batch/        # one JSON per book page — the structured dictionary
data/translations/fa.json    # Persian translations of the glosses & notes
data/research/               # research analyses (research.json) + semantic-field labels
data/ANOMALIES.md            # source-scan defects
tools/research.py            # computes every number on the Research tab
tools/ganjoor.py             # Ganjoor corpus analyses (data/research/ganjoor.json)
site/template.html           # the whole app (HTML+CSS+JS, data injected at build)
site/pages/                  # compressed scans of every chart page
tools/build_site.py          # data + template → site/risheh.html
tools/validate.py            # structural validation of the extracted JSON
.github/workflows/pages.yml  # builds & deploys to GitHub Pages on push
```

## Running locally

```sh
python3 tools/build_site.py data/extracted/batch -o site/risheh.html
# then open site/risheh.html in a browser — no server needed
```

## Found a mistake?

Transcriptions were made from a scan and slips are possible. Please
[open an issue](https://github.com/sfmqrb/rishe/issues) — see
[CONTRIBUTING.md](CONTRIBUTING.md) for what to include. The *View scanned page*
button under every chart makes verifying against the original easy.

---

<div align="center">

Built by [Sajad F. Maghrebi](https://www.cs.toronto.edu/~smaghrebi/) — because
Farsi is sugar. «فارسی شکر است»

</div>
