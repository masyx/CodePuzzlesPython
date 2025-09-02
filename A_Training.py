from typing import List, Optional
from collections import defaultdict

class Solution:
    def groupAnagrams_sort_1(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            res[sorted_s].append(s)
        
        return list(res.values())
    
    # O(n * m log m) time | O(n) space
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s not in res:
                res[sorted_s] = []
            res[sorted_s].append(s)
                
        
        return list(res.values())
    
    # O(n * m) time | O(n * m) space
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                # ord('a') is 97, it's its ascii value
                count[ord(char) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())
    
    
    
    
    
def main():
  strs = ["eat","tea","tan","ate","nat","bat"]
  
  sol = Solution()
  print(sol.groupAnagrams(strs))
  
  
if __name__ == "__main__":
    main()