# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def rec(root):
            if not root:
                return
            left,right = rec(root.left),rec(root.right)
            if left and not right:
                root.left,root.right = root.right,root.left
            elif left and right:
                root.right = left
                while left.right:
                    left = left.right
                left.right = right
                root.left = None
            return root
        rec(root)
