def connected_component_dfs(graph):
    component_count = 0
    visited_node = []

    for node in graph.keys():

        if node in visited_node:
            continue

        component_count += 1

        stack = [node]

        while stack:
            current_node = stack.pop()
            visited_node.append(current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited_node:
                    stack.append(neighbor)

    return component_count


def connected_component_recursive_dfs(graph):
    component_count = 0
    visited_node = []

    for node in graph.keys():
        component_count += explore(graph, node, visited_node)

    return component_count


def explore(graph, src, visited_node):
    if src in visited_node:
        return 0

    visited_node.append(src)

    for neighbor in graph[src]:
        explore(graph, neighbor, visited_node)

    return 1


graph = {
    '3': [],
    '4': ['6'],
    '6': ['4', '5', '7', '8'],
    '8': ['6'],
    '7': ['6'],
    '5': ['6'],
    '1': ['2'],
    '2': ['1'],

}

print(connected_component_dfs(graph))
print(connected_component_recursive_dfs(graph))
