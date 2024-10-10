from collections import defaultdict

# 012345
#    i
# abaabc
#      j
# seen = a b
# longest = 2

# 0123
#  i
# dvdf
#    j
# seen = v
# longest = 

# O(n) time | O(1) space
def longest_substring(s):
    seen = {}
    longest = 0
    i = 0
    for j in range(len(s)):
        while s[j] in seen:
            del seen[s[i]]
            i += 1
        seen[s[j]] = True
        longest = max(longest, j - i + 1)
    return longest

def longest_substring_array(s):
    seen = [" "] * 128
    i = 0
    longest = 0
    for j in range(len(s)):
        while seen[ord(s[j])] == s[j]:
            seen[ord(s[i])] = " "
            i += 1
        seen[ord(s[j])] = s[j]
        longest = max(longest, j - i + 1)
    return longest


if __name__ == "__main__":
    s="dvdf"
    print(longest_substring_array(s))