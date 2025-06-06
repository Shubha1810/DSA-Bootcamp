#  Insertion Sort Implementation in Python
## Problem Statement

Given a list of integers, sort the array in **ascending order** using the **Insertion Sort** algorithm. The user provides the number of elements and each element in the list via input.

---

## Approach / Thought Process

**Insertion Sort** works by building the final sorted array one element at a time. It picks an element from the unsorted portion and places it at the correct position in the sorted portion.

Steps:
1. Start from the second element (`index = 1`) as the first is trivially sorted.
2. Compare the current element (`key`) with those before it.
3. Shift all elements greater than `key` one position to the right.
4. Insert the `key` at its correct position.
5. Repeat until the entire array is sorted.

This algorithm is **in-place**, meaning no extra space is used, and it’s **stable**, preserving the order of equal elements.

---

##  Time & Space Complexity
| Case             | Explanation                                                                         | Complexity |
| ---------------- | ----------------------------------------------------------------------------------- | ---------- |
| **Best Case**    | The array is already sorted. Only one comparison per element is needed.             | O(n)       |
| **Average Case** | Elements are in random order. Each element may shift multiple positions.            | O(n²)      |
| **Worst Case**   | The array is in reverse order. Each new element is compared with all previous ones. | O(n²)      |

- `n` is the number of elements in the array.
- The algorithm uses constant auxiliary space (`O(1)`).


