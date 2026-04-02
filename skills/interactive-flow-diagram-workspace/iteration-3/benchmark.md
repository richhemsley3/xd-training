# Interactive Flow Diagram - Iteration 3 Benchmark

## Results Summary

| Eval | With Skill | Without Skill | Delta |
|------|-----------|---------------|-------|
| onboarding-flow | 12/12 (100%) | 9/10 (90%) | +10% |
| checkout-flow | 15/15 (100%) | 11/13 (84.6%) | +15.4% |
| mermaid-conversion | 15/15 (100%) | 11/13 (84.6%) | +15.4% |

## Aggregate

| Metric | With Skill | Without Skill |
|--------|-----------|---------------|
| Mean Pass Rate | **100.0%** | 86.4% |
| Stddev | 0.0 | 0.025 |
| Mean Tokens | n/a | 31,207 |
| Mean Time (s) | n/a | 93.2 |

**Overall Delta: +13.6 percentage points**

## Notable Findings

- **With skill achieved a perfect 100% pass rate across all 3 evals** (42/42 assertions).
- Without skill consistently failed the "Uses D3.js from CDN" assertion across all 3 evals. The skill enforces D3.js usage as a core architectural choice.
- Without skill also missed "Breadcrumb or back navigation" on checkout-flow and "Orthogonal connectors" on mermaid-conversion.
- Timing data was only available for 2 of 3 without_skill runs (no timing for checkout-flow without_skill, none for any with_skill runs).
