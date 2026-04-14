class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "(": ")", "[":"]"}
        pairs_rev = {v:k for k,v in pairs.items()}

        stack = []

        for i in range(len(s)):
            if s[i] in pairs.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if stack[-1] == pairs_rev.get(s[i]):
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0

