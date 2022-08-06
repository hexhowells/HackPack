
def get_neighbours(grid: list, point: tuple, diag=False: bool) -> list:
	"""Gets all neighbours around a given point on a 2D grid

	Args:
		grid (list): 2D list representing the grid
		point (tuple): x-y coordinates of the point (starts at 0)
		diag (bool): if True also fetches the diagonal neighbours
	"""
	height, width = len(grid), len(grid[0])
	(r, c) = point
	neighbour_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

	if diag:
		neighbour_cells.append([(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)])

	n = []
	for (r, c) in neighbour_cells:
		if (0 <= r < height) and (0 <= c < width):
			n.append((r, c))

	return n


def all_points(grid: list) -> tuple:
	"""Generator function that iterates over every point in a grid

	Args:
		grid (list): 2D list representing the grid
	"""
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			yield (r, c)


def create_grid(x: list) -> list:
	"""Creates a 2D grid given a 2D list of string values

	Args:
		x (list): 2 deep nested list of strings containing grid values
	"""
	return [[int(a) for a in list(line)] for line in x]