class Node:
    def __init__(self, val, next: 'Node' = None):
        self.val = val
        self.next = next


def print_linked_list(head: 'Node'):
    current = head

    while current:
        print(current.val)
        current = current.next


def recursive_print_linked_list(head: 'Node'):

    if head is None:
        return

    print(head.val)
    recursive_print_linked_list(head.next)


# def recursive_print_linked_list(head: 'Node'):
#     print(head.val)
#
#     if head.next:
#         recursive_print_linked_list(head.next)


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

recursive_print_linked_list(a)
