# Given a string, find the length of the longest substring 
# without repeating characters.
def main():
    print(longestSubstring2('abcabcbb'))

# abcafb
# 'pwwkew'   
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
 
 
def longestSubstring2(s: str):
    length = 0
    l = 0
    used = set()
    for r in range(len(s)):
        while s[r] in used:
            used.remove(s[l])
            l += 1
        used.add(s[r])
        length = max(length, r - l + 1)
    return length           


if __name__ == "__main__":
    main()   