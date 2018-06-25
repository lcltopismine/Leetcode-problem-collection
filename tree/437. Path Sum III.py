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
        :rtype: int
        """
        self.ans = 0
        def rec(root,tol,sum):
            if not root:
                return
            if root:
                tol+=root.val
                if tol==sum:
                    self.ans+=1
                rec(root.left,tol,sum)
                rec(root.right,tol,sum)
        def trans(root,tol,sum):
            if not root:
                return
            if root:
                rec(root,0,sum)
                #print root.val,self.ans
                trans(root.left,0,sum)
                trans(root.right,0,sum)
        trans(root,0,sum)
        return self.ans
                    
