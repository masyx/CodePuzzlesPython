class Solution(object):
    def is_valid_parenthesis(string):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in string:
            if char not in mapping:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
        return not stack

def main():
    print(Solution.is_valid_parenthesis("()[(]){}"))


if __name__ == "__main__":
    main()