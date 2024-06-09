class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Base cases
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize empty strings for each row
        rows = [''] * numRows
        currRow = 0
        direction = -1  # We'll start by setting it to -1 so the first change makes it go down
        
        for char in s:
            rows[currRow] += char
            
            # Change direction if we're at the top or bottom
            if currRow == 0 or currRow == numRows - 1:
                direction *= -1
            
            currRow += direction
        
        return ''.join(rows)