# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = ""
        buf = self
        while buf is not None:
            res += str(buf.val)
            buf = buf.next
            res += "->" if buf is not None else ""
        return res


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        return Solution._add_two_numbers(l1, l2, 0)

    @staticmethod
    def _add_two_numbers(l1: ListNode, l2: ListNode, offset: int) -> ListNode:
        if l1 is None and l2 is None and offset == 0:
            return None

        l1_value = l1.val if l1 is not None else 0
        l2_value = l2.val if l2 is not None else 0

        res_offset = (l1_value + l2_value + offset) // 10
        res_value = (l1_value + l2_value + offset) % 10

        cur_node = ListNode(res_value)
        cur_node.next = Solution._add_two_numbers(
            None if l1 is None else l1.next,
            None if l2 is None else l2.next,
            res_offset
        )

        return cur_node


def main():
    l1 = ListNode(5)

    l2 = ListNode(5)

    res = Solution.add_two_numbers(l1, l2)

    print(res)


if __name__ == '__main__':
    main()
