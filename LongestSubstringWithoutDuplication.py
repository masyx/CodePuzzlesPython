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


def longestSubstringWithoutDuplication(string):
    left = 0
    longest_idx = [0, 0]
    last_seen = {}
    for idx, char in enumerate(string):
        if char in last_seen:
            left = max(left, last_seen[char] + 1)
        if idx - left + 1 > longest_idx[1] - longest_idx[0]:
            longest_idx = [left, idx + 1]
        last_seen[char] = idx
    return string[longest_idx[0] : longest_idx[1]]

def main():
    # clementisacap
    string = 'clementisacap'
    print(longestSubstringWithoutDuplication(string))


if __name__ == "__main__":
    main()