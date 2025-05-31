# Selection Sort in Ascending and Descending Order

## Description

This Python program allows users to input elements into an array, then sorts the array using the *Selection Sort* algorithm in both *ascending* and *descending* order.

## Features

- Takes user input for array size and elements.
- Implements Selection Sort for:
  - Ascending order
  - Descending order
- Includes input validation for non-integer values.

## Sample Input & Output

*Input:*
Enter the number of elements in array: 5
Enter elements in array: 4
Enter elements in array: 2
Enter elements in array: 5
Enter elements in array: 1
Enter elements in array: 3

makefile
Copy
Edit

*Output:*
Array = [4, 2, 5, 1, 3]
Sorted Array in Ascending Order is: [1, 2, 3, 4, 5]
Sorted Array in Descending Order is: [5, 4, 3, 2, 1]

markdown
Copy
Edit

## Time Complexity

- *Best, Average, Worst Case:* O(n²)

## Space Complexity

- O(1) – In-place sorting

## How to Run

1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python selection_sort.py