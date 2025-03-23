from collections import defaultdict
from typing import List


class Solution:
    
    """
    board = 
                0           1           2
     j  0   1   2   3   4   5   6   7   8
   i
   0 [["5","3",".",".","7",".",".",".","."]
0  1 ,["6",".",".","1","9","5",".",".","."]
   2 ,[".","9","8",".",".",".",".","6","."]
   3 ,["8",".",".",".","6",".",".",".","3"]
1  4 ,["4",".",".","8",".","3",".",".","1"]
   5 ,["7",".",".",".","2",".",".",".","6"]
   6 ,[".","6",".",".",".",".","2","8","."]
2  7 ,[".",".",".","4","1","9",".",".","5"]
   8 ,[".",".",".",".","8",".",".","7","9"]]
    
    """
    # O(n^2) time | O(n^2) space, but it is sudoku so time and space are both O(1)
    def valid_sudoku(self, board: List[List[int]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                curr_number = board[i][j]
                if curr_number == ".":
                    continue
                
                curr_box = (i // 3, j // 3)
                if (curr_number in rows[i] or
                    curr_number in columns[j] or
                    curr_number in boxes[curr_box]):
                    return False
                
                rows[i].add(curr_number)
                columns[j].add(curr_number)
                boxes[curr_box].add(curr_number)
        return True

        
        

def main():
    
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    print(s.valid_sudoku(board))
    
     
if __name__ == "__main__":
    main()