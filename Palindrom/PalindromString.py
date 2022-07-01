# O(n) time | O(n) space
def isPalindromeString(str):
    reversedStr = str[::-1]
    if reversedStr == str:
        return True
    return False

# O(n^2) time | O(n) space
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


# O(n^2) time | O(n) space
def isPalindromeIterationReverse(string):
    reversedStr = ""
    for i in range(1, len(string) + 1):
        reversedStr += string[-i]
    if reversedStr == string:
        return True
    return False    


# O(n) time | O(n^2) space
def isPalindromeRecursionMy(string):
    if string == "":
        return True
    return string[0] == string[-1] and isPalindromeRecursionMy(string[1 : len(string) - 1])


# O(n) time|O(n) space
def isPalindromeRecursionMyBest(string, start = 0, end = -1):
    while start < len(string) // 2 :
        return string[start] == string[end] and isPalindromeRecursionMyBest(string, start + 1, end - 1)
    return True

def main():
    myString = "abcfcba"
    print(isPalindromeRecursionMyBest(myString))
    
if __name__ == "__main__":
    main()