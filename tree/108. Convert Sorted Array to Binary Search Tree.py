# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST_helper(self, nums, lo , hi):
        
        if(lo>hi):
            return None

        if(lo<hi):
            m=(lo+hi)//2 
            head=TreeNode(nums[m])
            head.left=self.sortedArrayToBST_helper( nums, lo , m-1)
            head.right=self.sortedArrayToBST_helper( nums, m+1 , hi)
        elif(lo==hi):
            head=TreeNode(nums[lo])

        return head
    
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.sortedArrayToBST_helper(nums, 0, len(nums)-1)
