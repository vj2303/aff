from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs_recursive(self, start):
        visited = [False] * len(self.graph)
        result = []

        def bfs_util(queue):
            if not queue:
                return
            node = queue.pop(0)
            result.append(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
            bfs_util(queue)

        visited[start] = True
        bfs_util([start])
        return result

    def dfs_recursive(self, start):
        visited = [False] * len(self.graph)
        result = []

        def dfs_util(node):
            visited[node] = True
            result.append(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)
        return result

if __name__ == "__main__":
    g = Graph()

    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input("Enter an edge (u v): ").split())
        g.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex: "))

    print("BFS Traversal:", g.bfs_recursive(start_vertex))
    print("DFS Traversal:", g.dfs_recursive(start_vertex))








# Enter the number of vertices: 6
# Enter the number of edges: 7
# Enter an edge (u v): 0 1
# Enter an edge (u v): 0 2
# Enter an edge (u v): 1 3
# Enter an edge (u v): 2 4
# Enter an edge (u v): 3 5
# Enter an edge (u v): 4 5
# Enter an edge (u v): 4 2
# Enter the starting vertex: 0
# BFS Traversal: [0, 1, 2, 3, 4, 5]
# DFS Traversal: [0, 1, 3, 5, 2, 4]




# O(V+E)