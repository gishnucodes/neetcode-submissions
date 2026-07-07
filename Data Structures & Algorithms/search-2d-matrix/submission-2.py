class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        if columns==1:
            for i in matrix:
                if i[0]==target:
                    return True
            return False

        shortedSearch = []
        for i in matrix:
            tempList = []
            tempList.append(i[0])
            tempList.append(i[-1])
            shortedSearch.append(tempList)
        
        flag = 0
        for i in range(0,len(shortedSearch)):

            if target >= shortedSearch[i][0] and target <= shortedSearch[i][-1]:
                flag = i 
                break 
        
        for i in range(0,len(matrix[flag])):
            if target == matrix[flag][i]:
                return True 
            
        return False
        
                



        
        