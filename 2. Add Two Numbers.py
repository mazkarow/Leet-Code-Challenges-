class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p, q, current = l1, l2, dummy
        carry = 0
        while p is not None or q is not None:
            sum = carry
            if p is not None:
                sum += p.val
                p = p.next
            if q is not None:
                sum += q.val
                q = q.next

            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next