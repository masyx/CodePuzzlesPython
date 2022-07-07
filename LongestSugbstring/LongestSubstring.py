# Given a string, find the length of the longest substring 
# without repeating characters.
def main():
    print(longestSubstring('abrkaabcdefghijjxxx'))
    
# "abrkaabcdefghijjxxx"
def longestSubstring(string):
    presentChars = {}
    counter = 0
    lengthOfLongestSubstring = 0
    for char in string:
        if char in presentChars:
            counter = 0
            presentChars.clear()
        
        presentChars[char] = True
        counter += 1
        if counter > lengthOfLongestSubstring:
            lengthOfLongestSubstring = counter
            
    return lengthOfLongestSubstring
             
             
    


if __name__ == "__main__":
    main()   