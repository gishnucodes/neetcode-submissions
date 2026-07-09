# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)  # Dummy head to simplify list construction
        curr = dummy
        carry = 0 
        
        # Include carry in the condition to catch the final dangling carry
        while l1 or l2 or carry:
            
            # Extract values, defaulting to 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry using divmod (or standard division/modulo)
            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10
            
            # Create the new node and advance the current pointer
            curr.next = ListNode(val)
            curr = curr.next
            
            # Safely advance l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next # Return the list skipping the initial dummy node