class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                lastInStack = stack.pop()
                if c == ")" and lastInStack != "(":
                    return False
                elif c == "]" and lastInStack != "[":
                    return False
                elif c == "}" and lastInStack != "{":
                    return False

        return len(stack) == 0