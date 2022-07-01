def isPalindromeString(str):
    reversedStr = str[::-1]
    if reversedStr == str:
        return True
    return False


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




def main():
    myString = "ABC"
    print(isPalindromeStringJoin(myString))
    
if __name__ == "__main__":
    main()