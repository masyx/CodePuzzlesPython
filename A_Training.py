from collections import defaultdict

def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    
    stack = []
    map = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    for char in s:
        if char not in map:
            stack.append(char)
        else:
            if not stack or stack[-1] != map[char]:
                return False
            stack.pop()
    return len(stack) == 0
       

if __name__ == "__main__":
    s="(){}}{"
    print(isValid(s))