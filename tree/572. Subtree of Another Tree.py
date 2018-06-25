# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        self.res = False
        def trans(s,t):
            if not s:
                return
            if s:
                if check(s,t):
                    self.res = True
                    return
                trans(s.left,t)
                trans(s.right,t)
        def check(s,t):
            if not s and not t:
                return True
            if s and t:
                return s.val==t.val and check(s.left,t.left) and check(s.right,t.right)
            return False
        trans(s,t)
        return self.res
                    
                
