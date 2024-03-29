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

# O(n(for loop) + n(while loop)) => O(n) time | O(k) space where k is distinct characters in the string
def longest_substring_with_k_distinct(str1, k):
    used = {}
    l = 0
    max_length = 0
    for r in range(len(str1)):
        if str1[r] not in used:
            used[str1[r]] = 0
        used[str1[r]] += 1

        while(len(used)) > k:
            used[str1[l]] -= 1
            if used[str1[l]] == 0:
                del used[str1[l]]
            l += 1
        max_length = max(max_length, r - l + 1)
    return max_length


def main():
    string1 = 'aakjjjio'
    print(longest_substring_with_k_distinct(string1, 2))


if __name__ == '__main__':
    main()