def caesarCipherEncryptor(string, key):
    result_chars = []
    key = key % 26
    for char in string:
        new_letter_code = ord(char) + key 
        if new_letter_code > 122:
            new_letter_code = 96 + new_letter_code % 122
        result_chars.append(chr(new_letter_code))
    return "".join(result_chars)

def main():
    print(caesarCipherEncryptor("abc", 52))

if __name__ == '__main__':
    main()