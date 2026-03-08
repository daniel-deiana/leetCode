"""

You are given a m×n 2D grid initialized with these three possible values:
    -1 - A water cell that can not be traversed.
    0 - A treasure chest.
    INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

"""


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def visitIslandFromChest(x,y):
            queue = [(x,y,0)]
            while queue :
                (row,col,distance) = queue.pop(0)
                if row >= rows or row < 0:
                    continue
                if col >= cols or col < 0:
                    continue
                if grid[row][col] == 0 and distance > 0:
                    continue
                if grid[row][col] == -1:
                    continue

                if not grid[row][col] == inf and grid[row][col] < distance:
                    continue
                
                grid[row][col] = distance
                
                adjacents = [
                    (row+1,col,distance+1),
                    (row-1,col,distance+1),
                    (row,col+1,distance+1),
                    (row,col-1,distance+1)
                ]
                for pos in adjacents:
                    queue.append(pos)
        
        cols = len(grid[0])
        rows = len(grid)
        inf =  2147483647
        print(inf)
        for i in range(0,rows):
            for j in range(0, cols):
                # i have found a chest, visit all the 
                if grid[i][j] == 0:
                    visitIslandFromChest(i,j)
