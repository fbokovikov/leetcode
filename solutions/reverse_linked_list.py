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
    def reverse_recursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head;
        new_head = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head;

    def reverse_3_ptr(self, head: ListNode) -> ListNode:
        next_node, cur_node, prev_node = head, head, None
        while next_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        def length(head: ListNode) -> int:
            if head is None:
                return 0
            else:
                return 1 + length(head.next)

        if length(head) < k:
            return head
        cur_node, prev_node, next_node = head, None, head
        for _ in range(k):
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        head.next = self.reverse_k_group(cur_node, k)
        return prev_node

    def swap_pairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        second = head.next
        next_node = head.next.next
        head.next.next = head
        head.next = self.swap_pairs(next_node)
        return second

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur, pre_reverse = head, head
        for _ in range(1, m):
            cur = cur.next
        for _ in range(1, m - 1):
            pre_reverse = pre_reverse.next
        post_reverse = cur
        prev_node, next_node = None, None
        for _ in range(0, n - m + 1):
            next_node = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_node

        post_reverse.next = next_node
        if m == 1:
            return prev_node
        pre_reverse.next = prev_node
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur is not None:
            prev = cur
            cur = cur.next
            if cur and cur.val == prev.val:
                while cur and cur.val == prev.val:
                    cur = cur.next
                prev.next = cur
        return head




def init_head() -> ListNode:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head


def main():
    sol = Solution()

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(4)
    print(head)
    print(sol.deleteDuplicates2(head))


if __name__ == "__main__":
    main()
