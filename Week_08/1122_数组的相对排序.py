class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        #将arr1 counter计数，按照arr2来取
        res = []
        counter = collections.Counter
        count = counter(arr1)
        #按照arr2将arr1的元素存入res
        for val in arr2:
            if val in count:
                nums = count[val]
                for i in nums:
                    res.append(val)
            #被存的元素删除掉
            del count[val]
        #剩下的元素排序放到末尾
        res += sorted(list(count.element()))

        return res


