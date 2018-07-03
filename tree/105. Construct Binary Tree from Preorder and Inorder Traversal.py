# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def rec(preorder,inorder):
            if not preorder or not inorder:
                return
            headval = preorder[0]
            root = TreeNode(headval)
            ind = inorder.index(root.val)
            root.left = rec(preorder[1:ind+1],inorder[:ind])
            root.right = rec(preorder[ind+1:],inorder[ind+1:])
            return root
        return rec(preorder,inorder)
        
        
