from typing import Optional 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)
    return inorder(root)[k - 1]