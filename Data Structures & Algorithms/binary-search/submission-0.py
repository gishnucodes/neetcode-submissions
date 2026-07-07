class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1  # Use the last valid index

        while l <= r:
            # Calculate m inside the loop
            m = (l + r) // 2 
            
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1 # Narrow search to the left half
            else:
                l = m + 1 # Narrow search to the right half
            
        return -1