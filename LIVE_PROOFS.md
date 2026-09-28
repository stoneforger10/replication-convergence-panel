# StudioNet proofs

Contract: [0x7908830bD11CA2BF039F4C9c99e3A0cb4cD19B2A](https://explorer-studio.genlayer.com/address/0x7908830bD11CA2BF039F4C9c99e3A0cb4cD19B2A). Explorer code was read back and compared with `contracts/ReplicationConvergencePanel.py`; the source text matches. Every cited transaction is FINALIZED with `MAJORITY_AGREE` and successful state-changing execution.

| Step | Finalized transaction | Observed result |
| --- | --- | --- |
| Deploy | [0x7e8c2c…eae751](https://explorer-studio.genlayer.com/tx/0x7e8c2c95a11de11cf1492ce3d9f568c3398b2c5ce93f318d127163310feae751) | Matching source published. |
| Open demonstration panel | [0xedb701…9bb3b](https://explorer-studio.genlayer.com/tx/0xedb701ff76b261ac3f01729ee98a85ea0c17dd4df2e93cd225b04ef00f19bb3b) | Bounded question and comparison rule. |
| Add study A | [0x7f6905…4391](https://explorer-studio.genlayer.com/tx/0x7f6905049f13e0690a861a723b28d20fe8085b8344a09e2ee012cb5839e54391) | GitHub API URL and SHA-256 commitment. |
| Add study B | [0xb5f97f…d291](https://explorer-studio.genlayer.com/tx/0xb5f97f62292b8ef9868338713bad14968107db1d16064092aef8f7f817a9d291) | jsDelivr URL and SHA-256 commitment. |
| Assess | [0xe63319…33bc](https://explorer-studio.genlayer.com/tx/0xe633198eb5bd203419cce636d8d05161229d375efd2834abe4a3b6b00ca433bc) | Both full bodies fetched, status 200, hashes matched; both comparable POSITIVE; `CONVERGENT`, eligible count 2. |
| Open negative control | [0xfc356c…ed43](https://explorer-studio.genlayer.com/tx/0xfc356c6743c9ac284b927596a3c0cfee97fa196986cd578ed3435e1ea510ed43) | Separate bounded panel. |
| Add study A | [0x09f86e…a0ad](https://explorer-studio.genlayer.com/tx/0x09f86e3ae6f56caeff559aa84765fae5a9ad09cce1ac303cb12aace9629fa0ad) | Correct commitment. |
| Add study B with wrong hash | [0x8541b2…5927](https://explorer-studio.genlayer.com/tx/0x8541b2331b14f900638c2647cb1cc1f3bed1ce1c030e7680bd8bd0ab70255927) | Deliberately false commitment. |
| Assess negative control | [0xb02944…49c](https://explorer-studio.genlayer.com/tx/0xb029442e6271d8b2a2214207d6bb483ad868d1d61ecdfc76e2d044aed92eb49c) | Study B fetched with status 200 but `hash_match=false`; eligible count 1, `INCONCLUSIVE`. |

The two fixture reports are synthetic and controlled by the same repository owner, despite being served on different hostnames. This is a contract-lifecycle proof, **not** evidence of two independent clinical replications or of the underlying medical claim.
