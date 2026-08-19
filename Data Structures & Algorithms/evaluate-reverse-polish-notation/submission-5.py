# ifelse solution:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if tokens[i] == '+':
                    result = num1 + num2
                elif tokens[i] == '-':
                    result = num1 - num2
                elif tokens[i] == '*':
                    result = num1 * num2
                elif tokens[i] == '/':
                    result = int(num1 / num2)
                stack.append(result)
            i += 1
        return stack[-1]