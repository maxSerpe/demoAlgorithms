from .list_node import ListNode


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # edge cases: n 0, list is length one, combination of those two
    # last node of list
    # n beyond length of list...maybe not valid?
    if(n == 0):
        return head
    nodes_list = []
    current_node = head
    while(current_node.next):
        nodes_list.append(current_node)
        current_node = current_node.next
    nodes_list.append(current_node)

    if(n == 1):
        if(len(nodes_list) == 1):
            return None
        before = nodes_list[len(nodes_list)-1-1]
        before.next = None

    elif(n == len(nodes_list)):
        head.next = None
        return nodes_list[1]
    else:
        before = nodes_list[len(nodes_list)-1-n]
        after = nodes_list[(len(nodes_list)-1-n+2)]
        before.next = after
    return head
