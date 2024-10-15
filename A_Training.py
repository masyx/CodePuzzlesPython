# O(n) time | O(1) space
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    seen = {}
    for char in s:
        seen[char] = seen.get(char, 0) + 1
    
    for char in t:
        if char not in seen:
            return False
        seen[char] -= 1
        if seen[char] == 0:
            del seen[char]
    return len(seen) == 0

def isAnagramArray(s, t):
    if len(s) != len(t):
        return False
    chars_count = [0] * 26
    for char in s:
        chars_count[ord(char) - ord('a')] += 1
    for char in t:
        chars_count[ord(char) - ord('a')] -= 1
    for char_count in chars_count:
        if char_count != 0:
            return False
    return True




if __name__ == "__main__":
    nums = [3, 10, 4, 1, 99] # [1,3,4,10,99]
    target = 11
    print(isAnagramArray("tar", "rac"))