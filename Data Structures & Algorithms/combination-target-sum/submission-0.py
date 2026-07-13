class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(start,choices):

            if sum(choices) == target:
                result.append(choices[:])
                return 
            elif sum(choices) > target:
                return 
            

            for i in range(start, len(nums)):

                choices.append(nums[i])
                backtrack(i,choices)
                choices.pop()
            
        backtrack(0,[])

        return result 