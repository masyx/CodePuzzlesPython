def isAnagram(s, t):
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
    return not seen

if __name__ == "__main__":
    s = "car"
    t = "acra"
    print(isAnagram(s, t))