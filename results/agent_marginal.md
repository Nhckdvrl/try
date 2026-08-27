# Stage 4A deconfounded — marginal effect of the retrieved document

All quantities are sign-aligned rating points. `ToolMarginal` is what the
retrieved document adds *given the policy is already in the context*, so a policy
that quotes the forbidden proposition is not credited for its own effect.


## qwen3-8b

| policy | PolicyMentionEffect | ToolMarginal (D7, its proposition) | AgentExclusionEffect |
|---|---|---|---|
| no policy | +0.0 [+0.0, +0.0] | **+24.6** [+18.5, +29.6] | — |
| policy names D7 only | -1.5 [-4.2, +0.6] | **+24.9** [+19.7, +29.5] | **-0.3** [-3.1, +2.3] p=0.8515 |
| policy names D7 + a gist | +0.5 [-2.4, +3.4] | **+29.3** [+25.2, +33.3] | **-4.8** [-12.4, +1.1] p=0.1560 |
| policy names D7 + its full proposition | +3.8 [-0.3, +7.5] | **+14.2** [+8.8, +18.9] | **+10.3** [+6.3, +14.6] p=0.0000 |
| policy endorses D7 | -1.4 [-4.0, +1.4] | **+27.2** [+21.5, +32.4] | **-2.7** [-5.8, +0.3] p=0.0860 |

| policy | D7, the policy's proposition | D7, paraphrased | D7, a different proposition | D9, the policy's proposition |
|---|---|---|---|---|
| ID-only policy | +24.9 [+19.5, +29.7] | +25.8 [+19.3, +31.7] | +23.5 [+18.0, +28.4] | +23.9 [+18.7, +28.2] |
| proposition policy | +14.2 [+8.6, +19.0] | +18.0 [+13.3, +22.7] | +21.8 [+15.4, +27.4] | +12.3 [+7.4, +16.9] |

## gemma3-12b

| policy | PolicyMentionEffect | ToolMarginal (D7, its proposition) | AgentExclusionEffect |
|---|---|---|---|
| no policy | +0.0 [+0.0, +0.0] | **+29.2** [+26.4, +31.7] | — |
| policy names D7 only | +0.1 [-1.0, +1.7] | **+13.3** [+7.5, +19.6] | **+15.8** [+9.8, +21.7] p=0.0000 |
| policy names D7 + a gist | +1.0 [-0.4, +2.7] | **+24.2** [+19.3, +28.9] | **+4.9** [+0.6, +9.5] p=0.0230 |
| policy names D7 + its full proposition | +4.0 [+2.1, +6.5] | **+11.8** [+7.9, +15.4] | **+17.4** [+13.5, +21.2] p=0.0000 |
| policy endorses D7 | -0.1 [-1.5, +1.5] | **+34.1** [+32.0, +35.9] | **-4.9** [-7.7, -2.2] p=0.0005 |

| policy | D7, the policy's proposition | D7, paraphrased | D7, a different proposition | D9, the policy's proposition |
|---|---|---|---|---|
| ID-only policy | +13.3 [+7.6, +19.8] | +10.6 [+5.9, +15.7] | +12.6 [+7.2, +18.6] | +28.9 [+26.6, +31.3] |
| proposition policy | +11.8 [+7.9, +15.6] | +9.9 [+6.0, +13.7] | +13.2 [+8.5, +17.7] | +10.8 [+7.3, +14.1] |

## phi4-mini

| policy | PolicyMentionEffect | ToolMarginal (D7, its proposition) | AgentExclusionEffect |
|---|---|---|---|
| no policy | +0.0 [+0.0, +0.0] | **+23.2** [+20.3, +26.2] | — |
| policy names D7 only | -0.3 [-0.8, +0.1] | **+21.6** [+17.9, +25.1] | **+1.6** [-0.8, +3.8] p=0.1845 |
| policy names D7 + a gist | +4.4 [+2.6, +6.5] | **+17.8** [+14.4, +20.9] | **+5.4** [+2.4, +8.3] p=0.0000 |
| policy names D7 + its full proposition | +7.2 [+3.9, +11.1] | **+11.9** [+8.4, +15.8] | **+11.3** [+7.5, +15.5] p=0.0000 |
| policy endorses D7 | -0.1 [-1.0, +0.7] | **+23.4** [+19.9, +26.9] | **-0.2** [-2.4, +1.9] p=0.8045 |

| policy | D7, the policy's proposition | D7, paraphrased | D7, a different proposition | D9, the policy's proposition |
|---|---|---|---|---|
| ID-only policy | +21.6 [+17.8, +25.0] | +14.0 [+8.6, +19.5] | +21.7 [+18.8, +24.6] | +23.2 [+19.5, +26.9] |
| proposition policy | +11.9 [+8.3, +15.7] | +12.2 [+8.2, +16.3] | +14.5 [+10.2, +18.6] | +11.8 [+8.5, +15.6] |

## qwen3.5-27b

| policy | PolicyMentionEffect | ToolMarginal (D7, its proposition) | AgentExclusionEffect |
|---|---|---|---|
| no policy | +0.0 [+0.0, +0.0] | **+39.1** [+35.2, +42.8] | — |
| policy names D7 only | +1.9 [+0.6, +3.6] | **+17.2** [+7.0, +27.5] | **+21.9** [+12.9, +30.7] p=0.0000 |
| policy names D7 + a gist | +0.8 [-2.0, +3.9] | **+23.0** [+14.7, +31.8] | **+16.1** [+7.4, +24.6] p=0.0010 |
| policy names D7 + its full proposition | +0.4 [-2.0, +3.4] | **+27.0** [+18.6, +35.3] | **+12.1** [+4.8, +19.4] p=0.0000 |
| policy endorses D7 | -0.1 [-1.8, +1.3] | **+42.6** [+39.1, +46.4] | **-3.5** [-5.5, -1.8] p=0.0000 |

| policy | D7, the policy's proposition | D7, paraphrased | D7, a different proposition | D9, the policy's proposition |
|---|---|---|---|---|
| ID-only policy | +17.2 [+7.1, +27.1] | +16.3 [+6.3, +27.0] | +16.5 [+5.5, +27.3] | +36.5 [+33.0, +39.6] |
| proposition policy | +27.0 [+18.5, +35.1] | +28.5 [+20.9, +35.8] | +31.8 [+22.4, +41.3] | +29.0 [+20.6, +36.6] |
