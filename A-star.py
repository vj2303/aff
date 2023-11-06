import heapq


class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0


def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(*start)
    goal_node = Node(*goal)

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current.x == goal_node.x and current.y == goal_node.y:
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        closed_set.add((current.x, current.y))

        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = current.x + dx, current.y + dy

            if (
                    0 <= new_x < len(grid) and
                    0 <= new_y < len(grid[0]) and
                    grid[new_x][new_y] != 1 and
                    (new_x, new_y) not in closed_set
            ):
                neighbor = Node(new_x, new_y, parent=current)
                neighbor.g = current.g + 1
                neighbor.h = abs(neighbor.x - goal_node.x) + abs(neighbor.y - goal_node.y)
                neighbor.f = neighbor.g + neighbor.h

                for _, node in open_list:
                    if node.x == neighbor.x and node.y == neighbor.y and node.f < neighbor.f:
                        break
                else:
                    heapq.heappush(open_list, (neighbor.f, neighbor))

    return None


def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print("S", end=" ")  # Start
            elif (i, j) == goal:
                print("G", end=" ")  # Goal
            elif (i, j) in path:
                print("*", end=" ")  # Path
            elif grid[i][j] == 1:
                print("#", end=" ")  # Obstacle
            else:
                print(".", end=" ")  # Empty cell
        print()


if __name__ == "__main__":
    # Input grid dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Create an empty grid with zeros
    grid = [[0] * cols for _ in range(rows)]

    # Input obstacle positions
    while True:
        obstacle_input = input("Enter obstacle positions (row col) or press Enter to finish: ")
        if not obstacle_input:
            break
        obstacle_row, obstacle_col = map(int, obstacle_input.split())
        grid[obstacle_row][obstacle_col] = 1

    # Input start and goal positions
    start = tuple(map(int, input("Enter the start position (row col): ").split()))
    goal = tuple(map(int, input("Enter the goal position (row col): ").split()))

    path = astar(grid, start, goal)

    if path:
        print("Path found:")
        print_grid(grid, path, start, goal)  # Pass start and goal to the print_grid function
    else:
        print("No path found.")


# Enter the number of rows: 5
# Enter the number of columns: 5

# Enter obstacle positions (row col) or press Enter to finish:
# 2 2
# 2 3
# 3 2
# 3 3
# 3 4

# Enter the start position (row col): 0 0
# Enter the goal position (row col): 4 4



# S . . . . 
# . # # . . 
# . # # * * 
# . . . * G 
# . . . . . 

#  A* has a time complexity of O(b^d), where b is the branching factor (maximum number of successors for each node) and d is the depth of the solution










