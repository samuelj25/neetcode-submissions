# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # slow now points at the middle of the linked list
        # we have to reverse the second half of the list
        
        prev, curr = None, slow.next
        slow.next = None

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev now should point to the end of the original list
        # which is now the start of the second half of the list reversed

        curr, rev = head, prev

        while (rev):
            t1, t2 = curr.next, rev.next
            curr.next = rev
            rev.next = t1
            curr, rev = t1, t2
