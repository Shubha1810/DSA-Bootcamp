
## Valid Parentheses Checker in Python

This Python script checks whether a given string consisting only of brackets (`()`, `{}`, `[]`) is **valid**. A string is considered valid if all types of brackets are **correctly opened and closed in the proper order**.

---

##  What is a Valid Parentheses String?

A string is valid if:
- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct **order**.
- Only `()`, `{}`, and `[]` characters are allowed.

### Examples of Valid Strings:
- `()`
- `([])`
- `{[()]}`
- `({[]})`

###  Examples of Invalid Strings:
- `([)]`
- `((())`
- `{[(])}`
- `()abc`

---

##  How It Works

1. A **stack** is used to track opening brackets.
2. For every character in the string:
   - If it's an opening bracket, it's **pushed** onto the stack.
   - If it's a closing bracket:
     - The stack is checked for a matching opening bracket.
     - If no match is found or the stack is empty, it's invalid.
3. If the stack is empty after processing all characters, the string is **valid**.

