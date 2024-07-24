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


# The key insight is that we are always trying to maximize the window size while keeping the 
# number of replacement <= k. We do this by maintaining a window where 
# window_size - max_frequent_char_count <=k. This inequality represents the number of replacements
# we need to make to have all characters in the window the same

# O(n) time | O(1) space, because alphabet has 26 chars
def characterReplacement(s: str, k: int) -> int:
    start = 0
    max_length_substr = 0
    max_repeating_char_count = 0
    char_count = {}

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        max_repeating_char_count = max(max_repeating_char_count, char_count[s[end]])

        window_size = end - start + 1
        # Calculate the number of replacements needed
        changes_needed_count = window_size - max_repeating_char_count

        # If number of changes exceeds k, shrink the window from the start
        if changes_needed_count > k:
            char_count[s[start]] -= 1
            start += 1

        max_length_substr = max(max_length_substr, end - start + 1)

    return max_length_substr
if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))  # Output: 4
    print(characterReplacement("AABABBA", 1))  # Output: 4
