class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Reduce the prefix size until it matches the start of `s`
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage:
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
