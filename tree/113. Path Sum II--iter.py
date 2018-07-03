# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root: return []
        stack=[(root,[root.val],root.val)]
        res=[]
        while stack:
            root,path,s=stack.pop()
            if not root.right and not root.left:
                if s==sum:
                    res.append(path)
            if root.left:
                stack.append((root.left,path+[root.left.val],s+root.left.val))
            if root.right:
                stack.append((root.right,path+[root.right.val],s+root.right.val))
        return res
        
