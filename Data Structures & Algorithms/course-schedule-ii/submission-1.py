class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for i,j in prerequisites:
            graph[i].append(j)
        
        stack = []
        state = [0]*numCourses

        UNSEEN = 0 
        VISITING = 1
        VISITED = 2 

        def dfs(i):
            
            if state[i]==VISITED: return True 
            elif state[i]==VISITING: return False 

            state[i]=VISITING

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            state[i]=VISITED 
            stack.append(i)
            return True

        
        for i in range(numCourses):

            if not dfs(i):
                return []
        
        return stack