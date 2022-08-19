# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    max_length = 0
    left, right = 0, 0
    for l in range(len(string) - 1):
        for r in range(l + 1, len(string)):
            if string[l] == string[r]:
                current_length = r - l + 1
                if current_length > max_length and is_substring_palindromic(string, l, r):
                    max_length = current_length
                    left, right = l, r
    return string[left:right + 1]

def is_substring_palindromic(string, left, right):
    l, r = left, right
    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True


def longestPalindromicSubstring_not_as_optimal(string):
    max_length = 0
    left, right = 0, 0
    for l in range(len(string) - 1):
        for r in range(l + 1, len(string)):
            if string[l] == string[r]:
                if is_substring_palindromic(string, l, r):
                    current_length = r - l + 1
                    max_length = max(max_length, current_length)
                    if max_length == current_length:
                        left, right = l, r
    return string[left:right + 1]


def main():
    myString = "fabaxyzzyx"
    print(longestPalindromicSubstring(myString))
    
if __name__ == "__main__":
    main()