def generateDocument(characters, document):
    resultTableCharacters = {}
    for Idx, char in enumerate(characters):
        count = 1
        if char not in resultTableCharacters:
            for i in range(Idx + 1, len(characters)):
                if char == characters[i]:
                    count += 1
            resultTableCharacters[char] = count
            
    resultTableDocument = {}
    for Idx, char in enumerate(document):
        count = 1
        if char not in resultTableDocument:
            for i in range(Idx + 1, len(document)):
                if char == document[i]:
                    count += 1
            resultTableDocument[char] = count
            
    for key in resultTableDocument:
        if key not in resultTableCharacters:
            return False
        elif resultTableCharacters[key] < resultTableDocument[key]:
            return False
    return True


def generateDocument2(characters, document):
    charactersTable = {}
    for Idx, char in enumerate(characters):
        count = 1
        if char not in charactersTable:
            for i in range(Idx + 1, len(characters)):
                if char == characters[i]:
                    count += 1
            charactersTable[char] = count
            
    for char in document:
        if char in charactersTable and charactersTable[char] > 0:
            charactersTable[char] -= 1
        else:
            return False
    
    return True


def generateDocument3(characters, document):
    charactersTable = {}
    for i in range(len(characters)):
        count = 1
        if characters[i] not in charactersTable:
            for j in range(i + 1, len(characters)):
                if characters[i] == characters[j]:
                    count += 1
            charactersTable[characters[i]] = count
            
    for char in document:
        if char in charactersTable and charactersTable[char] > 0:
            charactersTable[char] -= 1
        else:
            return False
    
    return True      

def generateDocumentOptimalReadable(characters, document):
    charactersCount = {}
    for character in characters:
        if character not in charactersCount:
            charactersCount[character] = 0
        charactersCount[character] += 1
        
    for character in document:
        if character not in charactersCount or charactersCount[character] == 0:
            return False
        charactersCount[character] -= 1
        
    return True 
    
    
    
    
    
def main():
    characters2 = "helloworldO "
    document2 = "hello wOrld"
    characters = "abcabc"
    document = "aabbccc"
    generateDocument3(characters, document)
   
if __name__ == "__main__":
    main() 