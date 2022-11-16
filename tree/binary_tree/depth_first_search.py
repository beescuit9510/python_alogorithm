from binary_tree import Node


def depth_first_values(root: Node) -> [int]:
    if root is None:
        return []

    result = []

    stack = [root]

    while stack:

        node = stack.pop()

        result.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

    return result


def recursive_depth_first_values(node: Node) -> [int]:
    if node is None:
        return []

    return [node.val] + recursive_depth_first_values(node.left) + recursive_depth_first_values(node.right)


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

print(depth_first_values(a))
print(recursive_depth_first_values(a))