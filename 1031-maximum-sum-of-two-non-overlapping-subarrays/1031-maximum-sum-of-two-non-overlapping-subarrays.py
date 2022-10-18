class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        start = [0]
        answer = 0
        for i in nums:
            start.append(start[-1] + i)       
        for j in range(2):
            left = 0  
            for i in range(firstLen + secondLen, len(nums) + 1):
                left = max(left, start[i - firstLen] - start[i-secondLen-firstLen])
                answer = max(answer, left + start[i] - start[i-firstLen])
             #swapping the first and second length   
            firstLen, secondLen = secondLen, firstLen 
            
        return answer