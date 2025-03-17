

def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1

    return True

        


def main():
    s = "    "
    print(isPalindrome(s))
    
     
if __name__ == "__main__":
    main()