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


class CodecClean:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}/:{s}" for s in strs)
    
    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        
        while i < len(s):
            delim = s.find('/:', i)
            length = int(s[i:delim])
            i = delim + 2
            result.append(s[i:i + length])
            i += length
        return result

class Codec_My:
    def encode(self, strs: List[str]) -> str:
        # result = ""
        # for s in strs:
        #     result += f"{len(s)}/:{s}"
        # return result
        return "".join(f"{len(s)}/:{s}" for s in strs)
    
    def decode(self, s: str):
        i = 0
        result = []
        while i < len(s):
            length_str = ""
            while s[i] != '/' and s[i + 1] != ':':
                length_str += s[i]
                i += 1
            length = int(length_str)
            result.append(s[i + 2 : i + 2 + length])
            i = i + 2 + length
        return result

class Codec_My_2:
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

class Codec_My_almost_good:
    # O(n) time, where n is the total number of characters in all strings
    # O(n) space, where n is the total number of characters in all strings
    def encode(self, strs: List[str]) -> str:
        result = [f"{self.length_as_string(s)}{s}" for s in strs ]
        return "".join(result)

    # O(n) time, where n is the total number of characters in all strings
    # O(n) space, where n is the total number of characters in all strings
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            str_length = int(s[i:i + 3])
            result.append(s[i + 3: i + 3 + str_length])
            i = i + 3 + str_length
        return result
    
    def length_as_string(self, s):
        len_str = str(len(s))
        zeros_needed = 3 - len(len_str)
        if zeros_needed > 0:
            len_str = "0" * zeros_needed + len_str
        return len_str
    
    def length_as_string(self, s):
        len_str = str(len(s))
        while len(len_str) < 3:
            len_str = "0" + len_str
        return len_str

class CodecNonAsciiDelimiter:
    def encode(self, strs: List[str]) -> str:
        return " Ж ".join(strs)
        
    def decode(self, s: str) -> List[str]:
        return s.split(" Ж ")
    
class CodecEscaping:
    def encode(self, strs):
        encoded_string = ''
        for s in strs:
            # Replace each occurrence of '/' with '//'
            # This is our way of "escaping" the slash character
            # Then add our delimiter '/:' to the end
            encoded_string += s.replace('/', '//') + '/:'

        # Return the final encoded string
        return encoded_string

    def decode(self, s):
        decoded_strings = []
        current_string = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == '/:':
                decoded_strings.append(current_string)
                current_string = ""
                i += 2
            elif s[i:i+2] == '//':
                # Add a single slash to the current_string
                current_string += '/'
                i += 2
            else:
                current_string += s[i]
                i += 1
        return decoded_strings
    
        
if __name__ == "__main__":
    strs = ["", "///://////\/\\", "W", "Hello","SuperDuper"]
    print(strs)
    codec = Codec()
    encoded = codec.encode(strs)
    print(encoded)
    decoded = codec.decode(encoded)
    print(decoded)
    
    
    # # Comprehensive testing
    # test_passed = True
    # for i in range(100000):
    #     random_strings = [''.join(random.choices(string.printable, k=random.randint(1, 20))) for _ in range(5)]
        
    #     codec = Codec()
    #     print(random_strings)
    #     decoded_string = codec.decode(codec.encode(random_strings))
    #     print(decoded_string)
        
    #     codec_failed = random_strings != decoded_string
    #     print(f"Is Codec failed: {codec_failed}")
    #     if codec_failed:
    #         print("Codec test FAILED")
    #         test_passed = False
    #         break
    # if test_passed:
    #     print("Codec test PASSED")