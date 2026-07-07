class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mapper = {}
        for i in set(nums):
            mapper[i]=0
        
        for i in nums:
            mapper[i]+=1
        
        val = sorted(mapper.items(),key=lambda x:x[1],reverse=True)
        
        val = val[:k]
        r =[]
        for i,j in val:
            r.append(i)
        return r
        