class Solution:
    # O(n + m) time | O(1) space
    def merge_strings_alt(self, word1, word2):
        shortest = len(word1) if len(word1) < len(word2) else len(word2)
        result = []
        for i in range(shortest):
            result.extend([word1[i], word2[i]])

        result += word1[shortest:] if shortest < len(word1) \
            else word2[shortest:]
        return "".join(result)
    
def main():
    word1 = "abc"
    word2 = "pppppppppppppp"
    solution = Solution()
    print(solution.merge_strings_alt(word1, word2))
    
    
if __name__ == "__main__":
    main()