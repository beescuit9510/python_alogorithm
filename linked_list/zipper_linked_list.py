from linked_list.convert_linked_list_to_array import linked_list_to_array
from node import Node


def zipper_lists(head_a: 'Node', head_b: 'Node') -> Node:
    current = head_a
    next = head_b
    flagged = False

    while current:

        if not current.next:
            flagged = True

        temp = current.next
        current.next = next
        current = next
        next = temp

        if flagged:
            return head_a

    return head_a


def zipper_lists_with_two_pointers(head_a: 'Node', head_b: 'Node') -> Node:
    current_a = head_a
    current_b = head_b
    flip = False

    while current_a and current_b:
        if not flip:
            temp = current_a.next
            current_a.next = current_b
            current_a = temp
        else:
            temp = current_b.next
            current_b.next = current_a
            current_b = temp

        flip = not flip

    return head_a


def recursive_zipper_lists(head_a: 'Node', head_b: 'Node') -> Node:
    if head_a is None and head_b is None:
        return None

    if head_a is None:
        return head_b

    if head_b is None:
        return head_a

    next_head_a = head_a.next
    next_head_b = head_b.next

    head_a.next = head_b

    head_b.next = recursive_zipper_lists(next_head_a, next_head_b)

    return head_a


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

print(linked_list_to_array(a))
print(linked_list_to_array(recursive_zipper_lists(a, A)))
