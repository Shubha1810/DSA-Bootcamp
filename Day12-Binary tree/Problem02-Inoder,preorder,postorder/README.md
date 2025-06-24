# 🌳 Binary Tree Traversals & Height Calculation (Python)

This Python program demonstrates three primary **binary tree traversal techniques**—**Inorder**, **Preorder**, and **Postorder**—and computes the **height** of a binary tree using recursion.

---

## 🔍 Problem Statement

Implement a binary tree with:
- Support for building nodes manually
- Perform **Inorder**, **Preorder**, and **Postorder** traversals
- Calculate and display the **height of the binary tree**

---

## 💡 Approach / Thought Process

### ✅ Tree Traversals:
1. **Inorder (Left → Root → Right)**
2. **Preorder (Root → Left → Right)**
3. **Postorder (Left → Right → Root)**

Each traversal is implemented recursively.

### ✅ Tree Height:
- The height of a tree is defined as the number of edges on the **longest path** from the root to a leaf.
- Use recursion to calculate the height:
  ```python
  height = 1 + max(height of left subtree, height of right subtree)
# 🌳 Binary Tree Traversals & Height Calculation (Python)

This Python program demonstrates three primary **binary tree traversal techniques**—**Inorder**, **Preorder**, and **Postorder**—and computes the **height** of a binary tree using recursion.

---

## 🔍 Problem Statement

Implement a binary tree with:
- Support for building nodes manually
- Perform **Inorder**, **Preorder**, and **Postorder** traversals
- Calculate and display the **height of the binary tree**

---

## 💡 Approach / Thought Process

### ✅ Tree Traversals:
1. **Inorder (Left → Root → Right)**
2. **Preorder (Root → Left → Right)**
3. **Postorder (Left → Right → Root)**

Each traversal is implemented recursively.

### ✅ Tree Height:
- The height of a tree is defined as the number of edges on the **longest path** from the root to a leaf.
- Use recursion to calculate the height:
  ```python
  height = 1 + max(height of left subtree, height of right subtree)
        1
       / \
      2   3
     / \  /
    4  5 6

    
Time & Space Complexity
Operation	Time Complexity	Space Complexity
Inorder Traversal	O(n)	O(h)
Preorder Traversal	O(n)	O(h)
Postorder Traversal	O(n)	O(h)
Height Calculation	O(n)	O(h)