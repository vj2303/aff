import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    graph = {}
    
    num_vertices = int(input("Enter the number of vertices: "))
    
    for i in range(num_vertices):
        edges = input(f"Enter the edges connected to vertex {i} (vertex weight, vertex weight): ")
        edges = [int(val) for val in edges.split()]
        graph[i] = [(edges[j], edges[j + 1]) for j in range(0, len(edges), 2)]

    start_vertex = int(input("Enter the starting vertex: "))

    result = dijkstra(graph, start_vertex)
    print(result)






# Enter the number of vertices: 6
# Enter the edges connected to vertex 0 (vertex weight, vertex weight, ): 3 9 5 4
# Enter the edges connected to vertex 1 (vertex weight, vertex weight, ): 4 4 2 10
# Enter the edges connected to vertex 2 (vertex weight, vertex weight, ): 5 10
# Enter the edges connected to vertex 3 (vertex weight, vertex weight, ): 0 9
# Enter the edges connected to vertex 4 (vertex weight, vertex weight, ): 1 4 5 3
# Enter the edges connected to vertex 5 (vertex weight, vertex weight, ): 0 4 1 10 4 3
# Enter the starting vertex: 1

# {0: 8, 1: 0, 2: 12, 3: 8, 4: 4, 5: 7}



# O(V^2) 