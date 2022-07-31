# O(n) time | O(n) space, where n is the total number of elements in the array 
def spiralTraverse(array):
    topRow = 0 
    bottomRow = len(array) - 1 # 3
    leftColumn = 0 
    rightColumn = len(array[0]) - 1 # 3
    
    result = []
    
    while topRow <= bottomRow and leftColumn <= rightColumn:
        for i in range(leftColumn, rightColumn + 1):
            result.append(array[topRow][i])
        
        for i in range(topRow + 1, bottomRow + 1):
            result.append(array[i][rightColumn])
            
        for i in range(rightColumn - 1, leftColumn, -1):
            if topRow == bottomRow:
                break
            result.append(array[bottomRow][i])
            
        for i in range(bottomRow, topRow, -1):
            if leftColumn == rightColumn:
                break
            result.append(array[i][leftColumn])
        
        topRow += 1
        bottomRow -= 1    
        leftColumn += 1
        rightColumn -= 1
                
    return result


def main():
    
    nums = [
    [1, 2, 3],
    [12, 13, 4],
    [11, 14, 5],
    [10, 15, 6],
    [9, 8, 7]
  ]
    print(spiralTraverse(nums))
    
    
if __name__ == '__main__':
    main()