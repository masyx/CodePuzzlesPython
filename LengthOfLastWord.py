class Solution:
    def lengthOfLastWord_simple(self, s: str) -> int:
        list_of_strings = s.split()
        return len(list_of_strings[-1])
    
    def lengthOfLastWord(self, s: str) -> int:
        # trimming the trailing spaces
        idx = len(s) - 1
        while idx >= 0 and s[idx] == ' ':
            idx -= 1
            
        # compute the length of last word
        length = 0
        while idx >= 0 and s[idx] != ' ':
            length += 1
            idx -= 1
        return length


def main():
    string1 = "Hello World"
    string2 = "   fly me   to   the moon  "
    stringSpecial = "l  "
    solution = Solution()
    print(solution.lengthOfLastWord(string1))
    print(solution.lengthOfLastWord(string2))
    print(solution.lengthOfLastWord(stringSpecial))

if __name__ == "__main__":
    main()
