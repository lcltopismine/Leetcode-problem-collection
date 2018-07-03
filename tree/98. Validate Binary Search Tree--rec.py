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
        self.ret,self.stop = True,False
        def rec(root,res):
            if not root or self.stop:
                return
            rec(root.left,res)
            res.append(root.val)
            if len(res)>1:
                if res[-2]>=res[-1]:
                    self.ret,self.stop = False,True
            rec(root.right,res)
        res = []
        rec(root,res)       
        return self.ret
                    
                    
        
