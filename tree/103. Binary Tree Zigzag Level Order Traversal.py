# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def rec(root,level,res):
            if not root:
                return
            if level>len(res):
                res.append([])
            if not level%2:
                res[level-1].insert(0,root.val)
            else:
                res[level-1].append(root.val)
            rec(root.left,level+1,res)
            rec(root.right,level+1,res)
        res = []
        rec(root,1,res)
        return res
    
