# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur: continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            
            if level:
                res.append(level)
        
        return res
        # DFS
        res = []
        self.level(root, 0, res)
        return res
    
    def level(self, root, level, res):
        if not root: return
        if len(res) == level: res.append([])
        res[level].append(root.val)
        if root.left: self.level(root.left, level + 1, res)
        if root.right: self.level(root.right, level + 1, res)
