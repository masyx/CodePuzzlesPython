from collections import defaultdict
from typing import List


class Codec:
    # ["", "W" "Hello","SuperDuper"]
    

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        res = ""
        for word in strs:
            res += f"{len(word):03}{word}"
        return res
        
    #  012345678901234567890
    #     i
    # "000001W005Hello010SuperDuper"
    #        j
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        res = []
  
        i = 0
        while i < len(s):
            j = i + 3
            length = int(s[i:j])
            if length == 0:
                res.append("")
                i = j
            else:
                res.append(s[j:j + length])
                i = j + length 
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

def main():
    codec = Codec()
    arr = ["", "W", "Hello","SuperDuper"]
    s = codec.encode(arr)
    print(s)
    print(codec.decode(s))    
    
if __name__ == "__main__":
    main()