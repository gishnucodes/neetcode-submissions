# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

#         if head == None or head.next == None:
#             return 

#         prev = None 
#         left = head 
#         right = head
#         count = 0 

#         for _ in range(n):
#             right = right.next
            
#         # 2. Edge Case: If right is None, n is equal to the length of the list.
#         # This means we need to remove the head node.
#         if right is None:
#             return head.next
        
#         while right.next!=None : 
#             right = right.next
#             left = left.next 
#             if prev == None:
#                 prev = head
#             else:
#                 prev = prev.next 

#         prev.next.next = right 
#         return head 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head 
        right = head
        
        # 1. Advance the right pointer by n steps
        for _ in range(n):
            right = right.next
            
        # 2. Edge Case: If right is None, n is equal to the length of the list.
        # This means we need to remove the head node.
        if right is None:
            return head.next
            
        # 3. Move both pointers until right reaches the last node
        while right.next is not None:
            right = right.next
            left = left.next
            
        # 4. left is now positioned immediately before the node to delete
        left.next = left.next.next
        
        return head