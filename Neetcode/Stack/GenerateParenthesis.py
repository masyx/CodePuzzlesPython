"""22. Generate Parentheses
Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 

Constraints:
1 <= n <= 8
"""

from typing import List
from collections import deque

class Solution:
    # O(2^2n * n) time | O(2^2n * n) space
    def generate_parenthesis_bf(self, n: int) -> List[str]:
        def is_valid(s):
            open = 0
            for char in s:
                open += 1 if char == "(" else -1
                # fail early
                if open < 0:
                    return False
            valid = open == 0
            return valid
        
        res = []
        queue = deque([""])
        while queue:
            curr_str = queue.popleft()
            if len(curr_str) == 2 * n:
                if is_valid(curr_str):
                    res.append(curr_str)
                # Using the continue statement here to skip the rest of the loop iteration after
                # checking if curr is a complete string (i.e. has length 2 * n)
                continue
            
            queue.append(curr_str + "(")
            queue.append(curr_str + ")")
            
        return res

    def generate_parenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                result.append("".join(current))
                return

            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count)
                current.pop()

            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1)
                current.pop()

        backtrack(0, 0)
        return result
    
    
def main():
    n = 1
    sol = Solution()
    print(sol.generate_parenthesis_bf(n))
    print(sol.generate_parenthesis(n))
    
    
if __name__ == "__main__":
    main()