# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def rec(p,q):
            res= False
            if not p and not q:
                res= True
                return res
            if not p and q or not q and p:
                res=False
                return res
            if p and q and p.val==q.val:
                res=True
            return res and rec(p.left,q.left) and rec(p.right,q.right)
        return rec(p,q)
