# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def rec(t1,t2):
            if not t1 and not t2:
                return
            if t1 and t2:
                t1.val += t2.val
                t1.left = rec(t1.left,t2.left)
                t1.right = rec(t1.right,t2.right)
                return t1
            elif t1:
                return t1
            elif t2:
                return t2
        return rec(t1,t2)
