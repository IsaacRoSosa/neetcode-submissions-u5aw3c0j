class Solution:
    def decodeString(self, s: str) -> str:
        decode = []

        for char in s:
            if char != "]":
                decode.append(char)
            else:
                #Construir el string
                chunk = []
                while decode and decode[-1] != "[":
                    chunk.append(decode.pop())
                #Darle pop al [
                decode.pop()
                chunk.reverse()
                
                nums =[]
                #Construimos el numero
                while decode and decode[-1].isdigit():
                    nums.append(decode.pop())
                nums.reverse()
                decode.append( ("".join(chunk) * int("".join(nums))))
        return "".join(decode)
                



        