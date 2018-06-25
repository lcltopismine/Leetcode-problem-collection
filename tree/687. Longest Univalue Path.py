# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def rec(root):
            if not root:
                return 0
            left = right = 0
            leftrec = rec(root.left)
            rightrec = rec(root.right)
            if root.left:
                if root.left.val==root.val:
                    left+=1+leftrec
            if root.right:
                if root.right.val==root.val:
                    right+=1+rightrec
            self.ans = max(self.ans,left+right)
            return max(left,right)
        rec(root)
        return self.ans
                
            
