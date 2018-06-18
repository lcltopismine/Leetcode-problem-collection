# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def rec(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return str(root.val)
            if root.left and root.right:
                return str(root.val)+'('+rec(root.left)+')'+'('+rec(root.right)+')'
            if root.left:
                return str(root.val)+'('+rec(root.left)+')'
            if root.right:
                return str(root.val)+'('+rec(root.left)+')'+'('+rec(root.right)+')'
        return rec(t)
                
        
