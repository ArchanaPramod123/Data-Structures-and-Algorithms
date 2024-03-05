import collections

def insert(v):
    if v in graph:
        print(v, " already present")
    else:
        graph[v] = []

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, " not present")
    elif v2 not in graph:
        print(v2, " not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def BFS(node, graph):
    visited = set()
    traversal_order = []  # To store the order of traversal

    if node not in graph:
        print(f"{node} not found in the graph!")
        return

    queue = collections.deque([node])
    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)
            traversal_order.append(current)

            for neighbor in sorted(graph[current]):
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

graph = {}
insert("A")
insert("B")
insert("C")
insert("D")
insert("E")
add_edge("A", "B")
add_edge("A", "C")
add_edge("B", "E")
add_edge("C", "D")
add_edge("D", "E")

print(graph)
bfs_order = BFS("A", graph)
print("BFS Traversal Order:", bfs_order)
