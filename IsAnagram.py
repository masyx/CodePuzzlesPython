# O(n + m) time, word1 could be 1,000 letters a
# and word2 could 1,000 letters b, so we have to iterate 
# through both words
# O(1) is space complexity, because the number of letters in
# an alphabet is 26
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

def isAnagramSort(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

if __name__ == "__main__":
    s = "car"
    t = "acr"
    print(isAnagram(s, t))
    print(isAnagramSort(s, t))
    print()