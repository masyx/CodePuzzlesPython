# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    newWord = []
    for char in string:
        newChar = ord(char) + key
        if newChar > 122:
            newChar = 96 + (newChar - 122) % 26
        newWord.append(chr(newChar))
        
    return "".join(newWord)


def caesarCipherEncryptor(string, key):
    newWord = []
    newKey = key % 26
    for char in string:
        newLetterCode = ord(char) + newKey
        if newLetterCode > 122:
            newLetterCode = 96 + newLetterCode % 122
        newWord.append(chr(newLetterCode))
        
    return "".join(newWord)


def main():
    print(caesarCipherEncryptor('xyz', 10000000)) 
    
    
if __name__ == "__main__":
    main()