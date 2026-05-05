class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #Check Rows
        print("Rows")
        for i in range(9):
            seen = set()
            for j in range(9):
                char = board[i][j]
                #es numero
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)
            
        #Check Columns

        for i in range(9):
            seen = set()
            for j in range(9):
                char = board[j][i]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)


        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True