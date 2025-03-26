from collections import defaultdict

class Solution:
    #   r
    #  l
    #i 0123456
    # "AABCBBA" k=2
    # w = 
    def character_replacement(self, s: str, k: int) -> int:
        l = 0
        counts = defaultdict(int)
        max_freq = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_freq = max(max_freq, counts[s[r]])
            
            if (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
            
        #       r
    #   l
    #  0123456
    # "AAABABB"
    # A = 3, B = 2
    # max_freq = 4
    # res = 5
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counts = [0] * 26
        l = 0
        max_freq = 0
        for r, char in enumerate(s):
            counts[ord(char) - ord('A')] += 1
            max_freq = max(max_freq, counts[ord(char) - ord('A')])
            if (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
    
def main():
    s = "AAABABBBB"
    sol = Solution()
    print(sol.character_replacement(s, 1))
    print(sol.characterReplacement(s, 1))

    
     
if __name__ == "__main__":
    main()