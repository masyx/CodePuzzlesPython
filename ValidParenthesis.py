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



def main():
    s = "{()[]}"
    solution = Solution()
    print(solution.isValid(s))


if __name__ == "__main__":
    main()