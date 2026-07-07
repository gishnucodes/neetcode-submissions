class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        n = len(nums)
        zero_index = []
        nonzero_index = []
        zero_arrary = []
        for i in range(0,n):
            if nums[i]==0:
                zero_index.append(i)
            else:
                nonzero_index.append(i)
            zero_arrary.append(0)


        if zero_index == []:

            product = 1
            for i in range(0,n):

                product = product * nums[i]

            for i in range(0,n):
                ans.append(product//nums[i])
            return ans 
        
        elif len(zero_index)==n:
            return nums
        elif (len(nonzero_index) >= 1 and len(zero_index) > 1 and len(nums)>2):
            return zero_arrary
        else:
            product = 1
            for i in range(0,n):
                if i not in zero_index:
                    product = product * nums[i]
            
            for i in zero_index:
                zero_arrary[i]=product 

            return zero_arrary
