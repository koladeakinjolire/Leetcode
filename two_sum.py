
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    result = []
    ln = len(nums)
    while i < ln:
        j = i + 1
        for j in range(j, ln):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
        i += 1
    return result