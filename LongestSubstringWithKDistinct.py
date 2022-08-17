# Given a string, find the length of the longest substring in it with no more than K distinct characters. (MEDIUM)
# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# 
# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# 
# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
# 
# Example 4:
# Input: String="cbbebi", K=10
# Output: 6
# Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".


def longest_substring_with_k_distinct(str1, k):
    used = set()
    l = 0
    max_length = 0
    curr_length = 0
    for r in range(len(str1)):
        while len(used) > k:
            used.remove(str1[l])
            l += 1
        used.add(str1[r])
        if len(used) <= k:
            curr_length += 1
        max_length = max(max_length, curr_length)
    return max_length


def main():
    string1 = 'araaci'
    print(longest_substring_with_k_distinct(string1, 1))


if __name__ == '__main__':
    main()