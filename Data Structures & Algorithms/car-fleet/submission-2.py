# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

#         toGo = []
#         factor = []

#         for i in position:
#             toGo.append(target-i)

#         for i in range(0,len(position)):

#             factor.append(toGo[i]//speed[i])

#         print("factor:",factor)
#         s = set(factor)

#         return len(s)



        

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Combine position and speed, then sort by position DESCENDING
        # We start with the car closest to the target.
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        
        for p, s in cars:
            # 2. Calculate time as a float (don't use int()!)
            time = (target - p) / s
            
            # 3. Add time to stack
            stack.append(time)
            
            # 4. If the current car (behind) takes LESS or EQUAL time 
            # than the car in front, they merge into one fleet.
            # We represent the fleet by the slower car's time (the one in front).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # Remove the faster car behind; it's now part of the fleet
        
        # The number of remaining times in the stack is the number of fleets.
        return len(stack)