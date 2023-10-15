class Solution:
    # O(n) time | O(v) space, where v is the number of vowels in a word
    def reverse_vowels_brute_force(self, word):
        vowels = set("AEIOUaeiou")
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
    
    # O(n) time | O(v) space, where v is length of a word
    def reverse_vowels_2(self, word):
        vowels = set("AEIOUaeiou")
        chars = list(word)
        l, r = 0, len(word) - 1
        
        while l < r:
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            elif chars[l] not in vowels:
                l += 1
            elif chars[r] not in vowels:
                r -= 1
        return "".join(chars)
    
    def reverse_vowels(self, word):
        vowels = set("AEIOUaeiou")
        chars = list(word)
        l, r = 0, len(word) - 1
        
        while l < r:
            while l < r and chars[l] not in vowels:
                l += 1
            while l < r and chars[r] not in vowels:
                r -= 1
        
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return "".join(chars)
    
    
def main():
    word = "bobik"
    sol = Solution()
    print(sol.reverse_vowels(word))
    
if __name__ == "__main__":
    main()