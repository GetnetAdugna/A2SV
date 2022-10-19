class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        sumAll = 0
        counter=0
        dict_[0] = 1
        for i in nums:
            sumAll += i
            counter += dict_.get(sumAll - k, 0)
            dict_[sumAll]+=1
        return counter