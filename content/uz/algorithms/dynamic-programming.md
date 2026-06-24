---
title: Dinamik dasturlash (Dynamic Programming)
description: Memoizatsiya (Memoization), tabulyatsiya (Tabulation) va klassik DP masalalari
order: 5
permalink: /uz/algorithms/dynamic-programming/
---

Dinamik dasturlash (Dynamic Programming, DP) bir-biriga kesishuvchi qism masalalarning (subproblem) natijalarini saqlab qoladi.

## DP qachon ishlatiladi

- Masala optimal son/qiymat/uzunlikni topishni talab qiladi.
- Oddiy rekursiya bir xil holatlarni qayta-qayta hisoblayveradi.
- Holat (state) kichik parametrlar yordamida aniqlanishi mumkin.

## Misol: Zinapoyaga chiqish (Climbing Stairs)

```python
def climb_stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
```

Vaqt: `O(n)`
Xotira: `O(1)`

## Misol: Tangalarni almashtirish (Coin Change — minimal tangalar soni)

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

Vaqt: `O(amount * len(coins))`
Xotira: `O(amount)`

## Misol: Fibonachchi (Yuqoridan pastga vs Pastdan yuqoriga)

### Yuqoridan pastga (Memoizatsiya)

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

### Pastdan yuqoriga (Tabulyatsiya)

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

## DP tekshiruv ro'yxati

1. Holatni (state) aniq belgilang.
2. O'tish munosabatini (transition) aniqlang.
3. Boshlang'ich holatlarni (base case) o'rnating.
4. Yuqoridan pastga yoki pastdan yuqoriga usulni tanlang.
5. Agar faqat oxirgi qatorlar/holatlar kerak bo'lsa, xotirani optimallashtiring.

## Klassik masalalar

### 1. 0/1 Knapsack (Ryukzak masalasi)

`n` ta predmetning og'irliklari va qiymatlari berilgan; `W` og'irlik sig'imidan oshmasdan qiymatni maksimal qiladigan qism to'plamni tanlang. Har bir predmet ko'pi bilan bir marta (0 yoki 1 marta) tanlanishi mumkin.

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[w] — w sig'imi uchun maksimal qiymatni saqlaydi
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Bir xil predmetni bir necha marta ishlatmaslik uchun teskari yo'nalishda yuramiz
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

- Vaqt: `O(n * W)`
- Xotira: `O(W)` (`O(n * W)` 2D massivdan optimallashtirilgan)

### 2. Eng uzun o'suvchi qism ketma-ketlik (Longest Increasing Subsequence, LIS)

Massivdagi eng uzun qat'iy o'suvchi qism ketma-ketlikning uzunligini toping.

```python
def length_of_lis(nums):
    if not nums:
        return 0
        
    # dp[i] — i indeksida tugaydigan LIS uzunligini saqlaydi
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)
```

- Vaqt: `O(n^2)`
- Xotira: `O(n)`

*(Eslatma: Ikkilamchi qidirish (binary search) yordamida ishlaydigan ilg'or `O(n log n)` yechim ham mavjud, lekin DP usuli holatlar orasidagi o'tishni juda yaxshi ko'rsatib beradi: `dp[i] = max(dp[i], dp[j] + 1)`).*
