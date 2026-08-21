class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, k):
            # Base Case 1: Word ke saare characters match ho gaye
            if k == len(word):
                return True

            # Base Case 2: Out of bounds ya character match nahi hua
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[k]):
                return False

            # 1. CHOOSE: Cell ko mark karo taaki same DFS path mein repeat na ho
            temp = board[r][c]
            board[r][c] = "#"

            # 2. EXPLORE: 4 Directions (Up, Down, Left, Right)
            res = (dfs(r + 1, c, k + 1) or
                   dfs(r - 1, c, k + 1) or
                   dfs(r, c + 1, k + 1) or
                   dfs(r, c - 1, k + 1))

            # 3. UN-CHOOSE / BACKTRACK: Cell ko original character me restore karo
            board[r][c] = temp

            return res

        # Har cell ko starting point banakar try karo
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False