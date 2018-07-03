# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def rec(root,key):
            if not root:
                return
            if root:
                if root.left and root.left.val==key:
                    #print 'a'
                    left,right = root.left.left,root.left.right
                    root.left = left
                    if root.left:
                        root = root.left
                        while root.right:
                            root = root.right
                        root.right = right
                    else:
                        root.left = right
                    return
                if root.right and root.right.val==key:
                    left,right = root.right.left,root.right.right
                    root.right = left
                    if root.right:
                        root = root.right
                        while root.right:
                            root = root.right
                        root.right = right
                    else:
                        root.right = right
                    return
                rec(root.left,key)
                rec(root.right,key)
        if not root:
            return
        dummy = TreeNode(float('-inf'))
        dummy.left,node = root,root
        rec(dummy,key)
        return dummy.left
            
                        
                    
                    
