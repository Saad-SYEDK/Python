class Graph:
    def __init__(self):
        # Use a dictionary where key = Node, value = List of Neighbors
        self.adj_list = {} # Adjacency List

    def add_edge(self, u, v):
        # Ensure both nodes exist in the dictionary
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        
        # Add the connection (Directed Graph)
        self.adj_list[u].append(v)

    def dfs(self, start_node):
        visited = set()
        self._dfs_recursive(start_node, visited)

    def _dfs_recursive(self, node, visited):
        # Mark as visited and print
        visited.add(node)
        print(f"Visited: {node}")

        # Explore neighbors
        for neighbor in self.adj_list.get(node, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start_node):
        visited = set()
        visited.add(start_node)
        
        from collections import deque # We will use queue for bfs 
        queue = deque()
        queue.append(start_node)
        
        while queue:
            current = queue.popleft()
            print("Visited: ", current)
            for node in self.adj_list[current]:
                if node not in visited:
                    queue.append(node)
                visited.add(node)
                
            
    
# --- Usage ---
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(4, 2)
g.add_edge(4, 5)

print("Starting DFS from node 0:")
g.dfs(0)


print("Starting BFS from node 0:")
g.bfs(0)