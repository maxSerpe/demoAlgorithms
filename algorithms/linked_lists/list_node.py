# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def linked_list_to_list(head_node):
        list_output = [head_node.val]
        current = head_node
        while(current.next):
            current = current.next
            list_output.append(current.val)
        return list_output

    def list_to_linked_list(list_input):
        head = ListNode()
        current = head
        current.val = list_input[0]
        for val in list_input[1:]:
            current.next = ListNode()
            current = current.next
            current.val = val

        return head
