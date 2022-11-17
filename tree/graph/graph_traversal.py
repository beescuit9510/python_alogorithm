def breadth_first_traversal(graph, source):
    stack = [source]

    while stack:
        current_node = stack.pop(0)
        print(current_node)

        for node in graph[current_node]:
            stack.append(node)


def depth_first_traversal(graph, source):
    stack = [source]

    while stack:
        current_node = stack.pop()
        print(current_node)

        for node in graph[current_node]:
            stack.append(node)


def recursive_depth_first_traversal(graph, source):
    print(source)

    for node in graph[source]:
        recursive_depth_first_traversal(graph, node)


graph = {
    "a": ["c", "b"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

breadth_first_traversal(graph, "a")
print("---------------------------")
depth_first_traversal(graph, "a")
print("---------------------------")
recursive_depth_first_traversal(graph, "a")
