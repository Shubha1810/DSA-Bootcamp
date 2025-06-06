# Sliding Window Maximum Subarray Sum (Python)

This Python script calculates the **maximum sum of any contiguous subarray of size `k`** using the **Sliding Window Technique**, which improves performance by reducing unnecessary recalculations.

---

## Problem Statement

Given an integer array and a number `k`, find the **maximum sum** possible from any contiguous subarray of size `k`.

---

## Approach / Thought Process

We use the **Sliding Window Technique** to maintain a window of size `k` as we traverse the array.

### Steps:
1. Compute the sum of the first `k` elements. This becomes the initial `window_sum`.
2. Move the window forward by one element at a time:
   - Subtract the element that goes out of the window.
   - Add the new element that comes into the window.
3. Keep track of the **maximum sum** encountered during the traversal.

This avoids recomputing the sum of each subarray from scratch, improving performance from `O(n*k)` to `O(n)`.

---

## Time & Space Complexity

### Time Complexity

| Operation                      | Complexity |
|-------------------------------|------------|
| Traverse the array once       | O(n)       |
| Sum calculation (first window)| O(k)       |
| Total                         | **O(n)**   |

- `n` is the number of elements in the array.
- Each element is visited once after the first window sum is computed.

### Space Complexity

| Resource Used      | Complexity |
|--------------------|------------|
| Variables and subarray sum | O(1)       |

- No additional data structures are used, only a few variables — hence it's constant space.

