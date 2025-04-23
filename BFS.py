import collections

# BFS function
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])  # Initialize
    visited.add(root)  # Mark root as visited

    while queue:
        vertex = queue.popleft()  # Get next node
        print(str(vertex) + " ", end="")  # Print node

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)  # Mark as visited
                queue.append(neighbour)  # Add to queue

# Main block to run BFS
if __name__ == '__main__':
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1, 2]
    }

    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
