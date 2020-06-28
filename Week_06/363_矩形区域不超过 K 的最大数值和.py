class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:    
        def maxSumSubarray(arr):
            sub_s_max = float("-inf")
            s_cur = 0
            prefix_sum = [float("inf")]
            for x in arr:
                bisect.insort(prefix_sum, s_cur)
                s_cur += x
                i = bisect.bisect_left(prefix_sum, s_cur - k)
                sub_s_max = max(sub_s_max, s_cur - prefix_sum[i])
            
            return sub_s_max
        
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        
        res = float("-inf")
        for y1 in range(n):
            for y2 in range(y1, n):
                arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
                res = max(res, maxSumSubarray(arr))
        
        return res