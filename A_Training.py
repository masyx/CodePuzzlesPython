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
            if abbr_p < len(abbr) and abbr[abbr_p].isdigit():
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
        
        return True if word_p == len(word) and abbr_p == len(abbr) else False

        


                    
    
def main():
    
    word = "hi"
    abbr = "1"
    sol = Solution()
    print(sol.validWordAbbreviation(word, abbr))
  
  
if __name__ == "__main__":
    main()