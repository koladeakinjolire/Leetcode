def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        nums = []
        result = 0
        for char in s:
            nums.append(roman_dict[char])

        length = len(nums)
        result = 0
        
        for i in range(0, length - 1):
            current_value = nums[i]
            next_value = nums[i+1]
            if current_value < next_value:
                result -= current_value
            else:
                result += current_value

        result += nums[length-1]
        return result