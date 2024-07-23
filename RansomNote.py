'''
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

import collections
def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    available_chars = {}
    for char in magazine:
        available_chars[char] = available_chars.get(char, 0) + 1

    for char in ransomNote:
        if char not in available_chars or available_chars[char] <= 0:
            return False
        available_chars[char] -= 1
    return True

def canConstruct_2(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    available_chars = collections.Counter(magazine)
    
    for char in ransomNote:
        if available_chars[char] <= 0:
            return False
        available_chars[char] -= 1
    return True

if __name__ == "__main__":
    print(canConstruct("ab", "bb"))