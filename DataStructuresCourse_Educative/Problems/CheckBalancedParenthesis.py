# O(n) time | O(n) space
def is_balanced(str):
    if len(str) % 2 != 0:
        return False

    visited = []
    parenthesis_map = { ")":"(", "]":"[", "}":"{" }
    
    for char in str:
        if char in parenthesis_map:
            if not visited or visited.pop() != parenthesis_map[char]:
                return False
        else:
            visited.append(char)
    
    return len(visited) == 0
        
        
        
if __name__ == "__main__":
    exp1 = "{[({})]}"
    exp2 = "{[]}"
    exp3 = ""
    exp4 = "]"
    exp5 = "()){(({)[}}}()){((])"
    exp6 = "))))))"
    exp7 = "[["
    print(is_balanced(exp6))