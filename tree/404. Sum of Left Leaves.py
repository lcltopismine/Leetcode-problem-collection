# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def rec(root,isleft):
            if not root:
                return 
            if not root.left and not root.right:
                if isleft:
                    self.sum+=root.val
                    return
            if root:
                if root.left:
                    rec(root.left,1)
                if root.right:
                    rec(root.right,0)
        rec(root,0)
        return self.sum
