from algorithms import removeNthFromEnd
from algorithms import ListNode
from tests import stopwatch


def test_remove_nth_from_end_base_case():
    # this is actually not testable given the leetcode format (returns head)
    # TODO write another algorithm (easy enough) that converts LL to just list
    linkedListInput = ListNode.list_to_linked_list([1, 2, 3, 4, 5])
    answer = ListNode.linked_list_to_list(removeNthFromEnd(linkedListInput, 2))
    assert answer == [1, 2, 3, 5]


def test_remove_nth_from_end_edge_case():
    long_list = [x for x in range(99)]
    long_linked_list = ListNode.list_to_linked_list(long_list)
    # same TODO as above, need list to LL as well
    assert stopwatch(removeNthFromEnd, [long_linked_list, 17]) < .1
