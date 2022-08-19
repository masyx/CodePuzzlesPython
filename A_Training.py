# O(n) time | O(n ) space
def is_palindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

def is_palindrome_recursive(string, left = 0):
    right = len(string) - 1 - left
    while left <= right:
        return string[left] == string[right] and is_palindrome_recursive(string, left + 1)
    return True


def is_palindrome_recursive_2(string, left = 0):
    right = len(string) - 1 - left
    if left >= right:
        return True
    else:
        return string[left] == string[right] and is_palindrome_recursive_2(string, left + 1)


def is_palindrome_rec(string):
    
    return 

def main():
    string = 'fdd'
    print(is_palindrome_recursive_2(string))
    
if __name__ == "__main__":
    main()