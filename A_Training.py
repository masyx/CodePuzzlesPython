from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs_hard_to_remember = "".join(str(len(s)).zfill(3) + s for s in strs)
        encoded_strs = ""
        for s in strs:
            encoded_strs += str(len(s)).zfill(3) + s
        return encoded_strs
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        res = []
        pointer = 0
        while pointer <= len(s) - 1:
            word_length = int(s[pointer:pointer + 3])
            word_end_index = pointer + 3 + word_length
            res.append(s[pointer + 3: word_end_index])
            pointer = word_end_index
        return res

        
        

def main():
    
    strs = ["we","say",":","yes"]

    s = Solution()
    print(s.encode(strs))
    print(s.decode(s.encode(strs)))
    
     
if __name__ == "__main__":
    main()