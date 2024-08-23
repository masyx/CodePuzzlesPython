from collections import defaultdict

def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if l < r and s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
       

if __name__ == "__main__":
    s=",."
    print(isPalindrome(s))