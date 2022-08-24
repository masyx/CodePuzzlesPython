#O(n) time | O(n) space
def reverseWordsInString(string):
    result = []
    curr_start = 0
    for i in range(len(string)):
        if string[i] == " ":
            result.append(string[curr_start:i])
            curr_start = i + 1
        if i == len(string) - 1:
            result.append(string[curr_start:])
    return " ".join(reversed(result))


def main():
    string = 'AlgoExpert is the best!'
    print(reverseWordsInString(string))
    
    
if __name__ == "__main__":
    main()