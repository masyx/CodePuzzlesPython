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

# O
def characterReplacement(s: str, k: int) -> int:
    start = 0
    max_length_substr = 0
    max_freq_char_count = 0
    char_count = {}

    for end in range(len(s)):
        # Add the current character to the count dictionary
        char_count[s[end]] = char_count.get(s[end], 0) + 1
        # Update the frequency of the most frequent character in the current window
        max_freq_char_count = max(max_freq_char_count, char_count[s[end]])

        # Calculate the number of changes needed
        current_window_length = end - start + 1
        changes_needed_count = current_window_length - max_freq_char_count

        # If number of changes exceeds k, shrink the window from the start
        if changes_needed_count > k:
            char_count[s[start]] -= 1
            start += 1

        # Update the maximum length of the window
        max_length_substr = max(max_length_substr, end - start + 1)

    return max_length_substr
if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))  # Output: 4
    print(characterReplacement("AABABBA", 1))  # Output: 4
