from list_node import ListNode
from linked_list import insert_after


def merge_two_sorted_lists(lst1, lst2):
    """
    The worst-case corresponds to the case when the lists are of comparable length, so the time complexity is O(n + m).
    In the best-case, one list is much shorter than the other and all its entries appear at the beginning of
    the merged list.
    Since we reuse the existing nodes, the space complexity is O(1)
    """

    dummy_head = tail = ListNode()  # head and tail start pointing to the same dummy node, then tail converges
    while lst1 and lst2:
        if lst1.data < lst2.data:
            tail.next = lst1  # the FIRST tail.next node is where the actual merge begins
            lst1 = lst1.next
        else:
            tail.next = lst2
            lst2 = lst2.next
        tail = tail.next
    # append the remaining nodes of list 1 or list 2
    tail.next = lst1 or lst2  # when one list becomes None, the 'or' returns the remaining nodes of the other
    return dummy_head.next  # dummy_head.next is the node appended with the FIRST tail.next statement


if __name__ == '__main__':
    lst1 = ListNode(2)
    lst2 = ListNode(3)

    insert_after(lst1, ListNode(5))
    insert_after(lst1.next, ListNode(7))

    insert_after(lst2, ListNode(11))

    res = merge_two_sorted_lists(lst1, lst2)
    print(res.data)

