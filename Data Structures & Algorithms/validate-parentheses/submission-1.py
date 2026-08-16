class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        my_stack = []

        for char in s:
            if char in brackets:
                if not my_stack or my_stack.pop() != brackets[char]:
                    return False
            else:
                my_stack.append(char)
        return not my_stack
