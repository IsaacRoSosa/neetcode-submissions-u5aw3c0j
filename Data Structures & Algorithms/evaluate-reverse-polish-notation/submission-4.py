class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for token in tokens:
            if token in "+*-/":
                second = result.pop()
                first = result.pop()
                if token == "+":
                    result.append(first + second)            
                elif token == "-":
                    result.append(first - second)            
                elif token == "*":
                    result.append(first * second)            
                elif token == "/":
                    result.append(int(first/second))            
            else:
                result.append(int(token))
            print(result)
        return result.pop()

        