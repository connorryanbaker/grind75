from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    
    root = TreeNode(preorder[0])
    root_inorder_idx = inorder.index(preorder[0])
    left_inorder = inorder[:root_inorder_idx]
    right_inorder = inorder[root_inorder_idx + 1:]
    root.left = self.buildTree(preorder[1:], left_inorder) 
    # root_inorder_idx + 1 ensures we skip all left subtree nodes and root
    root.right = self.buildTree(preorder[root_inorder_idx + 1:], right_inorder)
    return root