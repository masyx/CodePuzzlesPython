# Given a string, find the length of the longest substring 
# without repeating characters.
def main():
    print(longestSubstring('pwwkew'))
    print(longestSubstring('abrkaabcjjxxx'))
    
# "abrkaabcdefghijjxxx"
# "abrkaabcjjxxx"


def longestSubstring(s: str):
    length = 0
    start = 0
    chars = [0] * 128
    for right in range(len(s)):
        chars[ord(s[right])] += 1
        
        while chars[ord(s[right])] > 1:
            chars[ord(s[start])] -= 1
            start += 1
        length = max(length, right - start + 1)
    return length           
 # abcafb


if __name__ == "__main__":
    main()   