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

# O(k^2) time where k is number of elements in hash table | O(n) space
def firstNonRepeatingCharacter1(string):
    used = {}
    for char in string:
        if char not in used:
            used[char] =  1
            continue
        used[char] = used[char] + 1
    
    for element in used:
        if used[element] == 1:
            for i in range(len(string)):
                if string[i] == element:
                    return i
    
    return -1

def firstNonRepeatingCharacter2(string):
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