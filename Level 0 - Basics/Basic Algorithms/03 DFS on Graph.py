from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                return Graph.DFSUtil(neighbor, visited)
            
    def DFS(self, v):
        visited = set()
        return Graph.DFSUtil(self, v, visited)
