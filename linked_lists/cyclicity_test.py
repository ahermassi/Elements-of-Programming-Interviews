from list_node import ListNode


def has_cycle(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # There is a cycle.
            # Tries to find the start of the cycle.
            slow = head
            # Both pointers advance at the sane time,
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow  # slow is the start of cycle
    return None  # No cycle.


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node4 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(has_cycle(node1).data)
