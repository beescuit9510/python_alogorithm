def largest_component_dfs(graph):
    largest_component = 0
    visited_node = []

    for node in graph.keys():

        if node in visited_node:
            continue

        stack = [node]

        connected_components = []

        while stack:

            current_node = stack.pop()

            connected_components.append(current_node)

            visited_node.append(current_node)

            for neighbor in graph[current_node]:

                if neighbor in visited_node or neighbor in stack:
                    continue

                stack.append(neighbor)

        if len(set(connected_components)) > largest_component:
            largest_component = len(set(connected_components))

    return largest_component


def largest_component_recursive_dfs(graph) -> int:
    largest_component = 0
    visited_node = []

    for node in graph.keys():

        component = len(explore(graph, node, visited_node))

        if component > largest_component:
            largest_component = component

    return largest_component


def explore(graph, src, visited_node) -> int:
    if src in visited_node:
        return set()

    visited_node.append(src)

    component_size = set([src])

    for neighbor in graph[src]:
        component_size.update(explore(graph, neighbor, visited_node))

    return component_size


graph = {
    "0": ["8", "1", "5"],
    "1": ["0"],
    "5": ["0", "8", "9", "99"],
    "8": ["0", "5"],
    "2": ["3", "4"],
    "3": ["2", "4"],
    "4": ["3", "2"],
    "9": [],
    "99": [],
}

print(largest_component_dfs(graph))
print(largest_component_recursive_dfs(graph))