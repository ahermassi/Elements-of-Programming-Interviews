def search_list(lst, key):
    """
    Search the linked list for a given value
    :param lst: list to search
    :param key: value to look up
    :return: node that holds the sought key
    """
    while lst and lst.data != key:
        lst = lst.next
    return lst  # if list is null or key not found, None is returned


def insert_after(node, new_node):
    """
    Insert a new node after a specified node
    """
    new_node.next = node.next
    node.next = new_node


def deleter_after(node):
    """
    Delete the node past this one. Assume node is not a tail
    """
    node.next = node.next.next


def print_linked_list(lst):
    while lst:
        print(lst.data, end=' ')
        lst = lst.next
