'''
Write a function that takes a string as input and checks whether it can be a valid palindrome 
by removing at most one character from it.
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