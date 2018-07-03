# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def rec(root,res):
            if not root:
                return
            rec(root.left,res)
            res.append(root.val)
            rec(root.right,res)
        res = []
        rec(root,res)
        tep = iter(sorted(res))
        ind = []
                    
        def rec(root,v):
            if not root:
                return
            rec(root.left,v)
            value = next(v)
            if root.val!=value:
                root.val=value
            rec(root.right,v)
        
        rec(root,tep)
        
                
