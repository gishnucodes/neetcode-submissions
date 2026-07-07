class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        mainArr = []
        n = len(nums)
        count = 0
        for i in range(0,n):
            
            for j in range(n-1,i,-1):
                
                add = nums[i]+nums[j]

                for k in range(j-1,i,-1):

                    if nums[k]==(-1*add):
                        arr=[]
                        arr.append(nums[i])
                        arr.append(nums[j])
                        arr.append(nums[k])
                        mainArr.append(arr)
        
        unique_tuples = {tuple(my_list) for my_list in mainArr}
        unique_lists = [list(tup) for tup in unique_tuples]

        return unique_lists

