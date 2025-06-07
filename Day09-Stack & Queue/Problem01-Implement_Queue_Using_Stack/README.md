# Queue Using Two Stacks (Python)

This Python program implements a **queue** data structure using **two stacks**. The queue supports the typical operations: enqueue, dequeue, peek (front), and checking if it is empty.

## Problem Statement

Implement a **queue** using two stacks. The queue should support the following operations:

- **Enqueue**: Add an item to the end of the queue.
- **Dequeue**: Remove and return the item from the front of the queue.
- **Peek**: Get the front item without removing it.
- **Is Empty**: Check if the queue is empty.

## Approach / Thought Process

- Use two stacks, `stack1` and `stack2`.
- **Enqueue:** Push elements into `stack1`.
- **Dequeue / Peek:**  
  - If `stack2` is empty, pop all elements from `stack1` and push them into `stack2` (this reverses the order).
  - Then pop/peek from `stack2` which behaves like a queue front.
- This ensures FIFO behavior using LIFO stacks.

## Time & Space Complexity

| Operation | Time Complexity (Amortized) | Space Complexity |
|-----------|-----------------------------|------------------|
| Enqueue   | O(1)                        | O(n)             |
| Dequeue   | O(1) amortized              | O(n)             |
| Peek      | O(1) amortized              | O(n)             |
| Is Empty  | O(1)                        | O(1)             |

- Each element is moved between stacks at most once, making dequeue and peek amortized O(1).


