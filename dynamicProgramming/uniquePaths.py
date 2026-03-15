"""
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def traverse(row,col):
            # check bounds
            if row >= m or col >= n:
                return 0
            
            if row == m-1 and col == n-1:
                return 1

            return traverse(row+1, col) + traverse(row, col+1)

        return traverse(0,0)
