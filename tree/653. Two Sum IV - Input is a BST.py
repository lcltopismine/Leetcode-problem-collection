# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.res = False
        dic = {}
        def rec(root):
            if not root:
                return
            if root:
                if k-root.val not in dic:
                    dic[root.val] = k-root.val
                else:
                    self.res = True
                rec(root.left)
                rec(root.right)
        rec(root)
        #print dic
        return self.res
