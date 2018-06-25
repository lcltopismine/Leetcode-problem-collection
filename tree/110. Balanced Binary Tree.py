# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans =True 
        def rec(root):
            if not root:
                return 0
            left=right=leftrec=rightrec=0
            leftrec = rec(root.left)
            rightrec = rec(root.right)
            if abs(leftrec-rightrec)>1:
                self.ans = False
            return max(leftrec,rightrec)+1
        rec(root)
        return self.ans
            
            
