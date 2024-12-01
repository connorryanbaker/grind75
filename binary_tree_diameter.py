from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    def helper(root: Optional[TreeNode], lookup: dict) -> int:
        if not root:
            return 0
        curr_diameter = max_depth_at_node(root.left, lookup) + max_depth_at_node(root.right, lookup)
        return max(curr_diameter, helper(root.left, lookup), helper(root.right, lookup))
    return helper(root, {})

    
def max_depth_at_node(self, node: Optional[TreeNode], lookup: dict) -> int:
    if not node:
        return 0
    if node in lookup:
        return lookup[node]
    
    left_depth = 1 + max_depth_at_node(node.left, lookup)
    right_depth = 1 + max_depth_at_node(node.right, lookup)
    lookup[node] = max(left_depth, right_depth)
    return lookup[node]