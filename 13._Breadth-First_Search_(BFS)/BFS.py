from collections import deque

def bfs(graph, start_node):
    # Initialize a queue and add the starting node
    queue = deque([start_node])
    # Set of visited nodes to avoid processing a node more than once
    visited = set()

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        # Process the node if it hasn't been visited
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Get the graph from the user
user_input = input("Enter the graph as adjacency list (e.g., {'A': ['B', 'C'], 'B': ['A', 'D'], ...}): ")
graph = eval(user_input)

# Get the starting node from the user
start_node = input("Enter the starting node: ")

# Perform BFS
print("Breadth-First Search starting from node", start_node, ":")
bfs(graph, start_node)
