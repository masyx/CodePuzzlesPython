class Solution:
    # O(n) time | O(n) space
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        #return len(stack) == 0
        #return stack == []
        return not stack

class Solution2:
    
    #O(n) time | O(n) space, all characters in the string are opening brackets (like "(((([[[{{{"), and none of them are matched and popped. So all n characters end up on the stack.
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
    s = "{()[]}"
    solution = Solution()
    print(solution.isValid(s))


if __name__ == "__main__":
    main()