#!/usr/bin/env python3
"""G26A O5 — ROPE equivalence power note (mandatory before Phase A tag).

Zero-model, deterministic arithmetic on FROZEN inputs (G25A-O7 pattern).
Prereg: preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md §0 O5 + §7.

Frozen inputs (read + citation-asserted at runtime):
- results/g23a_zero_gating_analysis.json  — two-cell Gap CIs at C=68
  (raw 0-100 sign-aligned points; the §7-cited four-cell Delta_zero
  half-width 4.47 @68 clusters is reproduced as an algebra check);
- results/g24a/g24a_analysis_v1.json      — cell-level CIs on natural
  materials at C=469 (REI units; converted to raw points with the
  recorded median |L| = 32.69 — flagged as an assumption).

Standing algebra (§7, resolved here):
  equivalence is DECLARABLE iff CI half-width < delta:  1.96*SE(C) < 1.5
  with cluster scaling  SE(C) = SE(C0)*sqrt(C0/C).
  Declarability is necessary but NOT sufficient: power at a true-zero
  effect is  P(CI subset [-d,d]) = Phi((d-hw-m)/SE) - Phi((-d+hw-m)/SE);
  at m=0 this is 2*Phi((d-hw)/SE)-1, which -> 0 as hw -> d. 80% power at
  m=0 needs hw <= delta/(1.96+1.2816) = 0.4627*delta.

What the note MUST state (§7 O5):
  (a) declarable half-width at n <= 300 / C <= 300 under the two-cell
      constants;
  (b) verdict on delta=1.5 vs the noise floor (declarable AND powered?);
  (c) if delta or n must move: OPTIONS ONLY — user decision before the
      Phase A tag, never after outcomes exist. This script decides nothing.

Output: results/audits/g26a_rope_power_note_v1.json
"""

from __future__ import annotations

import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G23A = os.path.join(ROOT, "results", "g23a_zero_gating_analysis.json")
G24A = os.path.join(ROOT, "results", "g24a", "g24a_analysis_v1.json")
OUT = os.path.join(ROOT, "results", "audits", "g26a_rope_power_note_v1.json")

DELTA = 1.5                 # O5 ROPE, raw rating points (prereg §0/§7)
C_DESIGN = 300              # G26A cluster cap (§7 "cap 300")
C_GRID = (200, 300)         # S1-min scale and design cap
N_DESIGN_MAX = 300          # item cap (§7)
POWER_TARGET = 0.80
Z975 = 1.959963985
Z80 = 0.841621234           # Phi^-1(0.80), two-sided alpha .05 / power .80
Z_EQUIV_80 = 1.2816         # Phi^-1(0.90): 2*Phi(x)-1 = 0.80
MU_GRID = (0.0, 0.75)       # true effect under / at half the ROPE

# structural roles of the G23A two-cell constants for G26A PG/LG:
#   closest analog = gap_w000 (prospective timing gap, effect-scale),
#   at-null        = gap_w100 (null cell — variance where truth is ~0)
CLOSEST_ANALOG = "gap_w000"
AT_NULL = "gap_w100"


def phi(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def equiv_power(est_mean: float, se: float, hw: float) -> float:
    """P(CI subset [-d, +d]) for a normal est. at true mean `est_mean`."""
    hi = phi((DELTA - hw - est_mean) / se)
    lo = phi((-DELTA + hw - est_mean) / se)
    return max(0.0, hi - lo)


def main() -> int:
    g23a = json.load(open(G23A, encoding="utf-8"))
    g24a = json.load(open(G24A, encoding="utf-8"))

    # ---- citation asserts (the note may not drift from the frozen files)
    pooled = g23a["pooled"]
    d = pooled["delta"]
    c68 = d["n_clusters"]
    hw_delta = (d["ci_high"] - d["ci_low"]) / 2.0
    assert c68 == 68, c68
    assert round(hw_delta, 2) == 4.47, hw_delta          # §7 cites 4.47
    c_needed_4cell = c68 * (hw_delta / DELTA) ** 2
    assert 600 < c_needed_4cell <= 610, c_needed_4cell   # §7 cites "> 604"

    p4 = g24a["strata"]["pooled-4 (primary)"]
    assert g24a["strata"]["pooled-4 (primary)"]["n_clusters"] == 469
    rei_pre = p4["REI_pre"]        # [mean, ci_low, ci_high, boot_p]
    rei_post = p4["REI_post"]
    med_absL = p4["median_absL"]
    assert round(med_absL, 2) == 32.69, med_absL

    # ---- (a) two-cell constants: declarable half-width at the design cap
    two_cell = ["gap_w000", "gap_w001", "gap_w025", "gap_w050",
                "gap_w100", "gap_atten"]
    rows = []
    for key in two_cell:
        cell = pooled[key]
        assert cell["n_clusters"] == 68, key
        hw68 = (cell["ci_high"] - cell["ci_low"]) / 2.0
        se68 = hw68 / Z975
        entry = {
            "constant": key,
            "ci_at_68": [round(cell["ci_low"], 3), round(cell["ci_high"], 3)],
            "hw_at_68": round(hw68, 3),
            "se_at_68": round(se68, 3),
        }
        for C in C_GRID:
            hw = hw68 * math.sqrt(68.0 / C)
            se = hw / Z975
            entry[f"hw_at_C{C}"] = round(hw, 3)
            entry[f"declarable_at_C{C}"] = bool(hw < DELTA)
            entry[f"equiv_power_m0_at_C{C}"] = round(equiv_power(0.0, se, hw), 3)
            entry[f"equiv_power_m075_at_C{C}"] = round(equiv_power(0.75, se, hw), 3)
        # clusters needed: (i) hw < delta, (ii) 80% power at m=0
        entry["C_needed_hw_lt_delta"] = math.ceil(c68 * (hw68 / DELTA) ** 2)
        se80 = DELTA / (Z975 + Z_EQUIV_80)
        entry["C_needed_power80"] = math.ceil(c68 * (se68 / se80) ** 2)
        rows.append(entry)

    hw_cap = {r["constant"]: r["hw_at_C300"] for r in rows}
    binding_effect_scale = max(hw_cap[k] for k in two_cell if k != AT_NULL)
    binding_effect_key = max((k for k in two_cell if k != AT_NULL),
                             key=lambda k: hw_cap[k])
    at_null_hw = hw_cap[AT_NULL]

    # ---- G24A cell-level cross-check on natural materials (REI -> raw pts)
    def rei_hw_raw(cell):
        hw_rei = (cell[2] - cell[1]) / 2.0
        hw_raw_469 = hw_rei * med_absL          # assumption: |L| ~ median
        return hw_rei, hw_raw_469, hw_raw_469 * math.sqrt(469.0 / C_DESIGN)

    rei_rows = {}
    for name, cell in (("REI_pre", rei_pre), ("REI_post", rei_post)):
        hw_rei, hw469, hw300 = rei_hw_raw(cell)
        rei_rows[name] = {
            "ci_rei": [round(cell[1], 4), round(cell[2], 4)],
            "hw_rei": round(hw_rei, 4),
            "hw_raw_at_C469": round(hw469, 3),
            "hw_raw_at_C300": round(hw300, 3),
            "declarable_at_C300": bool(hw300 < DELTA),
        }

    # ---- (b) verdict on delta=1.5 vs the noise floor at the design cap
    closest = next(r for r in rows if r["constant"] == CLOSEST_ANALOG)
    at_null = next(r for r in rows if r["constant"] == AT_NULL)
    verdict = {
        "declarable_under_closest_analog": closest["declarable_at_C300"],
        "hw_closest_analog_at_cap": closest["hw_at_C300"],
        "declarable_under_at_null": at_null["declarable_at_C300"],
        "hw_at_null_at_cap": at_null_hw,
        "equiv_power_m0_closest_analog": closest["equiv_power_m0_at_C300"],
        "equiv_power_m0_at_null": at_null["equiv_power_m0_at_C300"],
        "power80_reachable_under": [
            r["constant"] for r in rows
            if r["equiv_power_m0_at_C300"] >= POWER_TARGET],
        "statement": (
            "delta=1.5 is DECLARABLE (hw < 1.5) at C=300 under every "
            "two-cell constant except the effect-scale closest analog "
            f"{CLOSEST_ANALOG} (hw={binding_effect_scale:.2f} raw pts, "
            f"needs C={closest['C_needed_hw_lt_delta']} > cap 300) and "
            "except under the natural-materials cell-level cross-check. "
            "Declarability is not sufficient: 80% equivalence power at a "
            "true zero is reachable only under the smallest constants; "
            "under the closest analog it is unreachable at any C <= 300 "
            f"(would need C={closest['C_needed_power80']}). The at-null "
            f"constant gives power {at_null['equiv_power_m0_at_C300']:.0%} "
            "at C=300 — declarable, honestly under-80%."),
    }

    # ---- (c) options — USER DECISION before the Phase A tag; none applied
    opts = []
    # option 1: keep delta=1.5, equivalence powered only under the at-null
    # + local constants, closest-analog constant used for positive claims
    opts.append({
        "option": "keep_delta_1.5_at_null_binding",
        "delta": DELTA, "c_cap": C_DESIGN,
        "meaning": "equivalence branches may fire only under the at-null/"
                   f"local two-cell constants (hw {at_null_hw:.2f}-"
                   f"{hw_cap['gap_w001']:.2f} < 1.5; power "
                   f"{at_null['equiv_power_m0_at_C300']:.0%}-"
                   f"{next(r for r in rows if r['constant']=='gap_w001')['equiv_power_m0_at_C300']:.0%}"
                   " at true 0); the effect-scale constant stays reserved "
                   "for positive-claim CIs (no equivalence declared there).",
        "cost": "equivalence underpowered vs the 80% target; a reviewer "
                "asking 'powered for equivalence?' gets a <80% answer.",
    })
    # option 2: raise delta so that 80% power holds under the closest analog
    se_closest_cap = closest["hw_at_C300"] / Z975
    delta80_closest = (Z975 + Z_EQUIV_80) * se_closest_cap
    opts.append({
        "option": "raise_delta_to_80pct_under_closest_analog",
        "delta": round(delta80_closest, 2), "c_cap": C_DESIGN,
        "meaning": "delta moves from 1.5 to "
                   f"{delta80_closest:.2f} raw points so that hw < delta "
                   "with >=80% equivalence power at true 0 even under the "
                   f"effect-scale constant {CLOSEST_ANALOG}.",
        "cost": "a 'no gain' claim now tolerates a "
                f"{delta80_closest:.1f}-point band — weakens the ≈0 "
                "sentence; delta 1.5 never appears in any claim.",
    })
    # option 3: raise the cluster cap (feasibility shown, not recommended)
    opts.append({
        "option": "raise_c_cap_for_delta_1.5_closest_analog",
        "delta": DELTA, "c_cap": closest["C_needed_hw_lt_delta"],
        "meaning": "keep delta=1.5 and expand clusters until the "
                   f"closest-analog constant is declarable "
                   f"(C={closest['C_needed_hw_lt_delta']}).",
        "cost": "exceeds the prereg cap 300 by "
                f"{closest['C_needed_hw_lt_delta'] - C_DESIGN} clusters; "
                "80% power still needs "
                f"C={closest['C_needed_power80']} — infeasible; shown "
                "only to price the infeasibility honestly.",
    })

    note = {
        "prereg": "PREREGISTRATION_G26A_LOAD_BEARING.md §0 O5 / §7",
        "zero_model": True,
        "inputs": {
            "g23a": os.path.relpath(G23A, ROOT),
            "g24a": os.path.relpath(G24A, ROOT),
            "g23a_delta_ci": [round(d["ci_low"], 3), round(d["ci_high"], 3)],
            "g23a_clusters": c68,
            "g24a_cell_clusters": 469,
            "g24a_median_absL": round(med_absL, 3),
        },
        "design": {"delta": DELTA, "c_cap": C_DESIGN,
                   "n_cap": N_DESIGN_MAX, "power_target": POWER_TARGET},
        "four_cell_reference": {
            "constant": "delta_zero", "hw_at_68": round(hw_delta, 3),
            "C_needed_hw_lt_delta": math.ceil(c_needed_4cell),
            "note": "reproduces §7's '> 604 clusters, impossible at cap 300'",
        },
        "two_cell_constants": rows,
        "natural_materials_cross_check": {
            "cells": rei_rows,
            "assumption": "REI units -> raw points via recorded median |L| "
                          "(per-row |L| varies; treat as stress-test, not "
                          "the binding constant)",
        },
        "binding": {
            "closest_analog": CLOSEST_ANALOG,
            "hw_at_cap_effect_scale": binding_effect_scale,
            "largest_two_cell_constant": binding_effect_key,
            "at_null_constant": AT_NULL, "hw_at_cap_at_null": at_null_hw,
        },
        "verdict_b": verdict,
        "options_c_user_decision": opts,
        "decision_owner": "user, BEFORE the Phase A tag (never after "
                          "outcomes exist); this script decides nothing",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(note, f, indent=1, ensure_ascii=False)
    print(json.dumps(note, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
