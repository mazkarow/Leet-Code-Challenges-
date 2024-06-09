class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read and ignore leading whitespaces
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check the sign of number
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        
        # Step 3: Read in characters until a non-digit character or the end of the string
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        # Apply the sign
        num *= sign
        
        # Step 4 and 5: Clamp to 32-bit signed integer range
        int_max = 2**31 - 1
        int_min = -2**31
        
        if num > int_max:
            return int_max
        if num < int_min:
            return int_min
        return num