# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        rmin = min(p.val,q.val)
        rmax = max(p.val,q.val)
        p,q = rmin,rmax
        while root and (not p<=root.val<=q):
            if root.val>q:
                root = root.left
            elif root.val<q:
                root = root.right
        return root
