
def isValidSubsequence(array, sequence):
    seq_idx = 0
    for num in array:
        if seq_idx < len(sequence) and num == sequence[seq_idx]:
            seq_idx += 1
    is_valid = len(sequence) == seq_idx
    return is_valid
                
        


def main():
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
    
    
if __name__ == "__main__":
    main()