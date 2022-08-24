#O(n) time | O(n) space
import string


def reverseWordsInString(string):
    result = []
    curr_start = 0
    for i in range(len(string)):
        if string[i] == " ":
            result.append(string[curr_start:i])
            curr_start = i + 1
    result.append(string[curr_start:])
    return " ".join(reverse_list(result))


def reverse_list(list):
    start, end = 0, len(list) - 1
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1
    return list


def main():
    string = 'AlgoExpert is the best!'
    print(reverseWordsInString(string))
    
    
if __name__ == "__main__":
    main()