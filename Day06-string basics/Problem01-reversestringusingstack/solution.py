def reverse_string():
    input_str = input("Enter the String: ")
    stack = list(input_str)
    reversed_chars = []

    while stack:
        reversed_chars.append(stack.pop())  # more efficient than += on string

    reversed_str = ''.join(reversed_chars)
    print("Reversed String:", reversed_str)

reverse_string()
