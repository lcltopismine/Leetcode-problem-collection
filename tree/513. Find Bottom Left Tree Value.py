# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.level = -1
        self.loc = 0
        def rec(root,level,isleft,loc):
            if not root:
                return
            if root:
                if level>self.level:
                    self.level = level
                    self.loc = loc
                    self.res = root.val
                rec(root.left,level+1,1,2*(level+1))
                rec(root.right,level+1,0,2*(level+1)+1)
        rec(root,0,0,1)
        return self.res
                
