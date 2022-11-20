from node import Node


def get_node_value(head: 'Node', index) -> int:
    current = head
    current_index = 0

    while current:
        if current_index == index:
            return current.val

        current = current.next
        current_index += 1

    return None


# def recursive_get_node_value(head: 'Node', target) -> int:
#     current_index = 0
#
#     def helper(head, target, current_index):
#         if head is None:
#             return None
#
#         if current_index == target:
#             return head.val
#
#         current_index += 1
#         return helper(head.next, target, current_index)
#
#     return helper(head, target, current_index)


def recursive_get_node_value(head: 'Node', target) -> int:
    if head is None:
        return None

    if target == 0:
        return head.val

    return recursive_get_node_value(head.next, target - 1)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

print(get_node_value(a, 3))
print(recursive_get_node_value(a, 3))
