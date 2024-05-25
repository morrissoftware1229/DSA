'''
Problem 36 on Leetcode
Rating: Medium

The prompt:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Expected output: true
'''

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I could manually check the row, then column, then the board, but let's find something better
        # I wonder if there is a mathematical relationship between the values to be checked. I will
        #   make some notes to see what the relationship would be on a 2x2 sudoku that uses 1 through
        #   4 instead.
        # If we arrange them in a dictionary one block at a time, row by row, before moving right
        # to the next block, we can check each block by using values of n through n + 8. We can check
        # the same row by checking n through n + 2 and skipping 6 before checking n through n + 2 again.
        # We can check the column by checking n + (n + 9) + (n + 18) + ...
        defaultDictOfBoardValues = {}
        for arr in range(0, len(board)):
            for n in range(0, len(arr)):
                # Loading values into defaultDict with keys of 1, 2, etc., O(n) where n is squares on
                #   board.
                if(board[arr][n] != "."):
                    defaultDictOfBoardValues[arr * len(board) + (n + 1)] = board[arr][n]
        # Checking one block at a time
        for n in range(1, len(board) * len(arr) + 1):
            if((n - 1) % 9 == 0):
                # Initially, I would want to check the list against the set, but 0 prevents that
                # I can revise my earlier code to preclude those.
                # Also, it's now occurring to me that I could have used Counter three ways faster
                #  in Python3.
                continue
        # It has been roughly an hour, so I'm hanging it up and checking the answers

'''
What I've Learned:
1. The editorial solution worked by breaking the issue into smaller pieces and allowing more leeway than I did. They took the remainder of floor diving by 3 to group boxes.
2. I need to first produce an answer before iterating on it. Trying to implement the best approach first leads to a lot of added complexity.
3. Space complexity can be improved here by using bitmasking. That is another section of Python I'll need to brush up on.
4. My biggest issue is still not being able to quickly implement my solutions because of a lack of knowledge on how to use basic data structures in unusual ways. For instance, I didn't immediately know how to iterate a list with an iterator other than one.
'''