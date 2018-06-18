# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.res = []
        def rec(root,level):
            if not root:
                return 
            if root:
                if len(self.res)<level:
                    self.res.append([0,0])
                self.res[level-1][0]+=root.val
                self.res[level-1][1]+=1
                if root.left:
                    rec(root.left,level+1)
                if root.right:
                    rec(root.right,level+1)
        rec(root,1)
        for i in range(len(self.res)):
            self.res[i] = self.res[i][0]*1.0/self.res[i][1]
        return self.res
