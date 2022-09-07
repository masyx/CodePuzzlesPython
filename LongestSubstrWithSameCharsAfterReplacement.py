# O(n) time | O(1) space. As we expect only lower case letters in the string, we can conclude that the
# space complexity is O(26), to store each letter frequency in the HashMap, which is asymptotically 
# equal to O(1)
def length_of_longest_substring(str1, k):
    left_idx, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for right_idx, char in enumerate(str1):
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[char])
    
        if (right_idx - left_idx + 1) - max_repeat_letter_count > k:
            left_char = str1[left_idx]
            frequency_map[left_char] -= 1
            left_idx += 1
            
        max_length = max(max_length, right_idx - left_idx + 1)
    
    return max_length



def main():
    # abbcb
    string = "abcb"
    print(length_of_longest_substring(string, 1))
    
    
if __name__ == "__main__":
    main()