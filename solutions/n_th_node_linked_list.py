class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self) -> str:
        res = ""
        while self.next is not None:
            res += str(self.val) + "->"
            self = self.next
        res += str(self.val)
        return res


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        list_length = self._length(head)
        if head is None or n > list_length:
            return head
        if n == list_length:
            return head.next
        current = head
        for _ in range(list_length - n - 1):
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        return head

    def _length(self, head: ListNode) -> int:
        if head is None:
            return 0
        else:
            return 1 + self._length(head.next)


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print(Solution().removeNthFromEnd(head, 5))
    print(Solution().removeNthFromEnd(head, 5))
    print(Solution().removeNthFromEnd(ListNode(1), 1))


if __name__ == "__main__":
    main()
