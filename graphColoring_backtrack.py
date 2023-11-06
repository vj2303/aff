class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[] for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.edges[start].append(end)
        self.edges[end].append(start)

def graph_coloring_backtracking(graph):
    def is_valid_coloring(coloring, vertex, color):
        return all(coloring[neighbor] != color for neighbor in graph.edges[vertex])

    def backtrack_coloring(current_vertex):
        if current_vertex == graph.num_vertices:
            return True  # All vertices colored

        for color in range(1, max_colors + 1):
            if is_valid_coloring(coloring, current_vertex, color):
                coloring[current_vertex] = color

                if backtrack_coloring(current_vertex + 1):
                    return True  # Move to the next vertex

        return False

    max_colors = graph.num_vertices
    coloring = [0] * graph.num_vertices

    return coloring if backtrack_coloring(0) else None

# Take user input to define the graph
graph = Graph(int(input("Enter the number of vertices: ")))

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    start, end = map(int, input("Enter edge (start end): ").split())
    graph.add_edge(start, end)

# Solve the graph coloring problem using backtracking
coloring = graph_coloring_backtracking(graph)

if coloring:
    print("Valid Coloring:", coloring)
else:
    print("No valid coloring exists.")



# Enter the number of vertices: 4
# Enter the number of edges: 4
# Enter edge (start end): 0 1
# Enter edge (start end): 0 2
# Enter edge (start end): 1 2
# Enter edge (start end): 2 3
# Valid Coloring: [1, 2, 3, 1]

# O(2^N)