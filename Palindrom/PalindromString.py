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


# O(n) time|O(n) space
def isPalindromeRecursionMyBest(string, start = 0, end = -1):
    while start < len(string) // 2 :
        return string[start] == string[end] and isPalindromeRecursionMyBest(string, start + 1, end - 1)
    return True

def isPalindromeRecursiveBEST(string, left = 0):
    right = len(string) - 1 - left
    # if left >= right:
    #     return True
    # else:
    #     return string[left] == string[right] and isPalindromeRecursiveBEST(string, left + 1) 
    return True if left >= right else string[left] == string[right] and isPalindromeRecursiveBEST(string, left + 1)
 
def isPalindromeRecursiveCLEAR(string, left = 0):
    right = len(string) - 1 - left
    if left >= right:
        return True
    elif string[left] != string[right]:
        return False    
    return isPalindromeRecursiveCLEAR(string, left + 1)   

# O(n) time | O(1) space
def isPalindromeIterativePointers(string):
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# O(n) time | O(1) space
def isPalindromeIterativePointers2(string):
    left = 0
    right = -1
    while left < len(string) // 2:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

def main():
    myString = "abcdcba"
    print(isPalindromeRecursiveCLEAR(myString))
    
if __name__ == "__main__":
    main()