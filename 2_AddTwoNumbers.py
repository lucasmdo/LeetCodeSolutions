# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        curr = result
        p = l1
        q = l2
        carry = 0

        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0

            sum = carry + x + y
            carry = int(sum / 10)
            curr.next = ListNode(sum % 10)

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return result.next
