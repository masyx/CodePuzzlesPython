# O(n) time | O(n) space
def is_palindrome(s):
    arr = [char.lower() for char in s if char.isalnum()]
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(f"Is string '{s}' a palindrome: {'Yes' if is_palindrome(s) else 'No'}")