from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def trace_path(node: 'TreeNode', target: int) -> List['TreeNode']:
        if not node:
            return []
        if node.val == target:
            return [node]
        left_path = [node] + trace_path(node.left, target)
        if left_path and left_path[-1].val == target:
            return left_path
        return [node] + trace_path(node.right, target)
    
    ppath = trace_path(root, p.val)
    qpath = trace_path(root, q.val)
    idx = 0
    lca = root
    while idx < len(ppath) and idx < len(qpath):
        if ppath[idx].val != qpath[idx].val:
            break
        else:
            lca = ppath[idx]
        idx += 1
    return lca
        