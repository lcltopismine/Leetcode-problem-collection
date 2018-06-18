class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maximum = jump = 0
        for i in range(len(nums)):
            if i+nums[i]>maximum:
                maximum = i+nums[i]
            if maximum<=jump:
                break
            jump+=1
        if i==len(nums)-1:
            return True
        return False
