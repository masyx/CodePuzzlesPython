''' 125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

# O(n) time | O(n) space
def is_palindrome_2(s):
    arr = [char.lower() for char in s if char.isalnum()]
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True

def is_palindrome(s: str):
    l = 0
    length = len(s)
    r = length - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def is_alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9') )
    

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(f"Is string '{s}' a palindrome: {'Yes' if is_palindrome(s) else 'No'}")