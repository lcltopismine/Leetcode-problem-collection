# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def rec(root):
            if not root:
                return 0
            #if not root.left and not root.right:
            #    return 0
            if root:
                left = right = 0
                if root.left:
                    left=rec(root.left)
                if root.right:
                    right = rec(root.right)
                self.res+= abs(left-right)
                return root.val+left+right
        rec(root)
        return self.res
                
