class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        visited = [False] * len(nums)

        def dfs():
            # Base Case: Agar path ki length nums ke barabar ho gayi
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                # Agar element pehle se path me included hai, to skip karo
                if visited[i]:
                    continue

                # 1. Choose
                visited[i] = True
                path.append(nums[i])

                # 2. Explore
                dfs()

                # 3. Un-choose / Backtrack
                path.pop()
                visited[i] = False

        dfs()
        return res
        