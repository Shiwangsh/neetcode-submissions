class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        my_stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                my_stack.append(char)
            else:
                if len(my_stack) == 0:
                    return False
                top = my_stack.pop()
                if brackets[char] != top:
                    return False
        if len(my_stack) == 0:
            return True
        else:
            return False


