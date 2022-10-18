class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_list = {}
        val = 0
        result = 0
        for i in range(len(s)):
            
            if s[i] not in visited_list:
                result = max(result,i-val+1)
            
            else:
                if visited_list[s[i]] < val:
                    result = max(result,i-val+1)
                else:
                    val = visited_list[s[i]] + 1
            visited_list[s[i]] = i
        return result