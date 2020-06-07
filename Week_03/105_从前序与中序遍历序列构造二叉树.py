# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 定义递归函数　TC:O(n) SC:O(n)
        def helper(preorder_left:int, preorder_right:int, inorder_left:int, inorder_right:int):
            if preorder_left > preorder_right: return None

            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]

            # 先将根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中，从 左边界+1 到开始的 size_left_subtree 个元素就对应了中序遍历中 从 左边界 开始到 根节点定位-1 的元素
            root.left = helper(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构建右子树
            # 先序遍历中从 左边界+1+左子树节点数目 开始到 右边界的元素就对应了 中序遍历中 从根节点+1 到右边界的元素
            root.right = helper(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root


        # 记录长度
        n = len(preorder)
        # 构建哈希映射，帮助我们快速定位根节点
        index = {val:k for k, val in enumerate(inorder)}

        return helper(0, n-1, 0, n-1)
