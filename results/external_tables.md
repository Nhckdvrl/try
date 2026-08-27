# External held-out validation

**A. Ramsey, Liu & Trueblood (2024)** medication-report paradigm, OSF 9ybnx.
Instruction wording verbatim from their experiment code. Their design flags the
fabricated report *in place*, which is the retrospective arm; announcing which
report will be fabricated before the stream is our addition. 48 items, exact
ground truth (the mean of the truthful reports).

| model | n | base error | admit (unflagged) | flag in place (their design) | flag announced first |
|---|---:|---|---|---|---|
| qwen3-8b | 48 | +0.0 | +2.4 | **+0.0** | **+0.4** |
| gemma3-12b | 48 | -0.0 | +2.4 | **+0.1** | **+0.1** |
| mistral-small-24b | 48 | -0.0 | +1.6 | **+0.1** | **-0.0** |

Values are the signed pull toward the fabricated report, in patients per 100, against the true mean of the truthful reports. 0 is perfect exclusion.

**B. Aiyer et al. (2023) replication of Baron & Hershey (1988)**, OSF knjhu.
The bypass-surgery vignette verbatim from their Qualtrics file, all four framings
actually administered. 4 items, so this is an anchor rather than a test.

| model | REI exclude-pre | REI exclude-post |
|---|---|---|
| qwen3-8b | +0.341 (n=4) | +0.435 |
| gemma3-12b | +0.600 (n=4) | +0.338 |
