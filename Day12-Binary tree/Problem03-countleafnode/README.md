
```markdown
# 🍃 Count Leaf Nodes in a Binary Tree (Python)

This Python program counts the number of **leaf nodes** in a binary tree using recursion.

---

## 🔍 Problem Statement

Given the root of a binary tree, write a program to **count the number of leaf nodes**.

📌 Definition:  
A **leaf node** is a node that **does not have any children** (i.e., both `left` and `right` pointers are `None`).

---

## 💡 Approach / Thought Process

- Use a **recursive** function `count_leaf_nodes(root)`:
  - **Base case**: If the node is `None`, return `0`.
  - If the node has **no left and right children**, it's a leaf → return `1`.
  - Otherwise, recursively count leaf nodes in left and right subtrees and return their sum.

---

## 🌲 Tree Structure Used

```

```
    1
   / \
  2   3
 / \
4   5
```

```

### ✅ Leaf Nodes:
- Nodes 4, 5, and 3 (total = 3)

---

## ⌛ Time & Space Complexity

| Operation         | Time Complexity | Space Complexity |
|------------------|------------------|------------------|
| Leaf Count       | O(n)             | O(h)             |

- `n` = total number of nodes  
- `h` = height of the tree (due to recursive call stack)

---

## 🧪 Sample Output

```

Number of leaf nodes: 3

