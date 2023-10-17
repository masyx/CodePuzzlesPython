class Solution:
    # O(n + m) time | O(n + m) space, this is because in a worst case
    # scenario both words have distinct chars, the size of the dictionary
    # is n + m
    def is_anagram(self, word_1, word_2):
        chars = {}
        for i, char in enumerate(word_1):
            chars[char] = chars.get(char, 0) + 1
            
        for i, char in enumerate(word_2):
            chars[char] = chars.get(char, 0) - 1
            
        return False if any(value != 0 for value in chars.values()) \
            else True
        
    
    
def main():
    word_1 = "lall"
    word_2 = "lball"
    print(Solution().is_anagram(word_1, word_2))

if __name__ == "__main__":
    main()