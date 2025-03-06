from collections import defaultdict
from typing import List


# O(n * m *log(m)) time | O(n) space
def groupAnagrams_bf(strs: List[str]) -> List[List[str]]:
    groups = {}
    for word in strs:
        key = str(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())

# O(n * m) time | O(n) space
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    #groups = defaultdict(list)
    groups = {} 
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        #groups[tuple(count)].append(word)
        groups.setdefault(tuple(count), []).append(word)
    return list(groups.values())


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
    
    
if __name__ == "__main__":
    main()
