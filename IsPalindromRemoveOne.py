def is_palindrome(word):
    start = 0
    end = len(word) - 1
    removed_chars = 0
    while start < end:
        if word[start] != word[end]:
            if removed_chars > 0:
                return False
            else:
                if word[start] == word[end - 1]:
                    end -= 1
                    removed_chars += 1
                elif word[start + 1] == word[end]:
                    start += 1
                    removed_chars += 1
                else:
                    return False

        start += 1
        end -= 1

    return True

if __name__ == "__main__":
    word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVgVUTSRQPONMLKLJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
    print(is_palindrome(word))