#5.Longest Palindromic Substring
#Given a string s, return the longest palindromic substring in s.

#Example 1:

#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.

#Example 2:
#Input: s = "cbbd"
#Output: "bb"

#Constraints:

#1 <= s.length <= 1000
#s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = ""
        max_length = 0
        for length in range(n):
            for i in range(n):
                j = i + length
                if j >= len(s):
                    break
                if length == 0:
                    dp[i][j] = 1
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and length + 1 > max_length:
                    max_length = length + 1
                    ans = s[i:j+1]
        return ans