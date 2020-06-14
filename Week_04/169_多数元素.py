class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        c = counts.most_common(1)
        return max(counts.keys(), key=counts.get)

        # 利用哈希表
        # n = len(nums)
        # if n == 1: return nums[0]
        # max_count = n // 2
        # hashmap = {}
        # for num in nums:
        #     if num not in hashmap:
        #         hashmap[num] = 1
        #         continue
        #     hashmap[num] += 1
        #     if hashmap[num] > max_count:
        #         return num

        # n = len(nums)
        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        #     if dic[num] > n / 2:
        #         return num

        # 利用投票法
        major = 0
        count = 0
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count += 1
            else:
                count -= 1
        
        return major






