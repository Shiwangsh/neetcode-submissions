import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+','-','*','/']
        ops = {
            '+': operator.add,
            '-':operator.sub,
            '*': operator.mul,
            '/':operator.truediv
        }
        stack=[]
        i = 0
        while i < len(tokens):
            if tokens[i] not in operators:
               stack.append(int(tokens[i]))
            else:
                num2=stack.pop()
                num1=stack.pop()
                
                result = ops[tokens[i]](num1,num2)
                stack.append(int(result))
            
            i += 1
        return stack[-1]
        