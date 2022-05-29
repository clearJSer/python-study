class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

