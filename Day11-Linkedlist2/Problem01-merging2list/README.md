# 🔗 Merge and Sort Two Linked Lists (Python)

This Python program allows users to:
- Create two separate linked lists
- Merge them (assuming they are sorted)
- Sort the merged list (if not already sorted)

It uses custom `Node` and `LinkedList` classes and provides a menu-driven interface.

---

## 🔍 Problem Statement

Design a program that:
1. Accepts elements into **two separate linked lists**
2. **Merges** the two linked lists into a single sorted list
3. Allows **sorting** the final merged list using Bubble Sort logic (if needed)
4. Provides options to view and manage the data dynamically

---

## 💡 Approach / Thought Process

- **Data Structure Used:** Singly Linked List
- Each list is represented using a custom `Node` class and managed using the `LinkedList` class.
- The merging function compares elements of both lists and creates a new combined sorted list.
- A bubble sort is applied to the merged list to ensure the final result is fully sorted.

### Core Components:

- `add_tail(data)` – Add node at the end of a list
- `merge_sorted_lists(head1, head2)` – Merge two sorted linked lists
- `sort()` – Sorts the merged list using Bubble Sort (node swapping)
- `display()` – Prints the list in human-readable format

---

## ⌛ Time & Space Complexity

| Operation                  | Time Complexity | Space Complexity |
|----------------------------|------------------|------------------|
| Add Tail                   | O(n)             | O(1)             |
| Display List               | O(n)             | O(1)             |
| Merge Sorted Lists         | O(n + m)         | O(1)             |
| Bubble Sort (on LinkedList)| O(n²)            | O(1)             |

> n = length of List 1, m = length of List 2

---

## 🧪 Sample Inputs / Outputs

### Sample Run:
Choose an option:

Add value to List 1

Add value to List 2

Display List 1

Display List 2

Merge both sorted lists

Display Sorted Merged List

Exit
Enter your choice: 1
Enter value to add to List 1: 5

Enter your choice: 1
Enter value to add to List 1: 10

Enter your choice: 2
Enter value to add to List 2: 3

Enter your choice: 2
Enter value to add to List 2: 7

Enter your choice: 5
Merged successfully!

Enter your choice: 6
Sorted Merged List:
3 -> 5 -> 7 -> 10 -> None