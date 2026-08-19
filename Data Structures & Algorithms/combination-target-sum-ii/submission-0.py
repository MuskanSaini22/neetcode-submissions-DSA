class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(i, current_sum):
            # Base Case 1: Target achieve ho gaya
            if current_sum == target:
                res.append(path.copy())
                return
            
            # Base Case 2: Out of bounds ya sum target se bada ho gaya
            if i >= len(candidates) or current_sum > target:
                return

            # CHOICE 1: TAKE candidates[i]
            path.append(candidates[i])
            dfs(i + 1, current_sum + candidates[i])
            path.pop()  # Backtrack

            # CHOICE 2: NOT TAKE candidates[i]
            # SAFE SKIP: Pehle boundary check (i + 1 < len), fir value comparison!
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Agle unique element par move karo
            dfs(i + 1, current_sum)

        dfs(0, 0)
        return res