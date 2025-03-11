from collections import defaultdict
from typing import List

#   j   0   1   2   3   4   5   6   7   8 
#   i
#[  0 ["5","3",".",".","7",".",".",".","."],
#   1 ["6",".",".","1","9","5",".",".","."],
#   2 [".","9","8",".",".",".",".","6","."],
#   3 ["8",".",".",".","6",".",".",".","3"],
#   4 ["4",".",".","8",".","3",".",".","1"],
#   5 ["7",".",".",".","2",".",".",".","6"],
#   6 [".","6",".",".",".",".","2","8","."],
#   7 [".",".",".","4","1","9",".",".","5"],
#   8 [".",".",".",".","8",".",".","7","9"]]
# i = 0, j = 0, box = 0, curr_val = 0

def valid_sudokuSergey(sudoku: List[List[int]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    box = defaultdict(set)
    
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            curr_val = sudoku[i][j]
            if curr_val == ".":
                continue
            
            box_number = (i // 3) * 3 + j // 3
            
            if (curr_val in rows[i] or 
                curr_val in columns[j] or 
                curr_val in box[box_number]):
                return False
            
            rows[i].add(curr_val)
            columns[j].add(curr_val)
            box[box_number].add(curr_val)
    return True

def valid_sudoku(board: List[List[str]]) -> bool:
    rows = defaultdict(set)
    columns = defaultdict(set)
    boxes = defaultdict(set)

    for row in range(len(board)):
        for column in range(len(board[row])):
            curr_val = board[row][column]
            
            if curr_val == ".":
                continue
            box = (row // 3, column // 3)
            
            if (curr_val in rows[row] or
                curr_val in columns[column] or
                curr_val in boxes[box]):
                return False
            
            rows[row].add(curr_val)
            columns[column].add(curr_val)
            boxes[box].add(curr_val)
    return True

def main():
    # invalid box(1,2), number 1 at row 1 and column 9
    sudoku = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".","1",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    
    print(f"Is sudoku valid? - {'Yes' if valid_sudoku(sudoku) else 'No'}")
    
if __name__ == "__main__":
    main()