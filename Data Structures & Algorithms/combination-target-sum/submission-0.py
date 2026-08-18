class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def dfs(i, current_sum):
            # Base Case 1: Target achieve ho gaya!
            if current_sum == target:
                res.append(path.copy())
                return
            
            # Base Case 2: Out of bounds ya sum target se bada ho gaya
            if i >= len(candidates) or current_sum > target:
                return

            # Decision 1: Include candidates[i] (Index 'i' same rehta hai for reuse)
            path.append(candidates[i])
            dfs(i, current_sum + candidates[i])

            # Backtrack
            path.pop()

            # Decision 2: Exclude candidates[i] (Move to next element 'i + 1')
            dfs(i + 1, current_sum)

        dfs(0, 0)
        return res