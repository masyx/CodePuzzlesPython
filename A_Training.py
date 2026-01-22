from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #               j
    #          0  1 2
    # space = [5,11]
    #             i                  
    #  0123456789112345           
    # "HelloPythonWorld" 
    # res = [Hello Python World]
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        s_idx, space_idx = 0, 0
        for i in range(len(s)):
            if (space_idx < len(spaces)
                and i == spaces[space_idx]):
                res.append(' ')
                space_idx += 1
            res.append(s[i])
        return "".join(res)
    
    # s = "EnjoyYourCoffee" spaces = [5, 9]
    def addSpaces_2(self, s: str, spaces: List[int]) -> str:
        res = []
        prev = 0
        for curr in spaces:
            res.append(s[prev:curr] + " ")
            prev = curr
        res.append(s[spaces[-1]:])
        return "".join(res)
    
                
            

            


                    
        
        
if __name__ == "__main__":
    s = "HelloPythonWorld"
    spaces = [5,11]
    sol = Solution()
    print(sol.addSpaces(s, spaces))
    