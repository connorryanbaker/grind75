# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = [[root]]
    while q:
        current_level, next_level, next_res = q.pop(0), [], []
        for n in current_level:
            next_res.append(n.val)
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        if next_res:
            result.append(next_res)
        if next_level:
            q.append(next_level)
    return result
    