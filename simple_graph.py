class Vertex:

    def __init__(self, val):
        self.Value = val
  
class SimpleGraph:
	
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for i in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, val):
        for i in range(self.max_vertex):
        	if self.vertex[i] is None:
        		self.vertex[i] = Vertex(val)
        		return

    def RemoveVertex(self, v):
        self.vertex[v] = None
        for i in range(self.max_vertex):
        	if self.m_adjacency[v][i] == 1:
        		self.m_adjacency[v][i] = 0
        		self.m_adjacency[i][v] = 0

    def IsEdge(self, v1, v2):
        if self.m_adjacency[v1][v2] == 1 and self.m_adjacency[v2][v1] == 1:
        	return True
        return False
	
    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0