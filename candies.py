class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        new_candies = [extraCandies + candies[i] for i in range(len(candies))]
        result = []
        for i in range(len(candies)):
            result.append(new_candies[i] >= max(candies))
        return result 