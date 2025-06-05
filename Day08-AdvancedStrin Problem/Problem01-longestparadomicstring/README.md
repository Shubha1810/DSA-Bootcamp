# Longest Even-Length Palindromic Substring in Python

This Python script finds the **longest even-length palindromic substring** within a given string. A palindrome is a sequence that reads the same forward and backward (e.g., `abba`, `deed`), and this program specifically looks for **even-length** palindromes only.

## Features

- Accepts a user-input string.
- Converts the string to lowercase for case-insensitive comparison.
- Finds the **longest even-length** palindrome by expanding around pairs of characters.
- Returns and prints the longest such palindrome found in the string.

## How It Works

1. For every adjacent pair of characters in the string, it checks if they can be expanded into a larger palindrome.
2. It uses two pointers (`left` and `right`) and expands outward as long as characters match.
3. Keeps track of the longest valid even-length palindrome.