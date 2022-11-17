def has_path_bfs(graph, source, target):
    queue = [source]

    while queue:
        current_node = queue.pop(0)

        if current_node == target:
            return True

        for node in graph[current_node]:
            queue.append(node)

    return False


def has_path_dfs(graph, source, target):
    stack = [source]

    while stack:
        current_node = stack.pop()

        if current_node == target:
            return True

        for node in graph[current_node]:
            stack.append(node)

    return False


def has_path_recursive_dfs(graph, source, target):
    if source == target:
        return True

    for node in graph[source]:
        if has_path_recursive_dfs(graph, node, target):
            return True

    return False


graph = {
    "f": ["g", "i"],
    "g": ["h"],
    "i": ["k", "g"],
    "j": ["i"],
    "k": [],
    "h": []
}

print(has_path_bfs(graph, "f", "k"))
print(has_path_dfs(graph, "f", "k"))
print(has_path_recursive_dfs(graph, "f", "k"))
