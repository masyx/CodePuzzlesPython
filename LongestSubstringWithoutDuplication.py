def longestSubstringWithoutDuplication(string):
    l = 0
    longest = 0
    used_chars = {}
    result = ''
    for r in range(len(string)):
        right_char = string[r]
        used_chars[right_char] = used_chars.get(right_char, 0) + 1
        while used_chars[right_char] > 1:
            left_char = string[l]
            used_chars[left_char] -= 1
            l += 1
        if r - l + 1 > longest:
            longest = r - l + 1
            result = string[l:r + 1]
    return result


def main():
    string = 'clementisacap'
    print(longestSubstringWithoutDuplication(string))


if __name__ == "__main__":
    main()