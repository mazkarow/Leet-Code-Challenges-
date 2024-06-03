#3. Longest Substring Without Repeating Characters
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        if not s:  # Check if s is empty or None
            return 0
        start, max_length = 0, 0
        seen = set()
    
        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length
