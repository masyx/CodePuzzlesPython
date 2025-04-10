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

# O(n + m) time | O(1) space
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

def isAnagramSort(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

if __name__ == "__main__":
    s = "car"
    t = "acr"
    print(isAnagram(s, t))
    print(valid_anagram(s, t))
    print()