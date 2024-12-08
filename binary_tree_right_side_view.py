from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def right_side_view(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root:
        return res
    q = [[root]]
    while q:
        currlevel = q.pop(0)
        nextlevel = []
        res.append(currlevel[-1].val)
        for node in currlevel:
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        if nextlevel:
            q.append(nextlevel)
    return res