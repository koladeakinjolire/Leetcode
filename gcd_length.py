class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Step 1: Check if GCD exists
        if str1 + str2 != str2 + str1:
            return ""

        #Step 2: Compute the GCD of lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a 

        gcd_length = gcd(len(str1), len(str2))

        #Step 3: Return substring length
        return str1[:gcd_length]