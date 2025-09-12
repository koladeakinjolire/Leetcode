def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #turn the numbers digits list into a single number
        numbers = int(''.join(map(str, digits)))
       
        #add one to that number
        numbers += 1

        #turn each number in the list back into an integer
        result = [int(i) for i in str(numbers)]
        return result

print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [4,3,2,2]
print(plusOne([0])) # [1]