Here is a complete `README.md` file for your **Mirror of a Binary Tree** Python program:

---

```markdown
# 🔁 Mirror a Binary Tree and Inorder Traversal (Python)

This Python script creates a binary tree, prints its **inorder traversal**, then mirrors the tree (i.e., swaps left and right subtrees recursively) and prints the **inorder traversal** of the mirrored tree.

---

## 🔍 Problem Statement

Given a binary tree, write a program to:
1. Perform **inorder traversal** of the original tree.
2. Create its **mirror** by swapping left and right children of every node.
3. Perform **inorder traversal** of the mirrored tree.

---

## 💡 Approach / Thought Process

### ✅ Inorder Traversal:
- Traverse the tree recursively in the order: `left → root → right`.

### ✅ Mirror Function:
- Recursively swap the left and right children of each node.
- The process is done in-place using post-order recursion (children first, then swap).

---

## 🌲 Tree Structure Used

### Original Tree:
```

```
    1
   / \
  2   3
 / \
4   5
```

```

### Mirrored Tree:
```

```
    1
   / \
  3   2
     / \
    5   4
```

```

---

## ⌛ Time & Space Complexity

| Operation         | Time Complexity | Space Complexity |
|------------------|------------------|------------------|
| Inorder Traversal | O(n)             | O(h)             |
| Mirroring         | O(n)             | O(h)             |

- `n` = number of nodes  
- `h` = height of the tree (due to recursion)

---

## 🧪 Sample Output

```

Inorder traversal before mirror: 4 2 5 1 3
Inorder traversal after mirror: 3 1 5 2 4

````

---

