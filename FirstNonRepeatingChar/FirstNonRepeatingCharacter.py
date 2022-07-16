# O(n) time | O(n) space
def firstNonRepeatingCharacter(string):
    used = {}
    for char in string:
        if char not in used:
            used[char] =  1
            continue
        used[char] = used[char] + 1
    
    for i in range(len(string)):
        if used[string[i]] == 1:
            return i
    
    return -1

#O(n) time | O(1) space
#The problem's prompt specifies that the input string only contains lowercase 
# English-alphabet letters. Since there are only 26 lowercase English-alphabet letters,
# our hash table will never store more than 26 character frequencies; 
# thus, the optimal solution's space complexity is O(1). 
# If the input string could contain any character, then the space complexity would be O(n).
def firstNonRepeatingCharacter(string):
    used = {}
    for char in string:
        used[char] = used.get(char, 0) + 1
        
    for i in range(len(string)):
        if used[string[i]] == 1:
            return i
    return - 1
        

def firstNonRepeatingCharacterBruteForce(string):
    for i in range(len(string)):
        foundDuplicate = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                foundDuplicate = True 
        if not foundDuplicate:
            return i
    return -1


def main():
    string = "aabcdcf"
    print(firstNonRepeatingCharacter2(string))
    
    
if __name__ == "__main__":
    main()