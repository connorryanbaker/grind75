from typing import Optional, Union
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
    def helper(node: Optional[TreeNode], mn: Union[int, float], mx: Union[int, float]) -> bool:
        if not node:
            return True
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        if node.val >= mx or node.val <= mn:
            return False
        return helper(node.left, mn, node.val) and helper(node.right, node.val, mx)
    return helper(root, -float('inf'), float('inf'))
    