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

# O(n) time | O(1) space, there 26 letters in alphabet
def lengthOfLongestSubstring(s):
    longest = 0
    left = 0
    observed_chars = {}
    for right in range(len(s)):
        while s[right] in observed_chars:
            observed_chars[s[left]] -= 1
            if observed_chars[s[left]] == 0:
                del observed_chars[s[left]]
            left += 1
            
        observed_chars[s[right]] = observed_chars.get(s[right], 0) + 1
        
        longest = max(longest, right - left + 1)
    return longest

if __name__ == "__main__":
    s = "pwwkew"
    #s ="dvdf"
    #s = "nfpdmpi"
    s = "abcabcbb"
    print("Length of the longest substring without "
        f"repeating char is: {lengthOfLongestSubstring(s)}")
        