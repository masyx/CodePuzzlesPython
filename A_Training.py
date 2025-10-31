import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        opt = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        
        for t in tokens:
            if t not in opt:
                stack.append(int(t))
            else:
                method = opt[t]
                val_2 = stack.pop()
                val_1 = stack.pop()
                res = method(val_1, val_2)
                stack.append(res)
            
        return res
                



                    
    
def main():
    
    tokens=tokens = ["4","13","5","/","+"]
    sol = Solution()
    print(sol.evalRPN(tokens))
  
  
if __name__ == "__main__":
    main()