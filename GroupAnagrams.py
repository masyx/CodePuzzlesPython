from collections import defaultdict
from typing import List

'''
49. Group Anagrams
Medium
Given an array of strings strs, group the anagrams together. You can return the 
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''


# O(n * m log m) where n in number of strings and m is the length of the string
# O(n * m) space
def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

# O(n * m log m) where n in number of strings and m is the length of the string
# O(n * m) space
def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for string in strs:
        sorted_str = sorted(string)
        res[tuple(sorted_str)].append(string)
    return res.values()
        
# O(n * m) where n in number of strings and m is the length of the string
# O(n * m) space
def groupAnagrams3(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for string in strs:
        chars = [0] * 26
        for char in string:
            chars[ord(char) - ord('a')] += 1
        res[tuple(chars)].append(string)
    return res.values()
    
def main():
    # ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    words = ["eat","tea","tan", "ant", "apa", "paa"]
    print(groupAnagrams3(words))
    
    
if __name__ == "__main__":
    main()