class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        response = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    response.append(i)
                    response.append(j)
                    return sorted(response)
        return response
        