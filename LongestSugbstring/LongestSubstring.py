# Given a string, find the length of the longest substring 
# without repeating characters.
def main():
    print(longestSubstringCopilot('abrkaabcdefghijjxxx'))
    
# "abrkaabcdefghijjxxx"
def longestSubstring(string):
    used = {}
    counter = 0
    longest = 0
    for char in string:
        if char in used:
            counter = 0
            used.clear()
        
        used[char] = True
        counter += 1
        if counter > longest:
            longest = counter
            
    return longest


def longestSubstringCopilot(string):
    longest = 0
    current = 0
    used = {}
    for i in range(len(string)):
        if string[i] in used:
            current = max(current, used[string[i]])
        used[string[i]] = i
        longest = max(longest, i - current)
    return longest           
             
    


if __name__ == "__main__":
    main()   