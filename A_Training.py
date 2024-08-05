def valid_anagram_array(s, t):
    if len(s) != len(t):
        return
    
    seen = [0] * 128
    for i in range(len(s)):
        seen[ord(s[i])] += 1
        seen[ord(t[i])] -= 1
    
    for char in s:
        if seen[ord(char)] != 0:
            return False
    return True

if __name__ == "__main__":
    s = "abb"
    t = "baa"
    print(f"Is '{t}' an anagram of '{s}': "
          f"{'Yes' if valid_anagram_array(s, t) else 'No'}")