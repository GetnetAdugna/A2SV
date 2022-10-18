class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        length = 0
        while j < len(nums):
            if nums[j] != 1:
                k -= 1
            if k < 0:
                if nums[i] != 1:
                    k += 1
                i=i+1
            length = max(length,j-i+1)
            j += 1
        return length