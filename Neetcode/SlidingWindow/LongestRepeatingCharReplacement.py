'''
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description/
Difficulty: Medium
You are given a string s and an integer k. You can choose any character of the string and change it to any 
other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length

'''

from collections import defaultdict



class Solution:
    # We don't update max_freq when shrinking the window because it's only used to check if the window is valid.
    # A stale (too high) max_freq might cause us to shrink the window earlier than necessary,
    # but it never breaks correctness and avoids expensive recomputation, keeping the algorithm O(n).
    def character_replacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        max_freq = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])
            
            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            
    #       r
    #   l
    #  0123456
    # "AAABABB"
    # A = 3, B = 2
    # max_freq = 4
    # res = 5
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = [0] * 26
        l = 0
        max_freq = 0
        for r, char in enumerate(s):
            counts[ord(char) - ord('A')] += 1
            max_freq = max(max_freq, counts[ord(char) - ord('A')])
            if (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    
    
# The key insight is that we are always trying to maximize the window size while keeping the 
# number of replacement <= k. We do this by maintaining a window where 
# window_size - max_frequent_char_count <=k. This inequality represents the number of replacements
# we need to make to have all characters in the window the same

# O(n) time | O(1) space, because alphabet has 26 chars
def characterReplacement(s: str, k: int) -> int:
    start = 0
    char_count = {}
    max_repeating_char_count = 0
    longest_substr = 0
    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_repeating_char_count = max(max_repeating_char_count, char_count[s[end]])
        window_size = end - start + 1
        # Calculate the number of replacements needed
        num_replacements = window_size - max_repeating_char_count

        # If number of replacements exceeds k, shrink the window from the start
        if num_replacements > k:
            char_count[s[start]] -= 1
            start += 1

        longest_substr = max(longest_substr, end - start + 1)
    return longest_substr

if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))  # Output: 4
    print(characterReplacement("AABABBA", 1))  # Output: 4
