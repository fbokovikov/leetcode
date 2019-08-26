from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pass

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if l1 and not l2:
            res = ListNode(l1.val)
            l1 = l1.next
        elif not l1 and l2:
            res = ListNode(l2.val)
            l2 = l2.next
        else:
            res = ListNode(min(l1.val, l2.val))
            if l1.val <= l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        cur_node = res
        while l1 or l2:
            if l1 and not l2:
                cur_node.next = ListNode(l1.val)
                l1 = l1.next
            elif l2 and not l1:
                cur_node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur_node.next = ListNode(min(l1.val, l2.val))
                if l1.val <= l2.val:
                    l1 = l1.next
                else:
                    l2 = l2.next
            cur_node = cur_node.next
        return res