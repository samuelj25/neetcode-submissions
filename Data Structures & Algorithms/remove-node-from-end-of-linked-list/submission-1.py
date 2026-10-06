# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointer
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while (n):
            right = right.next
            n -= 1
        
        while (right):
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next

        # Reverse Twice
        # def reverse(node: ListNode | None) -> ListNode | None:
        #     prev, curr = None, node
            
        #     while (curr):
        #         t = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = t
            
        #     return prev
        
        # rev = reverse(head)
        
        # if (n == 1):
        #     rev = rev.next
        # else:
        #     curr = rev
        #     count = 1
        #     while (count < n - 1):
        #         curr = curr.next
        #         count += 1
        #     curr.next = curr.next.next
        
        # res = reverse(rev)

        # return res
