# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        ram = {}
        count = 0 
        current = head

        # 1. Populate the dictionary with ALL nodes, starting at head
        while current is not None:
            ram[count] = current
            count += 1
            current = current.next
        
        # 2. Rewire using two pointers looking up keys in the dict
        n = count 
        i = 0 
        j = n - 1
        
        while i < j:
            # The current left node points to the current right node
            ram[i].next = ram[j]
            i += 1
            
            # If pointers meet, the rewiring is complete
            if i == j:
                break
                
            # The current right node points to the next left node
            ram[j].next = ram[i]
            j -= 1
            
        # 3. Terminate the final node to prevent an infinite cycle
        ram[i].next = None