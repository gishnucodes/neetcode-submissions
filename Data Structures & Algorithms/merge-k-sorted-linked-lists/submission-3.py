import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Initialize the heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                # Tuple format: (node_value, list_index, node_reference)
                heapq.heappush(heap, (node.val, i, node))
                
        dummy = ListNode()
        current = dummy
        
        # Process the heap until empty
        while heap:
            # Extract the node with the minimum value
            val, i, node = heapq.heappop(heap)
            
            # Append it to the merged list
            current.next = node
            current = node
            
            # If the extracted node has a subsequent node, push it into the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next