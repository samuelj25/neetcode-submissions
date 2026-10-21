# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        if (k == 0):
            return None
        
        heap = []
        dummy = ListNode()
        prev = dummy

        heapq.heapify(heap)

        for i in range(k):
            if (lists[i]):
                heapq.heappush(heap, (lists[i].val, i, lists[i].next))
        
        while (heap):
            val, list_index, next_node = heapq.heappop(heap)
            node = ListNode(val, None)
            prev.next = node
            prev = node

            if (next_node):
                next_val = next_node.val
                heapq.heappush(heap, (next_val, list_index, next_node.next))
        
        return dummy.next
