# Modern trees — instructions for building the corrected chart of one page

The site shows each of Ali Nourai's charts as he printed it. Every node of every chart has
already been checked against modern scholarship; the results are in
`data/verification/page-<pdf>.json` (verdicts, derivations in English and Persian, sources,
what Nourai's references say). Your job is to turn that verification record into a second
version of each chart, the **modern tree**: the same word family, drawn the way current
scholarship draws it. Readers will switch between "Nourai's chart" and "Modern view".

You are an editor here, not a new researcher. Every change you make must rest on what the
verification record for this page already says (its `derivation`, `note`, `modern_form`,
`ref_check`, `consulted`, `sources`). Do not introduce an etymology the record does not
support. If the record is unsure, keep Nourai's arrow and mark it uncertain rather than
inventing a replacement.

Use only the three input files below: the chart text, the extraction and the verification
record. They already contain everything needed. Do not open reference books, archived pages,
page images or the web, and do not run searches; read the three files and write the output.

## Inputs (PDF page N)

- Chart text: `/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-N.txt`
- Extraction: `/home/sfmqrb/git/rishe-private/data/extracted/batch/page-N.json`
- Verification: `/home/sfmqrb/git/rishe-private/data/verification/page-N.json`

Entries are numbered from 0 in the order of the extraction's `entries` array. Skip redirect
entries (root has `redirect`). The verification file uses the same entry numbers and node ids.

## Output

Write `/home/sfmqrb/git/rishe-private/data/corrected/page-N.json` (UTF-8, `indent=1`,
`ensure_ascii=False`):

```json
{
  "pdf_page": 31,
  "book_page": 1,
  "made_by": "claude-opus-5",
  "made_on": "2026-10-17",
  "entries": [
    {
      "entry": 0,
      "root": {"name": "*h₂ep-", "lang": "Indo-European", "gloss": "water, river",
               "change": "kept",
               "why": "", "why_fa": ""},
      "summary": "One or two sentences: what differs from Nourai's chart and why.",
      "summary_fa": "همان به فارسی، برای خوانندهٔ فارسی‌زبان.",
      "nodes": [
        {"id": 1, "parent": 0, "lang": "Avestan", "from_node": 1, "change": "kept",
         "words": [{"translit": "āp-", "gloss": "water", "script": null}],
         "why": "", "why_fa": ""},
        {"id": 101, "parent": 3, "lang": "Arabic", "from_node": null, "change": "added",
         "words": [{"translit": "julāb", "gloss": "rose water, syrup", "script": "جلاب"}],
         "why": "English julep came through Arabic julāb and Medieval Latin julapium; the record's derivation names this step.",
         "why_fa": "…"}
      ],
      "detached": [
        {"from_node": 5, "words": "âbnîk «آبنیک»",
         "belongs_to": "unknown; the Arabic al-anbīq is from Greek ámbix 'cup'",
         "why": "…", "why_fa": "…"}
      ]
    }
  ]
}
```

### Field rules

- `nodes` is the modern tree. `parent` 0 means the root. Every `parent` must be the `id` of
  another node in the same entry (or 0). No cycles.
- `id`: a node that continues one of Nourai's nodes keeps **his id**. New nodes you add get
  ids from 101 upward.
- `from_node`: the Nourai node id this node continues, or `null` for an added node. Each Nourai
  node id may appear as `from_node` at most once in `nodes`.
- `change` on a node, one of:
  - `kept` — same words, same parent as Nourai (glosses or spelling may be trivially tidied).
  - `corrected` — same place in the tree, but the form, gloss or language label is fixed
    (a misprint per the record's `correct_form`, an unattested form now starred `*`, "Avestan"
    that is really a reconstruction relabelled "Old Iranian (reconstructed)", a wrong gloss).
  - `moved` — the node keeps its words but hangs from a different parent (e.g. the Persian
    word came via Arabic, a sister form is not a descendant, the arrow ran the wrong way).
  - `split` — some words of Nourai's node stay here and the others went to `detached` or to
    another node; say which in `why`.
  - `added` — a step Nourai skipped that the record names (e.g. Middle Persian form, Arabic
    stage, Latin stage), or the real source of a word.
  - `uncertain` — Nourai's arrow kept because no better view exists, but the record calls it
    unverified or doubtful.

  When two apply, pick the stronger one and mention the other in `why`: `moved` beats
  `corrected` (a node both moved and relabelled is `moved`). An empty box of Nourai's that you
  fill with the real form the record names is `corrected`.
- `why` / `why_fa`: required (non-empty) for every change except `kept`. One or two sentences,
  plain, naming the source from the record ("MacKenzie reads wābar", "Horn and Hübschmann
  reject …"). `why_fa` is a real Persian explanation for a Persian reader (as in the
  verification files' `derivation_fa`), not a word-for-word translation.
  Write for a reader of the site: never say "the record", "the verification", "node 4" or
  "Nourai's box #3"; name the scholars or books instead ("Klein and AHD", "MacKenzie").
- `words`: list of `{translit, gloss, script}`; use the record's correct forms, mark
  reconstructions with `*`, keep Nourai's Persian script where it is correct.
- `script_extra` (optional): Nourai's extra Persian words for the node (the extraction's
  `script_extra`), with words that do not belong to the family removed. Words that appear only
  in `script_extra` count as words the book mentions, so they may become nodes of their own.
- `detached`: every Nourai node whose words do **not** belong to this family at all (the
  record says the word comes from a different root, is a loan from elsewhere, or is unrelated).
  `words` is a short string of the words; `belongs_to` says in a few words where they really
  come from (or "unknown"); `why`/`why_fa` explain. If only some words of a node are detached,
  list just those words here and mark the node `split`.
  A detached node whose own Nourai parent is also detached keeps that link: give it
  `"under": <from_node of the detached parent>`. A wrong branch then still reads as a chain
  (e.g. âbnîk → al-anbīq → alambique → alambic → alembic), shown apart from the family. Items
  without `under` are the tops of detached branches. `why`/`why_fa` may be short ("same origin
  as its parent") for items whose parent already explains the branch.
- Every Nourai node of the entry must be accounted for exactly once overall: as the
  `from_node` of a node in `nodes`, or in `detached`, or (only for empty connector boxes with
  no words) simply dropped — list dropped empty boxes in `"dropped_empty": [ids]` on the entry.
  An empty box that stands for a real missing step (e.g. an "Arabic" box with no word) should
  instead become a node with the real form if the record names it.
- `root.change`: `kept`, `corrected` (better reconstruction or gloss, e.g. *h₂ep- for "Ab"),
  or `replaced` (the record says the root itself is wrong, e.g. a loanword, not an IE root:
  then `name`/`lang`/`gloss` describe what modern scholarship gives as the origin).

### How to decide, by verdict

- `confirmed` → `kept` (tidy the form to the record's standard spelling if trivially needed).
- `plausible` → usually `kept` or `corrected` (star reconstructions, fix labels/glosses the
  record flags). Use `uncertain` if the record says the link itself is doubtful.
- `disputed` → read the derivation. If the word belongs to another family → `detached`. If
  the word belongs here but the route is wrong → `moved` (and `added` steps if the record
  names them). If only part of the node is wrong → `split`.
- `transcription_suspect` with `error_in: "book"` → `corrected` to `correct_form`.
- `unverified` → `uncertain`.

Keep the tree readable: the modern tree should look like a chart, not a lecture. Do not add
words the book does not mention, except the intermediate steps or true sources the record
explicitly names. Keep English, Latin, French etc. forms as the book has them unless the
record corrects them.

## Finish

1. Validate: `python3 /home/sfmqrb/git/rishe-private/tools/corrected_check.py N` must print no
   PROBLEM lines.
2. Temporary files must carry the page number in their name (other agents run in parallel).
   In the shell, `ls` is aliased to `eza`, which can hang; use `command ls` or `find`.
3. Reply with a short summary (≤ 12 lines): per entry, the root change, how many nodes were
   kept / corrected / moved / split / added / uncertain / detached, and the single most
   interesting correction.
