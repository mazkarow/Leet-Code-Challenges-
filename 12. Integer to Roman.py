class Solution:
    def intToRoman(self, num):
        # Define a list of tuples with Roman numerals and their values
        roman_numerals = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]

        roman = ""  # This will hold the resulting Roman numeral

        # Process each symbol starting from the largest
        for value, symbol in roman_numerals:
            # While the number is greater than or equal to the value
            while num >= value:
                roman += symbol  # Append the symbol to the result
                num -= value      # Subtract the value from the number

        return roman

# Example usage:
# Create an instance of Solution to use its method
sol = Solution()
print(sol.intToRoman(3749))  # Output: MMMDCCXLIX
print(sol.intToRoman(58))    # Output: LVIII
print(sol.intToRoman(1994))  # Output: MCMXCIV
