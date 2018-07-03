# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def rec(root,level,res):
            if not root:
                return
            if level>len(res):
                res.append([])
            res[level-1].append(root)
            if len(res[level-1])>1:
                res[level-1][-2].next = res[level-1][-1]
            rec(root.left,level+1,res)
            rec(root.right,level+1,res)
        res = []
        rec(root,1,res)
