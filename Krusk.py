def find_set(parent, v):
    if parent[v] == v:
        return v
    parent[v] = find_set(parent, parent[v])  # Path compression
    return parent[v]

# Helper function to join two sets
def union_sets(parent, rank, u, v):
    u = find_set(parent, u)
    v = find_set(parent, v)
    if u != v:
        if rank[u] < rank[v]:
            u, v = v, u
        parent[v] = u
        if rank[u] == rank[v]:
            rank[u] += 1

# Kruskal's algorithm
def kruskal(graph):
    edges = []
    for u in range(len(graph)):
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()  # Sort edges by weight

    minimum_spanning_tree = []
    parent = list(range(len(graph)))  # Initially, each vertex is its own parent
    rank = [0] * len(graph)

    for w, u, v in edges:
        if find_set(parent, u) != find_set(parent, v):
            minimum_spanning_tree.append((u, v, w))
            union_sets(parent, rank, u, v)

    return minimum_spanning_tree

# Input from the user
num_vertices = int(input("Enter the number of vertices: "))
graph = [[] for _ in range(num_vertices)]

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, w = map(int, input("Enter edge (u, v, weight): ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# Calculate and display the minimum spanning tree
mst = kruskal(graph)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"Edge: {u} - {v}, Weight: {w}")




#     Enter the number of vertices: 4
# Enter the number of edges: 5
# Enter edge (u, v, weight): 0 1 2
# Enter edge (u, v, weight): 0 2 4
# Enter edge (u, v, weight): 1 2 1
# Enter edge (u, v, weight): 2 3 3
# Enter edge (u, v, weight): 1 3 5

# Minimum Spanning Tree:
# Edge: 1 - 2, Weight: 1
# Edge: 0 - 1, Weight: 2
# Edge: 2 - 3, Weight: 3

# O(E log E),
