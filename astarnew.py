def createNode(index, gCost, hCost):
    dictionary = dict()
    dictionary["index"] = index
    dictionary["gCost"] = gCost
    dictionary["hCost"] = hCost
    dictionary["fCost"] = hCost + gCost

    return dictionary

def AstarAlgo(graph, heuristic, start, goal):
    n = len(graph)

    open_list = list()
    visited = set()

    # Add the start node to the open list
    open_list.append(createNode(start, 0, heuristic[start]))

    while open_list:
        current = open_list[0]
        open_list.pop(0)

        # Check if the current node is the goal
        if current["index"] == goal:
            return current["gCost"]

        visited.add(current["index"])

        for neighbor, edgeWeight in graph[current["index"]]:
            if neighbor not in visited:
                gCost = current["gCost"] + edgeWeight
                hCost = heuristic[neighbor]
                open_list.append(createNode(neighbor, gCost, hCost))
        
        open_list.sort(key = lambda x: x["fCost"])
    return -1


graph = [
    [(1, 7), (2, 9), (5, 14)],  # Node 0
    [(0, 7), (2, 10), (3, 15)],  # Node 1
    [(0, 9), (1, 10), (5, 2)],  # Node 2
    [(1, 15), (3, 11), (5, 9)],  # Node 3
    [(3, 6), (5, 9)],  # Node 4
    [(0, 14), (2, 2), (3, 9), (4, 9)]  # Node 5
]
heuristic = [11, 10, 6, 0, 0, 0]  # Heuristic values for each node

start = 0
goal = 4

shortest_path_cost = AstarAlgo(graph, heuristic, start, goal)

if shortest_path_cost == -1:
    print(f"No path found from node {start} to node {goal}")
else:
    print(f"Shortest path cost from node {start} to node {goal} is: {shortest_path_cost}")
