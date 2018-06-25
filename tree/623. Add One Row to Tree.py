# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            ret = TreeNode(v)
            ret.left = root
            return ret

        def rec(root,level,v,d):
            if not root:
                return
            if root:
                if level==d-1:
                    left,right = root.left,root.right
                    root.left,root.right = TreeNode(v),TreeNode(v)
                    root.left.left,root.right.right = left,right
                    return
                else:
                    rec(root.left,level+1,v,d)
                    rec(root.right,level+1,v,d)
        node = root
        rec(root,1,v,d)
        return node
