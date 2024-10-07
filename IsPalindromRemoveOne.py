'''
680. Valid Palindrome II
Easy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''

# O(n) time | O(1) space
def is_palindrome(word):
    def is_palindrome_helper(word, start, end):
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True
    
    start = 0
    end = len(word) - 1
    
    while start < end:
        if word[start] != word[end]:
            return is_palindrome_helper(word, start, end - 1) or \
                is_palindrome_helper(word, start + 1, end)
        start += 1
        end -= 1
    
    return True

if __name__ == "__main__":
    word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVgVUTSRQPONMLKLJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
    print(is_palindrome(word))