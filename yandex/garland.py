import sys
from collections import deque

def find_tree_center(n, adj):
    """Find the center of the tree using leaf peeling (BFS)."""
    if n == 1:
        return 1  # Only one node, it must be the answer
    
    # Step 1: Find all leaves (nodes with only one connection)
    degree = [0] * (n + 1)  # Count of edges for each node
    leaves = deque()

    for node in range(1, n + 1):
        degree[node] = len(adj[node])  # Count neighbors
        if degree[node] == 1:  # It's a leaf
            leaves.append(node)

    # Step 2: Iteratively remove leaves until only 1 or 2 nodes remain
    remaining_nodes = n
    while remaining_nodes > 2:
        leaf_count = len(leaves)
        remaining_nodes -= leaf_count  # Remove current layer of leaves
        
        for _ in range(leaf_count):
            leaf = leaves.popleft()
            for neighbor, _ in adj[leaf]:  # Find the only neighbor
                degree[neighbor] -= 1  # Reduce its edge count
                if degree[neighbor] == 1:  # If it becomes a leaf, add to queue
                    leaves.append(neighbor)
    
    # Step 3: Return the last remaining node(s)
    return leaves[0]  # The remaining node is the optimal power source

# Read input
n = int(sys.stdin.readline().strip())
adj = [[] for _ in range(n + 1)]  # Adjacency list

for _ in range(n - 1):
    a, b, t = map(int, sys.stdin.readline().split())
    adj[a].append((b, t))
    adj[b].append((a, t))

# Find and print the optimal lamp node
result = find_tree_center(n, adj)
print(result)
