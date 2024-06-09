class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        # Convert the integer to string and reverse it
        str_x = str(x)[::-1]
        
        # If the original number was negative, remove the '-' from the end and make it negative
        if x < 0:
            result = int(str_x[:-1]) * -1
        else:
            result = int(str_x)
        
        # Check if the result is within the 32-bit signed integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
   