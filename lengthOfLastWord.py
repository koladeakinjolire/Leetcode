def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #split string into individual words
        split_s = s.split()
        #return length of last word
        return len(split_s[-1])