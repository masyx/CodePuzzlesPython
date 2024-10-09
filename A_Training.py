from collections import defaultdict
#
# abcbwa

# 012345
#    i
# abaabc
#      j
# seen = a b
# longest = 2

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


if __name__ == "__main__":
    s="dvdf"
    print(longest_substring(s))