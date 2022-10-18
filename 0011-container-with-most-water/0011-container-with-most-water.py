class Solution:
    def maxArea(self, height: List[int]) -> int:
        initial_max=0
        counter=0
        j=len(height)-1
        while counter<j:
            if height[counter]>height[j]:
                h=height[j]
                a=h*(j-counter)
                j-=1
            else:
                h=height[counter]
                a=h*(j-counter)
                counter=counter+1
            initial_max=max(initial_max,a)
        return initial_max