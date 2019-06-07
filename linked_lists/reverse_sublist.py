from list_node import ListNode
from linked_list import insert_after, print_linked_list


def reverse_sublist(lst, start, finish):
    dummy_head = sublist_head = ListNode(0, lst)  # dummy_head and sublist_head start as 1 node that has lst as next
    for _ in range(1, start):
        sublist_head = sublist_head.next  # and then sublist_head advances
    '''
    Reversing the sublist works as follows:
    - Keep an iterator at the beginning of the sublist
    - The node that follows iterator is always the one to move to the head of the sublist
    Example: lst = 1 -> 2 -> 3 -> 4 -> 5 -> 6, reverse_sublist(lst, 2, 5) => reverse 2, 3, 4, 5
             Step 1:  head = 1, iterator = 2, temp = iterator.next = 3
             Step 2:  move temp = 3 to the head of the sublist
             2.next = 3.next (2 followed by 4), 3.next = head.next = 2 (3 followed by 2), head.next = temp = 3
             => 3, 2, 4, 5
             Step 3: head = 1, iterator = 2, temp = iterator.next = 4
             move temp = 4 to the head of the sublist
             2.next = 4.next = 5 (2 followed by 5), temp.next = head.next = 3 (4 followed by 3), head.next = temp = 4
             => 4, 3, 2, 5
             Step 4: head = 1, iterator = 2, temp = iterator.next = 5
             move temp = 5 to the head of the sublist...
             => 5, 4, 3, 2
             The node that follows iterator is always the one to move to the head of the sublist
    '''
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy_head.next  # dummy_head.next points to lst


if __name__ == '__main__':
    lst = ListNode(11)

    insert_after(lst, ListNode(3))
    insert_after(lst.next, ListNode(5))
    insert_after(lst.next.next, ListNode(7))
    insert_after(lst.next.next.next, ListNode(2))

    print("Original list: ")
    print_linked_list(lst)
    reverse_sublist(lst, 2, 4)
    print("\nList after reversal: ")
    print_linked_list(lst)
