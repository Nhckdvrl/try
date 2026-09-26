# ConfB restoration-control reanalysis (exploratory, post hoc)

Source: committed `g24a_confb_analysis_v1_cells.csv`; all 200 fresh claims × six models, no filters. Claims are the paired bootstrap unit (5,000 draws). Scores are 0–100. This analysis was conceived after the registered ConfB report and has no confirmatory status.

| Quantity | Mean [paired bootstrap 95% CI] |
|---|---:|
| CRE of actual CF center | 29.96 [28.14, 31.79] |
| Mean arm-wise absolute restoration error | 30.88 [29.10, 32.64] |
| Error of WithheldCF | 21.03 [19.61, 22.45] |
| Error of IrrelevantCF | 25.82 [24.04, 27.72] |
| Error of constant 50 predictor | 35.99 [34.58, 37.42] |
| Actual CF center error minus IrrelevantCF error | 4.14 [2.37, 5.92] |
| Actual CF center error minus WithheldCF error | 8.93 [7.18, 10.67] |
| Actual CF center error minus constant 50 error | -6.03 [-7.73, -4.43] |

Exact model×claim counts: both CF arms within 5 points of Y0: 153/1200; within 10 points: 208/1200.

Interpretation limit: the arm-center CRE can understate arm-wise errors by cancellation; WithheldCF and IrrelevantCF have different prompts from actual CF and are descriptive controls. The constant-50 comparison is a calibration reference, not a proposed retraction method.
