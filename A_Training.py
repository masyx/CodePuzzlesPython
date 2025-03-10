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

def valid_sudoku(sudoku: List[List[int]]) -> bool:
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

def main():
    # s[0][1] != s[1][1]
    sudoku = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]
    print(f"Is sudoku valid? - {'Yes' if valid_sudoku(sudoku) else 'No'}")
    
if __name__ == "__main__":
    main()