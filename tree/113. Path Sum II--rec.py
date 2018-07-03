# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def rec(root,tol,path,sum,res):
            if not root:
                return
            tol+=root.val
            path+=str(root.val)+'#'
            if not root.left and not root.right:
                #print tol,path
                if tol==sum:
                    path = path.split('#')
                    res.append([int(i) for i in path[:-1]])
            rec(root.left,tol,path,sum,res)
            rec(root.right,tol,path,sum,res)
        res = []
        rec(root,0,"",sum,res)
        return res
