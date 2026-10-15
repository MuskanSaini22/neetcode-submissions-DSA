class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n=len(temperatures)
        res=[0]*n
        stack=[]

        for i, temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_i=stack.pop()
                res[prev_i]=i-prev_i
            stack.append(i)
        
        return res