def isPalindromeString(str):
    reversedStr = str[::-1]
    if reversedStr == str:
        return True
    return False






def main():
    myString = "BOB"
    print(isPalindromeString(myString))
    
if __name__ == "__main__":
    main()