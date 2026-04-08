class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if token == "+":
                result.append((result.pop() + result.pop()))            
            elif token == "-":
                #El primer elemento al que hacemos pop en realidad es el segundo
                second = result.pop()
                first = result.pop()
                result.append(first - second)            
            elif token == "*":
                result.append((result.pop() * result.pop()))            
            elif token == "/":
                second = result.pop()
                first = result.pop()
                result.append(int(first/second))            
            else:
                result.append(int(token))
            print(result)
        return result.pop()

        