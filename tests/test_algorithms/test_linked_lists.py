from algorithms import removeNthFromEnd
from algorithms import mergeKLists
from algorithms import ListNode
from tests import stopwatch


def test_remove_nth_from_end_base_case():
    linkedListInput = ListNode.list_to_linked_list([1,  2,  3,  4,  5])
    answer = ListNode.linked_list_to_list(removeNthFromEnd(linkedListInput,  2))
    assert answer == [1,  2,  3,  5]


def test_remove_nth_from_end_edge_case():
    long_list = [x for x in range(99)]
    long_linked_list = ListNode.list_to_linked_list(long_list)
    assert stopwatch(removeNthFromEnd,  [long_linked_list,  17]) < .1


def test_merge_k_lists_base_case():
    inputLists = [[1, 4, 5],  [1, 3, 4],  [2, 6]]
    list_to_linked_list = ListNode.list_to_linked_list
    inputLists = [list_to_linked_list(linkedList) for linkedList in inputLists]
    answer = ListNode.linked_list_to_list(mergeKLists(inputLists))
    assert answer == [1, 1, 2, 3, 4, 4, 5, 6]
