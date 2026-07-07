class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        left = 0 
        right = n-1
        area = 0 
        value = 0 
        while left < right :
            minimum = min(heights[left],heights[right])
            value = (right-left)*minimum
            area = max(area,value)

            if heights[left]<heights[right]:
                left=left+1
            else:
                right = right-1
            
        

        return area
        