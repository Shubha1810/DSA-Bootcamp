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

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def get_data():
    ll = LinkedList()
    try:
        num = int(input("Enter number of elements in linked list: "))
        if num < 1:
            print("Number of elements must be greater than 0.")
            return None

        print("Choose insertion method: 1 for Head, 2 for Tail")
        method = input("Enter choice: ")

        print("Enter elements:")
        for _ in range(num):
            val = int(input())
            if method == '1':
                ll.add_head(val)
            elif method == '2':
                ll.add_tail(val)
            else:
                print("Invalid method chosen.")
                return None

        return ll

    except ValueError:
        print("Please enter valid integers only.")
        return None

# Main Execution
linked_list = get_data()
if linked_list:
    print("\nLinked List:")
    linked_list.display()
