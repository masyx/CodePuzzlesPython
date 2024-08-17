from collections import defaultdict

# O(n * m) time | O(1) space
def group_anagrams(strs):
    resutlt = defaultdict(list)
    for s in strs:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord('a')] += 1
        resutlt[tuple(chars)].append(s)
    return list(resutlt.values())

# O(m) time | O(1) space
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    seen = [0] * 26
    for i in range(len(s)):
        seen[ord(s[i]) - ord('a')] += 1
        seen[ord(t[i]) - ord('a')] -= 1
        
    for char in s:
        if seen[ord(char) - ord('a')] != 0:
            return False
    return True


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams_2(strs))