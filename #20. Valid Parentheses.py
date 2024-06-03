#20. Valid Parentheses
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.


#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "()[]{}"
#Output: true
#Example 3:

#Input: s = "(]"
#Output: false


#Constraints:

#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {"(": ")", "[": "]",  "{": "}"}

        for char in s:
            if char in bracket_map:  # If the character is an opening bracket
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                # If there is something on the stack and the current character is a closing bracket for the last opened one
                stack.pop()
            else:
                return False  # If the current character is not a closing bracket for the last opened one
        
        return not stack
