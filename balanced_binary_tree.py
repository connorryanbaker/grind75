from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)

def is_balanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)
    