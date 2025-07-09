
```markdown
# 🌳 Lowest Common Ancestor in a Binary Tree (Python)

This Python program finds the **Lowest Common Ancestor (LCA)** of two nodes in a binary tree using a recursive approach. The LCA of two nodes `p` and `q` is the lowest node in the tree that has both `p` and `q` as descendants.

---

## 🔍 Problem Statement

Given a binary tree and two node values, find their **Lowest Common Ancestor (LCA)**.  
The tree is **not** necessarily a Binary Search Tree (BST), so you cannot rely on ordering properties.

---

## 💡 Approach / Thought Process

### ✅ Recursive DFS (Depth-First Search)

1. Start from the root node.
2. If the root is `None`, return `None`.
3. If the root matches either `p` or `q`, return the root.
4. Recursively check the left and right subtrees for `p` and `q`.
5. If both left and right recursive calls return non-`None`, the current node is the LCA.
6. If only one side is non-`None`, return that one (propagate the ancestor upwards).

---

## ⌛ Time & Space Complexity

| Metric           | Complexity |
|------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(h)       |

> Where `n` is the number of nodes in the tree and `h` is the height of the tree (due to recursion stack).

---

## 🧪 Sample Input & Output

### 🧾 Tree Structure

```

```
       3
     /   \
    5     1
   / \   / \
  6   2 0   8
     / \
    7   4
```

```

### 🔢 Example 1:
```

Input: p = 5, q = 1
Output: 3

```

### 🔢 Example 2:
```

Input: p = 5, q = 4
Output: 5

````
