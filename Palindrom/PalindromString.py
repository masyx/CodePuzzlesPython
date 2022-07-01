# O(n) time | O(n) space
def isPalindromeString(str):
    reversedStr = str[::-1]
    if reversedStr == str:
        return True
    return False

# O(n) time | O(n) space
def isPalindromeStringIterative(str):
    reversedStr = ""
    for char in str:
        reversedStr = char + reversedStr
    if reversedStr == str:
        return True
    return False
        
    
def isPalindromeStringJoin(string):
    reversedStr = "".join(reversed(string))
    if reversedStr == string:
        return True
    return False


# O(n) time | O(n) space
def isPalindromeIterationReverse(string):
    reversedStr = ""
    for i in range(1, len(string) + 1):
        reversedStr += string[-i]
    if reversedStr == string:
        return True
    return False    




def main():
    myString = "BOB"
    print(isPalindromeIterationReverse(myString))
    
if __name__ == "__main__":
    main()