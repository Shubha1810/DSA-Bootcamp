
# Bubble Sort in Python

## Overview

This program allows a user to input an array of integers and sorts it using the *Bubble Sort* algorithm. The implementation uses arithmetic swapping (without a temporary variable) and includes input validation.

## How It Works

1. User is prompted to enter the length of the array (must be greater than 1).
2. Elements are input one by one with error handling for non-numeric values.
3. The array is sorted using Bubble Sort.
4. The sorted array is displayed.

## Features

- Input validation for array length and elements
- Bubble sort using arithmetic operations for swapping
- Suitable for small datasets and educational purposes

## Example

*Input:*
Enter the Length of Array = 5
Enter elements in the array:
5 2 8 1 3

makefile
Copy
Edit

*Output:*
Array = [5, 2, 8, 1, 3]
Sorted Array = [1, 2, 3, 5, 8]

markdown
Copy
Edit

## Notes

- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best used for teaching or small datasets due to inefficiency on large inputs