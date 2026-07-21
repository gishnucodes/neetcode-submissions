class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)


        for i,j in prerequisites:
         adjList[i].append(j)

        unseen = 0 
        visiting = 1 
        visited = 2 

        state = [0]*numCourses

        def dfs(i):
            
            if state[i]==visited:
                return True 
            elif state[i]==visiting:
                return False

            state[i]=visiting    
            

            for nei in adjList[i]:
                if not dfs(nei):
                    return False
            
            state[i]=visited
            return True 
                
        for i in range(numCourses):
            
            if not dfs(i):
                return False
        
        return True 
        