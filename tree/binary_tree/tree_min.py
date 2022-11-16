from binary_tree import Node


def tree_min_bfs(node: Node) -> int:
    if node is None:
        return None

    queue = [node]
    tree_min = float('inf')

    while queue:
        current_node = queue.pop(0)

        if tree_min > current_node.val:
            tree_min = current_node.val

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return tree_min


def tree_min_dfs(node: Node) -> int:
    if node is None:
        return float('inf')

    tree_min = node.val

    left = tree_min_dfs(node.left)
    right = tree_min_dfs(node.right)

    if tree_min > left:
        tree_min = left

    if tree_min > right:
        tree_min = right

    return tree_min


a = Node(11)
b = Node(23)
c = Node(12)
d = Node(5)
e = Node(19)
f = Node(43)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(tree_min_bfs(a))
print(tree_min_dfs(a))
 