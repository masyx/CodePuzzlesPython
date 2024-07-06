# O(n + m) time | O(1) space complexity because number of letters in alphabet is 26
def isAnagram(s: str, t: str) -> bool:
    chars = {}
    for char in s:
        chars[char] = chars.get(char, 0) + 1
    
    for char in t:
        if char not in chars:
            return False
        chars[char] -= 1
        if chars[char] == 0:
            chars.pop(char)
    return not chars

def is_anagram_sort(s, t):
    s_arr = sorted([char for char in s])
    t_arr = sorted([char for char in t])
    if len(s_arr) != len(t_arr):
        return False
    for i in range(len(s_arr)):
        if s_arr[i] != t_arr[i]:
            return False
    return True

def is_anagram_sort_2(s, t):
    s_arr = sorted(s)
    t_arr = sorted(t)
    if len(s_arr) != len(t_arr):
        return False
    for i in range(len(s_arr)):
        if s_arr[i] != t_arr[i]:
            return False
    return True

def is_anagram_sort_3(s, t):
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    
    print(f"Is '{t}' an anagram of '{s}': {'Yes' if isAnagram(s, t) else 'No'}")
    print(f"Is '{t}' an anagram of '{s}': {'Yes' if is_anagram_sort(s, t) else 'No'}")
    print(f"Is '{t}' an anagram of '{s}': {'Yes' if is_anagram_sort_2(s, t) else 'No'}")
    print(f"Is '{t}' an anagram of '{s}': {'Yes' if is_anagram_sort_3(s, t) else 'No'}")