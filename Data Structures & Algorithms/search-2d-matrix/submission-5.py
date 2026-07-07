def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2  # Find the middle index
        
        # Check if target is present at mid
            if arr[mid] == target:
                return mid
        
        # If target is greater, ignore left half
            elif arr[mid] < target:
                low = mid + 1
        
        # If target is smaller, ignore right half
            else:
                high = mid - 1

        return -1

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
        
        finalRow = binary_search(matrix[flag],target)

        if finalRow==-1:
            return False
        else :
            return True
        
                



        
        