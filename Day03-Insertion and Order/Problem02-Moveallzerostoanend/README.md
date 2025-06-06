#  Move All Zeros to End (Python)

This Python script modifies an input array to **move all the `0`s to the end** of the array **in-place** while maintaining the **relative order of the non-zero elements**.

## Problem Statement

Given an array of integers, move all zeros to the end **without using extra space** and **without changing the order** of the non-zero elements.

## Approach / Thought Process

We use a **two-pointer approach**:

1. Maintain a `non_zero_index` which keeps track of the position where the next non-zero element should go.
2. Traverse the array:
   - If the current element is not `0`, copy it to the `non_zero_index`, then increment the index.
3. After all non-zero elements are repositioned, fill the remaining positions in the array with `0`s.

This ensures in-place modification and maintains order.


## Time & Space Complexity

| Case         | Time Complexity | Space Complexity |
|--------------|------------------|------------------|
| All cases    | O(n)             | O(1)             |

- `n` is the number of elements in the array.
- Space complexity is constant as the operation is performed in-place.


