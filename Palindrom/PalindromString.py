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
        
    





def main():
    myString = "ABC"
    print(isPalindromeStringIterative(myString))
    
if __name__ == "__main__":
    main()