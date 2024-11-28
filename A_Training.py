from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    l = 0
    r = rows * cols - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // cols
        col = mid % cols
        if matrix[row][col] == target:
            return True
        elif target > matrix[row][col]:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target))
