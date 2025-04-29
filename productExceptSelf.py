def productExceptSelf(nums):
    n = len(nums)
    answers = [1] * n
    lp = 1
    for i in range(n):
        answers[i] = lp
        lp = lp * nums[i]
    rp = 1
    for i in range(n-1, -1, -1):
        answers[i] = answers[i] * rp
        rp = rp * nums[i]

    return answers

nums = [1,2,3,4,5,9,7]
print(productExceptSelf(nums))

nums = [4,5,1,7,4,9,7]
print(productExceptSelf(nums))

nums = [9,4,1,6,8,2,13,27,39]
print(productExceptSelf(nums))

nums = [1,3,5,7,9]
print(productExceptSelf(nums))

nums = [2,4,6,8]
print(productExceptSelf(nums))