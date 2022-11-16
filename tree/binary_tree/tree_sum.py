from binary_tree import Node


def tree_sum_bfs(node: Node) -> int:
    if node is None:
        return 0

    queue = [node]

    tree_sum = 0

    while queue:
        current_node = queue.pop(0)
        tree_sum += current_node.val

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

    return tree_sum


def tree_sum_dfs(node: Node) -> int:
    if node is None:
        return 0

    left_sum = tree_sum_dfs(node.left)
    right_sum = tree_sum_dfs(node.right)

    tree_sum = left_sum + node.val + right_sum

    return tree_sum


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

print(tree_sum_bfs(a))
print(tree_sum_dfs(a))
 