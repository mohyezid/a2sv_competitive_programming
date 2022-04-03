class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        distance = -1
        q = collections.deque()
        visited = set()
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    q.append((i,j))
    
        if len(q) == len(grid)*len(grid[0]):
            return -1
        
              
        
        while q:
            
             
            for i in range(len(q)):
                r,c = q.popleft()
                for dir in directions:
                    row, col = r+dir[0], c+dir[1]
                    if (row,col) not in visited and  0<= row < len(grid) and 0 <= col < len(grid[0]):
                        q.append((row,col))
                        visited.add((row,col))
            distance += 1
                
            
        return distance
        
