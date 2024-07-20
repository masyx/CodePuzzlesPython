'''
409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

# O(n) time | O(1) space, because alphabet has 26 letters only, 
# the size of a dictionary max can be 26, which is O(1)
def longestPalindrome(s):
    chars_count = {}
    length = 0
    odd_used = False
    for char in s:
        chars_count[char] = chars_count.get(char, 0) + 1
    
    for char in chars_count:
        if (chars_count[char] % 2) != 0:
            if not odd_used:
                length += chars_count[char]
                odd_used = True
            else:
                length += chars_count[char] - 1
        else:
            length += chars_count[char]
    return length

def longestPalindrome2(s: str) -> int:
    odd_freq_chars_count = 0
    frequency_map = {}

    for c in s:
        frequency_map[c] = frequency_map.get(c, 0) + 1

        if frequency_map[c] % 2 == 1:
            odd_freq_chars_count += 1
        else:
            odd_freq_chars_count -= 1
    # consider string 'acccab', a-2, c-3, b-1, so 6(total length) - 2(char odd count) + 1 = 5
    if odd_freq_chars_count > 0:
        return len(s) - odd_freq_chars_count + 1
    else:
        return len(s)
    
def longestPalindrome3(s: str) -> int:
    char_frequency = [0] * 52
    odd_chars_count = 0
    
    for char in s:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
        elif 'A' <= char <= 'Z':
            index = ord(char) - ord('A') + 26
        char_frequency[index] += 1

        if char_frequency[index] % 2 == 0:
            odd_chars_count -= 1
        else:
            odd_chars_count += 1

    if odd_chars_count == 0:
        return len(s)
    else:
        return len(s) - odd_chars_count + 1

def longestPalindrome4(s:str) -> int:
    chars = set()
    result = 0
    for char in s:
        if char in chars:
            result += 2
            chars.remove(char)
        else:
            chars.add(char)
    if chars:
        result += 1
    return result

if __name__ == "__main__":
    s = "aCCCab"
    print(longestPalindrome(s))
    print(longestPalindrome2(s))
    print(longestPalindrome3(s))
    print(longestPalindrome4(s))