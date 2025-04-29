class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                prev_spot = (i == 0) or (flowerbed[i-1] == 0)
                next_spot = (i == length - 1) or (flowerbed[i+1] == 0)
                if prev_spot and next_spot:
                    flowerbed[i] = 1
                    n -= 1 
                    if n <= 0:
                        return True
        return n <= 0
        