class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 合并之后排序, 时间复杂度为O((m+n)log(m+n))
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1

        # #双指针，从头开始, 时间复杂度O(m + n), 空间复杂度O(m)
        # p1, p2 = 0, 0
        # # 复制nums1
        # nums1_copy = nums1[:m]
        # nums1[:] = []

        # while p1 < m and p2 < n:
        #     if nums1_copy[p1] < nums1[p2]:
        #         nums1.append(nums1_copy[p1])
        #         p1 += 1
        #     else:
        #         nums1.append(nums2[p2])
        #         p2 += 1
        # if there are still elements to add
        # if p1 < m: nums1[p1 + p2:] = nums1_copy[p1:]
        # if p2 < n: nums1[p1 + p2:] = nums2[p2:]
        
        # return nums1

        # 三指针，从尾部开始,时间复杂度O(m+n)，空间复杂度O(1)
        p1 = m - 1
        p2 = n - 1
        p = m + n -1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
        
            p -= 1
        # add missing elements from nums2?

        nums1[:p2 + 1] = nums2[:p2 + 1]
     
        return nums1