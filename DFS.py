# Depth-First Search using recursion
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to track visited nodes

    visited.add(start)  # Mark current as visited
    print(start)  # Print current node

    # Visit unvisited neighbors
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

    return visited  # Return all visited nodes

# Sample graph (undirected)
graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}

# Run DFS from node '0'
visited_nodes = dfs(graph, '0')
print("\nVisited nodes:", visited_nodes)
