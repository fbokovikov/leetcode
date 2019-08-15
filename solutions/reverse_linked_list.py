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


def init_head() -> ListNode:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    return head


def main():
    sol = Solution()

    head = init_head()

    print(head)
    print(sol.reverse_k_group(head, 3))

    head = init_head()
    print(head)
    print(sol.swap_pairs(head))


if __name__ == "__main__":
    main()
