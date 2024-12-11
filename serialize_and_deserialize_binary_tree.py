# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        res = [] 
        q = [[root]]
        while q:
            curr = q.pop(0)
            res.append([ str(n.val) if n else 'None' for n in curr ])
            if all([ el is None for el in curr]):
                break
            next_level = []
            for n in curr:
                if n:
                    next_level.append(n.left)
                    next_level.append(n.right)
            q.append(next_level)
        return '|'.join([ ','.join(level) for level in res ] )



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        
        str_levels = data.split('|')
        levels = []
        for level in str_levels:
            levels.append([ TreeNode(int(v)) if v != 'None' else None for v in level.split(',') ])
        for i in range(len(levels) - 1):
            next_level_padding = 0
            for j in range(len(levels[i])):
                node = levels[i][j]
                if node:
                    node.left = levels[i+1][(j*2) - next_level_padding]
                    node.right = levels[i+1][(j*2 + 1) - next_level_padding]
                else:
                    next_level_padding += 2
        return levels[0][0]
