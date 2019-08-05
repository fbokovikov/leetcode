from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res, index = "", 0
        while True:
            if len(strs[0]) == index:
                return res
            else:
                cur_char = strs[0][index]
            for str in strs:
                if len(str) == index or str[index] != cur_char:
                    return res
            res += cur_char
            index += 1
        return res

    def isValid(self, s: str) -> bool:
        if not str:
            return False
        opening_pairs = {"{": "}", "[": "]", "(": ")"}
        bracket_stack = []
        for bracket in s:
            if bracket in opening_pairs:
                bracket_stack.append(bracket)
            else:
                if not bracket_stack:
                    return False
                if opening_pairs[bracket_stack.pop()] != bracket:
                    return False
        if bracket_stack:
            return False
        return True

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



def main():
    s = input()
    print(Solution().isValid(s))


if __name__ == "__main__":
    main()
