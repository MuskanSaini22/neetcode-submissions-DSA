class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posDiag=set()
        negDiag=set()

        res=[]
        board=[["."] * n for _ in range(n)]

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                #1 choose
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c]="Q"

                #2 explore
                backtrack(r+1)

                #3 backtrack
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
        