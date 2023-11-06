class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = [[] for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.edges[start].append(end)
        self.edges[end].append(start)

def graph_coloring_branch_and_bound(graph):
    def is_valid_coloring(coloring, vertex, color):
        return all(coloring[neighbor] != color for neighbor in graph.edges[vertex])

    def heuristic(graph, coloring):
        return sum(1 for i in range(graph.num_vertices) if coloring[i] == 0)

    def branch_and_bound_coloring(current_vertex):
        nonlocal chromatic_number
        nonlocal best_coloring

        if current_vertex == graph.num_vertices:
            num_colors_used = max(best_coloring)
            if num_colors_used < chromatic_number:
                chromatic_number = num_colors_used
                best_coloring[:] = current_coloring[:]
            return

        if heuristic(graph, current_coloring) >= chromatic_number:
            return

        for color in range(1, max_colors + 1):
            if is_valid_coloring(current_coloring, current_vertex, color):
                current_coloring[current_vertex] = color
                branch_and_bound_coloring(current_vertex + 1)
                current_coloring[current_vertex] = 0

    max_colors = graph.num_vertices
    coloring = [0] * graph.num_vertices
    chromatic_number = float('inf')
    best_coloring = [max_colors] * graph.num_vertices

    branch_and_bound_coloring(0)

    if chromatic_number == float('inf'):
        return None
    else:
        return best_coloring

# Take user input to define the graph
graph = Graph(int(input("Enter the number of vertices: ")))

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    start, end = map(int, input("Enter edge (start end): ").split())
    graph.add_edge(start, end)

# Solve the graph coloring problem using Branch and Bound
coloring = graph_coloring_branch_and_bound(graph)

if coloring:
    print("Valid Coloring:", coloring)
else:
    print("No valid coloring exists.")






# The complexity is often expressed as O(b^d), where b is the branching factor (maximum number of colors to choose from), and d is the depth of the solution tree