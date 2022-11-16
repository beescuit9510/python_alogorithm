from binary_tree import Node


def breadth_first_values(root: Node) -> [int]:
    if root is None:
        return []

    result = []

    queue = [root]

    while queue:

        node = queue.pop(0)

        result.append(node.val)

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)

    return result


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

# notice that there is no such a recursive way to implement the BFS
# since recursion uses stack

print(breadth_first_values(a))

