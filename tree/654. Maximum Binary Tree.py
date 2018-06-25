# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def checkmax(array):
            maxind,maxval = 0,float('-inf')
            for i in range(len(array)):
                if maxval<array[i]:
                    maxind,maxval = i,array[i]
            return [maxind,maxval]
                    
        def rec(array):
            if array:
                maxind,maxval = checkmax(array)
                root = TreeNode(maxval)
                left = array[:maxind]
                right = array[maxind+1:]
                root.left = rec(left)
                root.right = rec(right)
                return root
        return rec(nums)
            
        
                
                    
