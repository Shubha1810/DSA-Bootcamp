# Singly Linked List (Python)

This Python program implements a **singly linked list** with operations to insert elements at the **head** or **tail**, and display the list.

## Problem Statement

Design and implement a **singly linked list** that supports:
- Insertion of nodes at the beginning (`add_head`)
- Insertion of nodes at the end (`add_tail`)
- Displaying all elements in the linked list in order

Users can choose how to insert elements — either at the head or at the tail.

## Approach / Thought Process

- The `Node` class stores individual elements and a reference (`next`) to the next node.
- The `LinkedList` class handles the list:
  - `add_head(data)`: Creates a new node and places it at the beginning.
  - `add_tail(data)`: Traverses the list and adds the new node at the end.
  - `display()`: Traverses from `head` and prints all node values until `None`.
- User is prompted to:
  - Enter the number of nodes
  - Choose insertion method (`1` for head, `2` for tail)
  - Enter each node's value

---

## ⌛ Time & Space Complexity

| Operation        | Time Complexity | Space Complexity |
|------------------|------------------|------------------|
| Add at Head      | O(1)             | O(1)             |
| Add at Tail      | O(n)             | O(1)             |
| Display List     | O(n)             | O(1)             |

- Space used is constant per operation, excluding input size.
- Adding at tail requires traversal; adding at head is immediate.
