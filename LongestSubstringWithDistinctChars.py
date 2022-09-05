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


def non_repeat_substring_2(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
    string = 'aabcacde'
    print(non_repeat_substring_2(string))


if __name__ == "__main__":
    main()