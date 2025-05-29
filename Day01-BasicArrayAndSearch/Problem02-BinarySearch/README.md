# Binary Search with Input Validation

## Overview

This Python program performs binary search on a list of integers entered by the user. It includes error handling to ensure only numerical input is accepted.

## How It Works

1. User enters the length of the array.
2. Inputs integer values for the array.
3. The array is sorted automatically.
4. The user enters a target value to search.
5. Binary search is used to find the index of the target.
6. If found, the index is printed. Otherwise, `Index = -1` is displayed.

## Key Features

- Accepts dynamic user input
- Automatically sorts the array
- Uses efficient binary search
- Handles invalid (non-integer) inputs gracefully

## Example

**Input:**
Length = 5
Values = 8 3 1 9 4
Target = 3


**Output:**
Sorted array: [1, 3, 4, 8, 9]
1

## Notes

- Only integer inputs are allowed.
- The array must be sorted for binary search to work (handled internally).