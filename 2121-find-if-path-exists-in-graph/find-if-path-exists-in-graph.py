class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=self.createGraph(edges)
        
        return self.explore(graph,source,destination,set())
        



    def explore(self,graph,start,destination,visited):
        if start in visited:   
            return 
        if start==destination:
            return True
        for ele in graph[start]:
            visited.add(start)
            if self.explore(graph,ele,destination,visited):
                return True
        
        return False
        




    def createGraph(self,edges):
        g={}
        for a,b in edges:
            if a not in g:
                g[a]=[]
            if b not in g:
                g[b]=[]
            g[a].append(b)
            g[b].append(a)
        
        return g


        