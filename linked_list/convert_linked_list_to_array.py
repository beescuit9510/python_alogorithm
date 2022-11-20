from node import Node


def linked_list_to_array(head: 'Node') -> [int]:
    converted = []

    current = head

    while current:
        converted.append(current.val) 
        current = current.next

    return converted


def recursive_linked_list_to_array(head: 'Node') -> [int]:
    if head is None:
        return []

    return [head.val] + linked_list_to_array(head.next)


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
