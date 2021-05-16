
class MyGraphNode:
    
    def __init__(self, value):
        self.value = value
        self.edges = []


class MyGraph:
    
    def __init__(self):
        self.vertices = dict()
        self.vertexCount = 0
        self.visited = dict()

    def addVertex(self, value: str):
        if value not in self.vertices:
            node = MyGraphNode(value)
            self.vertices[value] = node
            self.vertexCount += 1
    
    def addEdges(self, vertex: str, edges):
        v:MyGraphNode = self.vertices.get(vertex)
        
        if v:
            for edge in edges:
                v.edges.append(edge)
    
    def dfs(self):
        self.visited = dict()
        
        for vertex in self.vertices:
            self.visited[vertex] = False 

        for vertex in self.vertices:
            self.dfsTraverse(vertex)
            
    
    def dfsTraverse(self, vertex):
        if not self.visited[vertex]:
            self.visited[vertex] = True
            print(F"Visiting {vertex}")

            for edge in self.vertices[vertex].edges:
                self.dfsTraverse(edge)


