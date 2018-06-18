# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def rec(p,q):
            if not p and not q:
                return True
            if not p and q or not q and p:
                return False
            if p and q and p.val==q.val:
                return rec(p.left,q.right) and rec(p.right,q.left)
            return False
        return rec(root,root)
        
