class Solution:
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 are not palindromes (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For odd digits number, reversed_half will be one digit longer, we can get rid of the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Example usage:
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121)) # Output: False
print(sol.isPalindrome(10))   # Output: False