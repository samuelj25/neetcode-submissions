class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in matches:
                if (not stack) or (matches[char] != stack.pop()):
                    return False
            else:
                stack.append(char)

        return (len(stack) == 0)
