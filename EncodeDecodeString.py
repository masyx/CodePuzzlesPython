'''
271. Encode and Decode Strings
Medium
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded 
back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

 

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
'''
import random
import string
from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        result = [f"{self.format_string(s)}{s}" for s in strs ]
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            str_length = int(s[i:i + 3])
            result.append(s[i + 3: i + 3 + str_length])
            i = i + 3 + str_length
        return result
    
    def format_string(self, s):
        len_str = str(len(s))
        zeros_needed = 3 - len(len_str)
        if zeros_needed > 0:
            len_str = "0" * zeros_needed + len_str
        return len_str
    
    def format_string_2(self, s):
        len_str = str(len(s))
        while len(len_str) < 3:
            len_str = "0" + len_str
        return len_str
    
if __name__ == "__main__":
    random_strings = [''.join(random.choices(string.ascii_letters + string.digits, 
                                             k=random.randint(1, 10))) for _ in range(5)]
    
    codec = Codec()
    print(random_strings)
    print(codec.decode(codec.encode(random_strings)))