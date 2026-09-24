class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        # 1. Use a list (array) to store the memory addresses of all nodes
        nodes = []
        curr = head
        
        # Change `while curr.next != None` to `while curr:` so the very last node is included.
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        n = len(nodes)
        
        # 2. Iterate until the middle to rewire the pointers
        for i in range(n // 2):
            # nodes[i] is L_0, L_1, L_2...
            # nodes[n - 1 - i] is L_n-1, L_n-2...
            
            # Link current node to the corresponding node from the end
            nodes[i].next = nodes[n - 1 - i]
            
            # Link that end node to the NEXT node in the normal sequence
            nodes[n - 1 - i].next = nodes[i + 1]
            
        # 3. Terminate the list to prevent infinite cycles
        # The new tail of the list will always be the middle node at index n // 2
        nodes[n // 2].next = None