class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 利用倒序遍历，时间复杂度为O(n)，空间复杂度为O(1)
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] != 9:
        #         digits[i] += 1
        #         return digits
        #     digits[i] = 0

        # digits.insert(0, 1)
        # return digits
        
        #pythonic方法，将列表转化为字符串再处理，时间复杂度为？
        digits = [str(x) for x in digits]
        nums = int("".join(digits)) + 1
        return [int(x) for x in str(nums)]