def runLengthEncoding(string):
    resultArray = []
    count = 0
    if len(string) == 1:
        resultArray.append(f"1{string[0]}")
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
            if count == 9:
                resultArray.append(f"{count}{string[i]}")
                count = 0
            if i == len(string) - 2:
                count += 1
                resultArray.append(f"{count}{string[i]}")
                count = 0
            
        else:
            count += 1
            resultArray.append(f"{count}{string[i]}")
            count = 0
            if i == len(string) - 2:
                count += 1
                resultArray.append(f"{count}{string[i + 1]}") 
        
    return "".join(resultArray)

def runLengthEncoding2(string):
    chars = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
            if count == 9:
                chars.append(f"{count}{string[i - 1]}")
                count = 0
        else:
            if count != 0:    
                chars.append(f"{count}{string[i - 1]}")
            count = 1
            
    chars.append(f"{count}{string[- 1]}")
    return "".join(chars)

# O(n) time | O(n) space
def runLengthEncoding3(string):
    chars = []
    count = 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1] or count == 9:
            chars.append(f"{count}{string[i - 1]}")
            count = 0
        count += 1
            
    chars.append(f"{count}{string[- 1]}")
    return "".join(chars)


def main():
    string = '.............______=========AAAA   AAABBBB   BBB'
    print(runLengthEncoding3(string))
    
if __name__ == "__main__":
    main()