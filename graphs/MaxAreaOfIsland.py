"""
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]



Output: 6

Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def computeAreaOfIsland(x,y):
            
            if x >= rows or x < 0:
                return 0
            if y >= cols or y < 0:
                return 0
            if grid[x][y] == 0 or grid[x][y] == "v":
                return 0
            
            grid[x][y] = "v"

            return (
                1 + computeAreaOfIsland(x,y+1) 
                + computeAreaOfIsland(x,y-1) 
                + computeAreaOfIsland(x+1,y) 
                + computeAreaOfIsland(x-1,y)
            )

        cols = len(grid[0])
        rows = len(grid)
        
        maxArea = 0
        for i in range(0,rows):
            for j in range(0,cols):
                currentArea = computeAreaOfIsland(i,j)
                if maxArea < currentArea:
                    maxArea = currentArea
        
        return maxArea
