class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_ancestors(root: 'TreeNode', target: 'TreeNode', ancestors: List['TreeNode']) -> List['TreeNode']:
    if not root:
        return []
    ancestors.append(root)
    if root.val == target.val:
        return ancestors
    if target.val < root.val:
        return get_ancestors(root.left, target, ancestors)
    return get_ancestors(root.right, target, ancestors)

def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    p_ancestors = get_ancestors(root, p, [])
    q_ancestors = set(get_ancestors(root, q, []))
    shared = [p for p in p_ancestors if p in q_ancestors]
    return shared[len(shared) - 1]
    