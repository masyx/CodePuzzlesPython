"""567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


from collections import Counter
#       01
# s1 = "ba", 
#     01234567
# s2="koabjyuu"
# l = 0, r = 1
# r - l + 1 = x ? > 2

# O(n + m) time | O(1) space
def check_inclusion(s1, s2):
    #s1_dict = Counter(s1)
    s1_dict = {}
    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    sliding_window_count = {}
    l = 0
    for r in range(len(s2)):
        sliding_window_count[s2[r]] = sliding_window_count.get(s2[r], 0) + 1
        if r - l + 1 > len(s1):
            sliding_window_count[s2[l]] -= 1
            if sliding_window_count[s2[l]] == 0:
                del sliding_window_count[s2[l]]
            l += 1
        if s1_dict == sliding_window_count:
            return True
    return False

# O(n + m) time | O(1) space
def check_inclusion_array(s1, s2):
    count1 = [0] * 26
    count2 = [0] * 26
    for char in s1:
        count1[ord(char) - ord('a')] += 1
    l = 0
    for r in range(len(s2)):
        count2[ord(s2[r]) - ord('a')] += 1
        if r - l + 1 > len(s1):
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        if count1 == count2:
            return True
    return False

if __name__ == "__main__":
    s1 = "ba"
    s2="koabjyuu"
    print(check_inclusion(s1, s2))
    print(check_inclusion_array(s1, s2))