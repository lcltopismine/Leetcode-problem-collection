# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur = root
        #flag = 1
        stack = []
        ret = []
        while stack or cur:
#            cur = stack.pop(-1)
            while cur:
                stack.append(cur)
                ret.append(cur.val)
                cur = cur.right
            if not cur:
                cur = stack.pop(-1)
            cur = cur.left
        ret.reverse()
        return ret
