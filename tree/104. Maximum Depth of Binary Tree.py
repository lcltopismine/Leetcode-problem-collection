# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxd = 0
        def rec(root,level):
            if not root:
                return
            if root:
                self.maxd = max(self.maxd,level)
                if root.left:
                    rec(root.left,level+1)
                if root.right:
                    rec(root.right,level+1)
        rec(root,1)
        return self.maxd
