def isAnagram(s: str, t: str) -> bool:
    chars = {}
    for char in s:
        chars[char] = chars.get(char, 0) + 1
    
    for char in t:
        if char not in chars:
            return False
        chars[char] -= 1
        if chars[char] == 0:
            chars.pop(char)
    return not chars

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    
    print(f"Is '{t}' an anagram of '{s}': {'Yes' if isAnagram(s, t) else 'No'}")