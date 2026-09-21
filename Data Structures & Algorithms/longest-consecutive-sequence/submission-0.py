class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
       if not nums:
        return 0

       sortedSet = list(sorted(set(nums)))


       count = 1
       maxCount=1
       for i in range(0,len(sortedSet)-1):
            if sortedSet[i+1]-sortedSet[i]==1:
                count+=1
                maxCount = max(maxCount,count)
            else:
                count=1
                continue
       
       return maxCount
                
            
        