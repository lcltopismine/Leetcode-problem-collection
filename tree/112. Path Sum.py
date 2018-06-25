# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ans = False
        def rec(root,tol,sum):
            if not root:
                return
            if not root.left and not root.right:
                tol+=root.val
                if tol==sum:
                    self.ans = True
                    return
            if root:
                tol+=root.val
                rec(root.left,tol,sum)
                rec(root.right,tol,sum)
        rec(root,0,sum)
        return self.ans
                    
