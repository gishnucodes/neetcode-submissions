class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = {}

        ## create a hashmap of val to index 

        for i,n in enumerate(nums):
            index[n]=i

        ## enumerate through the nums and find within hashmap if diff exists in map keys

        for i, n in enumerate(nums):

            diff = target - n 

            if diff in index and index[diff] != i:
                return [i,index[diff]]
        return []