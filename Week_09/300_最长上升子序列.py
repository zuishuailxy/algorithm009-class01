class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        tail, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tail[m] < num:
                    i = m + 1
                else:
                    j = m
            tail[i] = num
            if j == res:
                res += 1
        
        return res

                
 