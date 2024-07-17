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

def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_length = 0
    max_count = 0
    count = {}

    for right in range(len(s)):
        # Add the current character to the count dictionary
        count[s[right]] = count.get(s[right], 0) + 1
        # Update the count of the most frequent character in the current window
        max_count = max(max_count, count[s[right]])

        # Calculate the number of changes needed
        if (right - left + 1) - max_count > k:
            # If changes exceed k, shrink the window from the left
            count[s[left]] -= 1
            left += 1

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    print(characterReplacement("ABAB", 2))  # Output: 4
    print(characterReplacement("AABABBA", 1))  # Output: 4
