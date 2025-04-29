def reverseWords(s):
    s_list = s.split()
    s_list = s_list[::-1]
    new_sentence = " ".join(list(s_list))
    return new_sentence



s = 'the sky is blue'
print(reverseWords(s))