class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = [] 
        nums.sort()

        def backtrack(start, choices):

            result.append(choices[:])

            for i in range(start,len(nums)):

                if i > start and nums[i]==nums[i-1]:
                    continue

                choices.append(nums[i])
                backtrack(i+1,choices)
                choices.pop()
            
        backtrack(0,[])
        return result 