class Solution:
    def reverse_vowels(self, word):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        words_vowels = []
        for i, char in enumerate(word):
            if char in vowels:
                words_vowels.append(char)
        
        result = []
        for i, char in enumerate(word):
            if char in vowels:
                result.append(words_vowels.pop())
            else:
                result.append(char)
        
        return "".join(result) if result else None
    
def main():
    word = "aA"
    sol = Solution()
    print(sol.reverse_vowels(word))
    
if __name__ == "__main__":
    main()