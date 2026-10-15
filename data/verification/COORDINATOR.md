# Verification run — coordinator methodology

This is the playbook for the agent that *runs* the verification of Nourai's charts: it launches
one verification subagent per PDF page, checks what each one reports, fixes extraction errors,
and publishes. The per-page research method itself is in
[`agent/AGENT_INSTRUCTIONS.md`](agent/AGENT_INSTRUCTIONS.md); the subagents follow that file,
the coordinator follows this one. [`/prompt.md`](../../prompt.md) is the short paste-in prompt
that starts a coordinator session.

## 1. What the run produces

| Path | What it is |
|---|---|
| `data/extracted/batch/page-N.json` | The chart extraction (the dictionary data). Hand-formatted; edit only by exact substring replacement. |
| `data/verification/page-N.json` | One verification file per PDF page: root and node verdicts, derivations in English and Persian, `ref_check[]`, `consulted[]`, `sources[]`. Same node ids as the extraction. |
| `data/verification/process/verify-page-N.{md,jsonl}` | The full log of the subagent's tool calls, exported from its transcript. |
| `data/verification/sources/web/` | Archived copies of every cited web page (public). |
| `data/verification/sources/refs/` | The reference library: OCR and scans of copyrighted books, plus `ocr/BOOK/N.png` page images saved by agents. **Private only. Gitignored on the public branch.** |
| `site/risheh.html` | Built site. Gitignored; GitHub Pages rebuilds it from `main`. Commit `site/template.html` only. |

Progress at any time:

```sh
python3 tools/verify_check.py | tail -3          # totals and the list of unverified pages
for n in $(seq 300 571); do [ -f data/verification/page-$n.json ] || echo $n; done | head
```

Pages are done in ascending PDF order. Pages 146 and 163 are redirect-only and have empty
verification files by design.

## 2. Privacy rules (never break these)

- Work on branch `verified`. Public remote `origin` (sfmqrb/rishe) receives `verified` and `main`.
- Private remote `private` (sfmqrb/rishe-private) receives `verified`, `main`, and
  `verified-with-sources`. Only that last branch carries `data/verification/sources/refs/`.
- The only things from `sources/` allowed on the public branch: `sources/web/`,
  `refs_online.json`, `SOURCE_MATRIX.md`, `MISSING_REFERENCES.md`.
- Never `git checkout verified-with-sources` (or `main`) in the main working tree: switching
  deletes the untracked library or disturbs files running agents are writing. The private
  branch lives in the sibling worktree `../rishe-backup`, which `tools/verify_publish.sh` manages.
- Before every commit, check that nothing under `sources/refs/` is staged.
  `tools/verify_commit_deploy.sh` does this and aborts. The local `.git/hooks/pre-push` hook
  also blocks a push of `sources/refs/` to any non-private remote. It is not versioned, so
  re-create it on a fresh clone.
- A commit made by someone else (e.g. the owner committing in-progress files) is fine as long as
  `git show --name-only <sha> | grep sources/refs/` is empty. Check before pushing.

## 3. Launching subagents

- Model: Opus (`model: opus`, `subagent_type: general-purpose`). Sonnet only as a fallback.
- Concurrency and batch size are the owner's call and change often. Recent rule: batches of
  20 pages, up to 20 agents at once. Wait for an explicit go before every batch. When the owner
  says to stop agents, stop exactly the ones named (highest pages first if unspecified) with
  TaskStop, and launch nothing new.
- Before launching, confirm each page has no verification file and has
  `agent/charts/page-N.txt`.
- Use this prompt verbatim, with N substituted:

  > Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md
  > and follow them exactly for PDF page N only. Chart text:
  > /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-N.txt; source JSON:
  > /home/sfmqrb/git/rishe-private/data/extracted/batch/page-N.json. Write
  > /home/sfmqrb/git/rishe-private/data/verification/page-N.json, run
  > `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py N` (fix any PROBLEM lines), and reply
  > with the short summary described in the instructions.

- Write a page-to-agent-id map to the scratchpad immediately (`N <agentId>` per line). The
  scratchpad can disappear between sessions. If it does, rebuild the map from the transcripts:
  `grep -l "page-N.json" ~/.claude-work/projects/-home-sfmqrb-git-rishe-private/<session>/subagents/agent-*.jsonl`.
- Agents share the scratchpad, so AGENT_INSTRUCTIONS requires page-suffixed temp filenames.
  Two agents once overwrote each other's `e0.json`.

## 4. When an agent finishes

1. **Post-process:**
   `sh tools/verify_finish_page.sh N <transcript>`. This exports the process log, archives
   cited URLs, and runs `verify_check.py`. The page must show `nodes verified: k/k` and no PROBLEM lines.
2. **Read the agent's report for extraction errors.** Agents say "extraction error" or
   `error_in: "extraction"` when the JSON differs from the printed page. Never trust this
   blindly; check the printed page first (section 5).
3. **Commit and publish:** write a message file `Verify page N (Root/word, word; Root2/…)`
   ending with the `Co-Authored-By` and `Claude-Session` trailers. Then run
   `sh tools/verify_commit_deploy.sh msg.txt`. This validates the extraction (it must report
   `0 errors`; a malformed splice once deployed a broken page), builds the site, syntax-checks
   the JS, refuses if the reference library is staged, commits, runs `verify_publish.sh`, pushes
   `verified` to both remotes, and fast-forwards `main` on both remotes, which deploys the site.
   Several finished pages can go in one commit.
4. **Tell the owner** one word to look up on the site for the page, with the headline finding
   (the most interesting disputed or corrected derivation).

`verify_publish.sh` refuses when tracked files are dirty, which happens when running agents are
mid-way through archiving web pages. The commit script then still pushes `verified` directly. Run
`verify_publish.sh` again at the end of the batch so the private library catches up.

## 5. Checking and fixing extraction errors

Render the page and look:

```sh
pdftoppm -f N -l N -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf $SP/Nhi
# downscale by 4 for an overview, crop at full size for Persian script (PIL)
```

`site/pages/N.jpg` is a quicker low-resolution view.

Fix by exact substitution with a uniqueness assertion, and re-parse afterwards:

```python
s = open(p).read(); assert s.count(old) == 1; s = s.replace(old, new); json.loads(s); open(p, 'w').write(s)
```

Never `json.dump` an extraction file, because it destroys the hand formatting. Verification
files may be rewritten with `json.dump(d, f, ensure_ascii=False, indent=1)`.

What counts as an extraction error:

- **Errors to fix:** wrong letters, a lost diacritic or circumflex (`xvantan` for `xvântan`),
  wrong Persian letters (پ for ب, Arabic ك for Persian ک), missing words, dropped superscript
  numbers, capital I read as l, and a wrong `parent`. Trace the drawn arrow: a line leaving the
  bottom of a box makes that box the parent, even when it runs beside the left trunk.
- **Not errors:** dropped short vowels.
- **Book misprints:** when the book itself is wrong, the agent records `error_in: "book"`,
  `book_prints`, `correct_form`. The extraction stays faithful to the print.

**Blank boxes.** Agents often say the JSON "correctly omits" an empty printed box. It does not:
every printed box is a node. Append to the extraction entry
`{"id": max+1, "parent": P, "lang": null, "refs": null, "words": [], "script_extra": null, "note": null, "quote": null}`
(eight-space indented like its neighbours), and to the verification entry a node
`{"id": …, "lang": null, "words": "", "verdict": "unverified", "error_in": "extraction", "derivation": …, "derivation_fa": …}`
saying the box is printed empty.

**Root boxes with two headword lines** are one root: join names and glosses with `"; "`
(`"Kŭr, Quôros; Kâl"`, `"dark, blind; prison"`). If a second headword line was extracted as a
node, fold it into the root and renumber the nodes in both files.

After any edit: `verify_check.py N` and `validate.py` again.

## 6. Failure modes seen so far

- **Rate limit (HTTP 429) kills agents mid-run.** Often the agent has already written a complete
  `page-N.json` and died during its final self-check. Accept it after `verify_check.py` shows the
  full node count, and after checking every node has `verdict`, `derivation`, `derivation_fa`, and every
  root has `verdict` and `note_fa`. Otherwise resume the agent with SendMessage to its id, or relaunch.
- **Stopped or killed agents leave archived web pages** in `sources/web/` but usually no
  verification file. Check for partial `page-N.json` files and delete or finish them. The web
  archives are public-safe; commit them.
- **`git add -A` sweeps in other agents' in-progress files.** Before committing, make sure any
  `page-N.json` whose agent has not reported either passes `verify_check` or is left out.
- **Lost scratchpad** after a long break: rebuild the agent map (section 3) and re-render page images.

## 7. Recurring findings agents should expect

Nourai misreads Pokorny's "apr." (Old Prussian) as Old Persian. Many "Avestan" boxes hold
reconstructions or Sanskrit. Klein page numbers refer to the 1971 one-volume edition, so the 1966
set on disk is offset. `ref_page.py`'s Borhan-e Qāṭeʿ mapping drifts by a few pages, and Borhan
vol. 2 is printed page = leaf + 541. Wiktionary sometimes cites Nourai himself, so it is not
independent there. The complete Kent OCR is `refs/KNT_full.txt`.
