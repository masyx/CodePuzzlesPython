from typing import List

class Solution:
    #                v
    #i:  0   1   2   3   4
    #  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # stack = [3, 3]
    # val_2 = 1, val_1 = 2
    
    # O(n) time | O(m) space
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"*", "/", "+", "-"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val_2 = stack.pop()
                val_1 = stack.pop()
                result = 0
                if token == "+":
                    result = val_1 + val_2
                elif token == "-":
                    result = val_1 - val_2
                elif token == "*":
                    result = val_1 * val_2
                elif token == "/":
                    result = int(val_1 / val_2)
                stack.append(result)
        return stack[0]
            
        
        
  
    
def main():
    solution = Solution()
    tokens = ["18"]
    print(solution.evalRPN(tokens))
    
     
if __name__ == "__main__":
    main()