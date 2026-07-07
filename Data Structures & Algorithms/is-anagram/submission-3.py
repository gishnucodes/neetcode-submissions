class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(list(s))
        t=sorted(list(t))

        if s==t:
            return True
        else:
            return False
        