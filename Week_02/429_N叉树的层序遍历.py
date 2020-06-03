"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 广度优先搜索,利用队列 TC：SC:O(n)
        '''
        if not root: return None
        res = []
        deq = collections.deque([root])
        while deq:
            level = []
            for _ in range(len(deq)):
                node = deq.popleft()
                level.append(node.val)
                deq.extend(node.children)
            res.append(level)
        
        return res
        '''
        # 深度优先搜索，利用栈
        if not root:return None
        res = []

        def helper(node, level):
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            for chile in node.children:
                helper(chile, level+1)
        helper(root, 0)

        return res