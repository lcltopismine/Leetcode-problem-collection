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
            return []
        def preorder(root):
            stack,res = [root],[]
            while stack:
                cur = stack.pop(-1)
                if cur:
                    stack.append(cur.right)
                    stack.append(cur.left)
                    res.append(str(cur.val))
                else:
                    res.append('.')
            res = "#".join(res)
            return res
        return preorder(root)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        def helper(node):
            if node == '.':
                return None
            root = TreeNode(int(node))
            root.left = helper(next(nodes))
            root.right = helper(next(nodes))
            return root
        
        nodes = iter(data.split('#'))
        return helper(next(nodes))
