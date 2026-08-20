class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort for duplicate handling
        nums.sort()
        res=[]
        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            #1. include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            subset.pop() #backtrack

            #2 exclude nums[i] and skip duplicates
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res
