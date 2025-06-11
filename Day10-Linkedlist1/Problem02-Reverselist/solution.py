class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse_list(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next 
            current.next = prev       
            prev = current            
            current = next_node 

        self.head = prev
        print("List reversed successfully.")

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

while True:
    print("\nChoose an option:" \
          "\n1. Reverse the list" \
          "\n2. Add value at tail" \
          "\n3. Display list" \
          "\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.reverse_list()
        print("Reversed list:")
        linked_list.display()  # ✅ fixed here
    elif choice == 2:
        value = int(input("Enter value to add to rear: "))
        linked_list.add_tail(value)
    elif choice == 3:
        linked_list.display()
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")
