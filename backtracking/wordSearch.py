class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = []
        rows = len(board)
        cols = len(board[0])

        def backtrack(pos, i, curr, path):


            row = pos[0]
            col = pos[1]


            if len(word) == i:
                return True

            if row < 0 or col < 0 or row >= rows or col >= cols or i > len(word) or (row,col) in path:
                return False

            if not word[i] == board[row][col]:
                return False

            path.append((row,col))
            res = ( backtrack((row, col + 1), i + 1, curr + board[row][col], path) 
                or backtrack((row, col - 1), i + 1, curr + board[row][col], path) 
                or backtrack((row + 1, col), i + 1, curr + board[row][col], path) 
                or backtrack((row - 1, col), i + 1, curr + board[row][col], path)
            )
            path.pop()
            return res
    
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or backtrack((i,j), 0, board[i][j], [])

        return res
