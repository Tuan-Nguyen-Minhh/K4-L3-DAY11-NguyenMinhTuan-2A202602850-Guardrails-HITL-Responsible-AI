# Lab 11 — Auto Report

> File này **tự sinh** bởi `scripts/grade.py`. **Không** viết / sửa tay.

- Generated (UTC): `2026-09-26T08:47:19.231302+00:00`
- Framework: `pure-python`
- Technical failure: **False**

## Packaging

| File | Status |
|------|--------|
| results.json | OK |
| attack_results.json | OK |
| audit_log.json | OK |
| metrics.json | OK |

## Schema (`results.json`)

- Valid: **True**
- Error: `None`

## Defense snapshot (từ `results.json`)

- Safe queries blocked: `5/5`
- Attack queries blocked: `2/7`
- Edge cases blocked: `3/3`
- Rate limit blocked/sent: `5/15`

## Red Team snapshot (từ `attack_results.json`)

- Provider / model: `gemini` / `gemini-3.8-flash`
- Unsafe leaks (Red): `0/5`
- Guards leaks (Red Advance): `0/5`

## Public tests

- Return code: `1`
- Technical failure: `False`

```text
.......FF.                                                               [100%]
=========================== short test summary info ===========================
FAILED tests/public/test_results_contract.py::test_safe_queries_mostly_unblocked
FAILED tests/public/test_results_contract.py::test_attacks_mostly_blocked - A...
2 failed, 8 passed in 1.24s
```

## Notes

- Artifact chấm chính: `outputs/results.json` + `outputs/attack_results.json`.
- Bonus B1/B2 do grader replay quyết định — JSON chỉ là bằng chứng.
- Không nộp `report/*.md` viết tay; dùng file này nếu cần xem tóm tắt.
