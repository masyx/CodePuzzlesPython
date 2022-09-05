# O(n) time | O(1) space, where k is the number of distinct chars in array
""" The algorithm's space complexity will be O(K), where K is the number of distinct characters 
in the input string. This also means K<=N, because in the worst case, the whole string might not 
have any duplicate character, so the entire string will be added to the HashMap. Having said that, 
since we can expect a fixed set of characters in the input string (e.g., 26 for English letters),
we can say that the algorithm runs in fixed space O(1); in this case, 
we can use a fixed-size array instead of the HashMap.  """
def non_repeat_substring(string):
    l = 0
    longest = 0
    used_chars = {}
    for r in range(len(string)):
        right_char = string[r]
        used_chars[right_char] = used_chars.get(right_char, 0) + 1
        while used_chars[right_char] > 1:
            left_char = string[l]
            used_chars[left_char] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest


def main():
    string = 'aabcacde'
    print(non_repeat_substring(string))


if __name__ == "__main__":
    main()