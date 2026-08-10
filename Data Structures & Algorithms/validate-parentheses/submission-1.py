class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for e in s:
            if e in "({[":
                stack.append(e)

            if e in ")}]":
                
                if stack:
                    pair = stack.pop()
                else:
                    return False

                if pair != pairs[e]:
                    return False
        
        return not stack