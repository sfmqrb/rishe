# Extraction spec — Nourai Etymological Dictionary chart pages

You are given a page image from "An Etymological Dictionary of Persian, English and
other Indo-European Languages" by Ali Nourai. Each page contains one or more
**charts** (rounded-rectangle panels). Each chart is a derivation tree:

- At the top-left is the **root box** (dark shadowed box): root name in bold
  (e.g. `B.r.k`), its language label above it (e.g. `Semitic`, `Indo-European`),
  source refs after the 📖 symbol (e.g. `KLN:514`), and a gloss in italics.
- Below it, **word boxes**, one per language stage. Each box has:
  - a language header (e.g. `Arabic`, `Hebrew`, `Persian`, `Greek`, `Latin`,
    `Old French`, `English`, `Avestan`, `Pahlavi`, `Sanskrit`...) followed by
    📖 source refs (e.g. `KLN:164; FVQ:75`, `MON:2958`, `AHD:579`).
  - one or more word lines: `translit : gloss` in Latin script. Persian boxes
    additionally have the word(s) in **Perso-Arabic script** on the right side,
    sometimes with variant forms in parentheses or a comma-separated list.
  - sometimes a **poetry quote** in Persian script (one or two lines, hemistichs
    separated by `-` or layout), attributed to a poet in small Latin text at the
    box's lower-left or below the verse (e.g. `Ferdowsî`, `Sa`dî`,
    `Hadîqat-ol-Haqîqat`, `Hâfez`).
  - sometimes an italic explanatory note (e.g. biographical text about Avicena).
- **Arrows and connector lines** show derivation: a box's parent is the box its
  incoming arrow comes from. A vertical line dropping from the root (or from a
  box) with branching arrows feeds each child box. Horizontal chains
  (Greek → Latin → Old French → English) are parent→child left to right.
  Indentation depth also reflects tree depth. Follow the drawn arrows carefully.

## Output

Write a single JSON file (UTF-8, no BOM) with this exact shape:

```json
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
            {"translit": "b.r.k", "gloss": "to bless", "script": null},
            {"translit": "barakat", "gloss": "blessing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:45",
          "words": [
            {"translit": "barekat", "gloss": "blessing", "script": "برکت"}
          ],
          "script_extra": "تبریک ، تبرّک ، مبارک",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```

Rules:
- `book_page` = `pdf_page` − 30. It is also printed at the bottom of the page.
- `parent: 0` means the node descends directly from the root box. Otherwise
  `parent` is the `id` of another node in the same entry. Number nodes in
  reading order starting at 1.
- `words`: one object per word line in the box. Preserve transliteration
  diacritics exactly (â î û ŭ ě č š ž ǰ etc.). `gloss` is the italic text after
  the colon; null if none. `script` is the Perso-Arabic form printed for THAT
  word, or null.
- `script_extra`: additional Perso-Arabic forms in the box not tied to one
  transliterated word (variant lists, parenthesized forms). Strip the enclosing
  parentheses of a variant list but keep inner punctuation. Omit or null if none.
- `quote`: `{"text": "<Persian verse, hemistichs joined with ' - '>", "poet": "<attribution>"}`
  or null. Transcribe the verse EXACTLY as printed, keeping diacritics like
  tashdid (ّ) and hamza where printed.
- `note`: italic explanatory prose in the box (English), or null.
- `refs`: the citation string verbatim (e.g. `KLN:164; AHD:579`), null if none.
- If a chart at the top of the page has no root box (it continues from the
  previous page), set `"continues": true` on that entry and give its nodes
  `parent: 0` where the incoming arrow comes from off-panel.
- **Parts**: large roots span several charts labeled `PART 1`, `PART 2`, ... in
  the panel's top-right ("SEE OTHER PART(S) FOR MORE DERIVATIVES"). Record this
  as `"part": 1` (etc.) on the entry; omit or null when absent.
- **Cross-references**: a small pointing-hand symbol (☞) after a word or gloss
  followed by a root name (e.g. `julep ☞ Wrdho`, `hand ☞ Y.m.n`, `☞ Ud 1, Ôus 2`)
  means "see that root's own chart". Record on the word as
  `"see": ["Wrdho"]` (array — there can be several, comma-separated). Do not
  merge the referenced root name into the gloss.
- Some roots have a secondary ancestor box directly under the root box (e.g.
  `Avestan / Pahlavi — âp: water` under the Indo-European root). Treat it as a
  normal node with `parent: 0`; its language may be a compound like
  `Avestan / Pahlavi`.
- Do NOT invent, normalize, or "correct" any word — transcribe what is printed.
  If a Persian string is genuinely illegible, use "‼UNCLEAR" in its place.
- Accuracy of the Perso-Arabic script matters more than anything else. Read it
  character by character, including short-vowel diacritics and madda only when
  printed. For an ambiguous glyph (ه vs ح, ق vs غ, د vs ذ...), weigh which
  reading yields a real Persian/Arabic word fitting the gloss; for classical
  verse (Ferdowsî, Sa`dî, Hâfez...) prefer the canonical reading of the line if
  you recognize it AND it is consistent with the printed shapes.
- Stub entries like `Wreg 2 — see root: Wer 3` (no chart, just a redirect line)
  become `{"root": {"name": "Wreg 2", "redirect": "Wer 3"}, "nodes": []}`.
