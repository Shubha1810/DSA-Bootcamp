Here’s a detailed and professional `README.md` file for your **Tower of Hanoi** Python program:

---

````markdown
# 🗼 Tower of Hanoi - Recursive Python Solution

This Python script provides a solution to the classic **Tower of Hanoi** problem using recursion. The goal is to move all disks from a source rod to a destination rod using an auxiliary rod, following specific rules.

---

## 🔍 Problem Statement

Given **`n` disks** stacked in increasing size on a **source rod (A)**, move them all to a **destination rod (C)** using an **auxiliary rod (B)**, while obeying the following rules:

1. Only one disk may be moved at a time.
2. A disk can only be moved if it is the uppermost disk on a rod.
3. No disk may be placed on top of a smaller disk.

---

## 💡 Approach / Thought Process

This is a **classic recursive problem**.  
The idea is to break down the problem into smaller subproblems:

- Move `n-1` disks from **source** to **auxiliary**.
- Move the largest disk (`n`) from **source** to **destination**.
- Move `n-1` disks from **auxiliary** to **destination**.

This is done recursively until the base case of `n == 1`.

---

## ⌛ Time & Space Complexity

| Metric             | Complexity         |
|--------------------|--------------------|
| Time Complexity     | O(2ⁿ - 1)           |
| Space Complexity    | O(n) (due to recursion stack) |

---

## 🧪 Sample Inputs & Outputs

### 🔢 Input:
```python
n = 3
````

### 🖨️ Output:

```
Move disk 1 from rod A to rod C  
Move disk 2 from rod A to rod B  
Move disk 1 from rod C to rod B  
Move disk 3 from rod A to rod C  
Move disk 1 from rod B to rod A  
Move disk 2 from rod B to rod C  
Move disk 1 from rod A to rod C  
Total moves: 7
```

---

### 🔢 Input:

```python
n = 2
```

### 🖨️ Output:

```
Move disk 1 from rod A to rod B  
Move disk 2 from rod A to rod C  
Move disk 1 from rod B to rod C  
Total moves: 3
```