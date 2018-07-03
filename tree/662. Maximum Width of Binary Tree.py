# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def rec(root,level,loc,res):
            if not root:
                return
            if root:
                if level>len(res):
                    res.append([float('inf'),float('-inf')])
                res[level-1][0] = min(loc,res[level-1][0])
                res[level-1][1] = max(loc,res[level-1][1])
                rec(root.left,level+1,2*loc,res)
                rec(root.right,level+1,2*loc+1,res)
        res = []
        rec(root,1,1,res)
        maxn = 0
        for ele in res:
            maxn = max(ele[1]-ele[0]+1,maxn)
        return maxn
                
            
