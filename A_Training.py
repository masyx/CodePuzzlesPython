from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        for char in s1:
            count1[ord(char) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if count1 == count2:
                return True
        return False
        
        
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbao"
    
    sol = Solution()
    print(sol.checkInclusion(s1, s2))
    
    
    
    
    
    
    
public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        // s1!
        // s2*s1!

        // hashmap[char]=x
        // iterate through s2
        // for each char check if it exists in s1
        // decrement the number of times in map
        // if it doesn't exist - then reset the map
        // return true if map is empty
        // otherwise we return false

        // O(s2)
        // O(1)

        // s1 = "adc", s2 = "dcda"
        // init=a1d1c1
        // cur=d1c1a1
        // dcda
        // l r
        // a1b1c0d1
        // letter-'a'
        // abcde
        // 00000000000000000000000000

        var s1Map = s1.GroupBy(c=>c).ToDictionary(g=>g.Key, g=>g.Count());//s1

        var windowMap = s2.Take(s1.Length).GroupBy(c=>c).ToDictionary(g=>g.Key, g=>g.Count());//s1

        for (var i = 0; i < s2.Length-s1.Length+1; i++){//s2-s1
            if (CompareMaps(s1Map, windowMap)){//26
                return true;
            }
            if (i+s1.Length < s2.Length){
                RemoveElementFromWindow(windowMap, s2[i]);
                AddElementToWindow(windowMap, s2[i+s1.Length]);
            }
        }

        return false;
    }

    public bool CompareMaps(Dictionary<char, int> s1Map, Dictionary<char, int> windowMap){
        foreach(var pair in s1Map){
            if (windowMap.ContainsKey(pair.Key) && windowMap[pair.Key] == pair.Value){
                continue;
            }
            return false;
        }

        return true;
    }

    public void RemoveElementFromWindow(Dictionary<char, int> windowMap, char letter){
        windowMap[letter]--;
        if (windowMap[letter] == 0){
            windowMap.Remove(letter);
        }
    }

    public void AddElementToWindow(Dictionary<char, int> windowMap, char letter){
        if (!windowMap.ContainsKey(letter)){
            windowMap[letter] = 0;
        }
        windowMap[letter]++;
    }
}