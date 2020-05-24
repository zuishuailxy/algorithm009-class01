def rotate(nums, k):
            # 利用切片
        
    # nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
    k %= len(nums) 
    nums[:] = nums[-k:] + nums[:-k]
    
    return nums

    # 三次旋转 
    # n = len(nums)
    # k %= n

    # def swap(nums, l, r):
    #     while l < r:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l += 1
    #         r -= 1
        
    #     return nums

    # nums = swap(nums, 0, n-k-1)
    # nums = swap(nums, n-k, n-1)
    # nums = swap(nums, 0, n-1)

    # return nums


    

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))