class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 利用递归的方法
        ans = []
        def traver(root):
            if root:
                ans.append(root.val)
            else:
                return
            
            for child in root.children:
                traver(child)
                       
        traver(root)

        return ans

        # 一句话的递归
        return root and sum([[root.val], *map(self.preorder, root.children)], [])


        # 另一种递归写法
        if not root: return []
        ans = []

        # 根左右
        # ans.append(root.val)
        # if root.children:
        #     for child in root.children:
        #         ans += self.preorder(child)
        
        # return ans

        #迭代,维护一个栈
        stack = [root]
        ans = []
        while stack:
            temp = stack.pop() #先将栈顶的数据假如到输出
            ans.append(temp.val)
            if temp.children:
                for child in temp.children[::-1]:  #如果该元素有子节点children 则反转加入到 stack 里(因为是前序遍历，栈是先进后出)
                    stack.append(child)
        
        return ans