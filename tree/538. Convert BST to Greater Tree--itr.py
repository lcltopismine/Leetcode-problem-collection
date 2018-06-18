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
        stack = []
        cur = root
        tol = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop(-1)
            tol+=cur.val
            cur.val = tol
            cur = cur.left
        return root
            
                
