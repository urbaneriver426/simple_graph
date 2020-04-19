class SimpleTreeNode:
	
	def __init__(self, val, parent):
		self.NodeValue = val 
		self.Parent = parent 
		self.Children = [] 
	
class SimpleTree:

	def __init__(self, root):
		self.Root = root
	
	def AddChild(self, ParentNode, NewChild):
		ParentNode.Children.append(NewChild)
		NewChild.Parent = ParentNode
  
	def DeleteNode(self, NodeToDelete):
		NodeToDelete.Parent.Children.remove(NodeToDelete)
		NodeToDelete.Parent = None 

	def GetAllNodes(self,result = None, count = 0):
		if result is None:
			result = []
		if count == 0:
			if self.Root is not None:
				result.append(self.Root)
			else:
				return result
		for i in range(len(result[count].Children)):
			result.append(result[count].Children[i])
		count += 1
		if count < len(result):
			return self.GetAllNodes(result, count)
		else:	
			return result		

	def FindNodesByValue(self, val):
		x = self.GetAllNodes()
		result = []
		for node in x:
			if node.NodeValue == val:
				result.append(node)
		return result

	def MoveNode(self, OriginalNode, NewParent):
		OriginalNode.Parent.Children.remove(OriginalNode)
		NewParent.Children.append(OriginalNode)
		OriginalNode.Parent = NewParent
   
	def Count(self):
		return len(self.GetAllNodes())

	def LeafCount(self):
		x = self.GetAllNodes()
		result = 0
		for node in x:
			if len(node.Children) == 0:
				result += 1
		return result

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
		result = [self.vertex[VFrom]]
		visited = [self.vertex[VFrom]]
		if VFrom == VTo:
			return result
		else:
			self.vertex[VFrom].Hit = True
			for i in range(self.max_vertex):
				if self.m_adjacency[VFrom][i] == 1:
					if self.vertex[i].Hit == False:
						result += self.DepthFirstSearch(i,VTo)
						visited += self.DepthFirstSearch(i,VTo)
						if result[len(result)-1] == self.vertex[VTo]:
							for j in range(len(visited)):
								visited[j].Hit = False
							return result
			return []


	def BreadthFirstSearch(self, VFrom, VTo, quene = None, tree = None, visited = None):
		if quene == None:
			quene = []
			tree = SimpleTree(SimpleTreeNode(self.vertex[VFrom], None))
			visited = [self.vertex[VFrom]]
		currNode = tree.FindNodesByValue(self.vertex[VFrom])[0]
		if VFrom == VTo:
			result = []
			while currNode:
				result.insert(0, currNode.NodeValue)
				currNode = currNode.Parent
			for i in range(len(visited)):
				visited[i].Hit = False
			return result
		else:
			self.vertex[VFrom].Hit = True
			for i in range(self.max_vertex):
				if self.m_adjacency[VFrom][i] == 1:
					if self.vertex[i].Hit == False:
						quene.append(i)
						self.vertex[i].Hit = True
						visited.append(self.vertex[i])
						tree.AddChild(currNode, SimpleTreeNode(self.vertex[i],None))
			if len(quene) > 0:
				VFrom = quene.pop(0)
				return self.BreadthFirstSearch(VFrom, VTo, quene, tree, visited)
			else:
				return []
