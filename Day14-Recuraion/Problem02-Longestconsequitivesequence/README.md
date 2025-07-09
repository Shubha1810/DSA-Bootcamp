Here’s your `README.md` file for the **Longest Consecutive Sequence** problem using Python:

---

```markdown
# 🔗 Longest Consecutive Sequence (Python)

This Python program finds the **length of the longest consecutive sequence** of integers in an unsorted array using a `set` for O(n) time complexity.

---

## 🔍 Problem Statement

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

### ✅ Constraint:
- You must implement an algorithm that runs in **O(n)** time.

📌 Example:  
Input: `[100, 4, 200, 1, 3, 2]`  
Output: `4` (The sequence `[1, 2, 3, 4]` is the longest)

---

## 💡 Approach / Thought Process

- Convert the list to a `set` for O(1) lookups.
- Iterate through each number:
  - Only start counting if `(num - 1)` is **not** in the set (indicating the start of a sequence).
  - Then check how long the streak goes `(num+1, num+2,...)` and keep updating the max length.
- Efficient and avoids sorting the input.

---

## ⌛ Time & Space Complexity

| Metric             | Complexity |
|--------------------|------------|
| Time Complexity     | O(n)       |
| Space Complexity    | O(n)       |

---

## 🧪 Sample Input & Output

### ✅ Sample Input:
```

Enter the Length of Array = 6
Enter elements in the array:
Element 1: 100
Element 2: 4
Element 3: 200
Element 4: 1
Element 5: 3
Element 6: 2

```

### ✅ Sample Output:
```

Array = \[100, 4, 200, 1, 3, 2]

Length of Longest Consecutive Sequence: 4

````



