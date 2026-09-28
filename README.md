# Replication Convergence Panel

An open, append-only **cross-source result aggregation** primitive. It does not propose graph edges, certify scientific truth, or issue a transferable certificate. Participants submit public study URLs with exact SHA-256 commitments. At least two distinct hostnames are required. Any caller may assess when new reports have arrived.

## Why GenLayer

Hashes alone cannot decide whether studies measured the same outcome under a comparison rule. GenLayer leader and validators independently fetch each full report, verify status and content hash, then semantically extract method comparability and result direction. Exact equality of the source vector, interpretations, derived outcome, and report root is required. A genuinely new source is required before another assessment.

```text
open question + comparison rule → multi-party source submissions
→ independent fetch + hash check → semantic method/outcome extraction
→ exact validator agreement → CONVERGENT / DISPUTED / INCONCLUSIVE snapshot
```

CONVERGENT means at least two comparable, known directions match; DISPUTED means comparable directions conflict. It does **not** mean the underlying scientific claim is true. Two documents on different hosts are not necessarily independent publishers; consumers must inspect provenance. Unavailable, mismatched or ambiguous sources do not count as eligible. The state is an evolving panel record, not a one-time certificate.

`examples/study-a.txt` and `examples/study-b.txt` are synthetic trial fixtures. They may be served from different HTTPS hosts to exercise the mechanism, but remain one publisher's test data and must not be presented as independent scientific replications.

## API

`open_panel(panel_id, question, comparison_rule)`, `submit_study(panel_id, study_id, source_url, source_hash)`, `assess(panel_id, assessment_id)`, `get_panel`, `get_study`, `get_snapshot`.

## Verify and deploy

```powershell
genvm-lint check contracts/ReplicationConvergencePanel.py --json
pytest tests/direct -q
genlayer network set studionet
genlayer deploy --contract contracts/ReplicationConvergencePanel.py
```

Check each transaction for FINALIZED **and successful execution** before citing it. `LIVE_PROOFS.md` distinguishes completed proofs from planned calls.

## Security boundaries

- 2–5 reports, unique IDs and HTTPS hostnames; full decoded body ≤8 KiB.
- Publisher-controlled reports can be false; hash match proves only which bytes were assessed. Distinct hostnames do not prove independent ownership.
- Unknown method or direction never counts toward convergence. Decisions derive from exact normalized per-source interpretations, not caller-supplied scores.
- Assessment IDs and source counts block replay and duplicate assessments without new evidence. Reports and snapshots are append-only.
- The prompt treats fetched text as untrusted data. Semantic disagreement aborts consensus instead of accepting the leader's preferred interpretation.
