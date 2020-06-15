# 第四周心得小结
    这是参加训练营的第四周，也是修炼内功的第四周。主要学习了深度优先搜索、广度优先搜索、贪心、二分查找等算法。以下进行总结：

深度优先搜索：用栈实现
实例代码
visited = set()
def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for next_node in node.childred():
        if not next_node in visited:
            dfs(next_node, visited)

广度优先搜索:用队列实现
实例代码
visited = set()
def bfs(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)
    while queue:
        node = queue.pop()
        visited.add(node)
        process(node)
        node = generate_related_nodes(node)
        queue.push(nodes)

贪心算法：
在每一步选择中都采取当前状态下最优的选择，从而希望导致结果是全局最好或是最优的算法。
+ 贪心：它对每个子问题的解决方案都作出选择，不能回退。
+ 动态规划：会保存以前的结果，并根据以前的结果对当前进行选择，有回退功能。
使用于贪心的场景：
问题能分解成子问题来解决，子问题的最优解能递推到最终问题的最优解，这种子问题最优解称为最优子结构。

二分查找：
二分查找的前提：
1.目标函数具有单调性 2.存在上下界 3.能够通过索引访问
代码模板
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1