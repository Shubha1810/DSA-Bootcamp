# Subarray with Zero Sum (Python)

This Python script checks whether a **subarray with a sum of 0** exists in the given array. It prints `True` and the subarray (if any) or `False` otherwise.

---

## Problem Statement

Given an array of integers (positive, negative, or zero), check if there exists at least one **contiguous subarray** whose sum is equal to 0.  
If such a subarray exists, print it and return `True`; otherwise, return `False`.

---

## Approach / Thought Process

We use a **brute-force** approach:

1. First, check if any individual element is 0 (a single-element subarray with zero sum).
2. If not found, use **two nested loops** to find all possible subarrays:
   - Outer loop chooses the starting index
   - Inner loop chooses the ending index
   - For each subarray, compute the sum
3. If a subarray with sum = 0 is found, print it and exit.

---

## Time & Space Complexity

| Case               | Time Complexity | Space Complexity |
|--------------------|------------------|------------------|
| All cases (Brute)  | O(n²)            | O(1)             |

- `n` is the number of elements in the array.
- We use only a constant amount of space (`temp`, `i`, `j`, etc.)

