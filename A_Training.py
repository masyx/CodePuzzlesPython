from collections import defaultdict
from typing import List


def valid_anagram(s, t) -> bool:
    if len(s) != len(t):
        return False
    
    counter = [0] * 26
    for i in range(len(s)):
        counter[ord(s[i]) - ord('a')] += 1
        counter[ord(t[i]) - ord('a')] -= 1
    
    for count in counter:
        if count != 0:
            return False
    return True


def main():
    print(valid_anagram("rat", "car"))    
    
if __name__ == "__main__":
    main()