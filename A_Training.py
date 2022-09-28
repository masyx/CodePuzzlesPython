def runLengthEncoding_my(string):
    result = []
    counter = 0
    for i in range(len(string)):
        counter += 1
        if i == len(string) - 1:
            result.append(f"{counter}{string[i]}")
        elif counter == 9:
            result.append(f"{counter}{string[i]}")
            counter = 0
        elif string[i] == string[i + 1]:
            continue
        else:
            result.append(f"{counter}{string[i]}")
            counter = 0
    return "".join(result)



            
    chars.append(f"{count}{string[- 1]}")
    return "".join(chars)


def runLengthEncoding(string):
    encrypted_string = []
    counter = 1
    
    for i in range(1, len(string)):
        current_char = string[i]
        previous_char = string[i - 1]
        
        if current_char != previous_char or counter == 9:
            encrypted_string.append(f"{counter}{previous_char}")
            counter = 0
        
        counter += 1
    encrypted_string.append(f"{counter}{string[len(string) - 1]}")
    
    return "".join(encrypted_string)
    
    
def main():
    print(runLengthEncoding("AAAAAAAAAAAAABBCCCCED"))

if __name__ == '__main__':
    main()