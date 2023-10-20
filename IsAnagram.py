class Solution:
    # O(n + m) time, word1 could be 1,000 letters a
    # and word2 could 1,000 letters b, so we have to iterate 
    # through both words
    # O(1) is space complexity, because the number of letters in
    # an alphabet is 26
    def is_anagram_2(self, word_1, word_2):
        chars = {}
        for i, char in enumerate(word_1):
            chars[char] = chars.get(char, 0) + 1
            
        for i, char in enumerate(word_2):
            chars[char] = chars.get(char, 0) - 1
        
        if any(value != 0 for value in chars.values()):
            return False
        else:
            return True
        
    def is_anagram(self, word_1, word_2):
        chars_count = {}
        for i, char in enumerate(word_1):
            chars_count[char] = chars_count.get(char, 0) + 1
        
        for i, char in enumerate(word_2):
            if char not in chars_count:
                return False
            chars_count[char] -= 1
            if chars_count[char] == 0:
                del chars_count[char]
        return len(chars_count) == 0
    
    
def main():
    word_1 = "ball"
    word_2 = "allb"
    print(Solution().is_anagram(word_1, word_2))

if __name__ == "__main__":
    main()