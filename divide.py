def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #check if dividend and divisor are equal 
        if dividend == divisor:
            return 1

        #get the absolute values of divisor and dividend
        d1= int(abs(dividend))
        d2= int(abs(divisor))

        quotient = 0
        
        if dividend < 0 and divisor < 0 and d2 == 1:
             return d1
        
        while d1 >= d2:
            d1 -= d2
            quotient += 1

        #check if dividend or divisor is a negative number
        if dividend < 0 and divisor < 0:
            return quotient
        elif dividend < 0 or divisor < 0:
            return -quotient
        else:
            return quotient
        

print(divide(10, 2))  
print(divide(7, -3))  
print(divide(-8, 4))  
print(divide(-9, -3))  
print(divide(1, 1))
print(divide(-1, 1))
print(divide(-2147483648, -1))