def encode(strs) -> str:
        result = ""
        for s in strs:
               result += str(len(s)) + "|" + s
        return result
            

def decode(s) -> list:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i = j + 1 + length
        return result

print(encode(["neet","code","love","you"]))
print(decode('neet code love you'))
print(encode([""]))
print(decode(''))