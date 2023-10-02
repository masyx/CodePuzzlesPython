class Solution(object):
    def is_valid_parenthesis(string):
        # The stack to keep the track of opening brackets
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in string:
            if stack and char in mapping:
                top_element = stack.pop()
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack

def main():
    print(Solution.is_valid_parenthesis("())(){}"))


if __name__ == "__main__":
    main()