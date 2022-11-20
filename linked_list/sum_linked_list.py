from node import Node


def sum_linked_list(head: 'Node') -> int:

    sum = 0
    current = head

    while current:
        sum += current.val
        current = current.next

    return sum


def recursive_sum_linked_list(head: 'Node') -> int:
    if head is None:
        return 0

    return head.val + recursive_sum_linked_list(head.next)


a = Node(1)
b = Node(2)
c = Node(13)
d = Node(9)
e = Node(1)
f = Node(23)
g = Node(50)
h = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h

print(sum_linked_list(a))
print(recursive_sum_linked_list(a))
