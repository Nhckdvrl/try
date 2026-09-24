#!/usr/bin/env python3
"""G25A O7 — power/sensitivity note (mandatory, design-stage, zero model).

Deterministic arithmetic from FROZEN inputs; no simulation, no RNG.

Frozen inputs (all cited in preregistrations/PREREGISTRATION_G25A_NEAR_ZERO.md):
- G23A Delta_zero cluster-bootstrap CI = [+4.39, +13.33] at n=190 items /
  68 clusters (the prereg's frozen resampling constant);
- G25A design: 400 items / 342 clusters, within-item paired contrasts,
  same 0-100 sign-aligned raw-points scale (G23A discipline);
- O4 floor: point estimate >= 3.0 AND CI low > 0 (both co-primaries);
- design-stage expected effect ~ +8 (G23A shape: Delta_zero +8.83,
  Gap(0)-Gap(1) = 13.86 - 5.59 = 8.27).

Method:
- SE_G23A = half-width / 1.96 (two-sided 95%, percentile bootstrap taken as
  approximately normal);
- variance transfers as 1/n_clusters (within-item paired design; per-cluster
  variance assumed equal across material sets) -> SE_G25A =
  SE_G23A * sqrt(68/342); this ASSUMPTION is stress-tested with SE
  inflation factors 1.0 / 1.5 / 2.0;
- MDE80 = (z_0.975 + z_0.80) * SE  (two-sided alpha=0.05, power 0.80);
- floor resolvability: P(CI low > 0 | true effect = 3.0)
  = Phi(3.0/SE - 1.96); inflation tolerance k* = 3.0 / (1.96 * SE).
- detectable probability for the expected effect (+8) under each inflation.

Output: results/audits/g25a_power_note_v1.json
"""

from __future__ import annotations

import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "results", "audits", "g25a_power_note_v1.json")

G23A_CI = (4.39, 13.33)
G23A_N, G23A_CL = 190, 68
G25A_N, G25A_CL = 400, 342
FLOOR = 3.0
EXPECTED = 8.0            # prereg: "expected Delta_local0 ~ +8"
INFLATIONS = (1.0, 1.5, 2.0)
Z975, Z80 = 1.959963985, 0.841621234


def phi(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def main() -> int:
    half = (G23A_CI[1] - G23A_CI[0]) / 2.0
    se23a = half / 1.96
    se25a = se23a * math.sqrt(G23A_CL / G25A_CL)

    rows = []
    for k in INFLATIONS:
        se = se25a * k
        rows.append({
            "se_inflation": k,
            "se_g25a": round(se, 4),
            "mde80_points": round((Z975 + Z80) * se, 3),
            "p_ci_low_gt_0_if_true_3.0": round(phi(FLOOR / se - Z975), 4),
            "p_ci_low_gt_0_if_true_8.0": round(phi(EXPECTED / se - Z975), 4),
            "z_if_true_8.0": round(EXPECTED / se, 3),
        })

    k_star = FLOOR / (1.96 * se25a)
    note = {
        "g23a_basis": {
            "delta_zero_ci": list(G23A_CI),
            "items": G23A_N, "clusters": G23A_CL,
            "se_derived": round(se23a, 4),
            "source": "frozen prereg citation of G23A cluster bootstrap",
        },
        "g25a_design": {"items": G25A_N, "clusters": G25A_CL,
                        "se_equal_variance": round(se25a, 4)},
        "sensitivity": rows,
        "floor_3_resolvable_up_to_se_inflation": round(k_star, 3),
        "floor_3_resolvable_up_to_variance_inflation": round(k_star ** 2, 3),
        "expected_effect_points": EXPECTED,
        "assumption": "per-cluster variance equal across material sets "
                      "(G23A synthetic -> G25A natural); stress-tested by "
                      "SE inflation 1.0/1.5/2.0",
        "conclusion": (
            "O4 floor (3.0) stays CI-resolvable under up to ~1.5x SE "
            "inflation (variance ~2.3x); the design-stage expected effect "
            "(~+8) remains detected at >=97% even at 2.0x inflation; MDE80 "
            "is 2.8-5.7 points across the grid. n=400/342 clusters is not "
            "arbitrary: it is what pulls MDE80 below the floor at equal "
            "variance (G23A's 68 clusters alone would give MDE80 6.39 "
            "points > floor)."),
        "zero_model": True,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(note, f, indent=1, ensure_ascii=False)
    print(json.dumps(note, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
