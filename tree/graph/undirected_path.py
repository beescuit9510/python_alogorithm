def has_path_bfs(edges, src_node, dst_node):
    graph = build_graph(edges)

    queue = [src_node]
    visited_node = []

    while queue:
        current_node = queue.pop(0)
        visited_node.append(current_node)

        if current_node == dst_node:
            return True

        for node in graph[current_node]:
            if node not in visited_node:
                queue.append(node)

    return False


def has_path_dfs(edges, src_node, dst_node):
    graph = build_graph(edges)

    stack = [src_node]
    visited_node = []

    while stack:
        current_node = stack.pop()
        visited_node.append(current_node)

        if current_node == dst_node:
            return True

        for node in graph[current_node]:
            if node not in visited_node:
                stack.append(node)

    return False


def has_path_recursive_dfs(edges, src_node, dst_node, visited_nodes):
    graph = build_graph(edges)

    if src_node in visited_nodes:
        return False

    if src_node == dst_node:
        return True

    visited_nodes.append(src_node)

    for node in graph[src_node]:
        if has_path_recursive_dfs(edges, node, node, visited_nodes):
            return True

    return False


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
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

print(build_graph(edges))
print(has_path_bfs(edges, "i", "o"))
print(has_path_dfs(edges, "i", "l"))
print(has_path_recursive_dfs(edges, "i", "l", []))
