import time
from AdjacenySet import AdjacencySet
from Queue import Queue

class Graph(AdjacencySet):
	# our modified bfs algorithm that is based on the 2050 bfs aglorithm
	def bfs(self, v):
		goal = [1,2,3,4,5,6,7,8,0]				# end goal
		first_node = tuple(v)   				# starting board (v) will come as a list
		self.add_vertex(first_node)				# add first node (board) to the graph
					
		tree = {}										# tree to keep track of the path
		to_visit = Queue()								# create Queue object
		to_visit.enqueue((None, first_node))			# enqueue a tuple of the following form: (parent, child)

		while to_visit:									# Execute the following while Queue is not empty:
			a, b = to_visit.dequeue()					# Pop from the Queue (we unpack the tuple in a and b)
														# a is parent and b is current node (child)

			if list(b) == goal:							# if child is the end puzzle, then
				tree[b] = a 								# add to tree
				self.print_moves(self.create_path(tree))	# call function to print all the moves made
				return										# end the program

			b_possible_child = self.calculate_next_possible_moves(list(b))	# calculate all the next moves current board (b) could become... comes as a nested list

			# remember we have to build the graph up as we go
			# need to add all the possible boards (children) as verticies and edges with current board (b)
			for child in b_possible_child:
				tc = tuple(child)			# cast to tuple (cant add a list to set in graph)
				self.add_vertex(tc)			# add child to set of verticies

				edge = (b, tc)				# create a tuple that is an edge between current node (b) and its child (tc)
				self.add_edge(edge)			# add the edge to graph

			if b not in tree:						# if current node (b) isnt in the tree yet:
				tree[b] = a 						# add current node (b) and its parent (a) to the tree

				for n in self._neighbors(b):		# for each neighbor of b - really each edge of b

					if n not in tree:				# check to see if we have already done this, why would we do it again?
						to_visit.enqueue((b,n))		# enqueue the tuple of (current node, child of current node)

		print("Queue is empty. The puzzle is not solvable.")				
		return												# Should only return here if puzzle is not solvable


	# function to calculate all possible moves based on current puzzle board
	def calculate_next_possible_moves(self, node):	# returns new list contains new possible lists 
		
		curr_node = list(node) 	# node should come in as a tuple ... cast it to be a list

		possible_moves = []
		possible_nodes = []

		empty = curr_node.index(0)	# find the index of zero in current board

		# basic if-else statements to find which row zero is in
		if (empty >= 0 and empty <= 2):
			row = 0
		elif (empty >= 3 and empty <= 5):
			row = 1
		else:
			row = 2

		# If we moving 0 down is valid, add to possible moves
		if (empty - 3) >= 0:
			possible_moves.append(empty - 3)

		# If we moving 0 left is valid, add to possible moves	
		if (empty - 1 >= row * 3) and (empty - 1 <= row * 3 + 2):
			possible_moves.append(empty - 1)

		# If we moving 0 up is valid, add to possible moves
		if (empty + 3) <= 8:
			possible_moves.append(empty + 3)

		# If we moving 0 right is valid, add to possible moves
		if (empty + 1 >= row * 3) and (empty + 1 <= row * 3 + 2):
			possible_moves.append(empty + 1)

		# for each possible index to where 0 can move
		for index in possible_moves:			
			copy = curr_node[::]									# create copy of current state/node
			copy[empty], copy[index] = copy[index], copy[empty]		# switch zero to new spot
			possible_nodes.append(copy)								# add that new state/node to possible_nodes

		return possible_nodes	# return list of possilbe new boards: [[possible node], [possible node]...]

	# Given a tree generated by BFS, this will generate will traverse the tree in reverse to find the optimal path	
	def create_path(self, tree):
		path = []
		path.append((1,2,3,4,5,6,7,8,0))
		parent = tree[(1,2,3,4,5,6,7,8,0)]
		while parent is not None:
			path.append(parent)
			parent = tree[parent]

		return path

	# Function to print each move that was made in the proper format
	def print_moves(self, lst):
		count = 0
		for i in range(len(lst)-1, -1, -1):
			string = 'Step: {}\n'.format(count)
			string += '******************\n'
			row1 = '   {}    {}    {}    \n'.format(lst[i][0], lst[i][1], lst[i][2])
			row2 = '   {}    {}    {}    \n'.format(lst[i][3], lst[i][4], lst[i][5])
			row3 = '   {}    {}    {}    \n'.format(lst[i][6], lst[i][7], lst[i][8])
			string += row1 + row2 + row3
			string += '******************\n' 
			print(string)
			count += 1

# Write test cases below
if __name__ == '__main__':
	x = time.time()			# start timer
	G = Graph()				# create the Graph object

	# Test Case 1:	The main test case
	G.bfs([8,7,6,5,4,3,2,1,0])

	# Test Case 2:
	#G.bfs([1,2,0,4,5,3,7,8,6])

	# Test Case 3:	Unsolvable
	#G.bfs([8,1,2,0,4,3,7,6,5])

	# Test Case 4:	Unsolvable
	#G.bfs([7,1,2,5,3,4,8,0,6])

	# Test Case 5:	No steps required
	#G.bfs([1,2,3,4,5,6,7,8,0])
	
	# print how long it took to solve
	print("Time to solve: {} seconds.".format(time.time() - x))