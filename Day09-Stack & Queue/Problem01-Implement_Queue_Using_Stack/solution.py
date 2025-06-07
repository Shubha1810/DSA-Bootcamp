stack1 = []
stack2 = []

def enqueue(item):
    stack1.append(item)

def is_empty():
    if len(stack1) == 0 and len(stack2) == 0:
        return True
    else:
        return False

def dequeue():
    if is_empty():
        return "Empty"
    else:
        if len(stack2) == 0:
            while len(stack1) > 0:
                stack2.append(stack1.pop())
        return stack2.pop()
    
def peek():
    if is_empty():
        return "Empty"
    else:
        if len(stack2) == 0:
            while len(stack1) > 0:
                stack2.append(stack1.pop())
        return stack2[-1]

while True:
    print("Choose Operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Is Empty?")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        val = int(input("Enter value to enqueue: "))
        enqueue(val)
    elif choice == '2':
        print("Dequeued:", dequeue())
    elif choice == '3':
        print("Front of Queue:", peek())
    elif choice == '4':
        print("Is queue empty:", is_empty())
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Try again.")
    