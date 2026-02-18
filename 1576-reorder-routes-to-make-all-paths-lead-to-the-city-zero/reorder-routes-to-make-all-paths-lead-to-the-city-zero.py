class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges={ (a,b) for a,b in connections}
        count=0
        visited=set()
        d={city:[] for city in range(n)}
        
        for a,b in connections:
            d[a].append(b)
            d[b].append(a)
        
        def dfs(city):
            nonlocal edges,d,visited,count

            for neighbour in d[city]:
                if neighbour in visited:
                    continue
                if (neighbour, city) not in edges:
                    count+=1
                visited.add(neighbour)
                dfs(neighbour)    

        visited.add(0)
        dfs(0)
        return count
        