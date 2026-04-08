class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        characters = {
            "{":"}",
            "(":")",
            "[":"]"
        }

        n = len(s)
        if n % 2 != 0:
            return False
        
        for char in s:
            if char in characters.keys():
                stack.append(char)
            else: 
                if not stack:
                    return False
                peek = stack[-1]
                if characters[peek] != char:
                    return False
                stack.pop()
        return not stack
            