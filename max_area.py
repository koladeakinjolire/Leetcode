def maxArea(height):
    """
    type height = list[int]
    rtype = int
    """
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


height = [1,2,13,48,3,32,35,116,125,77,5,7,16,56,82,6,73,83,64,57,48,25,54,93,56,37,35,42,68,95,106,45,34,21,23,87]
print(maxArea(height))