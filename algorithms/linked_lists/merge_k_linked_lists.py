from .list_node import ListNode


def mergeKLists(lists: [ListNode]) -> ListNode:
    allListValues = []
    for linList in lists:
        if(linList):
            allListValues.append(linList.val)
            while(linList.next):
                linList = linList.next
                allListValues.append(linList.val)
    if(not allListValues):
        return ListNode(val='')
    allListValues.sort()
    head = ListNode()
    current = head
    current.val = allListValues[0]
    for value in allListValues[1:]:
        current.next = ListNode()
        current = current.next
        current.val = value
    return head
