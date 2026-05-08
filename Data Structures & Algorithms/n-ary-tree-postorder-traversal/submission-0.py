"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #postorder: left > right > root

        result = []

        def dfs(node):
            
            if not node:
                return

            #traverse all children
            for child in node.children:
                dfs(child)

            result.append(node.val)

        dfs(root)
        return result

        
        