from typing import List

def func(op, val1, val2):
    if op == '+':
        return val1 + val2
    elif op == '-':
        return val1 - val2
    elif op == '*':
        return val1 * val2
    else:
        # Standard RPN behavior: truncate toward zero
        return int(val1 / val2)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'} # Using a set for faster lookup

        for i in tokens:
            if i not in operators:
                # If it's a number, push it onto the stack
                stack.append(int(i))
            else:
                # If it's an operator, pop the top two values
                # Note: The second pop is actually the 'left' operand
                val2 = stack.pop()
                val1 = stack.pop()
                
                # Calculate the result
                result = func(i, val1, val2)
                
                # THE TWEAK: Push the result back onto the stack
                stack.append(result)
        
        # At the end, the only thing left on the stack is the final answer
        return stack[0]