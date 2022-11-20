from node import Node


def linked_list_find(head: 'Node', target) -> bool:

    current = head

    while current:
        if current.val == target:
            return True

        current = current.next

    return False


def recursive_linked_list_find(head: 'Node', target) -> bool:
    if head is None:
        return False

    if head.val == target:
        return True

    return recursive_linked_list_find(head.next, target)


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

print(linked_list_find(a, "f"))
print(recursive_linked_list_find(a, "f"))
