def get_input():
    try:
        user_input = input("Enter a string containing only brackets:\n")
        return user_input
    
    except Exception as e:
        print("Input only types of paranthesis", e)
        exit()

def is_valid_parentheses(string):
    stack = []
    paranthesis = {'(':')', '[':']', '{':'}'}

    if len(string) % 2 != 0:
        print(False)
        return

    for char in string:
        if char in paranthesis:  
            stack.append(char)
        elif char in paranthesis.values():  
            if not stack or paranthesis[stack.pop()] != char:
                return False
        else:
            return False  
   
    return len(stack) == 0  


input_string = get_input()
result = is_valid_parentheses(input_string)
print(result)
