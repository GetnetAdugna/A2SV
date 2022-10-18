class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first=0
        second=1
        while first<len(nums) and  second<len(nums):
            if nums[first]==0 and nums[ second]!=0:
                nums[first],nums[ second]=nums[ second],nums[first]
                first+=1
            elif nums[first]!=0:
                first+=1
            second+=1