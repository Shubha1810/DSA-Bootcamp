```markdown
# 🌀 Fibonacci Sequence with Memoization (Python)

This Python program prints the **first 500 Fibonacci numbers** using **memoization** via the `functools.lru_cache` decorator to greatly improve performance by caching previous results.

---

## 🔍 Problem Statement

Write a Python function to compute the `n`th Fibonacci number efficiently and print the first 500 Fibonacci numbers.

### 📌 Fibonacci Formula:

```

F(n) = F(n-1) + F(n-2)
F(1) = 1, F(2) = 1

```

---

## 💡 Approach / Thought Process

- A simple recursive solution to Fibonacci has exponential time complexity.
- We use **memoization** with `@lru_cache` to **store results of previous function calls** and avoid redundant computation.
- This makes the recursive approach efficient even for large `n`.

---

## 🚀 Technologies Used

- `Python 3`
- `functools.lru_cache` for memoization

---

## ⌛ Time & Space Complexity

| Aspect             | Complexity |
|--------------------|------------|
| Time Complexity    | O(n)       |
| Space Complexity   | O(n) (for cache & recursion stack) |

- Each value from `1 to n` is computed only once and then reused from cache.

---

## 🧪 Sample Output

```

1 : 1
2 : 1
3 : 2
4 : 3
5 : 5
...
500 : 139423224561697880139045716414506361683613000452408302021628736001016217483508679892259414274289305843112264702306604463413296880

````

---

## 🛠️ How to Run

1. Save the file as `fibonacci_memoized.py`
2. Run the script using:

```bash
python fibonacci_memoized.py
````

---

## 📌 Notes

* The cache size `maxsize=1000` is enough to store results for all values up to `n = 500`.
* Without memoization, computing even `fibonacci(50)` via recursion would be very slow.

---
