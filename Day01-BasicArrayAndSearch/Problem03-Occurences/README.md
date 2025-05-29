# Count Occurrences of a Number in an Array

## Overview

This Python program takes a list of integers from the user and counts how many times a specified number appears in that list. The input process is interactive and includes error handling for invalid entries.

## How It Works

1. Prompts the user to enter the length of the array (must be a positive number).
2. Accepts only numeric inputs to populate the array.
3. Asks the user for a target value.
4. Counts and displays how many times the target appears in the array.

## Functions

- `GetData()`: Handles input for array length and elements. Ensures all values are numeric and valid.
- `Occurences_of_Number(arr, arr_length)`: Counts how many times a given target number appears in the array.

## Example

**Input:**
Enter the Length of Array = 5
Values = 2 4 2 6 2
Target = 2

makefile
Copy
Edit

**Output:**
Array = [2, 4, 2, 6, 2]
Count = 3

css
Copy
Edit

## Notes

- Non-numeric inputs are rejected with a clear message.
- The program uses a linear scan to count occurrences (O(n) time complexity).
- Suitable for small to medium-sized datasets.