class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = left + 1 
        length = 0 

        if(len(s)==1):
            return 1
        

        while(left <= right and right < len(s)):

            n = len(s[left:right+1])
            set_s = set(s[left:right+1])

            length = max(len(set_s),length)

            if len(set_s)<n:
                left = left + 1
            else:
                right = right + 1 
        
        return length
        