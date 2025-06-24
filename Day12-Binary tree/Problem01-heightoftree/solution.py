class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_tree_height(root):
  
    if root is None:
        return -1
    else:
        left_height = get_tree_height(root.left)
        right_height = get_tree_height(root.right)

        return 1 + max(left_height, right_height)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Calculate and print the height of the tree
height = get_tree_height(root)
print(f"The height of the binary tree is: {height}")