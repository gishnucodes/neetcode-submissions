class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence=''
        for i in strs:
            sentence+=i+'ñ'
        
        return sentence


    def decode(self, s: str) -> List[str]:

        splitList = s.split('ñ')
        
        n = len(splitList)
        return splitList[0:n-1]
        
