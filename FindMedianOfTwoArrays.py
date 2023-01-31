from typing import List

# O(n) time | O(n + m) space
def findMedianOfTwoArrays(num1: List[str], num2: List[int]) -> List[int]:
    resultList = [0] * (len(num1) + len(num2))
    i, j, k = 0, 0, 0
    while i != len(num1) or j != len(num2):
        if j == len(num2) or (i < len(num1) and num1[i] < num2[j]):
            resultList[k] = num1[i]
            i += 1
        else:
            resultList[k] = num2[j]
            j += 1
        k += 1

    median_idx = (len(resultList) - 1) // 2
    if len(resultList) & 1 == 1:
        return  resultList[median_idx]
    else:
        return (resultList[median_idx] + resultList[median_idx + 1]) / 2.0


def main():
    l1 = [1, 3, 4]
    l2 = [2, 5]
    print(findMedianOfTwoArrays(l1, l2))
    
    
if __name__ == "__main__":
    main()