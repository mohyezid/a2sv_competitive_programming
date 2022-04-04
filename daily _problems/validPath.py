class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        q = collections.deque()
        q.append(source)
        visited = set()
        visited.add(source)
        while q:
            node = q.popleft()
            if node == destination:
                return True
            
            for i in range(len(edges)):
                if node ==edges[i][0] and edges[i][1] not in visited:
                    q.append(edges[i][1])
                    visited.add(edges[i][1])
                elif node ==edges[i][1] and edges[i][0] not in visited :
                    q.append(edges[i][0])
                    visited.add(edges[i][0])
