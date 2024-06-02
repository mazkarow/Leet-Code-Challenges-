class Solution:
    def romanToInt(self, s):
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0  # Previous value, initialized to 0
        
        # Traverse the string from the end to the beginning
        for char in reversed(s):
            # Get the integer value of the current Roman numeral
            int_value = roman_to_int[char]
            
            # If the current value is less than the previous value, we must subtract it
            if int_value < prev_value:
                total -= int_value
            else:
                # Otherwise, just add the current value
                total += int_value
                prev_value = int_value
        
        return total

# Example usage:
sol = Solution()
print(sol.romanToInt("III"))     # Output: 3
print(sol.romanToInt("LVIII"))   # Output: 58
print(sol.romanToInt("MCMXCIV")) # Output: 1994
