nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
def longestOnes(nums, k):
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        # Shrink window if zeros exceed k
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update max_len if window is valid
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longestOnes(nums, k))

