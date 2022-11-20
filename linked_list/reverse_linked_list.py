from linked_list.convert_linked_list_to_array import linked_list_to_array
from node import Node


def get_node_value(head: 'Node') -> Node:
    previous = None
    current = head

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def recursive_get_node_value(head: 'Node', prev=None) -> Node:
    if head is None:
        return prev

    next = head.next
    head.next = prev

    return recursive_get_node_value(next, head)


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

print(linked_list_to_array(a))
print(linked_list_to_array(get_node_value(a)))

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H

print(linked_list_to_array(recursive_get_node_value(A)))
