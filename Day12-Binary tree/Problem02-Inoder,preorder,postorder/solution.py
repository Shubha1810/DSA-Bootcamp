class TreeNode:
    def _init(self, value):  # ✅ fixed to __init_
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Build the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Traversals
print("Inorder traversal: ", end="")
inorder_traversal(root)
print()

print("Preorder traversal: ", end="")
preorder_traversal(root)
print()

print("Postorder traversal: ", end="")
postorder_traversal(root)
print()

# Tree height
def get_tree_height(root):
    if root is None:
        return -1
    else:
        left_height = get_tree_height(root.left)
        right_height = get_tree_height(root.right)
        return 1 + max(left_height, right_height)

height = get_tree_height(root)
print(f"The height of the binary tree is: {height}")