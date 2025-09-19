def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
       # Convert binary strings to decimal integers
        decimal_a = int(a,2)
        decimal_b = int(b,2)

        #handle edge case where both inputs are "0"
        if decimal_a == 0 and decimal_b == 0:
            return "0"
        
        # Sum the decimal integers
        decimal_sum = decimal_a + decimal_b

        # Convert the sum back to binary
        binary_result = []
        while decimal_sum > 0:
            binary_result.append(decimal_sum % 2)
            decimal_sum = abs(decimal_sum // 2)

        # Convert list of binary digits to string
        binary_result = [str(num) for num in binary_result[::-1]]

        #Join the list into a single string and return the result
        result = ''.join(binary_result)
        return result

print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("0", "0"))
