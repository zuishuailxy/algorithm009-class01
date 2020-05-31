# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # if not root: return []
        # ans = []
        # ans.append(root.val)
        # if root.left: ans += self.preorderTraversal(root.left)
        # if root.right: ans += self.preorderTraversal(root.right)

        ans = []
        def help(node):
            if not node: return
            ans.append(node.val)
            helper(node.left)
            helper(node.right)
        
        helper(root)

        return ans 
        
        # return ans
        
        #迭代 时间复杂度：O(N) 空间复杂度：O(N)
        # if not root: return []
        # stack = [root] 
        # ans = []
        # while stack:
        #     temp = stack.pop()
        #     ans.append(temp.val)
        #     if temp.right: stack.append(temp.right)
        #     if temp.left: stack.append(temp.left)
        
        # return ans
    
    '''
    通用解法 1.递归
    '''
       # 前序遍历 根-左-右
       p = lambda x : [x.val] + p(x.left) + p(x.right) if x else []
       # 中序遍历 左-根-右
       p = lambda x : p(x.left) + [x.val] + p(x.right) if x else []
       # 后序遍历 左-右-根
       p = lambda x : p(x.left) + p(x.right) + [x.val] if x else []

       return p(root)

    '''
    通用解法 2.迭代，用栈，注意翻转
    '''
        stack, ans = [root], []
        while stack:
            temp = stack.pop()
            if isinstance(temp, TreeNode):
                # 前序遍历 根左右 变为 右左根（因为栈先进后出）
                # stack.extend([temp.right, temp.left, temp.val])
                # # 中序遍历 左根右 变为 右根左
                # stack.extend([temp.right, temp.val, temp.left])
                # # 后序遍历 左右根 变为 根右左
                stack.extend([temp.val, temp.right, temp.left])
  
            elif isinstance(temp, int):
                ans.append(temp)

        return ans