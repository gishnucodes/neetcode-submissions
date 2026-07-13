class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        candidates.sort()

        def backtrack(start, choices):

            if sum(choices)==target:
                result.append(choices[:])
            elif sum(choices) > target:
                return 
            
            for i in range(start, len(candidates)):

                if i > start and candidates[i]==candidates[i-1]:
                    continue 
                    
                choices.append(candidates[i])
                backtrack(i+1,choices)
                choices.pop()
            
        backtrack(0,[])
        return result 