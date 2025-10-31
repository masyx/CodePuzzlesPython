"""150. Evaluate Reverse Polish Notation
Solved
Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List

class Solution:
    def evalRPN_clean(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        opt = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            # Use int(a / b) instead of a // b: Python's // floors toward -∞, 
            # but the problem requires truncation toward 0 (e.g., -7//3 == -3; expected -2).
            "/": lambda a, b: int(a / b)
            
        }
        
        for t in tokens:
            if t not in opt:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(opt[t](a, b))
        return stack[0]
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val_2 = stack.pop()
                val_1 = stack.pop()
                res = 0
                if token == "+":
                    res = val_1 + val_2
                elif token == "-":
                    res = val_1 - val_2
                elif token == "*":
                    res = val_1 * val_2
                elif token == "/":
                    res = int(val_1 / val_2)
                stack.append(res)
        return stack[0]
            
        
    
    
def main():
    tokens = ["4","13","5","/","+"]
    #tokens = ["2","1","+","3","*"]
    solution = Solution()
    print(solution.evalRPN(tokens))
    print(solution.evalRPN_clean(tokens))
    
if __name__ == "__main__":
    main()