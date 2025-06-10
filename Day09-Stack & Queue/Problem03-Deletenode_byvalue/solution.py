class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def delete_byvalue(self, value):
        if self.head is None:
            print("The list is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("The node with value deleted:", value)
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                print("The node with value deleted:", value)
                return
            current = current.next

        print("Node not found")

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
          "\n1. Delete node" \
          "\n2. Add value at tail" \
          "\n3. Display list" \
          "\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to delete node: "))
        linked_list.delete_byvalue(value)
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
