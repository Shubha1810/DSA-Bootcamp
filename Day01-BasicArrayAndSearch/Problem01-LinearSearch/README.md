# Linear Search with Input Validation

## Overview

This Python program performs a **linear search** to find a target value in a user-defined list. It includes basic input validation and error handling to ensure only numeric values are processed.

## How It Works

1. The user inputs the length of the array.
2. Inputs are collected and stored in a list.
3. The user provides a target value.
4. The program searches linearly through the array.
5. If the target is found, its index is printed.
6. If the target is not found, it prints `Index = -1`.

## Key Features

- Works for small or unsorted arrays
- Simple and beginner-friendly logic
- Handles invalid (non-numeric) inputs gracefully
- Checks if the array length is valid (>1)

## Example

**Input:**
Length = 4
Values = 10 20 30 40
Target = 30

**Output:**
[10, 20, 30, 40]
Index = 2


**Input:**
Length = 3
Values = 5 6 7
Target = 9

**Output:**
[5, 6, 7]
Index = -1

## Notes

- Linear search is ideal for small datasets or unsorted data.
- Avoid using it for large data if performance is critical.