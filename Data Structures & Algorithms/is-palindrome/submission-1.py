class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i)
        
        rst = lst[::-1]

        if str(lst)==str(rst):
            return True
        else:
            return False
        