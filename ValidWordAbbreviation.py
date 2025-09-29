"""408. Valid Word Abbreviation
Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.

"""

class Solution:
    # 0123
    # 11n

    # 0123456789 10 11
    # substituti  o  n
    # w_p = 12
    # a_p = 1
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_p = 0 # 12
        abbr_p = 0 # 3
        while word_p < len(word)  and abbr_p < len(abbr):
            if abbr[abbr_p].isdigit():
                if abbr[abbr_p] == "0":
                    return False
                    
                abbr_p_start = abbr_p # 0
                while abbr_p < len(abbr) and abbr[abbr_p].isdigit():
                    abbr_p += 1 # 2

                number = int(abbr[abbr_p_start: abbr_p]) # 11
                word_p += number
            else:
                if word[word_p] != abbr[abbr_p]:
                    return False
                word_p += 1
                abbr_p += 1
        
        return word_p == len(word) and abbr_p == len(abbr)
              
    
def main():
    
    word = "hi"
    abbr = "1"
    sol = Solution()
    print(sol.validWordAbbreviation(word, abbr))
  
  
if __name__ == "__main__":
    main()