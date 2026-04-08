class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        stack = []
        for char in s:
            if char in openToClose:
                stack.append(char)
            else:
                if stack and openToClose[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
                    
        return True if not stack else False

        