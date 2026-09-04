# Model comparison (2026-09-04)

Pages 32 and 33 were verified from scratch, under identical instructions and the same local
library, by three models. Fable's runs predate the "consult every book" rule. Files here are
the three outputs per page plus the full process logs of the Sonnet and Opus runs.

| page | Fable 5.1 | Opus 5 | Sonnet 5 |
|---|---|---|---|
| 32 (4 nodes) | 80K tokens (no every-book layer); 2 confirmed, 2 disputed | 166K; same verdicts; 26 book lookups / 20 books; quoted Addi Shir verbatim; found KLN:2 is the wrong page | 166K; same disputed; 12 lookups / 11 books; could not find the Addi Shir entry; root downgraded to plausible over the POK page number |
| 33 (16 nodes) | 131K; 10/2/2/2 (conf/plaus/disp/transcr) | 171K; 8/3/4/1; 62 lookups / 20 books; found «آبو» is a misreading of أبو; showed borrâco and Jaob are misprints in the printed book; positive evidence against Hindustani bojīna | 169K; 8/3/3/1 + 1 unverified; 31 lookups / 13 books; caught FVQ:44 covering a different word; missed borrāgō |

Decision: Opus 5 for subsequent pages and every-book passes (quality ≥ Fable at a lower
rate); Sonnet 5 as the budget fallback. The Opus records for pages 32 and 33 were adopted
into data/verification/ (they already carry the every-book layer).
