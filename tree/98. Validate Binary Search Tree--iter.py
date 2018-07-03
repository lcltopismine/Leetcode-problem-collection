# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #iteration in-order tranverse
        stack,cur,ret = [],root,[]
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop(-1)
            ret.append(cur.val)
            if len(ret)>1 and ret[-2]<=ret[-1]:
                return False
            cur = cur.left
        return True
