def removeDuplicates(nums): 
    #edge cases
    if len(nums) == 0:
        return []
        
    #removing duplicates in place
    wi = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[wi] = nums[i]
            wi += 1
        
    #returning first k unqiue elements
    return len(nums[:wi])