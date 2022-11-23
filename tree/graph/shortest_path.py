def shortest_path(edges, start, dest):
    if start == dest:
        return 0

    graph = build_graph(edges)
    queue = [[start, 0]]
    visited = set()

    while queue:
        [current, depth] = queue.pop(0)
        visited.add(current)

        if current == dest:
            return depth

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append([neighbor, depth + 1])


def build_graph(edges):
    graph = {}

    for pair in edges:
        node_a = pair[0]
        node_b = pair[1]

        if graph.get(node_a) is None:
            graph[node_a] = []
        if graph.get(node_b) is None:
            graph[node_b] = []

        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph


edges = [
    ['w', 'x'],
    # ['a', 'y'],
    # ['a', 'f'],
    # ['d', 'f'],
    # ['d', 'v'],
    ['x', 'd'],
    ['d', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],
]
print(build_graph(edges))
print(shortest_path(edges, "w", "y"))
