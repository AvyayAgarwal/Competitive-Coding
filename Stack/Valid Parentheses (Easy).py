# 20. Valid Parentheses - Easy
# Tags - Stack, String

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else:
                if len(stack) == 0 or s[i] != stack.pop():
                    return False
        return len(stack) == 0