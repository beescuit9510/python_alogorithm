from binary_tree import Node


def tree_includes_bfs(node: Node, target: Node) -> bool:
    if node is None:
        return False

    queue = [node]

    while queue:
        current_node = queue.pop(0)

        if current_node.val == target.val:
            return True

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return False


# def tree_includes_dfs(node: Node, target: Node) -> bool:
#     if node is None:
#         return False
#
#     if node.val == target.val:
#         return True
#
#     if tree_includes_dfs(node.left, target) is True:
#         return True
#
#     if tree_includes_dfs(node.right, target) is True:
#         return True
#
#     return False

def tree_includes_dfs(node: Node, target: Node) -> bool:
    if node is None:
        return False

    if node.val == target.val:
        return True

    return tree_includes_dfs(node.left, target) or tree_includes_dfs(node.right, target)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_includes_bfs(a, f))
print(tree_includes_dfs(a, d))
