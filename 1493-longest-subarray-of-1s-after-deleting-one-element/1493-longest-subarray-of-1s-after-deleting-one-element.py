class Solution:
    def longestSubarray(self, nums: List[int]) -> int:  
        zeros = {}
        counter = 0
        left=0
        right = 0
        while right < len(nums):
            if nums[right] == 0 and len(zeros) == 0:
                zeros[0] = right
            elif nums[right] == 0 and len(zeros) > 0:
                counter = max(counter, right - left - 1)
                left = zeros[0] + 1
                zeros[0] = right
            right += 1
        if len(zeros) > 0:
            counter = max(counter, right - left - 1)
        else:
            counter = max(counter, right - left - 1)
        return counter