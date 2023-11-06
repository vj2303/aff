# import heapq

# def prim_spanning_tree(V, adj):
#     pq = []
#     vis = [False] * V
#     pq.append((0, 0))
#     total_weight = 0

#     while pq:
#         wt, node = heapq.heappop(pq)

#         if vis[node]:
#             continue

#         vis[node] = True
#         total_weight += wt

#         for neighbor, edge_weight in adj[node]:   
#             if not vis[neighbor]:
#                 heapq.heappush(pq, (edge_weight, neighbor))

#     return total_weight

# if __name__ == "__main__":
#     # Input the number of vertices from the user
#     V = int(input("Enter the number of vertices:"))

#     # Create an adjacency list based on user input
#     adj = [[] for _ in range(V)]
#     for i in range(V):
#         while True:
#             edge_input = input(f"Enter edges connected to vertex {i} and their weights (vertex weight), separated by spaces (e.g., '1 2 3 4' for edges to vertices 1 and 3 with weights 2 and 4): ")
#             if edge_input.strip() == "":
#                 break
#             edges = list(map(int, edge_input.split()))
#             for j in range(0, len(edges), 2):
#                 neighbor = edges[j]
#                 weight = edges[j + 1]
#                 adj[i].append((neighbor, weight))

#     result = prim_spanning_tree(V, adj)
#     print("The weight of the minimum spanning tree is:", result)




#   # Number of vertices and edges (for simplicity, use a predefined graph)
#     # V = 5
#     # adj = [
#     #     [(1, 2), (2, 4)],
#     #     [(0, 2), (2, 1), (3, 5)],
#     #     [(0, 4), (1, 1), (3, 3), (4, 6)],
#     #     [(1, 5), (2, 3), (4, 7)],
#     #     [(2, 6), (3, 7)]
#     # ]

#     # result = prim_spanning_tree(V, adj)
#     # print("The weight of the minimum spanning tree is:", result)



# # Enter the number of vertices: 4

# # Enter edges connected to vertex 0 and their weights (vertex weight), separated by spaces (e.g., '1 2 3 4' for edges to vertices 1 and 3 with weights 2 and 4): 1 2 3 4

# # Enter edges connected to vertex 1 and their weights (vertex weight), separated by spaces (e.g., '1 2 3 4' for edges to vertices 1 and 3 with weights 2 and 4): 2 3 1 5

# # Enter edges connected to vertex 2 and their weights (vertex weight), separated by spaces (e.g., '1 2 3 4' for edges to vertices 1 and 3 with weights 2 and 4): 3 4

# # Enter edges connected to vertex 3 and their weights (vertex weight), separated by spaces (e.g., '1 2 3 4' for edges to vertices 1 and 3 with weights 2 and 4):

# # The minimum spanning tree weight is: 9

import heapq

def prim_spanning_tree():
    num_vertex = int(input("Enter number of vertices: "))
    num_edges = int(input("Enter number of edges: "))
    adj = [[] for _ in range(num_vertex)]
    for _ in range(num_edges):
        u, v, w = map(int,input("Enter u,v, weight: ").split())
        adj[u].append((v,w))
        adj[v].append((u,w))

    pq = []
    vis = [False]*num_vertex
    pq.append((0,0))
    total_weight = 0

    while pq:
        wt, node = heapq.heappop(pq)
        if vis[node]:
            continue
        vis[node] = True
        total_weight += wt

        for neighbor, edge_weight in adj[node]:
            if not vis[neighbor]:
                heapq.heappush(pq, (edge_weight, neighbor))
    print("Total cost :", total_weight)

prim_spanning_tree()


# O(E log V)

