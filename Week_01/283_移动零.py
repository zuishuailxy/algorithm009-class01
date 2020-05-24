class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # loop,记住0的个数，后面放0，前面放数字
        # # TC:O(N), SC:O(1)
        # i = 0
        # # for j in range(len(nums)):
        # #     if nums[j] != 0:
        # #         nums[i] = nums[j]

        # # for k in range(i, len(nums)):
        # #     nums[k] = 0

        # # 也可以直接处理
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i] = nums[j]
        #         if i != j:
        #             nums[j] = 0
        #         i += 1
      
        # return nums

        # 利用双指针,进行交换，将非零移动到前面，零移动到后面
        # TC:O(n), SC:O(1)
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        return nums