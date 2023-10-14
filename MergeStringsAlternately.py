class Solution:
    # O(n + m) time | O(1) space
    def merge_strings_alt_my_init_solution(self, word1, word2):
        shortest = len(word1) if len(word1) < len(word2) else len(word2)
        result = []
        for i in range(shortest):
            result.extend([word1[i], word2[i]])

        result += word1[shortest:] if shortest < len(word1) \
            else word2[shortest:]
        return "".join(result)
    
    # O(n) time, where n is the length of a longest word
    # O(1) space
    def merge_alternately(self, word1, word2):
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return "".join(result)
    

def main():
    word1 = "abc"
    word2 = "pppppppppppppp"
    solution = Solution()
    print(solution.merge_alternately(word1, word2))
    
    
if __name__ == "__main__":
    main()