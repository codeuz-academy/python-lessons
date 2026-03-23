---
title: Dynamic Programming
description: Memoization, tabulation, and classic DP problems
order: 5
permalink: /en/algorithms/dynamic-programming/
---

Dynamic Programming (DP) stores overlapping subproblem results.

## When to Use DP

- Problem asks for optimal count/cost/length.
- Naive recursion repeats same states.
- State can be defined with small parameters.

## Example: Climbing Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
```

Time: `O(n)`
Space: `O(1)`

## Example: Coin Change (Minimum Coins)

```python
def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for x in range(1, amount + 1):
        for c in coins:
            if c <= x:
                dp[x] = min(dp[x], dp[x - c] + 1)

    return dp[amount] if dp[amount] <= amount else -1
```

Time: `O(amount * len(coins))`
Space: `O(amount)`

## Example: Fibonacci (Top-Down vs Bottom-Up)

### Top-Down (Memoization)

```python
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

### Bottom-Up (Tabulation)

```python
def fib_bottom_up(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```

## DP Checklist

1. Define state precisely.
2. Define transition relation.
3. Set base cases.
4. Choose top-down or bottom-up.
5. Optimize space if only recent rows/states are needed.

## Classic Problems

### 1. 0/1 Knapsack

Given weights and values of `n` items, pick a subset to maximize value without exceeding a weight capacity `W`. Each item can be picked at most once (0 or 1 time).

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[w] stores the max value for capacity w
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse backwards to prevent using the same item multiple times
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

- Time: `O(n * W)`
- Space: `O(W)` (Optimized from `O(n * W)` 2D array)

### 2. Longest Increasing Subsequence (LIS)

Find the length of the longest strictly increasing subsequence in an array.

```python
def length_of_lis(nums):
    if not nums:
        return 0
        
    # dp[i] stores the LIS ending at index i
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)
```

- Time: `O(n^2)`
- Space: `O(n)`

*(Note: There is also an advanced `O(n log n)` solution using binary search, but the DP approach perfectly illustrates the state transition: `dp[i] = max(dp[i], dp[j] + 1)`).*
