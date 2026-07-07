
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The minimum possible speed is 1, maximum is the largest pile
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours_spent = 0
            
            # Calculate total hours needed at speed k
            for p in piles:
                hours_spent += math.ceil(p / k)
            
            if hours_spent <= h:
                # If we finished in time, try a slower speed to find the minimum
                res = k
                r = k - 1
            else:
                # Too slow, must increase speed
                l = k + 1
                
        return res