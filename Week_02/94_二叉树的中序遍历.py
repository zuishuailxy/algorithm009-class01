# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # ans = []
        # def helper(node):
        #     if not node:return 
        #     helper(node.left)
        #     ans.append(node.val)
        #     helper(node.right)
        # helper(root)
        # return ans

        # ans, stack = [], []
        # while stack or root:
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     ans.append(root.val)
        #     root = root.right
        
        # return ans

        # pythonic 写法
        p = lambda x: p(x.left) + [x.val] + p(x.right) if x else []
        return p(root)

        #迭代
        # stack, ans = [root], []
        # while stack:
        #     temp = stack.pop()
        #     if isinstance(temp, TreeNode):
        #         stack.extend([temp.right, temp.val, temp.left])
            
        #     if isinstance(temp, int):
        #         ans.append(temp)
        
        # return ans