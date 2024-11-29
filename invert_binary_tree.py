class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    tmp = root.left
    root.left = root.right
    root.right = tmp
    invert_tree(root.left)
    invert_tree(root.right)
    return root