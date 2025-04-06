
from typing import List, Optional
import math

class Solution:
    # n - number of pairs
    # We CAN keep adding "(" if its count is less than n
    # We CAN keep adding the ")" if its count is less than the count of "("
    # ()
    # ((
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(left_count, right_count, curr = ""):
            if left_count == right_count == n:
                res.append("".join(curr))

            if left_count < n:
                backtracking(left_count + 1, right_count, curr + "(")
            if right_count < left_count:
                backtracking(left_count, right_count + 1, curr + ")")

        backtracking(0, 0)
        return res

def main():
    n = 10
    solution = Solution()
    print(solution.generateParenthesis(n))
    
     
if __name__ == "__main__":
    main()
        