def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for _ in range(len(nums)):
            if val in nums:
                nums.remove(val)
        
        return len(nums)