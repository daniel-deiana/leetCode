"""
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1: 

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

Output: 1

"""


class Solution:
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        def visitIsland(pos):

            col = pos[1]
            row = pos[0]

            if col >= cols or col < 0:
                return
            if row >= rows or row < 0:
                return

            if pos in visited:
                return

            if grid[row][col] == "0":
                return

            visited.add(pos)

            neighbors = [
            (row+1, col),
            (row-1, col),
            (row, col+1),
            (row, col-1)
            ]
            for pos in neighbors:
                visitIsland(pos)
            


            
        visited = set()
        cols = len(grid[0])
        rows = len(grid)
        numIslands = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    numIslands +=1
                    visitIsland((i,j))

        return numIslands
