class Solution:
    def decodeString(self, s: str) -> str:
        decode = []
        #Recorremos el arreglo
        for char in s:
            #Vamos agregando a nuestro stack hasta encontrar el primer bracket cerrado
            if char != "]":
                decode.append(char)
            else:
                #1, Construir el nuevo string
                chunk = []
                #Detenernos en el open bracket
                while decode[-1] != "[":
                    chunk.append(decode.pop())
                #1.2 hacemos pop del open bracket
                decode.pop()
                chunk.reverse()
                newString = "".join(chunk)
                #2, Obtener el numero
                nums = []
                while decode and decode[-1].isdigit():
                    nums.append(decode.pop())
                nums.reverse()
                num = "".join(nums)

                #3 multiplicamos el string y lo agregamos
                newString *= int(num)
                print("Modified string", newString)
                decode.append(newString)
                
        return "".join(decode)


        