graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'I'],
    'E': ['B', 'J'],
    'F': ['B', 'K'],
    'G': ['C', 'L'],
    'H': ['C', 'M'],
    'I': ['D', 'N', 'O'],
    'J': ['E'],
    'K': ['F'],
    'L': ['G'],
    'M': ['H'],
    'N': ['I'],
    'O': ['I']
}

visited = set()
queue = list()
traversal = list()

def bfs(curr_node):
    if curr_node not in visited:
        traversal.append(curr_node)
        visited.add(curr_node)
        for next_node in graph[curr_node]:
            queue.append(next_node)
            
    if len(queue) != 0:
        next_node = queue[0]
        queue.pop(0)
        bfs(next_node)

def printTraversal():
    print("BFS Traversal is:")
    for i in traversal:
        print(f"{i} -> ", end="")
    print("stop")

def main():
    bfs('A')
    printTraversal()


main()