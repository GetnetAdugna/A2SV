class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        counter=0
        for i in (pushed):
            stack.append(i)
            while len(stack)and popped[counter]==stack[-1]:
                stack.pop()
                counter+=1
        return counter==len(popped)