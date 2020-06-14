class Solution:
    def canJump(self, nums) :
        if nums == [0]: return True
        max_ind = 0
        end_ind = len(nums) - 1
        for i, jump in enumerate(nums):
            if max_ind >= i and i + jump > max_ind:
                max_ind = i + jump
                if max_ind >= end_ind:
                    return True
        
        return False