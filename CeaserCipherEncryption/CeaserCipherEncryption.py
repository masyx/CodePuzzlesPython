def caesarCipherEncryptor(string, key):
    newWord = []
    for char in string:
        newChar = ord(char) + key
        if newChar > 122:
            newChar = 96 + (newChar - 122) % 26
        newWord.append(chr(newChar))
        
    return "".join(newWord)


def main():
    print(caesarCipherEncryptor('xyz', 2)) 
    
    
if __name__ == "__main__":
    main()