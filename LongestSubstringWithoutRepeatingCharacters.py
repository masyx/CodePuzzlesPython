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

# O(n) time | O(1) space, where k is the number of distinct chars in array
""" The algorithm's space complexity will be O(K), where K is the number of distinct characters 
in the input string. This also means K<=N, because in the worst case, the whole string might not 
have any duplicate character, so the entire string will be added to the HashMap. Having said that, 
since we can expect a fixed set of characters in the input string (e.g., 26 for English letters),
we can say that the algorithm runs in fixed space O(1); in this case, 
we can use a fixed-size array instead of the HashMap.  """
def lengthOfLongestSubstring_my_og(s):
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

#O(2n) -> O(n) time | O(1) space
def lengthOfLongestSubstring(s):
    longest = 0
    used_chars = {}
    left = 0
    for right in range(len(s)):
        used_chars[s[right]] = used_chars.get(s[right], 0) + 1
        
        while used_chars[s[right]] > 1:
            used_chars[s[left]] -= 1
            left += 1
        
        longest = max(longest, right - left + 1)
    return longest


def length_of_longest_substring_improved(s):
    if len(s) == 0:
        return 0
    start, longest = 0, 0
    last_seen_at = {}
    for index, char in enumerate(s):
        if char in last_seen_at and last_seen_at[char] >= start:
            start = last_seen_at[char] + 1
        
        last_seen_at[char] = index
        longest = max(longest, index - start + 1)
    return longest

def length_of_longest_substring_array(s):
    if len(s) == 0:
        return 0
    start, longest = 0, 0
    last_seen_at = [-1] * 128
    for i, char in enumerate(s):
        if last_seen_at[ord(char)] >= start:
            start = last_seen_at[ord(char)] + 1
        
        last_seen_at[ord(char)] = i
        longest = max(longest, i - start + 1)
    return longest


if __name__ == "__main__":
    #s = "pwwkew"
    #s ="dvdf"
    #s = "nfpdmpi"
    #s = "abcabcbb"
    unicode_number = ord("A")
    char = chr(unicode_number)
    s = "ACCABabcxyzXYZ"
    print("Length of the longest substring without "
        f"repeating char is: {length_of_longest_substring_array(s)}")
        