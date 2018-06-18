# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        def rec(root):
            if root:
                rec(root.right)
                self.sum+=root.val
                root.val = self.sum
                rec(root.left)
        node = root
        rec(root)
        return node
                
