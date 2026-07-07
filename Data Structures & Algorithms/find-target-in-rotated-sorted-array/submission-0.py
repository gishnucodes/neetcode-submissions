# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
        
#         n=len(nums)
#         l=0
#         r=n-1 

#         while l<=r:

#             m = (l+r)//2

#             if nums[m]==target:
#                 return m 
#             elif target > nums[l] and target < nums[r] and target > nums[m]:
#                 l = m+1 
#             elif target > nums[l] and target < nums[r] and target > nums[m]:
#                 r = m-1 
#             elif target < nums[l] and target > nums[r] and target < nums[m]:
#                 r = m-1 
#             elif target < nums[l] and target > nums[r] and target < nums[m]:
#                 l = m+1 
#         return -1 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1 

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m 

            # Identify if the LEFT side is sorted
            if nums[l] <= nums[m]:
                # Logic: Is the target strictly inside this sorted left range?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # Otherwise, the RIGHT side MUST be sorted
            else:
                # Logic: Is the target strictly inside this sorted right range?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
        return -1
            