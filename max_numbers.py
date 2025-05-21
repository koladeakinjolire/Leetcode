class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i,j = 0, len(nums) - 1
        r = 0
        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                r += 1
                i += 1
                j += 1
            elif total < k:
                i += 1
            else:
                j += 1
        
        return r