nums = [1,12,-5,-6,50,3]
k = 4
def findMaxAverage(nums, k):
    i = 0
    averages = []
    ln = len(nums)
    while i <= ln - k:
        slide_array = nums[i:i+k]
        avg = sum(slide_array)/len(slide_array)
        averages.append(avg)
        i += 1

    averages = sorted(averages, reverse=True)
    return averages[0]


print(findMaxAverage(nums, k))