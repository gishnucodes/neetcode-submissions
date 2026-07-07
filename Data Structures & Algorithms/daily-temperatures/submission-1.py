# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
#         n = len(temperatures)
#         result = [0]*n

#         maxTemp = temperatures[n-1]
#         maxIndex = n-1 

#         for i in range(n-2,0,-1):

#             if temperatures[i]<maxTemp:
#                 result[i]=maxIndex-i
            
#             else:
#                 result[i]=0
#                 maxTemp=temperatures[i]
#                 maxIndex=i

#         return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # This will store pairs of [temperature, index]

        for i, temp in enumerate(temperatures):
            # While the stack is not empty and current temp is warmer 
            # than the temp at the top of the stack
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index
            
            stack.append([temp, i])

        return result
