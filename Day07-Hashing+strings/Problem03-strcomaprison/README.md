# String Compression in Python

This Python script compresses a string by replacing consecutive repeating characters with the character followed by the count of its repetitions. If a character appears only once, it's added without a count.

### Example:
- Input: `aaabbc`
- Output: `a3b2c`

## Features

- Accepts a string from the user.
- Compresses the string by counting consecutive repeated characters.
- Prints and returns the compressed string.
- Handles edge cases like non-repeating characters or empty input.

## How It Works

1. The user inputs a string.
2. The program iterates through the string, counting consecutive repeating characters.
3. It appends each character (and count if >1) to a list.
4. The list is joined into a final compressed string.