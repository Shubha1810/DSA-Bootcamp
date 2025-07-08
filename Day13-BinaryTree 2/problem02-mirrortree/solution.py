class Node:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def mirror(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder traversal before mirror: ", end="")
inorder(root)
print()


mirror(root)


print("Inorder traversal after mirror: ", end="")
inorder(root)
print()