class Solution:
    
    # stack: [")"]
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char not in map:
                stack.append(char)
            elif stack and map[char] == stack[-1]:
                    stack.pop()
            else:
                return False
        return len(stack) == 0
        
  
    
def main():
    solution = Solution()
    s = ")()[{}]"
    print(solution.isValid(s))
    
     
if __name__ == "__main__":
    main()