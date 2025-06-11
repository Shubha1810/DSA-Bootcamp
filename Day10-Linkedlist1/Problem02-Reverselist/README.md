# 🔁 Reverse a Singly Linked List (Python)

This Python project implements a singly linked list with the ability to add nodes at the tail, reverse the list, and display the contents.

---

## 📌 Features

- Add nodes to the tail of the linked list.
- Reverse the entire linked list in-place.
- Display the contents of the linked list.

---

## 🧠 How Reversal Works

The `reverse_list()` method reverses the direction of the `next` pointers of each node. It uses three pointers:

- `prev`: to keep track of the reversed portion.
- `current`: to iterate through the list.
- `next_node`: to temporarily store the next node.

After reversal, the `head` of the linked list is updated to the last visited node.

---

## 🛠️ Functions Used

| Function Name      | Description                                       |
|--------------------|---------------------------------------------------|
| `add_tail(data)`   | Adds a new node with `data` at the end of the list |
| `reverse_list()`   | Reverses the entire linked list in-place          |
| `display()`        | Prints the list elements from head to tail        |

---

## 📦 Sample Input/Output

```bash
Choose an option:
1. Reverse the list
2. Add value at tail
3. Display list
4. Exit
Enter your choice: 2
Enter value to add to rear: 10

Enter your choice: 2
Enter value to add to rear: 20

Enter your choice: 3
10 -> 20 -> None

Enter your choice: 1
List reversed successfully.
Reversed list:
20 -> 10 -> None
