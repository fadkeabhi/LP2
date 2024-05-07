import heapq

# Structure to represent a node in the graph
class Node:
    def __init__(self, index, g_cost, h_cost):
        self.index = index  # Index of the node
        self.g_cost = g_cost  # Cost from start node to this node
        self.h_cost = h_cost  # Heuristic cost (estimated cost from this node to goal node)
        self.f_cost = g_cost + h_cost  # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.f_cost < other.f_cost

# A* algorithm function
def a_star(graph, heuristic, start, goal):
    n = len(graph)

    # Priority queue to store nodes to be explored, ordered by f_cost
    open_list = []
    heapq.heapify(open_list)

    # List to keep track of visited nodes
    visited = [False] * n

    # Add the start node to the open list
    heapq.heappush(open_list, Node(start, 0, heuristic[start]))

    while open_list:
        # Get the node with the lowest f_cost from the open list
        current = heapq.heappop(open_list)

        # Check if the current node is the goal
        if current.index == goal:
            return current.g_cost

        # Mark current node as visited
        visited[current.index] = True

        # Expand current node
        for neighbor, edge_weight in graph[current.index]:
            # Check if neighbor is not visited
            if not visited[neighbor]:
                g_cost = current.g_cost + edge_weight
                h_cost = heuristic[neighbor]
                f_cost = g_cost + h_cost

                # Add neighbor to open list
                heapq.heappush(open_list, Node(neighbor, g_cost, h_cost))

    # If goal node is not reachable
    return -1

# Constants for inputs
n = 6  # Number of nodes
graph = [
    [(1, 7), (2, 9), (5, 14)],  # Node 0
    [(0, 7), (2, 10), (3, 15)],  # Node 1
    [(0, 9), (1, 10), (5, 2)],  # Node 2
    [(1, 15), (3, 11), (5, 9)],  # Node 3
    [(3, 6), (5, 9)],  # Node 4
    [(0, 14), (2, 2), (3, 9), (4, 9)]  # Node 5
]
heuristic = [11, 10, 6, 0, 0, 0]  # Heuristic values for each node
start = 0  # Start node
goal = 4  # Goal node

# Find shortest path cost
shortest_path_cost = a_star(graph, heuristic, start, goal)

if shortest_path_cost == -1:
    print(f"No path found from node {start} to node {goal}")
else:
    print(f"Shortest path cost from node {start} to node {goal} is: {shortest_path_cost}")
