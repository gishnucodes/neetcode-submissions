class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        hashmap = {}

        def dfs(curr):
            # If we've already created a clone for this node, stop to prevent infinite loops
            if curr in hashmap:
                return 
            
            # 1. Clone the node and store it in the hashmap
            hashmap[curr] = Node(curr.val)
            
            # 2. Continue DFS on all neighbors
            for neighbor in curr.neighbors:
                dfs(neighbor)
                
        # First pass: populate the hashmap with all cloned nodes
        dfs(node)
        
        # Second pass: wire up the neighbors using the cloned references
        for original_node, cloned_node in hashmap.items():
            # Find the cloned equivalent of every original neighbor
            cloned_node.neighbors = [hashmap[n] for n in original_node.neighbors]

        return hashmap[node]