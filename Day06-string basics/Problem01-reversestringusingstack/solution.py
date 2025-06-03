def reverse_string():
    input_str = input("Enter the String: ")
    stack = list(input_str)
    reversed_str = ""

    while stack:
        reversed_str += stack.pop()

    print("Reversed String:", reversed_str)

reverse_string()
