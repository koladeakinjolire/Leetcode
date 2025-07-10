def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Create dummy node to simplify merging
    dummy = ListNode(0)
    current = dummy

    # Traverse both lists while they have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1  # Fixed: assign list1 node, not list2.val
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes from list1 or list2
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next