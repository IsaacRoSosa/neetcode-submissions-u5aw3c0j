class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
           encoded += str(len(string))
           encoded += "#"
           encoded += string
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            k = i
            #recorremos el numero
            while s[k] != "#":
                k += 1
            num = int(s[i:k])
            i = k+1
            k = i + num
            decode.append(s[i:i+num])
            i = k
        return decode

            
            
            
