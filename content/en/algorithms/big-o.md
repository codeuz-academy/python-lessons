---
title: Big-O and Analysis
description: Growth rate analysis, estimation rules, and common complexity patterns
order: 1
permalink: /en/algorithms/big-o/
---

Big-O describes growth rate as input size `n` increases.

## Why It Matters

- Helps compare solutions independent of hardware.
- Predicts behavior on large inputs.
- Guides data structure choices.

## Fast Complexity Estimation Rules

1. Keep only the dominant term (`n^2 + n -> n^2`).
2. Drop constants (`5n -> n`).
3. Sequential blocks add (`O(a + b)`).
4. Nested loops multiply (`O(a * b)`).

## Examples

```python
def sum_all(nums):
    total = 0
    for x in nums:
        total += x
    return total
```

Time: `O(n)`
Space: `O(1)`

```python
def all_pairs(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result.append((nums[i], nums[j]))
    return result
```

Time: `O(n^2)`
Space: `O(n^2)` due to output size.

## Amortized Analysis

Some operations are occasionally expensive but cheap on average.

- Dynamic array append: occasional resize `O(n)`, average `O(1)` amortized.

## Quick Pattern Map

| Pattern                      | Typical Complexity |
| ---------------------------- | ------------------ |
| Single loop                  | `O(n)`             |
| Nested loops over same input | `O(n^2)`           |
| Divide by 2 each step        | `O(log n)`         |
| Loop + binary operation      | `O(n log n)`       |

## Practice

1. Analyze complexity of finding max value in a list.
2. Analyze nested loops where inner loop runs `k` times only.
3. Compare linear search vs binary search complexity.
