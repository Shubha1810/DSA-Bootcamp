# Character Permutation Checker in Python

This Python script checks whether **all characters in one string are present in another**. It can be used to verify if a string is a permutation or partial match of another string's characters.

## Features

- Accepts two user input strings.
- Converts both strings to lowercase and sorts them.
- Prints the sorted strings.
- Checks if all characters of the first string are found in the second string.

## How It Works

1. Takes two strings as input.
2. Converts both to lowercase and sorts them.
3. Iterates through the characters of the first string.
4. Returns `True` if every character of `str1` exists in `str2`, otherwise `False`.