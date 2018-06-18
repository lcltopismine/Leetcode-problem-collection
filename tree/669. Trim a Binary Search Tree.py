# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def rec(root):
            if not root:
                return  
            if L<=root.val<=R:
                if root.left and root.left.val<=R:
                    root.left = rec(root.left)
                if root.right and root.right.val>=L:
                    root.right = rec(root.right)
                return root
            elif root.val>R:
                if root.left:
                    root = rec(root.left)
                    return root
            else:
                if root.right:
                    root = rec(root.right)
                    return root
        return rec(root)
