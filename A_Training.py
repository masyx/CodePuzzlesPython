def is_palindrome(word):
    start = 0
    end = len(word) - 1
    removed_chars = 0
    while start < end:
        if word[start] != word[end]:
            if removed_chars > 1:
                return False
            else:
                

    return True

if __name__ == "__main__":
    word = "abcbma"
    print(is_palindrome(word))