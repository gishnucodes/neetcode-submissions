class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        n = len(numbers)
        for i in range(0,n):
            diff = numbers[i]-target 
            print(diff)
            for j in range(i+1,n):
                if (diff == numbers[j] or numbers[j] == (-diff)):
                    val = numbers[i]+numbers[j]
                    print("val:",val)
                    if val == target:
                        res.append(i+1)
                        res.append(j+1)
                        break
        
        return res
        