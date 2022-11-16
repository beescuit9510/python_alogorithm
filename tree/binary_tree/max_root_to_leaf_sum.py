from binary_tree import Node


def max_path_sum_dfs(node: Node) -> int:
    if node is None:
        return 0

    max_leaf = node.val
    left_leaf_sum = node.val + max_path_sum_dfs(node.left)
    right_leaf_sum = node.val + max_path_sum_dfs(node.right)

    if max_leaf < left_leaf_sum:
        max_leaf = left_leaf_sum

    if max_leaf < right_leaf_sum:
        max_leaf = right_leaf_sum

    return max_leaf


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

print(max_path_sum_dfs(a))
