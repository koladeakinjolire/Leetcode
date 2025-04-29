class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        text_vowels = []
        indices = []
        string = list(s)
        for i, char in enumerate(string):
            if char in vowels:
                text_vowels.append(char)
                indices.append(i)

        indices = list(reversed(indices))
        vowels_dict = dict(zip(indices, text_vowels)) 
        for key in vowels_dict.keys():
                string[key] = vowels_dict[key]

        return str(''.join(string))