from collections import defaultdict
#
# abcbwa


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeHelper(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        if not s or len(s) <= 2:
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return validPalindromeHelper(s , l + 1, r) or validPalindromeHelper(s, l, r - 1)
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s="abaasba"
    palindromeChecker = Solution()
    print(palindromeChecker.validPalindrome(s))