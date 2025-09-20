def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    #create a dictionary to hold the anagrams
    anagram_map = {}
    
    #iterate through each string in the input list
    for string in strs:
        sorted_str = ''.join(sorted(string))
        #check if the sorted string is already a key in the dictionary
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(string)
        else:
            anagram_map[sorted_str] = [string]
    
    #return the values of the dictionary as a list of lists
    return list(anagram_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "ant","bat","act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))