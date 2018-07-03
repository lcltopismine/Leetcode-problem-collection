# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        def rec(root,level,loc):
            if not root:
                return
            if root:
                if level>len(self.ret):
                    self.ret.append([0,0])
                if loc>self.ret[level-1][0]:
                    self.ret[level-1][0] = loc
                    self.ret[level-1][1] = root.val
                rec(root.left,level+1,2*loc)
                rec(root.right,level+1,2*loc+1)
        rec(root,1,1)
        for i in range(len(self.ret)):
            self.ret[i] = self.ret[i][1]
        return self.ret
