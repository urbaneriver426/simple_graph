class TestSimpleGraph(unittest.TestCase):
	def setUp(self):
		self.simpleGraph = SimpleGraph(16)

	def testDFS6Vertex(self):
		for i in range(6):
			self.simpleGraph.AddVertex(i)
		self.simpleGraph.AddEdge(1,0)
		self.simpleGraph.AddEdge(1,2)
		self.simpleGraph.AddEdge(1,3)
		self.simpleGraph.AddEdge(2,5)
		self.simpleGraph.AddEdge(3,4)
		x = self.simpleGraph.DepthFirstSearch(2,4)
		y = []
		for i in range(len(x)):
			y.append(x[i].Value)
		assert y == [2,1,3,4]

	def testDFS15Vertex(self):
		for i in range(15):
			self.simpleGraph.AddVertex(i)
		self.simpleGraph.AddEdge(0,1)
		self.simpleGraph.AddEdge(0,2)
		self.simpleGraph.AddEdge(2,1)
		self.simpleGraph.AddEdge(3,1)
		self.simpleGraph.AddEdge(3,2)
		self.simpleGraph.AddEdge(4,1)
		self.simpleGraph.AddEdge(5,2)
		self.simpleGraph.AddEdge(5,6)
		self.simpleGraph.AddEdge(4,6)
		self.simpleGraph.AddEdge(5,8)
		self.simpleGraph.AddEdge(4,7)
		self.simpleGraph.AddEdge(7,8)
		self.simpleGraph.AddEdge(7,9)
		self.simpleGraph.AddEdge(8,10)
		self.simpleGraph.AddEdge(9,11)
		self.simpleGraph.AddEdge(11,13)
		self.simpleGraph.AddEdge(14,13)
		self.simpleGraph.AddEdge(14,12)
		self.simpleGraph.AddEdge(12,10)
		x = self.simpleGraph.DepthFirstSearch(0,14)
		y = []
		for i in range(len(x)):
			y.append(x[i].Value)
		assert y == [0,1,2,5,6,4,7,8,10,12,14]

	def testDFSNoWay(self):
		for i in range(15):
			self.simpleGraph.AddVertex(i)
		self.simpleGraph.AddEdge(0,1)
		self.simpleGraph.AddEdge(0,2)
		self.simpleGraph.AddEdge(2,1)
		self.simpleGraph.AddEdge(3,1)
		self.simpleGraph.AddEdge(3,2)
		self.simpleGraph.AddEdge(4,1)
		self.simpleGraph.AddEdge(5,2)
		self.simpleGraph.AddEdge(5,6)
		self.simpleGraph.AddEdge(4,6)
		self.simpleGraph.AddEdge(5,8)
		self.simpleGraph.AddEdge(4,7)
		self.simpleGraph.AddEdge(7,8)
		self.simpleGraph.AddEdge(7,9)
		self.simpleGraph.AddEdge(8,10)
		self.simpleGraph.AddEdge(9,11)
		self.simpleGraph.AddEdge(11,13)
		self.simpleGraph.AddEdge(12,10)
		x = self.simpleGraph.DepthFirstSearch(0,14)
		y = []
		for i in range(len(x)):
			y.append(x[i].Value)
		assert y == []

if __name__ == '__main__':
	unittest.main()
