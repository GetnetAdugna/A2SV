class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivotStart = 0
        sumValue = 0
        total =0

        for i in nums:
            total += i
       
        while pivotStart < len(nums):
            temp =  nums[ pivotStart] + sumValue
            sumResult = total - temp 
            if sumResult == sumValue:
                return  pivotStart
            else:
                sumValue += nums[ pivotStart]
            pivotStart +=1
        return  -1