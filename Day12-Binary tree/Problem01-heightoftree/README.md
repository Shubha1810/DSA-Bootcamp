# 🌳 Binary Tree Height Calculation (Python)

This Python script computes the **height of a binary tree** using recursion. The height is defined as the number of edges on the longest path from the root to a leaf.

---

## 🔍 Problem Statement

Given the root of a binary tree, calculate the **height of the tree**.

📌 Definition:  
- Height of a binary tree = Number of edges on the longest path from root to any leaf node.
- A tree with only the root node has a height of `0`.
- An empty tree has a height of `-1`.

---

## 💡 Approach / Thought Process

- Use a recursive function `get_tree_height` to compute the height.
- Base case: If the node is `None`, return `-1`.
- Recursive case:
  - Calculate the height of left and right subtrees.
  - Return `1 + max(left_height, right_height)`

> The recursive call dives down to the leaf level, then bubbles up the height values.

---

## ⌛ Time & Space Complexity

| Operation               | Time Complexity | Space Complexity |
|------------------------|------------------|------------------|
| Height Calculation     | O(n)             | O(h)             |

- `n` = number of nodes in the tree  
- `h` = height of the tree (due to recursion stack)

---

## 🧪 Sample Input & Output

### ✅ Sample Tree Structure

    1
   / \
  2   3
 / \  /
4  5 6
