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

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    @staticmethod
    def merge_sorted_lists(head1, head2):
        dummy = Node(0)
        tail = dummy

        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

        return dummy.next

    def sort(self):
        if self.head is None:
            return

        end = None
        while end != self.head:
            current = self.head
            while current.next != end:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                current = current.next
            end = current



list1 = LinkedList()
list2 = LinkedList()
merged = LinkedList()

while True:
    print("\nChoose an option:"
          "\n1. Add value to List 1"
          "\n2. Add value to List 2"
          "\n3. Display List 1"
          "\n4. Display List 2"
          "\n5. Merge both sorted lists"
          "\n6. Display Sorted Merged List"
          "\n7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        val = int(input("Enter value to add to List 1: "))
        list1.add_tail(val)

    elif choice == '2':
        val = int(input("Enter value to add to List 2: "))
        list2.add_tail(val)

    elif choice == '3':
        print("List 1:")
        list1.display()

    elif choice == '4':
        print("List 2:")
        list2.display()

    elif choice == '5':
        merged.head = LinkedList.merge_sorted_lists(list1.head, list2.head)
        print("Merged successfully!")

    elif choice == '6':
        if merged.head is None:
            print("No merged list found. Merge first.")
        else:
            merged.sort()
            print("Sorted Merged List:")
            merged.display()

    elif choice == '7':
        print("Exit")
        break

    else:
        print("Invalid choice. Please try again.")
