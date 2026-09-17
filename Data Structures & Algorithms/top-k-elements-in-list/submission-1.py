class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}

        ## count and store all numbers and their freq in nums -> freq map 
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        
        ## then create a heap - python impl min-heap , which means the root will be smallest
        
        heap = []

        for nums in hashmap.keys():
            heapq.heappush(heap,(hashmap[nums],nums))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result