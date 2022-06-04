class Graph:
	def __init__(self, num_nodes, directed=False):
		self._nodes = {n: [] for n in range(num_nodes)}
		self._edge_weights = {}
		self._directed = directed
		self._node_values = {n: None for n in range(num_nodes)}

	@property
	def node_count(self):
		return len(self._nodes)

	@property
	def edge_count(self):
		return sum(map(len, self._nodes.values()))

	def add_node(self, node):
		self._nodes[node] = []

	def add_edge(self, u, v):
		self._nodes[u].append(v)
		if not self._directed:
			self._nodes[v].append(u)

	def remove_node(self, node):
		self._nodes.pop(node)

	def remove_edge(self, u, v):
		node_pairs = [(u,v)] if self._directed else [(u,v), (v,u)]

		for a, b in node_pairs:
			edges = self._nodes[a]
			edges.remove(b)
			self._nodes[a] = edges

	def neighbours(self, node):
		for n in self._nodes[node]:
			yield n

	def adjacent(self, u, v):
		return (u in self._nodes) and (v in self._nodes[u])

	def get_node_value(self, node):
		return self._node_values[node]

	def set_node_value(self, node, value):
		self._node_values[node] = value

	def get_edge_value(self, u, v):
		return self._edge_weights([u,v])

	def set_edge_value(self, u, v, weight):
		self._edge_weights[(u,v)] = weight

	def __str__(self):
		return f'{self._nodes}\n{self._edge_weights}'