class TestSimpleGraph(unittest.TestCase):
	
	def setUp(self):
		self.simpleGraph = SimpleGraph(16)

		def testDFSDtoA(self):
		letters = ["A","B","C","D","E"]
		for i in letters:
			self.simpleGraph.AddVertex(i)
		self.simpleGraph.AddEdge(0,1)
		self.simpleGraph.AddEdge(0,2)
		self.simpleGraph.AddEdge(0,3)
		self.simpleGraph.AddEdge(1,0)
		self.simpleGraph.AddEdge(1,3)
		self.simpleGraph.AddEdge(1,4)
		self.simpleGraph.AddEdge(2,0)
		self.simpleGraph.AddEdge(2,3)
		self.simpleGraph.AddEdge(3,0)
		self.simpleGraph.AddEdge(3,1)
		self.simpleGraph.AddEdge(3,2)
		self.simpleGraph.AddEdge(3,3)
		self.simpleGraph.AddEdge(3,4)
		self.simpleGraph.AddEdge(4,1)
		self.simpleGraph.AddEdge(4,3)
		x = self.simpleGraph.DepthFirstSearch(0,4)
		for i in range(len(x)):
			x[i] = x[i].Value
		y = self.simpleGraph.DepthFirstSearch(3,0)
		for i in range(len(y)):
			y[i] = y[i].Value
		assert x == ["A","B","D","E"]
		assert y == ["D","A"]
