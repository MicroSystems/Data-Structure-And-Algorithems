### Depth-First Search (DFS) Algorithm

The **Depth-First Search (DFS)** is a graph traversal algorithm used to explore nodes and edges of a graph. It starts at a given node and explores as far as possible along each branch before backtracking. It is commonly used for searching tree or graph data structures.

### How DFS Works

- DFS starts at a root node and explores each branch as deeply as possible before moving to the next branch.
- It uses a stack (either explicitly or via recursion) to keep track of the path and backtracks once a node has no unvisited neighbors.

### Steps in DFS

1. **Start at a node** (usually the root).
2. **Mark the node as visited**.
3. **Recursively visit all unvisited neighbors** of the current node.
4. **Backtrack** to previous nodes when no unvisited neighbors are left.
5. Continue until all nodes are visited or the search is complete.

### Example Graph

Consider the following graph represented as an adjacency list:

```
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

```

This graph can be visualized as:

```
    A
   / \\
  B   C
 / \\   \\
D   E   F

```

### Recursive DFS Example in Python

```python
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set on the first call

    # Mark the current node as visited
    visited.add(start_node)
    print(start_node, end=" ")  # Process the current node (e.g., printing)

    # Recur for all the neighbors of the current node
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run DFS starting from node 'A'
dfs(graph, 'A')

```

### Output

```
A B D E C F

```

### Explanation:

1. Starting at `A`, DFS visits `B`, then `D`, and backtracks to visit `E`. After exhausting all neighbors of `B`, it moves to `C` and then `F`.
2. DFS explores as deep as possible before backtracking.

### DFS Using Stack (Iterative Approach)

Instead of recursion, we can implement DFS using an explicit stack.

```python
def dfs_iterative(graph, start_node):
    # Create a stack for DFS and initialize with the start_node
    stack = [start_node]

    # Set to keep track of visited nodes
    visited = set()

    # While there are nodes to explore
    while stack:
        # Pop the last node from the stack
        current_node = stack.pop()

        # If the node hasn't been visited
        if current_node not in visited:
            print(current_node, end=" ")  # Process the current node (printing it here)
            visited.add(current_node)

            # Add all unvisited neighbors to the stack
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Run DFS iteratively starting from node 'A'
dfs_iterative(graph, 'A')

```

### Output

```
A C F B E D

```

### Time and Space Complexity:

- **Time Complexity**: O(V + E), where `V` is the number of vertices and `E` is the number of edges. DFS explores every vertex and edge once.
- **Space Complexity**: O(V) for the recursion stack or explicit stack, and O(V) for the visited set.

### Applications of DFS:

- **Pathfinding**: Used to find a path between two nodes in a graph.
- **Topological Sorting**: DFS can be used to perform topological sorting in a directed acyclic graph (DAG).
- **Cycle Detection**: DFS helps detect cycles in both directed and undirected graphs.
- **Connected Components**: DFS can find all connected components in a graph.
- **Maze Solving**: DFS is used to explore all possible paths in a maze, often combined with backtracking.

Let me know if you need more details or examples for a specific application of DFS!

**DFS in Python (using recursion):**

```python
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set on first call

    # Mark the current node as visited
    visited.add(start_node)
    print(start_node, end=" ")  # Process the current node (printing it here)

    # Recur for all the neighbors of the current node
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

# Run DFS starting from node 'A'
dfs(graph, 'A')

```

### Output:

```
A B D E C F

```

### Explanation:

1. **Graph Representation**: Like BFS, we represent the graph as an adjacency list. Each key in the `graph` dictionary corresponds to a node, and its value is a list of its neighboring nodes.
2. **Recursion**: The DFS function is recursive:
    - It starts at the `start_node`, marks it as visited, and processes it (in this case, it prints the node).
    - It then recursively explores each unvisited neighbor by calling itself (`dfs`) for each neighbor.
3. **Visited Set**: A `visited` set is passed as a parameter to keep track of nodes that have already been visited, preventing infinite loops (cycles).
4. **Traversal Process**:
    - Starting at node `A`, it explores as far as possible along each branch before backtracking (this is the key feature of DFS).
    - The order of traversal might vary depending on how the neighbors are ordered in the adjacency list.

### DFS using an Explicit Stack (Iterative)

Here’s an **iterative** version using an explicit stack instead of recursion:

```python
def dfs_iterative(graph, start_node):
    # Create a stack for DFS and initialize with the start_node
    stack = [start_node]

    # Set to keep track of visited nodes
    visited = set()

    # While there are nodes to explore
    while stack:
        # Pop the last node from the stack
        current_node = stack.pop()

        # If the node hasn't been visited
        if current_node not in visited:
            print(current_node, end=" ")  # Process the current node (printing it here)
            visited.add(current_node)

            # Add all unvisited neighbors to the stack
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Run DFS iteratively starting from node 'A'
dfs_iterative(graph, 'A')

```

### Output:

```
A C F B E D

```

### Explanation of the Iterative Version:

1. **Stack**: DFS is typically implemented using recursion (which implicitly uses a stack), but here we explicitly use a list as a stack to avoid recursion.
2. **Traversal Process**:
    - Start by pushing the `start_node` onto the stack.
    - Pop the top node from the stack, process it, and push its unvisited neighbors onto the stack.
    - Continue this process until the stack is empty.

Both approaches (recursive and iterative) implement the same DFS algorithm but differ in how they handle the function calls.

Let me know if you'd like further clarification or modifications!