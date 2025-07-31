def scoreOfString(s):
        """
        :type s: str
        :rtype: int
        """
        #edge case
        if len(s) < 2:
            return 0
        
        #calculate the score
        score = 0
        for i in range(len(s) - 1):
            result = abs(ord(s[i]) - ord(s[i+1]))
            score += result

        return score

print(scoreOfString("hello"))
print(scoreOfString("zaz"))
print(scoreOfString("paramecium"))
print(scoreOfString('valuable'))
print(scoreOfString('acrobatic'))
print(scoreOfString('a'))
print(scoreOfString(''))
print(scoreOfString('cryptography'))