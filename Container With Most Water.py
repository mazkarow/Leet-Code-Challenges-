class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current pair of lines
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage (this part is typically not included when you submit your solution on coding platforms):
if __name__ == "__main__":
    sol = Solution()
    height1 = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height1))  # Output: 49

    height2 = [1,1]
    print(sol.maxArea(height2))  # Output: 1
    