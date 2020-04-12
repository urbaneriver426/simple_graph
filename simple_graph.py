class Vertex:

	def __init__(self, val):
		self.Value = val
		self.Hit = False
  
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

	def DepthFirstSearch(self, VFrom, VTo):
		stack = []
		visited = []
		stack.append(VFrom)
		visited.append(self.vertex[VFrom])
		self.vertex[VFrom].Hit = True
		while len(stack) != 0 and VFrom != VTo:
			if self.m_adjacency[VFrom][VTo] == 1:
				stack.append(VTo)
				VFrom = VTo			
			else:
				count = 1
				for i in range(self.max_vertex):
					if self.m_adjacency[VFrom][i] == 1:
						if self.vertex[i].Hit == False:
							stack.append(i)
							VFrom = i
							self.vertex[i].Hit = True
							visited.append(self.vertex[i])
							count = 0
							break
				if count > 0:
					stack.pop()
					VFrom = len(stack)-1
		for i in range(len(stack)):
			stack[i] = self.vertex[stack[i]]
		for i in range(len(visited)):
			visited[i].Hit = False
		return stack
