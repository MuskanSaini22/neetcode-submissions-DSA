class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for _ in range(len(nums)+1)] #list of lists=2D list
        for n in nums:
            count[n]=count.get(n,0)+1 #frequency of number={number:frequency}
        for n,c in count.items():
            freq[c].append(n)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
