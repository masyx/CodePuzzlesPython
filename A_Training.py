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

def is_palindrome(s):
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

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(f"Is string '{s}' a palindrome: {'Yes' if is_palindrome(s) else 'No'}")