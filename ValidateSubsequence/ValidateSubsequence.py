def main():
    array = [1, 1, 6, 1]
    sequence = [1, 1, 1, 6]    
    print(isValidSubsequence2(array, sequence))
    

# O(n) time | O(1) space    
def isValidSubsequence1(array, sequence):
    arrIdx, seqIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return  seqIdx == len(sequence)

def isValidSubsequence2(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx < len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
    
            
    



    
    
if __name__ == "__main__":
    main()