def main():
    array = [1, 1, 6, 1]
    sequence = [1, 1, 1, 6]    
    print(isValidSubsequence(array, sequence))
    

# O(n) time | O(1) space    
def isValidSubsequence(array, sequence):
    arrIdx, seqIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return  seqIdx == len(sequence)
            
    



    
    
if __name__ == "__main__":
    main()