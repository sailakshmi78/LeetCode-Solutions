class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        map={}
        for right in range(len(s)):
            if s[right]in map and  map[s[right]]>=left:
                left=map[s[right]]+1
            map[s[right]]=right
            longest=max(longest,right-left+1)
        return longest