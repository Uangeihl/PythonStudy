from codecs import latin_1_decode
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # res = ListNode()
        # while not list1 or not list2:
        #     if list1.val <= list2.val:
        #         res.next = list1
        #         list1 = list1.next
        #     else:
        #         res.next = list2
        #         list1 = list2.next
        # if list1 is None:
        #     res.next = list2
        # else:
        #     res.next = list1
        # return res
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
