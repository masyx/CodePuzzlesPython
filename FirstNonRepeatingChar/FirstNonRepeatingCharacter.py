# O(n) time | O(n) space
def firstNonRepeatingCharacter(string):
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


def main():
    string = "abcdcaf"
    print(firstNonRepeatingCharacter(string))
    
    
if __name__ == "__main__":
    main()