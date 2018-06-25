# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def rec(root):
            if not root:
                return
            root.left = rec(root.left)
            root.right = rec(root.right)
            if root.val!=0:
                return root
            if root.left or root.right:
                return root
        return rec(root)
            
