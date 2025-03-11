'''
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Example 3:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

     j      0       1       2
    i   +-------+-------+-------+
        | 1 2 . | . 3 . | . . . |
    0   | 4 . . | 5 . . | . . . |  
        | . 9 8 | . . . | . . 3 |
        +-------+-------+-------+
        | 5 . . | . 6 . | . . 4 |
    1   | . . . | 8 . 3 | . . 5 |
        | 7 . . | . 2 . | . . 6 |
        +-------+-------+-------+
        | . . . | . . . | 2 . . |
    2   | . . . | 4 1 9 | . . 8 |
        | . . . | . 8 . | . 7 9 |
        +-------+-------+-------+

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
'''

from collections import defaultdict
from typing import List


# O(n^2) time O(n^2) space
def isValidSudoku(board: List[List[str]]) -> bool:
    row = defaultdict(set)
    column = defaultdict(set)
    box = defaultdict(set)
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            num = board[r][c]
            if num == ".":
                continue
            
            box_index = (r // 3) * 3 + c // 3
            
            if (num in row[r] or
                num in column[c] or
                num in box[box_index]):
                return False
            
            row[r].add(num)
            column[c].add(num)
            box[box_index].add(num)
    return True

def valid_sudoku_more_intuitive(board: List[List[str]]) -> bool:
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

if __name__ == "__main__":
    board = [["1","2",".",".","3",".",".",".","."],
             ["4",".",".","5",".",".",".",".","."],
             [".","9","8",".",".",".",".",".","3"],
             ["5",".",".",".","6",".",".",".","4"],
             [".",".",".","8",".","3",".",".","5"],
             ["7",".",".",".","2",".",".",".","6"],
             [".",".",".",".",".",".","2",".","."],
             [".",".",".","4","1","9",".",".","8"],
             [".",".",".",".","8",".",".","7","9"]]

    print(f"Is sudoku valid? -  {'Yes' if valid_sudoku_more_intuitive(board) else 'No'}")