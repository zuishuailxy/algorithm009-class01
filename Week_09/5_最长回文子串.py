class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for x in range(n):
            for i in range(n):
                j = i + x
                if j >= len(s):
                    break
                if x == 0:
                    dp[i][j] = True
                elif x == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                
                if dp[i][j] and x + 1 > len(ans):
                    ans = s[i:j+1]
        
        return ans
