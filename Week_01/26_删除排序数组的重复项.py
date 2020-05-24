class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 利用双指针，快指针，慢指针
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        
        return i+1