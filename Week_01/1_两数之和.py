 # mothod 1 暴力破解真的蠢
    #执行用时 :6304 ms, 在所有 Python3 提交中击败了7.52%的用户
    #内存消耗 :30.3 MB, 在所有 Python3 提交中击败了5.06%的用户
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == target - nums[j] :
    #                 return  [i,j]

    # mothod 2 排序加遍历
    #执行用时 :116 ms, 在所有 Python3 提交中击败了44.51%的用户
    #内存消耗 :30.2 MB, 在所有 Python3 提交中击败了5.06%的用户
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     sort_to_lst = sorted(range(len(nums)), key = lambda x: nums[x])
    #     left_p = 0
    #     right_p = len(nums) - 1
    #     while left_p < right_p:
    #         sums = nums[sort_to_lst[left_p]] + nums[sort_to_lst[right_p]]
    #         if sums == target:
    #             return [sort_to_lst[left_p], sort_to_lst[right_p]]
    #         if sums < target:
    #             left_p += 1
    #         if sums > target:
    #             right_p -= 1

    # Method 3 hash map
    #执行用时 :124 ms, 在所有 Python3 提交中击败了44.45%的用户
    # 内存消耗 :30.7 MB, 在所有 Python3 提交中击败了5.06%的用户
    def twoSum(self, nums, target):
        hash_map = dict()
        for key, value in enumerate(nums):

            diff = target - value
            if diff in hash_map:
                return [hash_map[diff], key]
            hash_map[value] = key
            # print(hash_map)