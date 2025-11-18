class Solution:
    # word1 = "abc", word2 = "xyz"
    # smallest = 3
    # res = [axbycz]
    # i =
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        smallest = min(n, m)

        res = []
        for i in range(smallest):
            res.extend([word1[i], word2[i]])
        
        if n < m:
            res.extend(word2[smallest:])
        else:
            res.extend(word1[smallest:])


        return "".join(res)

        
if __name__ == "__main__":
    word1 = "abc"
    word2 = "xyz"
    
    sol = Solution()
    print(sol.mergeAlternately(word1, word2))