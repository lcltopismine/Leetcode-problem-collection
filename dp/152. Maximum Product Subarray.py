class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [nums[0]]
        g = [nums[0]]
        for i in range(1,len(nums)):
            f.append(max(nums[i],max(nums[i]*f[i-1],nums[i]*g[i-1])))
            g.append(min(nums[i],min(nums[i]*f[i-1],nums[i]*g[i-1])))
        return max(f)
