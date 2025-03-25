from typing import List


class Solution:
    """
               r
            l  
    i:    01234567
    s:   "pwwkew"
    l = 3, r = 5, res = 3
    seen= {k,e}
    
    """
    # O(n) time | O(n) space
    def length_of_longest_substring(self, s: str)-> int:
        if len(s) == 0:
            return 0
        res = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
    
    
def main():
    
    #s = "abcabcbb"
    #s = "aaa"
    #s = "aaaabaaaa"
    #s = "pwwkew"
    s = " "
    sol = Solution()
    print(sol.length_of_longest_substring(s))

    
     
if __name__ == "__main__":
    main()