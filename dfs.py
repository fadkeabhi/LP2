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

traversal = list()

def dfs(curr_node):
    if curr_node in visited:
        return
    traversal.append(curr_node)
    visited.add(curr_node)
    for next_nodes in graph[curr_node]:
        dfs(next_nodes)

def printTraversal():
    print("DFS Traversal is:")
    for i in traversal:
        print(f"{i} -> ", end="")
    print("stop")

def main():
    dfs('O')
    printTraversal()


main()