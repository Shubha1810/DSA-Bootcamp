class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.count = 0  # Initialize count

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def add_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.count += 1

    def mid(self):
        if self.count == 0:
            print("List is empty.")
            return
        mid_index = self.count // 2
        current = self.head
        for i in range(mid_index):
            current = current.next
        print(f"Middle node value is: {current.data}")

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
    print("\nChoose an option:"
          "\n1. Show middle node"
          "\n2. Add value at tail"
          "\n3. Display list"
          "\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        linked_list.mid()
    elif choice == 2:
        value = int(input("Enter value to add to tail: "))
        linked_list.add_tail(value)
    elif choice == 3:
        linked_list.display()
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")