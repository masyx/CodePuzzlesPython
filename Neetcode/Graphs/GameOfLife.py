""" 289. Game of Life
https://leetcode.com/problems/game-of-life/description/
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial 
state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its 
eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to 
every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.
Note that you do not need to return anything.

 
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
 
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: 
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches upon the border 
of the array (i.e., live cells reach the border). How would you address these problems?
"""

from typing import List


class Solution:
    # board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    def gameOfLife_extra_space(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        directions = [[-1,-1], [-1, 0], [-1, 1],
                      [0, -1],          [ 0, 1],
                      [1, -1], [ 1, 0], [ 1, 1]]

        next_board = []
        for row in range(rows):
            next_board.append([0] * cols)

        def apply_rules(current_state, live_neighbors):
            is_live = current_state == 1
            
            if is_live and 2 <= live_neighbors <= 3:
                return 1
            elif not is_live:
                if live_neighbors == 3:
                    return 1
            return 0

        # iterate through all cells and calculate the number of live neighbors
        for row in range(rows):
            for col in range(cols):
                current_cell = board[row][col]
                live_neighbors_count = 0
                for delta_row, delta_col in directions:
                    neighbor_row = row + delta_row
                    neighbor_col = col + delta_col
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        live_neighbors_count += board[neighbor_row][neighbor_col]
                
                next_board[row][col] = apply_rules(current_cell, live_neighbors_count)

        board[:] = next_board


    ''' Explanation:
        I cannot overwrite cells directly because later neighbor counts need the original board.
        So I encode transitions:
        2 means originally live but now dead.
        3 means originally dead but now live.
        When counting neighbors, I count only values that were originally live: 1 and 2.
        Then I do a cleanup pass.
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        #    was     now
        # 0: dead -> dead
        # 1: live -> live
        # 2: live -> dead
        # 3: dead -> live

        rows = len(board)
        cols = len(board[0])
        
        dirs = [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1,-1), (0,-1)]

        def get_next_state(row, col):
            curr_cell = board[row][col]

            live_cells = 0
            for dir_r, dir_c in dirs:
                new_r = row + dir_r
                new_c = col + dir_c
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if board[new_r][new_c] in (1, 2):
                        live_cells += 1

            # apply rules
            is_cell_live = curr_cell == 1
            if is_cell_live:
                if live_cells == 2 or live_cells == 3:
                    return 1
                else:
                    return 2
            else:
                if live_cells == 3:
                    return 3
                else:
                    return 0

        for r in range(rows):
            for c in range(cols):
                board[r][c] = get_next_state(r, c)

        for r in range(rows):
            for c in range(cols):
                state = board[r][c]
                if state == 2:
                    board[r][c] = 0
                elif state == 3:
                    board[r][c] = 1

def main():
    board = [[0,1,0],
             [0,0,1],
             [1,1,1],
             [0,0,0]]
    print(board)
    sol = Solution()
    sol.gameOfLife(board)
    print()
    print(board)
    
if __name__ == "__main__":
    main()