# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def rec(s):
            if s:
                if not s.left and not s.right:
                    return s
                if (not s.left and s.right) or (not s.right and s.left):
                    s.left,s.right = s.right,s.left
                    if s.left:
                        s.left = rec(s.left)
                    if s.right:
                        s.right = rec(s.right)
                    return s
                if s.left and s.right:
                    s.left,s.right = s.right,s.left
                    if s.left:
                        s.left = rec(s.left)
                    if s.right:
                        s.right = rec(s.right)
                    return s
        return rec(root)
