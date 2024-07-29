'''
Description
Medium

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# Check later if this is a duplicate 
# "LongestSubstringWithDistinctChars.py', this is mihailescu

def lengthOfLongestSubstring(s):
    longest = 0
    left = 0
    observed_chars = set()
    for right in range(len(s)):
        if s[right] in observed_chars:
            observed_chars.remove(s[right])
            left += 1
        observed_chars.add(s[right])
        
        longest = max(longest, right - left + 1)
    return longest

if __name__ == "__main__":
    s = "pwwkew"
    print("Length of the longest substring without "
        f"repeating char is: {lengthOfLongestSubstring(s)}")
        