

```markdown
# 🗳️ Majority Element Finder using Boyer-Moore Algorithm (Python)

This Python program identifies the **majority element** in an array — the element that appears more than `n/2` times — using the **Boyer-Moore Voting Algorithm**, an efficient approach with linear time and constant space complexity.

---

## 🔍 Problem Statement

Given an array of integers, determine the **majority element**, i.e., the element that appears more than `⌊n/2⌋` times.

> If such an element is guaranteed to exist, return it.

---

## 💡 Approach / Thought Process

### ✅ Boyer-Moore Voting Algorithm

- Maintains a `candidate` and a `count`.
- If `count` is 0, a new candidate is chosen.
- If the current element matches the candidate, `count` is incremented, else it’s decremented.
- The final candidate is the majority element (assuming it exists).

This algorithm works in:
- **One pass** (O(n) time)
- **Constant space** (O(1) space)

---

## ⚙️ Program Flow

1. User is prompted to enter the number of elements in the array.
2. The user inputs each element one by one.
3. The program computes and prints the majority element using the algorithm.

---

## ⌛ Time & Space Complexity

| Operation          | Complexity |
|-------------------|------------|
| Time Complexity    | O(n)       |
| Space Complexity   | O(1)       |

---

## 🧪 Sample Input / Output

### **Input:**

```

Enter the Length of Array = 7
Enter elements in the array:
Element 1: 3
Element 2: 3
Element 3: 4
Element 4: 2
Element 5: 3
Element 6: 3
Element 7: 3

```

### **Output:**

```

Array = \[3, 3, 4, 2, 3, 3, 3]

Majority Element is: 3

````

---


