from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left = 1 + max_depth(root.left)
    right = 1 + max_depth(root.right)
    return max(left, right)
