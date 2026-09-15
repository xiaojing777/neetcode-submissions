class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                if char==")" or char=="]" or char=="}":
                    return False
                else:
                    stack.append(char)
            elif char=="]":
                tmp = stack.pop()
                if tmp!="[":
                    return False
            elif char==")":
                tmp = stack.pop()
                if tmp!="(":
                    return False
            elif char=="}":
                tmp = stack.pop()
                if tmp!="{":
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        else:
            return False

        