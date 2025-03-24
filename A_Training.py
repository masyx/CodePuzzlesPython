from typing import List


class Solution:
    """
           r
          l  
    i:    01234567
    s:   "abcabcbb"
    l = 0, r = 1, res = 2
    seen= {a,b}
    
    """
    # O(n) time | O(n) space
    def length_of_longest_substring_my_original(self, s: str)-> int:
        if not s:
            return 0
        res = 1
        l, r = 0, 1
        seen = {s[l]}
        while r < len(s):
            curr_char = s[r]
            if curr_char not in seen:
                res = max(res, r - l + 1)
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(curr_char)
            r += 1
        return res
    
    # O(n^2) time | O(n) space
    def length_bf(self, s):
        res = 1
        for l in range(len(s) - 1):
            seen = {s[l]}
            r = l + 1
            curr_res = 1
            while r < len(s):
                if s[r] not in seen:
                    seen.add(s[r])
                    curr_res += 1
                    res = max(res, curr_res)
                    r += 1
                else:
                    break
        return res

def main():
    
    #s = "abcabcbb"
    #s = "aaa"
    #s = "aaaabaaaa"
    s = "pwwkew"
    # = ""
    sol = Solution()
    print(sol.length_of_longest_substring_my_original(s))
    print(sol.length_bf(s))
    
     
if __name__ == "__main__":
    main()