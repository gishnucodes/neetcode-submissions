class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Identify which half is sorted
            # Case 1: Left half [l...m] is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in the left sorted half
                else:
                    l = m + 1  # Target must be in the right half
            
            # Case 2: Right half [m...r] is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in the right sorted half
                else:
                    r = m - 1  # Target must be in the left half

        return -1