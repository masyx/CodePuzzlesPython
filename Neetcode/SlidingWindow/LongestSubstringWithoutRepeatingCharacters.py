'''
3. Longest Substring Without Repeating Characters
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

# O(n) time | O(m) space, where m is the total number of distinct chars in array
def length_of_longest_substring_my_original(s: str)-> int:
    if not s:
        return 0
    res = 1
    l, r = 0, 1
    seen = {s[l]}
    while r < len(s):
        curr_char = s[r]
        if curr_char not in seen:
            res = max(res, r - l + 1)
        else:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
        seen.add(curr_char)
        r += 1
    return res

#O(2n) -> O(n) time | O(1) space
def lengthOfLongestSubstring(s):
    longest = 0
    used_chars = {}
    l = 0
    for r in range(len(s)):
        used_chars[s[r]] = used_chars.get(s[r], 0) + 1
        
        while used_chars[s[r]] > 1:
            used_chars[s[l]] -= 1
            l += 1
        
        longest = max(longest, r - l + 1)
    return longest

def length_of_longest_substring(s: str) -> int:
    seen = set()
    l = 0
    max_len = 0

    for r, char in enumerate(s):
        # Shrink the window until `char` is no longer in the set
        while char in seen:
            seen.remove(s[l])
            l += 1

        seen.add(char)
        max_len = max(max_len, r - l + 1)

    return max_len



if __name__ == "__main__":
    s = "pwwkew"
    #s ="dvdf"
    #s = "nfpdmpi"
    #s = "abcabcbb"
    #s = "accabdaz"
    print(length_of_longest_substring(s))
        