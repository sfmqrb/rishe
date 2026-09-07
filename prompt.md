# Handoff prompt — Nourai etymology verification

Paste everything below this line into a fresh Claude Code session (start it inside
`tmux attach -t rishe`, then `claude`) to continue the verification run.

---

**Project.** Repo `/home/sfmqrb/git/rishe` (owner Sajad) renders Ali Nourai's *Etymological
Dictionary of Persian, English and other Indo-European Languages* as a website. The book's charts
were extracted to JSON in `data/extracted/batch/page-<pdf>.json` (541 files, 537 with chart
content, 1,790 entries, ~7,895 nodes). The task is to re-verify every derivation arrow in every
chart against modern scholarship and against the exact pages Nourai cites, and to show the
results on the site. Check progress and the next unverified page before doing anything:

```
for n in $(seq 300 560); do [ -f data/verification/page-$n.json ] || echo "$n TODO"; done | head
```

Order is simply ascending PDF page. Pages 146 and 163 are redirect-only with empty verification
files by design. Always check for an existing file before launching an agent for a page.

**Branches and privacy (most important constraint).** Work happens on branch `verified`. Public
remote `origin` (sfmqrb/rishe) gets `verified` and `main`. Private remote `private`
(sfmqrb/rishe-private) has branch `verified-with-sources`, which additionally carries the reference
library: OCR texts and page scans of copyrighted books under `data/verification/sources/refs/`.
That directory is gitignored on the public branch. The public branch may contain only
`data/verification/sources/web/` (archived web pages), `refs_online.json`, `SOURCE_MATRIX.md`,
`MISSING_REFERENCES.md`. Never check out `verified-with-sources` in the main working tree.
Publish only with `sh tools/verify_publish.sh` (pushes `verified` to origin and updates the
private worktree). It refuses if there are uncommitted tracked changes; commit and rerun.
Deploy the site (GitHub Pages builds from `main`) every two to three pages by fast-forwarding
`main`. Never `git checkout main` (running agents touch `sources/web/index.jsonl`); instead:

```
git merge-base --is-ancestor main verified && git push -q origin verified:main && git push -q private verified:main && git branch -f main verified
```

**Concurrency.** Max 6 verification subagents at once (`subagent_type: general-purpose`,
`model: opus`; Sonnet only as fallback). Session rate limits (HTTP 429) have killed whole batches;
killed agents often leave complete JSON, which can be published after `verify_check.py` confirms
the node count, or the agent can be resumed with SendMessage. If the user says "don't start new
agents", stop launching and just finish/publish the running ones.

**Per-page verification.** One subagent per page, always with this prompt:

> Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md
> and follow them exactly for PDF page N only. Chart text:
> /home/sfmqrb/git/rishe/data/verification/agent/charts/page-N.txt; source JSON:
> /home/sfmqrb/git/rishe/data/extracted/batch/page-N.json. Write
> /home/sfmqrb/git/rishe/data/verification/page-N.json, run
> `python3 /home/sfmqrb/git/rishe/tools/verify_check.py N` (fix any PROBLEM lines), and reply
> with the short summary described in the instructions.

`AGENT_INSTRUCTIONS.md` defines the methodology: verify the root and every node; give a concrete
phonetic and historical derivation; verdict per node and root (confirmed, plausible, disputed,
unverified, transcription_suspect); `ref_check[]` for every reference Nourai cites (locate the
exact page in the OCR texts or via `tools/ref_page.py ABBR:page --image` for scanned volumes,
saving what was read to `<page>.vision.txt`); `consulted[]` covering every relevant book on disk
per `SOURCE_MATRIX.md`; `sources[]` only for URLs archived with `tools/fetch_source.py`; a native
Persian `derivation_fa` per node and `note_fa` per root; for transcription_suspect the agent
must look at the printed page and set `error_in` (book or extraction), `book_prints`,
`correct_form`, and copy the page image to `sources/refs/ocr/BOOK/<page>.png`.

**Coordinator routine after each agent finishes.** Its transcript is at
`~/.claude/projects/-home-sfmqrb-git-rishe/<current-session-id>/subagents/agent-<id>.jsonl`
(find the directory with `ls -t ~/.claude/projects/-home-sfmqrb-git-rishe/*/subagents | head`).
Keep a page-to-agent-id map in the scratchpad. Run, in order:

```
python3 tools/verify_export_process.py <transcript> verify-page-N
python3 tools/verify_archive_sources.py N
python3 tools/verify_check.py N                    # must show 0 PROBLEM lines
python3 tools/validate.py data/extracted/batch     # must show 0 errors
python3 tools/build_site.py data/extracted/batch -o site/risheh.html
node tools/jscheck.js                              # syntax-checks each <script> block of site/risheh.html
git add -A && git commit -m "Verify page N (root/words…)" ; sh tools/verify_publish.sh
```

Commits end with the Co-Authored-By and Claude-Session trailers. After each page, tell the user
one word to look up on the site, with the headline finding.

**Handling extraction errors reported by agents.** Always verify against the page image first
(`site/pages/N.jpg`, or `pdftoppm -f N -l N -r 300 -png -singlefile
EtymologicalDictionary-persian-english.pdf out` and crop with PIL for small script). Then edit
`data/extracted/batch/page-N.json` by exact text substitution with an assertion that the target
string occurs once. Never rewrite these files with `json.dump` (hand formatting). Verification
files may be rewritten with `json.dump(..., ensure_ascii=False, indent=1)`. Conventions: blank
boxes in the printed chart are nodes with `"lang": null, "words": []`; when an agent reports a
missing blank box, append a node (id = max+1, correct parent) to the extraction entry and a
matching `unverified` node with `error_in: "extraction"` to the verification file. Multi-line
root boxes are encoded by joining names and glosses with `"; "` (e.g. `"Kŭr, Quôros; Kâl"`,
`"dark, blind; prison"`). Dropped short vowels are not errors; wrong letters, missing words,
wrong parents, dropped superscript numbers, and capital I read as lowercase l are.

**Recurring findings worth knowing.** Nourai repeatedly misread Pokorny's abbreviation "apr."
(Old Prussian) as Old Persian. Many "Avestan" boxes hold reconstructions or Sanskrit forms.
Klein page numbers refer to the 1971 one-volume edition; the 1966 set on disk is offset.
`ref_page.py`'s Borhan-e Qateʿ volume 3 mapping drifts by 2 to 4 pages, and Nourai's BQT page
numbers for volume 4 run 2 lower than the scan; agents note the corrected PDF page in
`ref_check`. Wiktionary sometimes cites Nourai himself, so it is not independent there.

**Memory.** `~/.claude/projects/-home-sfmqrb-git-rishe/memory/` holds the pacing rules, model
choice, and private-repo notes; keep them updated when the user changes the rules.
