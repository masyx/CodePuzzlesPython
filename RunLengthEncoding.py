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
            


def main():
    string = "A" #'AAAAAAAAAAAAABBCCCCDF'
    print(runLengthEncoding(string))
    
if __name__ == "__main__":
    main()