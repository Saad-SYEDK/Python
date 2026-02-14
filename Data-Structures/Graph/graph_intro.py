# Similar to Trees, Graphs are also a non-linear data structure.
# They consist of a finite set of vertices (or nodes) and a set of edges that connect pairs of vertices. 

# Properties of Graphs:
# Graphs can be directed or undirected,
# They can also be weighted or unweighted.
# They can also be cyclic or acyclic, depending on whether they contain cycles (i.e., paths that start and end at the same vertex).


# Graphs are used to represent various real-world problems, such as social networks, transportation networks, and computer networks.

# Graphs can be represented using 2 Ways:
    # 1. Using adjacency list.
    # 2. Using adjacency matrix.
    
# In an adjacency list, each vertex has a list of its adjacent vertices.
    # It is a more space-efficient representation for sparse graphs, where the number of edges is much less than the square of the number of vertices.
    
# In an adjacency matrix, a 2D array is used to represent the connections between vertices, where the value at row i and column j indicates whether there is an edge from vertex i to vertex j.
    # It is a more space-efficient representation for dense graphs, where the number of edges is close to the square of the number of vertices.
    
    
# EXAMPLE:
# Consider a directed graph with 8 vertices (0 to 7) and the following edges:
# (0, 1), (1, 2), (0, 3), (3, 4), (3, 6), (3, 7), (4, 2), (4, 5), (5, 2) 
# it means (start, end) i.e vertex 0 is connented to vertex 1, vertex 1 is connected to vertex 2 and so on. 
            # Try to draw this graph on a paper.

# Now let us represent this graph using an adjacency matrix.
n = 8 # number of vertices/nodes
edges = [(0, 1), (1, 2), (0, 3), (3, 4), (3, 6), (3, 7), (4, 2), (4, 5), (5, 2)] # Given edges

# our matrix will be of size n x n, where n is the number of vertices.
# We will initialize it with 0s, indicating no edges between vertices.

a_matrix = [ [0] * n for _ in range(n) ] # This will create an n x n matrix filled with 0s.
print(a_matrix)

#output:
'''
    [vertex name 0  1  2  3  4  5  6  7  
            0   [0, 0, 0, 0, 0, 0, 0, 0],
            1   [0, 0, 0, 0, 0, 0, 0, 0],
            2   [0, 0, 0, 0, 0, 0, 0, 0],
            3   [0, 0, 0, 0, 0, 0, 0, 0],
            4   [0, 0, 0, 0, 0, 0, 0, 0],
            5   [0, 0, 0, 0, 0, 0, 0, 0],
            6   [0, 0, 0, 0, 0, 0, 0, 0],
            7   [0, 0, 0, 0, 0, 0, 0, 0],
    ]
'''
 
 # Now we iterate through our edges and update the matrix to indicate the presence of edges between vertices.

for i, j in edges:
    a_matrix[i][j] = 1
     
print(a_matrix)
'''
[
    [0, 1, 0, 1, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 1, 1], 
    [0, 0, 1, 0, 0, 1, 0, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0]
]
'''
# Now for the same graph, let us create a adjacency list
# We will create a dictionary of lists, where each key represents the vertex and,
# its values represents the nodes that it can visit 
a_list = {}
for i , j in edges:
    if not i in a_list:
        a_list[i] = [j]
    else:
        a_list[i].append(j)

print(a_list)

# Moving forward, we will create a class for graph and add all the methods in it