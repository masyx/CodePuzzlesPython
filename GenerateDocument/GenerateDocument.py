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
                
                
    
    
    
    
    
def main():
    characters = "helloworldO "
    document = "hello wOrld"
    generateDocument(characters, document)
   
if __name__ == "__main__":
    main() 