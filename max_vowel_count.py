class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a','e','i','o','u'} #Set of vowels
        s_len = len(s)
        i = 0
        if k > s_len or k <= 0:
            return 0
        cvc = 0 #cvc = current vowel count
        for i in range(k):
            if s[i] in vowels:
                cvc += 1
        mvc = cvc #mvc = maximum vowel count
        for i in range (k, s_len):
            if s[i - k] in vowels:
                cvc -= 1

            if s[i] in vowels:
                cvc += 1
            
            mvc = max(mvc, cvc)

        return mvc