class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None

# Example usage
nums = [2, 7, 11, 15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method on the instance
result = solution.twoSum(nums, target)
print(result)