class Solution:
    def isValid(self, s: str) -> bool:
        closedOpen = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        stack = []
        for char in s:
            if char not in closedOpen:
                stack.append(char)
            else:
                if stack and stack[-1] == closedOpen[char]:
                    stack.pop()
                else:
                    return False
        return not stack
        