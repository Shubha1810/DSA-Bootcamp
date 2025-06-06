# Kadane's Algorithm - Maximum Subarray Sum (Python)

This Python script implements **Kadane’s Algorithm** to find the **maximum sum of any contiguous subarray** in a given list of integers.

## Problem Statement

Given an array of integers (positive, negative, or both), find the **maximum sum of any contiguous subarray**.  
This problem is often referred to as the **Maximum Subarray Problem**.

---

## Approach / Thought Process

We use **Kadane’s Algorithm**, which is a **Dynamic Programming** approach to solve this in linear time:

1. Start with `max_current = max_global = array[0]`
2. Traverse the array from index `1`:
   - At each index, calculate:  
     `max_current = max(array[i], max_current + array[i])`
   - Update:  
     `max_global = max(max_global, max_current)`
3. Finally, `max_global` holds the result.

The logic is: *either start a new subarray at index `i`, or extend the previous subarray to include `array[i]`.*


## Time & Space Complexity

| Case          | Time Complexity | Space Complexity |
|---------------|------------------|------------------|
| All cases     | O(n)             | O(1)             |

- `n` is the number of elements in the array.
- Only constant space is used for tracking current and global maximums.


